/* RAN Air Wing public stats. Reads GET {RAW_API}/stats (see server/worker.js).
   Add ?demo to preview the layout with clearly labelled sample data. */
(function () {
  var app = document.getElementById('app');
  var ACS = { a4: 'A-4G Skyhawk', s2: 'S-2 Tracker' };
  var MISSIONS = { T1: 'T1', T2: 'T2', T3: 'T3', T4: 'T4', T5: 'T5', T6: 'T6', T7: 'T7', T8: 'T8', T9: 'T9', S1: 'S1 Fleet defence', S2: 'S2 Maritime strike' };
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function fmt(n) { return Number(n || 0).toLocaleString('en-AU'); }
  function pcts(a, b) { return b ? (Math.round(1000 * a / b) / 10) + '%' : '–'; }
  function hours(s) { var h = (s || 0) / 3600; return h >= 100 ? fmt(Math.round(h)) : h >= 1 ? h.toFixed(1) : h.toFixed(2); }
  function by(rows, key, val, k, f) { var t = 0; rows.forEach(function (r) { if (r[key] === val && r.k === k) t += r[f || 'n']; }); return t; }
  function kind(d, k, f) { var t = 0; d.kinds.forEach(function (r) { if (r.k === k) t += r[f || 'n'] || 0; }); return t; }

  function demo() {
    var r = function (n) { return Math.floor(Math.random() * n); };
    var daily = []; for (var i = 29; i >= 0; i--) { var d = new Date(Date.now() - i * 864e5).toISOString().slice(0, 10), f = 25 + r(60); daily.push({ d: d, k: 'flight_start', n: f }, { d: d, k: 'trap', n: Math.round(f * .5) + r(8) }, { d: d, k: 'mission_start', n: Math.round(f * .35) }, { d: d, k: 'crash', n: r(10) }); }
    var ms = [['T1', 190, 150, 30], ['T2', 160, 120, 30], ['T3', 140, 100, 32], ['T4', 110, 70, 30], ['T5', 90, 55, 28], ['S1', 60, 30, 25], ['S2', 40, 16, 20]], mis = [];
    ms.forEach(function (m) { mis.push({ ms: m[0], k: 'mission_start', n: m[1] }, { ms: m[0], k: 'mission_complete', n: m[2] }, { ms: m[0], k: 'mission_fail', n: m[3] }); });
    return { demo: true, updated: Date.now(), since: Date.now() - 30 * 864e5, daily: daily, missions: mis,
      kinds: [{ k: 'flight_start', n: 1850 }, { k: 'flight_secs', n: 0, secs: 612000 }, { k: 'trap', n: 920 }, { k: 'bolter', n: 410 }, { k: 'crash', n: 260 }, { k: 'eject', n: 190 }, { k: 'mission_start', n: 790 }, { k: 'mission_complete', n: 541 }, { k: 'mission_fail', n: 195 }, { k: 'aircraft_select', n: 330 }],
      aircraft: [{ ac: 'a4', k: 'flight_start', n: 1600 }, { ac: 'a4', k: 'flight_secs', n: 0, secs: 540000 }, { ac: 'a4', k: 'trap', n: 800 }, { ac: 'a4', k: 'bolter', n: 350 }, { ac: 'a4', k: 'crash', n: 240 }, { ac: 'a4', k: 'aircraft_select', n: 180 },
        { ac: 's2', k: 'flight_start', n: 250 }, { ac: 's2', k: 'flight_secs', n: 0, secs: 72000 }, { ac: 's2', k: 'trap', n: 120 }, { ac: 's2', k: 'bolter', n: 60 }, { ac: 's2', k: 'crash', n: 20 }, { ac: 's2', k: 'aircraft_select', n: 150 }] };
  }

  function kpi(cls, l, v, s) { return '<div class="kpi ' + cls + '"><p class="l">' + esc(l) + '</p><p class="v">' + esc(v) + '</p>' + (s ? '<p class="s">' + esc(s) + '</p>' : '') + '</div>'; }
  function bars(items) {
    var max = 0; items.forEach(function (i) { if (i.v > max) max = i.v; });
    if (!items.length || !max) return '<p class="empty">No data yet.</p>';
    return '<ul class="rows">' + items.map(function (i) { return '<li class="row"><span class="n" title="' + esc(i.n) + '">' + esc(i.n) + '</span><span class="t"><span class="b" style="width:' + (100 * i.v / max).toFixed(1) + '%"></span></span><span class="c">' + fmt(i.v) + (i.s ? '<small>' + esc(i.s) + '</small>' : '') + '</span></li>'; }).join('') + '</ul>';
  }

  function dailyChart(d) {
    var days = {}; d.daily.forEach(function (r) { var o = days[r.d] || (days[r.d] = { f: 0, t: 0, m: 0, c: 0 }); if (r.k === 'flight_start') o.f = r.n; else if (r.k === 'trap') o.t = r.n; else if (r.k === 'mission_start') o.m = r.n; else if (r.k === 'crash') o.c = r.n; });
    var keys = []; for (var i = 29; i >= 0; i--) keys.push(new Date(Date.now() - i * 864e5).toISOString().slice(0, 10));
    var W = 720, H = 200, L = 34, B = 24, T = 8, pw = W - L - 6, ph = H - B - T, bw = pw / keys.length, max = 1;
    keys.forEach(function (k) { if (days[k]) max = Math.max(max, days[k].f); });
    var step = max <= 5 ? 1 : max <= 20 ? 5 : max <= 60 ? 10 : max <= 150 ? 25 : max <= 600 ? 100 : 500, top = Math.ceil(max / step) * step;
    var svg = '<svg viewBox="0 0 ' + W + ' ' + H + '" role="img" aria-label="Flights started per day, last 30 days">';
    for (var g = 0; g <= top; g += step) { var y = T + ph - ph * g / top; svg += '<g class="grid"><line x1="' + L + '" x2="' + (W - 6) + '" y1="' + y + '" y2="' + y + '"/></g><text x="' + (L - 6) + '" y="' + (y + 3.5) + '" text-anchor="end">' + g + '</text>'; }
    keys.forEach(function (k, i) {
      var o = days[k] || { f: 0, t: 0, m: 0, c: 0 }, x = L + i * bw + bw * .2, w = bw * .6, h = ph * o.f / top;
      if (h) svg += '<path d="M' + x.toFixed(1) + ' ' + (T + ph) + 'V' + (T + ph - h + 4).toFixed(1) + 'Q' + x.toFixed(1) + ' ' + (T + ph - h).toFixed(1) + ' ' + (x + 4).toFixed(1) + ' ' + (T + ph - h).toFixed(1) + 'H' + (x + w - 4).toFixed(1) + 'Q' + (x + w).toFixed(1) + ' ' + (T + ph - h).toFixed(1) + ' ' + (x + w).toFixed(1) + ' ' + (T + ph - h + 4).toFixed(1) + 'V' + (T + ph) + 'Z" fill="#e8c547"/>';
      if (i % 5 === 0 || i === keys.length - 1) svg += '<text x="' + (x + w / 2).toFixed(1) + '" y="' + (H - 6) + '" text-anchor="middle">' + k.slice(5) + '</text>';
      svg += '<rect class="hit" tabindex="0" data-k="' + k + '" x="' + (L + i * bw).toFixed(1) + '" y="' + T + '" width="' + bw.toFixed(1) + '" height="' + ph + '"/>';
    });
    svg += '</svg>';
    var rows = keys.map(function (k) { var o = days[k] || { f: 0, t: 0, m: 0, c: 0 }; return '<tr><td>' + k + '</td><td>' + o.f + '</td><td>' + o.m + '</td><td>' + o.t + '</td><td>' + o.c + '</td></tr>'; }).join('');
    return { days: days, html: '<div class="chart" id="dchart">' + svg + '<div class="tip" id="dtip"></div></div><details class="tbl"><summary>View as table</summary><div class="tblwrap"><table class="dt"><thead><tr><th>Day (UTC)</th><th>Flights</th><th>Missions</th><th>Traps</th><th>Crashes</th></tr></thead><tbody>' + rows + '</tbody></table></div></details>' };
  }
  function wireTip(dc) {
    var box = document.getElementById('dchart'), tip = document.getElementById('dtip'); if (!box) return;
    function show(el) {
      var k = el.getAttribute('data-k'), o = dc.days[k] || { f: 0, t: 0, m: 0, c: 0 }, rb = el.getBoundingClientRect(), bb = box.getBoundingClientRect();
      tip.innerHTML = '<b>' + k + '</b><br>Flights <b>' + o.f + '</b><br>Missions <b>' + o.m + '</b><br>Traps <b>' + o.t + '</b><br>Crashes <b>' + o.c + '</b>';
      tip.style.left = Math.min(Math.max(rb.left - bb.left + rb.width / 2, 70), bb.width - 70) + 'px'; tip.style.top = '10px'; tip.classList.add('on');
    }
    box.querySelectorAll('rect.hit').forEach(function (r) { ['mouseenter', 'focus'].forEach(function (e) { r.addEventListener(e, function () { show(r); }); }); ['mouseleave', 'blur'].forEach(function (e) { r.addEventListener(e, function () { tip.classList.remove('on'); }); }); });
  }

  function render(d) {
    var flights = kind(d, 'flight_start'), secs = kind(d, 'flight_secs', 'secs'), traps = kind(d, 'trap'), bolt = kind(d, 'bolter'), crash = kind(d, 'crash'), ej = kind(d, 'eject');
    var mst = kind(d, 'mission_start'), mok = kind(d, 'mission_complete'), mfail = kind(d, 'mission_fail');
    var h = '';
    if (d.demo) h += '<p class="banner"><b>Sample data.</b> This is a layout preview, not real flights.</p>';
    h += '<p class="meta">UPDATED ' + new Date(d.updated).toLocaleString('en-AU', { dateStyle: 'medium', timeStyle: 'short' }).toUpperCase() + (d.since ? ' · COUNTING SINCE ' + new Date(d.since).toLocaleDateString('en-AU', { dateStyle: 'medium' }).toUpperCase() : '') + '</p>';
    h += '<div class="kpis">' + kpi('hero', 'Flight hours logged', hours(secs), 'Time airborne, all pilots, both aircraft') +
      kpi('', 'Missions flown', fmt(mst), fmt(mok) + ' completed · ' + fmt(mfail) + ' failed') +
      kpi('', 'Flights', fmt(flights), 'Free flights and missions') +
      kpi('', 'Arrested landings', fmt(traps), 'Trapped aboard Melbourne') +
      kpi('', 'Bolters', fmt(bolt), 'Missed every wire') +
      kpi('', 'Aircraft lost', fmt(crash), fmt(ej) + ' ejections') + '</div>';

    var dc = dailyChart(d), acs = {}; d.aircraft.forEach(function (r) { acs[r.ac] = 1; });
    var acl = Object.keys(acs).map(function (a) { return { a: a, sel: by(d.aircraft, 'ac', a, 'aircraft_select'), fl: by(d.aircraft, 'ac', a, 'flight_start'), secs: by(d.aircraft, 'ac', a, 'flight_secs', 'secs'), tr: by(d.aircraft, 'ac', a, 'trap'), cr: by(d.aircraft, 'ac', a, 'crash'), bo: by(d.aircraft, 'ac', a, 'bolter') }; });
    var totSel = acl.reduce(function (t, a) { return t + a.sel; }, 0), totFl = acl.reduce(function (t, a) { return t + a.fl; }, 0);
    h += '<div class="grid">';
    h += '<section class="card wide"><h2>Flights per day</h2><p class="sub">Flights started over the last 30 days (UTC).</p>' + dc.html + '</section>';
    h += '<section class="card"><h2>Aircraft selected</h2><p class="sub">Times a pilot switched to each aircraft with N.</p>' + bars(acl.slice().sort(function (a, b) { return b.sel - a.sel; }).map(function (a) { return { n: ACS[a.a] || a.a, v: a.sel, s: pcts(a.sel, totSel) }; })) + '</section>';
    h += '<section class="card"><h2>Flights by aircraft</h2><p class="sub">Flights started in each aircraft, including the default A-4G.</p>' + bars(acl.slice().sort(function (a, b) { return b.fl - a.fl; }).map(function (a) { return { n: ACS[a.a] || a.a, v: a.fl, s: pcts(a.fl, totFl) }; })) + '</section>';
    h += '<section class="card wide"><h2>Aircraft results</h2><p class="sub">Flight hours, arrested landings and losses per type. Trap rate is traps divided by traps plus bolters.</p><div class="tblwrap"><table class="dt"><thead><tr><th>Aircraft</th><th>Flights</th><th>Hours</th><th>Traps</th><th>Bolters</th><th>Lost</th><th>Trap rate</th></tr></thead><tbody>' +
      acl.sort(function (a, b) { return b.fl - a.fl; }).map(function (a) { return '<tr><td>' + esc(ACS[a.a] || a.a) + '</td><td>' + fmt(a.fl) + '</td><td>' + hours(a.secs) + '</td><td>' + fmt(a.tr) + '</td><td>' + fmt(a.bo) + '</td><td>' + fmt(a.cr) + '</td><td>' + pcts(a.tr, a.tr + a.bo) + '</td></tr>'; }).join('') + '</tbody></table></div></section>';

    var mset = {}; (d.missions || []).forEach(function (r) { mset[r.ms] = 1; });
    var ml = Object.keys(mset).map(function (m) { return { m: m, st: by(d.missions, 'ms', m, 'mission_start'), ok: by(d.missions, 'ms', m, 'mission_complete'), no: by(d.missions, 'ms', m, 'mission_fail') }; }).sort(function (a, b) { return a.m < b.m ? 1 : -1; }).sort(function (a, b) { return b.st - a.st; });
    h += '<section class="card"><h2>Missions flown</h2><p class="sub">Starts for each mission.</p>' + bars(ml.map(function (x) { return { n: MISSIONS[x.m] || x.m, v: x.st }; })) + '</section>';
    h += '<section class="card"><h2>Mission results</h2><p class="sub">Completion rate is completed divided by started.</p><div class="tblwrap"><table class="dt"><thead><tr><th>Mission</th><th>Started</th><th>Done</th><th>Failed</th><th>Rate</th></tr></thead><tbody>' +
      (ml.length ? ml.map(function (x) { return '<tr><td>' + esc(MISSIONS[x.m] || x.m) + '</td><td>' + fmt(x.st) + '</td><td>' + fmt(x.ok) + '</td><td>' + fmt(x.no) + '</td><td>' + pcts(x.ok, x.st) + '</td></tr>'; }).join('') : '<tr><td colspan="5">No missions yet.</td></tr>') + '</tbody></table></div></section>';
    h += '</div><p class="note">Flight hours count time airborne with the player in the cockpit or chase view, not paused and not crashed. A mission start also counts as a flight. Some missions end without a complete or fail record if the pilot leaves. Counts start from the day the stats feed went live.</p>';
    app.innerHTML = h; wireTip(dc);
  }

  function msg(t) { app.innerHTML = '<p class="empty">' + t + '</p>'; }
  if (/[?&]demo\b/.test(location.search)) return render(demo());
  var api = window.RAW_API;
  if (!api) return msg('The stats feed is not connected yet. Check back soon.');
  fetch(api + '/stats').then(function (r) { if (!r.ok) throw 0; return r.json(); }).then(function (d) {
    if (!d.kinds || !d.kinds.length) return msg('No flights recorded yet. Be the first: <a href="/">fly the sim</a>.');
    render(d);
  }).catch(function () { msg('Could not load the stats right now. Try again in a minute.'); });
})();
