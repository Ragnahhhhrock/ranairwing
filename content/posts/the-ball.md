---
title: "The ball: how the landing aid works in the sim"
categories: [carrier-ops, how-to-fly]
summary: "The ball shows whether you are high or low on the glidepath. Here is what it means, and what the sim does with it."
shot: s15-ball
hero_alt: "The cockpit view on final approach, with the HUD showing the ball and angle-of-attack indicator and the ship ahead on the horizon."
---
A carrier pilot on approach needs to know one thing above all: am I on the glidepath? A visual landing aid answers that. On HMAS Melbourne it was a mirror landing aid on a port-side sponson about amidships, and the sim models the sponson.

## The idea

The pilot looks at a light, called the ball. The ball sits against a row of fixed reference lights. If the ball is level with them, the aircraft is on the glidepath. If it rises above them, the aircraft is high. If it sinks below, the aircraft is low.

## What the sim shows

The sim draws the ball on the HUD, on the right of the display, instead of rendering the mirror itself.

- **When it appears.** Within about 2.7 nm (5,000 m) of the deck and roughly lined up with it.
- **The glidepath.** 3.5 degrees.
- **The ball.** An amber dot against two green datum bars. It moves up the display as you go high and down as you go low.
- **Red ball.** The dot turns red when you are more than 0.9 degrees below the glidepath. Add power and pull up.
- **Line-up.** "LINED UP", "COME LEFT" or "COME RIGHT" below the ball, measured against the angled deck's centreline.
- **Range.** In nautical miles, under the line-up cue.

The ball takes the ship's heave into account, so in a heavy sea it moves with the deck.

## The second instrument: angle of attack

On the left of the HUD is an indexer that tells you whether you are at the right speed, using angle of attack instead of airspeed:

- **Amber doughnut.** On speed, between about 9.2 and 11.8 degrees.
- **Red chevron, pointing up.** Fast. Ease the power.
- **Green chevron, pointing down.** Slow. Add power.

The sim also shows STALL above 16.5 degrees.

## How to use them together

Watch both. If the ball is high, tap <kbd>↑</kbd> to push the nose down, or reduce power. If it is low, tap <kbd>↓</kbd> or add power. If the indexer shows fast, ease the power with <kbd>-</kbd>. If it shows slow, add power with <kbd>=</kbd>. Small, early corrections beat large, late ones.

The full sequence is in [approach and arrested landing, step by step](/blog/approach-and-trap-step-by-step/).
