---
title: "Arrestor wires, bolters and the hook"
categories: [carrier-ops]
summary: "How a landing is judged in the sim: five wires, what counts as a trap, a bolter or a crash."
shot: s17-wires
hero_alt: "The island camera looking aft along the flight deck toward the stern, with the white and yellow deck markings and the red foul line."
---
A carrier landing is a controlled crash onto a short deck. The aircraft's tail hook has to catch a cross-deck wire, and the wire's arrestor gear stops the aircraft within the landing area.

## The sim's wires

Five wires are modelled, spaced 6 m apart along the angled deck. The count and spacing are approximate: the drawings were not clear enough to confirm them.

## What counts as a trap

All of these must be true at touchdown:

- The hook is down.
- You are moving faster than about 29 kn over the deck.
- You are within 11 m of the angled deck's centreline.
- The hook touches down short of the last wire.

The sim then says which wire you caught and your sink rate, for example "Trapped: 3 wire, 650 fpm sink", and the TRAPS counter increases.

## A bolter

If you touch down beyond the wires, off the centreline, or with the hook up, and you are still moving fast, you have a bolter. With the hook down the sim says "Bolter! Full power and go around." With the hook up it says "Hook up: touch and go." Add full power and fly another circuit. The angled deck is what makes this possible: see [the angled deck](/blog/the-angled-deck/).

## When touchdown goes wrong

The sim ends a landing with a crash if you arrive:

- **Banked.** More than about 21 degrees of bank: wing strike. Fatal.
- **Nose too high.** Beyond about 25 degrees: tail strike. The aircraft is damaged and the pilot survives.
- **Nose too low.** Beyond about 10 degrees nose-down: nose-first touchdown. Also survivable.
- **Too fast down.** A sink rate over about 1,570 fpm collapses the gear. Above about 2,560 fpm that is fatal.

You can also crash on deck by hitting something: a parked aircraft, a tractor, the island, a towed aircraft, the parked helicopter or an open lift well. If you are moving faster than about 23 kn it is fatal.

After a crash the sim resets you on the carrier a few seconds later. The [stats panel](/blog/the-stats-panel/) keeps count.

## Tips

- Do not flare. The deck is not a runway.
- A steady, small sink rate is better than a flat one that floats past the wires.
- Keep the hook down from step 4 of the approach until the aircraft has stopped.
