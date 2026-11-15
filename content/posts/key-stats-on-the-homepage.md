---
title: "Launches, traps and crashes on the homepage"
date: 2026-11-15T20:30+08:00
categories: [dev-diary]
summary: "The title panel now keeps a running count of launches, traps and crashes."
shot: s44-key-stats
hero_alt: "The sim title panel with an Australian White Ensign, three counters labelled Launches, Traps and Crashes, and a status line under them."
---
The title panel now carries three counters: launches, traps and crashes. They count what happens in the sim, the same events the sim already tracks. A cat shot that starts the run counts as a launch, an arrested landing counts as a trap, and any crash counts, whether or not the pilot survives. Bolters and ejections are not counted.

## Two modes

The panel shows totals from everyone flying, and the line under it reads "Live from pilots worldwide". The shared figures refresh every minute. If the counter cannot be reached, the panel falls back to your own totals, kept in this browser's local storage, and the line says so. Clear your site data and those reset.

The counts started from zero when the counter went live. The counter is a small Cloudflare Worker, and the figures are approximate: the store is eventually consistent, and each visitor is limited to one counted event of each kind per minute, so a very fast run of crashes will undercount.

