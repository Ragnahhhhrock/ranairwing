---
title: "The home screen now has a working flight deck"
date: 2026-11-25T15:28+08:00
categories: [dev-diary, aircraft]
summary: "A Tracker and a Skyhawk now take turns launching, circling the carrier, recovering and parking on the home screen. The Tracker folds its wings. The lift routine and the helicopter are gone."
shot: s53-home-fold
hero_alt: "Island camera view of an S-2 Tracker on the flight deck with one outer wing panel folded up and the other part-way."
---
One A-4G Skyhawk and one S-2 Tracker now work the deck on the home screen, so the ship looks busy while you choose what to fly. The old routine of towing a Tracker up and down the lift is gone, and so is the Sea King on the forward spot.

## The cycle

- **Launch.** The Skyhawk goes first when the home screen opens, and the Tracker follows. Each aircraft sits on the catapult, then goes down the track and off the bow. The Tracker has its wings out and propellers turning. The catapult crew give the turn-up, crouch and launch signals.
- **Patrol.** The aircraft climbs out and circles the carrier counter-clockwise at about 750 m radius and 130 m altitude.
- **Recovery.** It turns onto a base leg, lines up on the angled deck, comes down the 3.5 degree glidepath and catches a wire.
- **Fold and park.** The Tracker taxis clear, folds its outer wings up and back as it goes, and parks forward of the island with the propellers stopped. The Skyhawk parks on the forward deck. It does not fold anything.
- **Respot.** After a wait (90 seconds for the Tracker, 45 for the Skyhawk) it taxis to the catapult and goes again. Only one aircraft uses the catapult or the landing area at a time, so the other waits its turn.

## Try it

Open the home screen with the orbit camera (key 1) and watch. The cycle stops as soon as you start a flight (catapult, approach, tutorial or mission), and the deck is yours. The camera work is covered in a separate post.

## Still approximate

- The speeds, timings and the circuit are game values, not RAN procedure.
- Both aircraft taxi under their own power. The tractor and tow crew from the old routine have been removed.
- The Sea King is no longer on the deck at all. The PEDRO plane guard helicopter still flies off the quarter.
- Of the three Skyhawks parked forward, the first one is the home-screen aircraft. The Skyhawk that used to sit on the catapult is hidden while the cycle runs, and everything returns to normal when you start a flight.
- There is no engine sound for the home-screen aircraft yet.
