---
title: "Missions and training: the sim now has a structure"
date: "2026-11-15T20:02+08:00"
categories: [dev-diary, how-to-fly, carrier-ops]
summary: "Twelve scored missions, from a catapult launch to a maritime strike, unlock in order and keep your best score."
shot: s37-missions
hero_alt: "The mission list open over the ocean, showing nine training missions and two sorties with the first mission's briefing on the right."
sources:
  - title: "Douglas A4G Skyhawk, Sea Power Centre - Australia"
    url: "https://seapower.navy.gov.au/aircraft/douglas-a4g-skyhawk"
  - title: "Grumman S-2 Tracker in Australian service, Wikipedia"
    url: "https://en.wikipedia.org/wiki/Grumman_S-2_Tracker_in_Australian_service"
  - title: "RAN VF-805, skyhawk.org"
    url: "https://www.skyhawk.org/node/283"
---
Until now the sim was free flight: launch, land, repeat. It now has missions, each with a briefing, objectives, a score and a debrief.

## Try it

Press <kbd>Y</kbd> (or the Missions button) to open the list. Pick a mission and press Fly. Press <kbd>R</kbd> to retry, <kbd>Esc</kbd> to leave. The sim pauses while the list or the loadout screen is open.

## The missions

| ID | Mission | What you do |
|---|---|---|
| T1 | Catapult launch and climb | Launch, gear and flaps up, climb through 2,000 ft, reach 250 kt |
| T2 | Day deck landing | Fly the approach and trap |
| T3 | Heavy weather recovery | The same, in sea state 6 |
| T4 | Gunnery | 15 cannon hits on a towed sleeve |
| T5 | Rocket attack | Hit a barge with 3 rockets |
| T6 | Bombing | Destroy a barge with bombs |
| T7 | Sidewinder intercept | Splash a drone with an AIM-9B |
| T8 | Buddy refuelling | Take 400 kg from a tanker, then land |
| T9 | Launch emergency | Engine failure after the cat shot: eject and survive |
| S1 | Fleet air defence patrol | Splash two bogeys circling the task group, then land |
| S2 | Maritime strike | Sink a ship 55 km out, then land. A tanker waits 18 km out |

Missions unlock in order. T1 is open; later ones need earlier ones (S1 needs T7 and T2, S2 needs T6 and T8). Tick "unlock all missions" if you want to skip ahead. Your best score for each is saved in the browser.

## Scoring

Each objective is worth points. Missions that end with a landing add a bonus for fuel left, a bonus for the wire (the third wire pays most) and lose 10 points for each bolter. Ejecting or crashing fails the mission, except in T9 where ejecting is the point.

## Where the missions come from

The roles follow what the A-4G did: fleet air defence, maritime strike and support to the Army, per the Navy's Sea Power Centre. The find-then-attack pattern of the strike mission was seen in a 1969 exercise, where Trackers found the opposing force and Skyhawks attacked it; in S2 the sim simply tells you where the ship is. T9 is modelled on A-4G 888, which lost its engine just after a catapult launch in the Andaman Sea in 1979 (the pilot ejected).

## Still approximate

- These are generic exercises. None recreates a dated event, and every target (sleeve, barge, drone, ship) is a simple stand-in.
- There is no shore base yet, so no Nowra circuit or field carrier landing practice.
- No night flying, and the Tracker and Sea King have no missions.
- The sortie dates and places are not tied to the 1977-1982 calendar yet.
