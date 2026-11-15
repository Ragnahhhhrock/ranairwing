---
title: "The A-4G's ailerons and rudder now move"
date: 2026-11-15T20:35+08:00
categories: [dev-diary, aircraft]
summary: "The Skyhawk's ailerons and rudder are now separate surfaces that deflect with your stick and pedals, so you can see the controls working from the chase camera."
shot: ailerons-and-rudder
hero_alt: "Chase camera view from behind the A-4G Skyhawk in a banked turn, with the checkerboard rudder swung to one side and an aileron raised on the wing."
---
The A-4G used to fly with a solid wing and a fixed fin. Now the ailerons and the rudder are separate moving surfaces, so you can watch your control inputs from the chase camera.

## What moves

- **Ailerons.** A hinged panel on the outboard trailing edge of each wing. They move in opposite directions: roll right and the right aileron goes up while the left goes down. Full stick gives about 20 degrees either way.
- **Rudder.** The checkerboard rudder on the fin now hinges at the fin's rear edge. Press the right pedal and its trailing edge swings right; full pedal gives about 26 degrees.

The surfaces follow the same eased stick and pedal values that drive the flight model, so they move as smoothly as your inputs do.

## Try it

Press <kbd>C</kbd> for the chase camera, then roll with <kbd>A</kbd> / <kbd>D</kbd> (or the left and right arrows) and yaw with <kbd>Q</kbd> / <kbd>E</kbd>. Drag to orbit the camera around the tail.

## Still approximate

- The travel angles are game values, not the A-4G's published control throws.
- The model has no spoilers or other roll surfaces, and the tailplane does not move with the pull of the stick yet.
- The S-2 Tracker's surfaces are not animated yet.
