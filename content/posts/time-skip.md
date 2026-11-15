---
title: "Time skip: run the sun forwards or backwards"
date: 2026-11-15T21:30+08:00
categories: [dev-diary]
summary: "A new Time skip control in the menu runs the time of day forwards or backwards at 2x, 4x or 8x."
shot: s-time-skip
hero_alt: "The sim menu scrolled to the Time skip row, with the Back toggle and the 4x button highlighted, and the Time slider reading 08:53."
---
The menu now has a **Time skip** row under the Time slider. It moves the sun and sky through the day on its own, so you can watch the light change on the deck without dragging the slider.

## How to try it

- Open the menu and scroll to **Time skip**.
- Press **2x**, **4x** or **8x** to start. Press the same button again to stop.
- The **Fwd / Back** button sets the direction. You can flip it while skipping.
- The Time slider and its readout follow along.

## What it does and does not do

- It changes the time of day only: sun position, sky colour, light and fog. Ship, aircraft and mission clocks run at normal speed.
- 1x is set at 5 game minutes per real second, so 2x, 4x and 8x are 10, 20 and 40 minutes per second. These rates are a game choice.
- The clock wraps within the slider's range, 05:30 to 18:30. Night flying is not built yet.
- It pauses while the Missions or Loadout screens are open.
