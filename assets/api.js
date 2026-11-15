/* RAN Air Wing stats API base URL: the Cloudflare Worker in server/ (setup in docs/stats.md). No trailing slash.
   Deployed on the malgordonperth Cloudflare account (Worker ranairwing-stats, D1 database ranairwing-stats). If empty, the home page hides its stats block and /stats/ says the feed is not connected. */
window.RAW_API='https://ranairwing-stats.malgordonperth.workers.dev';
