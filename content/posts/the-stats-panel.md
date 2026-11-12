---
title: "Traps, losses and the stats panel"
categories: [how-to-fly, dev-diary]
summary: "What the three counters count, when they reset, and what the sim sends to analytics."
shot: s31-stats
hero_alt: "The cockpit view on the catapult with the stats panel showing traps, aircraft lost and pilots lost at zero."
---
The panel at the bottom left of the screen shows the ship's readouts and, at the bottom, three counters.

## What they count

- **TRAPS.** Every arrested landing.
- **AIRCRAFT LOST.** Every aircraft destroyed, including after an ejection.
- **PILOTS LOST.** Every pilot killed while still aboard.

See [crashes, ejecting and the counters](/blog/crashes-and-ejecting/) for the cases.

## When they reset

The counters live in the page, not in your browser's storage, so reloading the page sets them to zero. The sim does not save scores or progress.

## What the sim sends

The sim sends anonymous gameplay events to Google Analytics: for example a launch, a trap with the wire number and sink rate, a bolter, a crash with its reason, an ejection, a camera change, and the start and finish of the tutorial. That tells us which parts of the sim people use and where they fail, and so what to fix first. The events describe what happened in the sim, not who you are.

## Using it as a goal

A simple challenge: three traps in a row, without a bolter, at sea state 4. The counter does not track streaks, so you will have to keep count yourself.
