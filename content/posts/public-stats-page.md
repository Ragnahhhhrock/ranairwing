---
title: "Flight hours, missions and aircraft choices, in public"
date: "2026-11-15T20:40+08:00"
categories: [dev-diary]
summary: "The home page now shows what every pilot has logged, and a new Stats page breaks it down by aircraft and mission."
shot: s-public-stats
hero_alt: "Orbit camera on HMAS Melbourne at sea in the sim, with the title panel at top left."
---
The home page now carries a block of totals in the title panel: flight hours, missions flown, flights and arrested landings, summed over every pilot who has flown the sim. Click through to [/stats/](/stats/) for the longer list.

## What is counted

- **Flight hours**: time airborne with you in the cockpit or chase view, not paused and not crashed.
- **Missions flown**: every mission start, with completed and failed counted separately for each mission.
- **Flights**: free flights from the catapult or approach buttons, plus every mission start.
- **Arrested landings, bolters, aircraft lost and ejections.**
- **Aircraft selected**: how often pilots switch between the A-4G Skyhawk and the S-2 Tracker with N, plus flights, hours and trap rate per type.
- A 30-day chart of flights per day, with a table view.

## Privacy

The counts are anonymous. The sim sends a short event ("a trap in the A-4G", "mission T5 started", "30 seconds airborne") to a small Cloudflare Worker that adds it to a counter. No names, IP addresses, cookies or accounts are stored, and nothing is sent if your browser has Do Not Track on. Only flights played on ranairwing.com count.

## Still approximate

- The totals start from the day the feed went live, so they are small at first. The home page block stays hidden until the first flight is recorded.
- Flight hours count time in the cockpit or chase view, so an aircraft flying on while you look at it from the deck camera does not add hours.
- A mission that a pilot abandons records a start but neither a completion nor a failure.

`/stats/?demo` previews the page layout with clearly labelled sample data.
