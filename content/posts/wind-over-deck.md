---
title: "Wind over deck: why the ship turns into the wind"
categories: [carrier-ops, how-to-fly]
summary: "A carrier steams into the wind to give aircraft airflow over the deck. Here is the sum the sim does, and the numbers at each sea state."
shot: s06-wod
hero_alt: "HMAS Melbourne at speed on the orbit camera at sea state 4, with the wind over deck readout visible at bottom left."
---
Wind over deck is the speed of the air moving along the flight deck. It is the ship's own speed plus the true wind, when the ship steams straight into that wind.

More wind over deck helps both ends of a flight. A launching aircraft has less speed to gain from the catapult. A landing aircraft arrives with less speed relative to the deck, so the wire has less to absorb.

## What the sim does

The sim holds the ship on heading 250 degrees and puts the true wind on 250 degrees, so the wind always blows along the ship's track. The readout is simply wind plus ship speed.

| Sea state | True wind | Wind over deck at 20 kn | At 24 kn |
|---|---|---|---|
| 0 | 2 kn | 22 kn | 26 kn |
| 1 | 5 kn | 25 kn | 29 kn |
| 2 | 9 kn | 29 kn | 33 kn |
| 3 | 14 kn | 34 kn | 38 kn |
| 4 | 19 kn | 39 kn | 43 kn |
| 5 | 25 kn | 45 kn | 49 kn |
| 6 | 32 kn | 52 kn | 56 kn |

The default is sea state 3 at 20 kn, which gives 34 kn over the deck.

## Why it matters when you fly

The wind is part of the flight physics. Your airspeed is measured against moving air, not against the sea. If you slow the ship, the wind over deck drops, and your approach speed relative to the deck changes with it.

Try it: fly the same approach with the ship at 0 kn, then at 24 kn, and notice how differently the deck comes at you.

## What the sim leaves out

In practice a carrier chooses a heading to give the best wind over deck while also staying on its operating track, and the wind rarely lines up exactly. The sim fixes the wind direction to keep the first versions simple.
