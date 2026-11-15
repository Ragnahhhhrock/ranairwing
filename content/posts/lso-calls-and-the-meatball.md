---
title: "The LSO talks you down, and the meatball is on the mirror"
date: 2026-11-15T20:56+08:00
categories: [dev-diary, carrier-ops]
summary: "The approach now has radio calls on screen, a 3D ball with datum and wave-off lights on the mirror, and an LSO grade for each trap."
shot: s49-lso-calls
hero_alt: "Cockpit view on approach with a panel at the top of the screen showing four radio lines between the LSO and the pilot, from Roger Skyhawk to Roger ball."
---
The landing sequence now has the voice of a landing signal officer (LSO) on it. Fly an approach and a radio panel at the top of the screen shows the calls as they happen.

## The sequence

- At about 1.4 nm the pilot calls "paddles contact" and the LSO answers.
- At 0.75 nm the LSO says "Call the ball." The pilot answers with the ball and, in the Skyhawk, the fuel state in thousands of pounds, then the LSO says "Roger ball."
- In the groove the LSO corrects you: high, low, fast, slow, "Power", "Easy with it", and "Left for line-up" or "Right for line-up". If the ball and line-up stay good you get "Looking good."
- If gear or hook is still up inside about 1,300 m the LSO tells you to check it.

## Wave-off

The LSO waves you off if you are dangerously low (more than 1 degree under the glidepath inside 1,000 m), well out of line, or not configured. The red wave-off lights flash on the mirror and on the HUD ball, "WAVE OFF" flashes on screen, and the LSO calls it twice. Ignoring a wave-off and landing anyway earns "no grade".

## The meatball on the mirror

The mirror sight on the port side now has a real ball, a pair of green datum bars and red wave-off lights. The ball rises and falls with your glideslope error, and turns red when you are low. The lights are scaled up with range so you can still read them from a mile out. The HUD ball has datum lights to match.

## The grade

After a trap the LSO gives a grade based on the average ball and line-up error over the last 1,000 m: OK with a 3 wire for a tight pass, OK, FAIR, or NO GRADE. A hard landing is also no grade. A bolter is graded as a bolter. Missions that end in a landing show the grade in the debrief.

## Approximations

The call set and the thresholds are game values, modelled on general mirror-landing practice. They are not taken from RAN procedures, and the wording is mine. The grade scale is a simplification of the grades a real LSO gives, and the sim has no cut or deck-fouled lights yet. The meatball is drawn from your own glideslope, not from the optics of a real Fresnel lens sight.

## Fly it

Press <kbd>T</kbd> to start on approach, put the gear (<kbd>G</kbd>), flaps (<kbd>F</kbd>) and hook (<kbd>H</kbd>) down, and fly the ball. Try a deliberately low approach to see the wave-off. The calls also work for the Tracker.
