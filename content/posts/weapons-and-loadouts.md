---
title: "Loadouts: what the Skyhawk carried, and what it did not"
date: "2026-11-15T20:03+08:00"
categories: [dev-diary, aircraft]
summary: "A loadout screen with five stations, six presets, real weights and fuel, based on the A-4G's actual stores."
shot: s38-loadout
hero_alt: "The loadout screen showing five stations, the six presets and the all-up weight against the catapult limit."
sources:
  - title: "McDonnell Douglas A-4G Skyhawk, Wikipedia"
    url: "https://en.wikipedia.org/wiki/McDonnell_Douglas_A-4G_Skyhawk"
  - title: "A-4 Skyhawk, The Australian Connection, skyhawk.org"
    url: "https://www.skyhawk.org/article-unit/a4-australian-connection"
  - title: "RAN VF-805, skyhawk.org"
    url: "https://www.skyhawk.org/article-unit/ran-vf805"
  - title: "Douglas A4G Skyhawk, Sea Power Centre - Australia"
    url: "https://seapower.navy.gov.au/node/1121"
---
Press <kbd>V</kbd> to open the loadout screen. Click a station to cycle through what it can carry, or pick a preset, then Apply to restart on the catapult. Weight and fuel now matter.

## What the A-4G carried

- Two 20 mm cannon with 100 rounds each.
- Up to four AIM-9B Sidewinders, one on each wing station, after a wiring modification.
- 250 lb and 500 lb bombs.
- 2.75 in and 5 in rocket pods.
- Drop tanks, and a buddy refuelling pod (see the refuelling post).

## What it did not carry

The A-4G could not launch the guided air-to-ground weapons that the US Navy's A-4F could. There are no Bullpup, Shrike or Maverick missiles in the sim. We found no source for RAN Skyhawks carrying torpedoes or mines either, so the sim has none. Some web pages list those weapons for the Skyhawk family in general; they are not RAN stores.

## Stations and presets

Five stations: left outer, left inner, centreline, right inner, right outer. Each takes only some stores (5 in pods go on the inner stations, 500 lb bombs on the inner and centre stations; a 300 gallon tank goes on the centreline or an inner station, and the centreline also takes the buddy pod).

| Preset | Stores |
|---|---|
| Clean | Nothing |
| Fleet defence | 4 AIM-9B, centreline tank |
| Strike | 2 x 500 lb, 2 x 250 lb, centreline tank |
| Rocket attack | 2 x 2.75 in pods, 2 x 5 in pods, centreline tank |
| Buddy tanker | D-704 pod on the centreline |
| Ferry | Three drop tanks |

## Weight and fuel

The Skyhawk now has fuel: 1,900 kg internal, plus whatever is in tanks. Engine flow follows throttle. At zero the engine flames out. A BINGO warning shows below 550 kg. In missions fuel burns four times faster than real so that it matters in a ten-minute sortie; free flight uses the real rate.

All-up weight changes the catapult shot and the climb. A strike load launches fine but climbs far slower than a clean aircraft. The catapult limit is 10,500 kg and no preset reaches it. Drop tanks and ordnance can be jettisoned with <kbd>J</kbd>.

## Still approximate

- Store weights, tank sizes and the 10,500 kg catapult limit are game values, not figures from the sources.
- Whether RAN Skyhawks carried 1,000 lb bombs is unconfirmed, so the sim stops at 500 lb.
- The 2.75 in and 5 in pods are modelled as 19 and 4 rounds.
- Free flight on the catapult uses your chosen loadout. Starting on the approach is always clean.
