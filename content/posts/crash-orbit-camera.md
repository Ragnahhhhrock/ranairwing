---
title: "After a crash, the camera circles the wreck"
date: 2026-11-25T15:29+08:00
categories: [dev-diary]
summary: "When you crash, the sim now cuts to the chase view and slowly orbits the crash site instead of leaving you looking out of the cockpit."
shot: crash-orbit-cam
hero_alt: "Chase view just after a crash: the fireball and smoke over the sea, seen from behind as the camera begins its orbit."
---
When the aircraft crashes, the camera now switches to the chase view at once and starts a slow orbit of the crash site. One lap takes about 25 seconds.

## How to try it

Fly into the water or the ramp on purpose. The orbit runs until the sim restarts you on the catapult after a few seconds, or until the mission debrief.

## What is still approximate

If you ejected before the crash, the sim keeps the ejection camera on you and the parachute, so the orbit only follows crashes with the pilot still aboard. You can still drag the mouse to shift the angle while it turns. The orbit speed and starting distance are game values.
