---
title: "Buddy refuelling: Skyhawks tanking Skyhawks"
date: "2026-11-15T20:05+08:00"
categories: [dev-diary, how-to-fly, aircraft]
summary: "A tanker A-4G with a D-704 pod, a drogue to find with the probe, and a fuel state that makes you need it."
shot: s40-refuel
hero_alt: "Chase camera behind a Skyhawk, with the tanker ahead trailing its hose and drogue and the HUD showing the drogue 14 metres away."
sources:
  - title: "McDonnell Douglas A-4G Skyhawk, Wikipedia"
    url: "https://en.wikipedia.org/wiki/McDonnell_Douglas_A-4G_Skyhawk"
  - title: "Douglas A4G Skyhawk, Sea Power Centre - Australia"
    url: "https://seapower.navy.gov.au/aircraft/douglas-a4g-skyhawk"
  - title: "N13 A-4G serial histories, adf-serials.com.au"
    url: "https://adf-serials.com.au/ran/n13"
---
The RAN had no tanker aircraft. Its Skyhawks refuelled each other. One carried a D-704 buddy pod on the centreline, with a hose and a drogue, and the others plugged into it. At the time, the A-4G was the only Australian military aircraft that could refuel in flight, and the capability let the squadron reach out for coastal and shipping attacks. Records of A-4G 883 note that it buddy-refuelled US Navy A-4s during RIMPAC 80.

## In the sim

Mission T8 starts you low on fuel (BINGO) behind a tanker. Mission S2 has a tanker holding 18 km along the route.

- The tanker flies straight legs of about 100 seconds at 135 m/s, then a slow 180 degree turn. Tank up on the straight.
- The drogue trails behind the pod and sways a little, more in turns and rougher seas.
- The HUD shows distance to the drogue and closing speed once you are within 150 m.
- Get the probe tip within about 1.5 m of the drogue with a closing speed under 10 m/s and you get CONTACT. Fuel flows at 20 kg/s.
- Closing faster hits the basket and you must wait a few seconds to try again. Drifting more than about 5 m away, or faster than 14 m/s, breaks the connection.
- The pod holds 1,000 kg. Fly into the tanker and you crash.

The probe is the one already modelled on the Skyhawk's nose.

## Try it

Press <kbd>Y</kbd> and pick T8. Match the tanker's speed from behind and below (use <kbd>=</kbd> and <kbd>-</kbd> in small steps), then creep up.

## Still approximate

- The fuel flow, the drogue's sway, the contact rules and the 1,000 kg pod are game values. They are not sourced figures.
- You can only fly as the receiver. Flying the tanker is not in yet.
- There is no sourced detail on how often the squadron refuelled at sea, so no mission claims a historical frequency.
- We could not confirm from our sources that the RAN's Skyhawks carried a probe on every airframe, so treat the probe as the sim's assumption.
