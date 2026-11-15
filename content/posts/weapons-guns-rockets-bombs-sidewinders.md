---
title: "Firing the guns, rockets, bombs and Sidewinders"
date: "2026-11-15T20:04+08:00"
categories: [dev-diary, how-to-fly, aircraft]
summary: "Four weapons with different sights: a gun cross, a rocket and bomb pipper, and a Sidewinder seeker that only sees tailpipes."
shot: s39-weapons
hero_alt: "Cockpit view with the AIM-9B seeker circle, a LOCK cue and a bracket on a drone about 1.8 km ahead."
sources:
  - title: "RAN VF-805, skyhawk.org"
    url: "https://www.skyhawk.org/article-unit/ran-vf805"
  - title: "McDonnell Douglas A-4G Skyhawk, Wikipedia"
    url: "https://en.wikipedia.org/wiki/McDonnell_Douglas_A-4G_Skyhawk"
---
Press <kbd>I</kbd> to cycle the weapon (GUN, AIM-9B, ROCKET, BOMB, depending on what you carry). The HUD shows the selected weapon and how many you have left.

## Guns

Hold <kbd>K</kbd>. The gun cross marks where the two 20 mm cannon point. You have 200 rounds, and the shells drop under gravity, so aim a little high at range. Tracers show where they go.

## Rockets

Hold <kbd>K</kbd> to ripple rockets from your pods. The pipper shows where a rocket fired now would land. 2.75 in pods hold 19 rockets and 5 in pods hold 4.

## Bombs

Press <kbd>K</kbd> to release one bomb. The pipper shows where it would land if released now. Against a barge, a 500 lb bomb kills within about 25 m and a 250 lb bomb within about 18 m.

## Sidewinders

The AIM-9B was an early missile, and the sim treats it that way. The seeker looks only in a 10 degree cone ahead, out to 4 km, and only sees a target pointing away from you. Get behind the drone, put it inside the circle, wait for the LOCK cue and tone, then press <kbd>K</kbd>. The missile flies up to 650 m/s, steers on the target, and gives up if the target leaves its field of view. A hit within about 15 m destroys the drone.

The HUD draws a bracket and range on every target, with an arrow at the screen edge when one is off to the side.

## Try it

Missions T4 to T7 teach each weapon in turn.

## Still approximate

- Muzzle and rocket speeds, the rate of fire, and the lethal radii are game values.
- Drones and barges are generic. Nothing models real damage, fuzes or the AIM-9B's real seeker limits.
- Rockets and bombs fall on a flat sea with no wind. The pipper ignores your own manoeuvring.
- Bombs and rockets cannot hit the ship, the escorts or the tanker.
