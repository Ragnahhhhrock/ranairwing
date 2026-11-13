---
title: "Crashes, ejecting and the counters"
categories: [how-to-fly, dev-diary]
summary: "What happens in the sim when things go wrong, how to eject, and how the sim keeps score."
shot: s28-eject
hero_alt: "HMAS Melbourne from the orbit camera in warm afternoon light, the ship steaming away to port."
---
Carrier aviation is dangerous, and the sim tells you so plainly. When something goes wrong, the message says what happened.

## Crashes

- **Fatal.** The aircraft is lost and the pilot is killed. A fireball or splash marks where it ended.
- **Survivable.** For a tail strike or a nose-first touchdown the sim says "Aircraft damaged. Pilot survived."
- **On deck.** Hitting a parked aircraft, a tractor, the island, a towed aircraft, the parked helicopter or an open lift well is fatal above about 23 kn and survivable below it.

A few seconds later you are reset on the catapult.

The reasons and limits are in [arrestor wires, bolters and the hook](/blog/wires-bolters-and-the-hook/).

## Ejecting

Press <kbd>X</kbd> twice. The first press shows "Press X again to eject" for about a second and a half. The second fires the seat.

- The canopy goes first.
- The pilot leaves the aircraft in a rocket seat. A drogue parachute steadies the seat, the pilot separates from it, and a main parachute opens. The camera follows. The stages are in [a jointed pilot and a longer ejection](/blog/a-jointed-pilot-and-a-longer-ejection/).
- Too low, with the parachute not yet open, the pilot is killed. Otherwise the pilot is picked up from the water or lands on the deck.
- The aircraft carries on and crashes without a pilot. It is counted as lost, but the pilot is not counted as killed.

## The counters

Three numbers at the bottom left of the screen:

| Counter | Counts |
|---|---|
| TRAPS | Arrested landings |
| AIRCRAFT LOST | Aircraft destroyed, including after an ejection |
| PILOTS LOST | Pilots killed in a crash while still aboard |

## A note on tone

The counters are a game mechanic. Real losses were real people, and the ship's history includes accidents with loss of life. History posts about them will be written carefully, with official sources.
