# Worldwide counter

Backs the homepage key stats (launches, traps, crashes).

1. Cloudflare dashboard: Workers & Pages > KV > create a namespace `ranairwing-counts`.
2. Create a Worker `ranairwing-counter`, paste `worker.js`, and bind the namespace as `COUNTS` (Settings > Bindings).
3. Copy the Worker URL into `COUNTER_URL` in `index.html`, commit and push.

Until `COUNTER_URL` is set, the panel shows this device's own totals from localStorage.
KV is eventually consistent and the rate limit is per IP, so treat the figures as approximate.
