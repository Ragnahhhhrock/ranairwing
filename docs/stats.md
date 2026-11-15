# Stats feed

The home page stats block and `/stats/` read anonymous counts from a Cloudflare Worker (`server/worker.js`, D1 database). Nothing is stored except counters: no IP addresses, names, cookies or accounts. The sim only reports from ranairwing.com, and not when the browser sends Do Not Track.

## Deployed
Live at `https://ranairwing-stats.malgordonperth.workers.dev` (Worker `ranairwing-stats`, D1 database `ranairwing-stats`, binding `DB`), set up through the Cloudflare dashboard on 15 Nov 2026. `assets/api.js` already points at it. The steps below rebuild it from scratch, or update the code with `npx wrangler deploy` from `server/`.

## Deploy (once)
1. `cd server && npx wrangler d1 create ranairwing-stats`, then paste the `database_id` into `wrangler.toml`.
2. `npx wrangler d1 execute ranairwing-stats --remote --file=schema.sql`
3. `npx wrangler deploy`, which prints `https://ranairwing-stats.<account>.workers.dev`.
4. Put that URL in `assets/api.js` as `window.RAW_API`, commit and push.

Until `RAW_API` is set the home page hides its stats block and `/stats/` says the feed is not connected. `/stats/?demo` previews the page with clearly labelled sample data.

## Events (POST /e, JSON body sent as text/plain)
`flight_start`, `aircraft_select`, `trap`, `bolter`, `crash`, `eject`, `mission_start`, `mission_complete`, `mission_fail`, `flight_secs`. Each may carry `ac` (`a4` or `s2`) and `ms` (mission id). `flight_secs` carries airborne seconds, posted about every 30 s of flight and when the tab is closed.

## What the numbers mean
- Flight hours: seconds airborne (wheels off the deck, not crashed, sim not paused), summed over all pilots.
- Flights: free flights started from the catapult or approach buttons, plus every mission start.
- Missions flown: mission starts. Completed and failed are counted separately.
- Aircraft selected: times a pilot switched aircraft with N. The A-4G is the default, so it is also counted by flights.
- Counts start from the day the feed went live.
