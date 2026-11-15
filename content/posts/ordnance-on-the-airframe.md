---
title: "Ordnance you can see: stores on the airframe"
date: "2026-11-15T20:19+08:00"
categories: [dev-diary, aircraft]
summary: "Every store in the loadout screen is now drawn on the Skyhawk, and the same model falls away when you drop, fire or jettison it."
shot: s42-stores-strike
hero_alt: "A Skyhawk on the catapult with olive-drab bombs with yellow bands on the left inner and outer stations, beside a white drop tank."
sources:
  - title: "RAN VF-805, skyhawk.org"
    url: "https://www.skyhawk.org/article-unit/ran-vf805"
  - title: "RAN VC-724, skyhawk.org"
    url: "https://skyhawk.org/node/282"
  - title: "McDonnell Douglas A-4G Skyhawk, Wikipedia"
    url: "https://en.wikipedia.org/wiki/McDonnell_Douglas_A-4G_Skyhawk"
  - title: "Mark 81 bomb, Wikipedia"
    url: "https://en.wikipedia.org/wiki/Mark_81_bomb"
---
Until now the loadout screen changed the weight and the weapon list, but the airframe always showed the same two drop tanks. The airframe now draws whatever is on each of the five stations.

## What is drawn

- **AIM-9B Sidewinder** on a launch rail, with a dark seeker dome, four canards, four rear fins and an orange band. One of the reference photographs of 886 shows an AIM-9 with an orange band on the outer left pylon.
- **250 lb and 500 lb bombs** in olive drab with yellow bands, a fuze in the nose and a conical fin with a ring.
- **2.75 in (19-tube) and 5 in (4-tube) rocket pods** with a nose fairing and a tail fairing.
- **150 and 300 gallon tanks**, and the **D-704 buddy pod** with its nose turbine and stowed basket.

Drop a bomb (<kbd>K</kbd> with BOMB selected), fire a Sidewinder, or jettison everything (<kbd>J</kbd>) and the same model leaves the pylon and falls or flies away. Rockets are still drawn as trails.

## One change to the stores list

The 300 gallon tank can now go on the inner stations as well as the centreline. The reference photographs of 884 and 886 show large tanks under the wings.

## What the sources say, and how sure the shapes are

VF-805 could carry four AIM-9B, one on each wing station. A VF-805 account describes armourers hanging pods of Zuni rockets and bombs. A 1974 photograph caption describes 886 on the ramp with practice bombs and drop tanks. The A-4G could not launch guided air-to-ground weapons, so none are drawn.

The sizes are the weak point. Only the Mk 81 (1.88 m long, 23 cm across) was checked against a source. The tank sizes come from their fuel volume and the proportions in the photographs. The Sidewinder, Mk 82 and rocket pod sizes are from memory of standard data or estimates, not yet checked, and may be a few percent out. They are listed in the `STDIM` table in `index.html`, each with its confidence.

## Still to do

- Practice bombs are described in a source but are not a store in the sim yet.
- The Tracker and Sea King have no stores. The Tracker took two torpedoes or depth charges in the bay and rocket pods, torpedoes or 250 lb bombs on six underwing points; the Sea King Mk 50 carried Mk 46 torpedoes and depth charges. Both need their own loadouts before they ship.
