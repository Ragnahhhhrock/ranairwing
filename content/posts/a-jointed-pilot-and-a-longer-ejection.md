---
title: "A jointed pilot and a longer ejection"
date: 2026-11-13T09:10+08:00
categories: [dev-diary, how-to-fly]
summary: "The pilot now has a head, torso, arms and legs, and an ejection runs as a sequence from seat rocket to parachute to landing."
shot: s34-eject-chute
hero_alt: "A pilot in a flight suit and white helmet hangs under an orange and white parachute over the sea, hands up on the risers."
hero_caption: "Screenshot from the sim. Ejection camera, 15:00, sea state 3, ship at 20 kn. About four seconds after pressing X twice."
---
The pilot used to be three boxes and a helmet. Now there is a body, and the ejection is a sequence you can watch.

## The pilot

The pilot has a helmet with a visor and oxygen mask, a torso with harness straps and a parachute pack, a life preserver around the neck, and two arms and two legs, each with its joints. Gloves and boots are modelled.

In the cockpit of the A-4G or the S-2 Tracker the pilot sits in a rocket seat. The right hand follows the stick and the left hand follows the throttle, and the head sags a little under g. You see this from the outside cameras, for example Chase (<kbd>7</kbd>). The Cockpit camera (<kbd>6</kbd>) looks out from the pilot's eyes, so the body is not drawn there.

## The ejection

Press <kbd>X</kbd> twice, as before. What happens next, with times from the moment of the second press:

1. **Canopy.** The canopy goes first. The pilot's hands come up to the face and the legs are drawn in.
2. **Seat rocket, 0 to 0.45 s.** The seat fires along its rails and climbs away from the aircraft.
3. **Windblast.** Once the hands let go, the arms and legs flail. The faster the air moves past, the harder they are thrown about, up to about 65 m/s (roughly 125 kn).
4. **Drogue, from 0.45 s.** After the rocket burns out the seat pitches backwards. A small drogue parachute streams downwind of the seat and damps the tumble.
5. **Separation, at 1.3 s.** The seat falls away on its drogue and the pilot is pushed clear.
6. **Main parachute, from 1.6 s.** The canopy opens over about a second and a half. The pilot swings upright with both hands on the risers and the legs hanging, and sways a little on the way down at about 6.5 m/s.

The readout under the camera follows the stages: seat rocket, drogue chute, seat separated, parachute opening, parachute open.

{{shot: s33-eject-seat | Screenshot from the sim. Ejection camera, 15:00, sea state 3, ship at 20 kn. About one second after pressing X twice: the drogue is out and the arms are blown back.}}

## Landing

The rules are the same as before. A pilot who hits the deck or the sea before the parachute is almost fully open, while falling fast, is killed. Otherwise:

- **In the water.** The life preserver inflates and the pilot floats head up. The message says the rescue helicopter picks the pilot up.
- **On the flight deck.** The pilot lands and sits up.
- **Too low.** The pilot lies still and the life preserver stays flat.

## What is still approximate

- The seat is a generic rocket seat. It is not a model of the seat fitted to either aircraft, and the timings are tuned to look right, not taken from seat data.
- The limbs are animated, not simulated. The flailing is a set of overlapping oscillations scaled by airspeed, not a physics model of a body in the airstream.
- The drogue steadies the tumble but adds no drag, so the seat and pilot fall at the same rate as before.
- The pilot's hands in the cockpit move with the controls but are not placed on a modelled stick or throttle.

See [crashes, ejecting and the counters](/blog/crashes-and-ejecting/) for what the counters do after an ejection.
