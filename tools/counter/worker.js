// Cloudflare Worker: worldwide launch / trap / crash counters for ranairwing.com
// Bind a KV namespace as COUNTS. Routes: GET /stats, POST /hit/{launches|traps|crashes}
const KEYS = ['launches', 'traps', 'crashes'];
const CORS = {
  'access-control-allow-origin': 'https://ranairwing.com',
  'access-control-allow-methods': 'GET, POST, OPTIONS',
  'access-control-allow-headers': 'content-type',
};
const json = (o, status = 200, extra = {}) =>
  new Response(JSON.stringify(o), { status, headers: { 'content-type': 'application/json', ...CORS, ...extra } });

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    if (req.method === 'OPTIONS') return new Response(null, { headers: CORS });
    if (url.pathname === '/stats' && req.method === 'GET') {
      const v = await Promise.all(KEYS.map(async k => parseInt((await env.COUNTS.get(k)) || '0', 10)));
      return json(Object.fromEntries(KEYS.map((k, i) => [k, v[i]])), 200, { 'cache-control': 'public, max-age=15' });
    }
    const m = url.pathname.match(/^\/hit\/(launches|traps|crashes)$/);
    if (m && req.method === 'POST') {
      // Light abuse limit: one hit per type per IP per minute (KV minimum TTL). KV is eventually consistent, so counts are approximate.
      const ip = req.headers.get('cf-connecting-ip') || 'x', rl = `rl:${m[1]}:${ip}`;
      if (await env.COUNTS.get(rl)) return json({ ok: false }, 429);
      await env.COUNTS.put(rl, '1', { expirationTtl: 60 });
      const n = parseInt((await env.COUNTS.get(m[1])) || '0', 10) + 1;
      await env.COUNTS.put(m[1], String(n));
      return json({ ok: true });
    }
    return json({ error: 'not found' }, 404);
  },
};
