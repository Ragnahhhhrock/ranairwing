---
title: "Making the deck sound right"
categories: [dev-diary]
summary: "Gear, flaps, speedbrakes and hook each got their own sound instead of a generic click."
shot: s14-sound
hero_alt: "The deck camera at dawn, looking along the flight deck with its yellow centreline toward the island."
---
The first version of the sim used one click sound for every control. It told you something had happened and nothing else. Each of the four systems now has its own sound.

## What each one is

- **Gear.** A hydraulic whine, then thumps as the gear locks.
- **Flaps.** A run of an actuator while the flaps move.
- **Speedbrakes.** A hiss and a thump, with a rumble of airflow while they are out.
- **Hook.** A drop and a clunk.

The sim also has sounds for the catapult, the arrestor wire, touchdown and crashes, plus engine and wind sound that follow the throttle and speed.

## How they are made

The sounds are generated in the browser, not played from recorded files. That keeps the page small and means no sound has to be licensed. The cost is that the sounds are impressions of the real ones, built from noise and tones.

## Is it accurate?

These are designed sounds. They are not recordings of a Skyhawk or of Melbourne's deck. If you have served on one and know what the real thing sounded like, email [contact@ranairwing.com](mailto:contact@ranairwing.com). A better description is more use than any amount of guessing.

## Controls

Press <kbd>M</kbd> to mute and unmute. Browsers will not play sound until you click or press a key in the page, so the first sound waits for your first input.
