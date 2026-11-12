---
title: "Testing a flight sim without a pilot"
categories: [dev-diary]
summary: "How scripts fly the sim in a headless browser to check launches, landings and the tutorial, and what that cannot tell you."
shot: s18-testing
hero_alt: "A Skyhawk on approach seen from behind on the chase camera in the late afternoon, with the ship ahead."
---
A flight sim is hard to test by looking at it. Does the tutorial still work after a change to the flight model? Does the ship still pitch correctly at sea state 5? Checking by hand every time does not scale.

## How the tests work

- The sim runs in a headless Chrome with software rendering, so no graphics card is needed.
- A debug handle on the page lets a script press keys, change the sea state, jump the simulation forward in time and read the aircraft's state.
- Scripts launch from the catapult, fly the approach and check what happens: trap or bolter, crash or not.

## Flying the tutorial by script

The guided tutorial was tested by a script that presses only the keys the tutorial asks for, as a new player would. It checks that every step completes and that the lesson ends in a trap. Running it several times at different wave phases shows how reliable it is. When a step was too strict, such as the limit on nose-down attitude at touchdown, the tests showed it and the limit was loosened.

## Screenshots

The images on this blog come from the same machinery. A script sets the camera, time of day, sea state and ship speed, lets the sim run for a few seconds, and saves the frame. That keeps every screenshot honest: it shows what the sim really draws.

## What tests cannot do

- **Sound.** A script can check that a sound was triggered. It cannot hear whether it sounds right.
- **Feel.** Whether the aircraft feels right on a keyboard is a human judgement.
- **Real-world accuracy.** Tests check that the sim does what the code says, not that the code matches the real ship.

So the sim still needs people to fly it and say what they think. Feedback is welcome at [contact@ranairwing.com](mailto:contact@ranairwing.com).
