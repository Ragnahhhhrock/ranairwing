---
title: "The home screen now has a working flight deck"
date: 2026-11-25T15:28+08:00
categories: [dev-diary, aircraft]
summary: "A Tracker now launches, recovers, folds its wings and parks on the home screen, then is spotted for the catapult again. The lift routine is gone."
shot: s53-home-fold
hero_alt: "Island camera view of an S-2 Tracker taxiing on the flight deck with one outer wing panel folded up and the other still extending."
---
The home screen used to show a Tracker being towed onto the forward lift, lowered and brought back. That routine is gone. One S-2 now runs a full deck cycle, so the ship looks busy while you choose what to fly.

## The cycle

- **Launch.** The Tracker sits on the catapult with its wings out and propellers turning, then goes down the track and off the bow. The catapult crew give the turn-up, crouch and launch signals.
- **Recovery.** After a few minutes it comes back down the glidepath onto the angled deck, catches a wire and stops.
- **Fold and park.** It taxis clear and folds its outer wings up and back as it goes, then parks forward of the island with the propellers stopped.
- **Respot.** After 90 seconds parked it taxis to the catapult, spreading its wings on the way, and launches again.

## Try it

Open the home screen with the orbit, deck or island camera and watch. The cycle stops as soon as you start a flight (catapult, approach, tutorial or mission), and the catapult is yours.

## Still approximate

- The speeds, timings and the flight path out of sight are game values, not RAN procedure.
- The Tracker taxis under its own power. The tractor and tow crew from the old routine have been removed.
- The Sea King on the forward helicopter spot disappears for the length of each launch, because the Tracker's wing would pass through it. This is the same trick the sim uses when you launch a Tracker yourself.
- The Skyhawk that used to sit on the catapult on the home screen is hidden while the cycle runs. It reappears when you start a flight.
- There is no engine sound for the home-screen aircraft yet.
