---
title: "The home screen now cuts between launches, landings and the escorts"
date: 2026-11-25T15:50+08:00
categories: [dev-diary, carrier-ops]
summary: "On the home screen the orbit camera now cuts between a chase view of each landing, a front view and orbit of each launch, patrol shots, and close-ups of the escort ships."
shot: s54-home-chase
hero_alt: "Chase view from behind a Skyhawk on final approach, with the carrier and her wake ahead."
---
The home screen camera used to circle the ship on a fixed orbit. It now picks shots the way a documentary crew might, and cuts to whatever is happening.

## What it shows

The home screen opens on a ten-second orbit of the carrier, then cuts to the Skyhawk on the catapult. The Tracker follows it later in the cycle.

- **Landings.** A chase view behind the aircraft on final, a long lens from the LSO platform, and a low view along the deck as it catches a wire.
- **Launches.** A front view of the aircraft on the catapult, a view from the side, and a slow orbit around it as it goes off the bow.
- **Fold and park.** A close view of the Tracker folding its wings.
- **Patrol.** A view alongside the aircraft as it circles the carrier, and a long lens from the island.
- **Escorts and carrier.** Between events it alternates ten-second shots of HMAS Perth, Derwent and Supply (an orbit, a close pass along the side, a view of the bow) with orbits and bow views of the carrier.

Landings and launches take priority, then the fold, then patrol shots, then the escort and carrier reel.

## Try it

Open the home screen with the orbit camera (key 1). Drag or scroll and the automatic camera pauses for about nine seconds, then resumes. Pressing 1 again brings it straight back. Pressing O to orbit an escort turns it off until you cycle back to the carrier. Starting a flight ends the home cycle and the camera.

## Still approximate

- Shot positions and timings are tuned by eye, not a script. A shot can start with the aircraft small in frame, such as the LSO view at the start of the final approach.
- The camera is cut by the game, not blended, and it stays above the waves.
- There is no sound change between shots.
