---
title: "Phase 2: a flyable A-4G Skyhawk"
categories: [dev-diary, aircraft]
summary: "The ship got an aircraft: a Skyhawk with a simplified flight model, a cockpit view and a HUD, flown from the keyboard."
shot: s07-skyhawk
hero_alt: "An A-4G Skyhawk seen from behind on the catapult at full power, on the chase camera."
---
Phase 2 added the aircraft the whole project is built around, the McDonnell Douglas A-4G Skyhawk flown by the Royal Australian Navy.

## What was added

- **A procedural Skyhawk.** Built from simple shapes in code, with the livery described in the [livery post](/blog/a-4g-livery-and-markings/).
- **A flight model.** Lift, drag, thrust and weight are calculated every step. Air thins with altitude, and the engine responds to the throttle with a lag, as a jet does.
- **Keyboard control.** The stick commands an angle of attack rather than a rate, which suits the keyboard. Full stick is limited to about 3 g.
- **Gear, flaps, hook and speedbrakes.** All animated. Gear, flaps and speedbrakes each add drag.
- **Cockpit and chase cameras.** Keys <kbd>6</kbd> and <kbd>7</kbd>, with <kbd>C</kbd> to switch between them.
- **A HUD.** Speed, altitude, climb rate, engine, configuration flags and a landing aid.

## What it is not

This is a game-grade flight model, not a study sim. It is tuned so that a person on a keyboard can launch and land, and it will be refined. The numbers behind it are approximate, and nobody should use the sim to learn the real aircraft's handling.

## What came next

Launching from the catapult and catching a wire came straight after, followed by a guided tutorial. See [the guided tutorial](/blog/the-guided-tutorial/) for how that was built.
