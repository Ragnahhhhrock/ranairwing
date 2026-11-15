/* RAN Air Wing anonymous stats feed (Cloudflare Worker + D1).
   POST /e      body {k, ac?, ms?, secs?}  records one event (text/plain JSON, so browsers send no CORS preflight)
   GET  /stats  public aggregate counts for the home page and /stats/
   Stores counts only: no IP addresses, names, cookies or accounts. */
const ORIGINS = new Set(['https://ranairwing.com', 'https://www.ranairwing.com']);
const KINDS = new Set(['flight_start', 'aircraft_select', 'trap', 'bolter', 'crash', 'eject', 'mission_start', 'mission_complete', 'mission_fail', 'flight_secs']);
const ACS = new Set(['a4', 's2']);
const MS = /^[TS]\d{1,2}$/;
const MAX_SECS = 120;          // airborne seconds accepted per post (the sim posts about every 30 s)
const hits = new Map();        // per-isolate burst limiter; keys are never stored or logged

const cors = (origin) => ({ 'Access-Control-Allow-Origin': origin || '*', 'Vary': 'Origin' });
const json = (obj, status = 200, extra = {}) => new Response(JSON.stringify(obj), { status, headers: { 'Content-Type': 'application/json', ...extra } });

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    const origin = req.headers.get('Origin');
    if (req.method === 'OPTIONS') return new Response(null, { status: 204, headers: { ...cors(origin), 'Access-Control-Allow-Methods': 'GET, POST', 'Access-Control-Allow-Headers': 'Content-Type' } });

    if (url.pathname === '/stats' && req.method === 'GET') return stats(env);

    if (url.pathname === '/e' && req.method === 'POST') {
      if (!ORIGINS.has(origin)) return json({ error: 'origin' }, 403);
      const ip = req.headers.get('CF-Connecting-IP') || '', now = Date.now();
      const h = (hits.get(ip) || []).filter((t) => now - t < 10000);
      if (h.length >= 40) return json({ error: 'slow down' }, 429, cors(origin));
      h.push(now); hits.set(ip, h); if (hits.size > 5000) hits.clear();
      let b; try { b = JSON.parse(await req.text()); } catch (e) { return json({ error: 'json' }, 400, cors(origin)); }
      if (!b || !KINDS.has(b.k)) return json({ error: 'kind' }, 400, cors(origin));
      const ac = ACS.has(b.ac) ? b.ac : '', ms = typeof b.ms === 'string' && MS.test(b.ms) ? b.ms : '';
      const secs = b.k === 'flight_secs' ? Math.max(0, Math.min(MAX_SECS, Math.round(Number(b.secs) || 0))) : 0;
      if (b.k === 'flight_secs' && !secs) return json({ error: 'secs' }, 400, cors(origin));
      const d = new Date().toISOString().slice(0, 10);
      await env.DB.prepare('INSERT INTO counts (d,k,ac,ms,n,secs) VALUES (?,?,?,?,?,?) ON CONFLICT(d,k,ac,ms) DO UPDATE SET n=n+excluded.n, secs=secs+excluded.secs')
        .bind(d, b.k, ac, ms, b.k === 'flight_secs' ? 0 : 1, secs).run();
      return new Response(null, { status: 204, headers: cors(origin) });
    }
    return json({ error: 'not found' }, 404);
  },
};

async function stats(env) {
  const since = new Date(Date.now() - 29 * 86400e3).toISOString().slice(0, 10);
  const [tot, acs, mis, daily, first] = await Promise.all([
    env.DB.prepare('SELECT k, SUM(n) n, SUM(secs) secs FROM counts GROUP BY k').all(),
    env.DB.prepare("SELECT ac, k, SUM(n) n, SUM(secs) secs FROM counts WHERE ac<>'' GROUP BY ac, k").all(),
    env.DB.prepare("SELECT ms, k, SUM(n) n FROM counts WHERE ms<>'' AND k IN ('mission_start','mission_complete','mission_fail') GROUP BY ms, k").all(),
    env.DB.prepare("SELECT d, k, SUM(n) n FROM counts WHERE d>=? AND k IN ('flight_start','trap','mission_start','crash') GROUP BY d, k ORDER BY d").bind(since).all(),
    env.DB.prepare('SELECT MIN(d) d FROM counts').first(),
  ]);
  return json({ updated: Date.now(), since: first && first.d ? Date.parse(first.d) : null, kinds: tot.results, aircraft: acs.results, missions: mis.results, daily: daily.results },
    200, { 'Cache-Control': 'public, max-age=60', 'Access-Control-Allow-Origin': '*' });
}
