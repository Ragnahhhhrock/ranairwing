---
title: "The guided tutorial"
categories: [dev-diary, how-to-fly]
summary: "How the step-by-step tutorial works: it watches the aircraft, not the keyboard."
shot: s20-tutorial
hero_alt: "The chase camera on the catapult with the tutorial panel at the top of the screen showing lesson 1."
---
A carrier landing needs eight things done in the right order, and few people want to read a manual first. The guided tutorial is the answer: press <kbd>U</kbd> and the sim teaches itself.

## How it works

The tutorial is two lessons, one for launching and one for landing. Each lesson is a list of steps. Each step has an instruction, a short explanation and a condition that the aircraft has to meet before the tutorial moves on: RPM above 97%, gear up, flaps up, level at 1,000 ft, and so on.

Because the check is on the aircraft and not on the key that was pressed, any way of reaching the state works. A player who gets the gear up with the right key and one who gets there by accident both move on.

## Feedback

- The panel's edge turns green for a moment when a step is done.
- If you land beyond the wires, the panel says "Bolter. Setting up another approach…" and restarts the approach after a few seconds.
- If you crash, the lesson restarts.
- <kbd>Esc</kbd> leaves the tutorial. <kbd>Enter</kbd> starts the landing lesson after the launch lesson.

## Making it fair

The tutorial approach starts further out, at 3.5 nm and 800 ft, than the <kbd>T</kbd> approach, which starts at 1.2 nm. That gives time to configure the aircraft. The aircraft also levels its own wings from shallow banks, and the stick is softened for keyboard flying, so line-up corrections are small taps.

## Still to do

Ideas for later lessons include go-arounds and a full circuit. They are ideas, not promises. See the [roadmap](/blog/roadmap-eras-and-aircraft/).
