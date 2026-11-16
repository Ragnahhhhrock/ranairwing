---
title: "The jet blast deflector rises behind the Skyhawk"
date: "2026-11-15T21:58+08:00"
categories: [dev-diary]
summary: "A hinged blast shield now lies flush in the deck behind the port catapult and rises when a Skyhawk reaches launch power."
shot: s51-blast-deflector
hero_alt: "Sim screenshot: the raised jet blast deflector behind a Skyhawk on the port catapult."
---
A hinged blast shield now sits in the deck behind the port catapult. Before this it was only a dark patch painted on the flight deck.

- It lies flush in the deck, hinged on the edge nearest the aircraft, 3.7 m wide and set just port of the forward lift, with a yellow-and-black hazard edge.
- When a Skyhawk on the catapult reaches launch power (RPM above 85%), the panel rises to about 52 degrees leaning aft, on two hydraulic rams, in roughly a second.
- It stays up through the launch and lowers once the aircraft has left the catapult. Pulling the throttle back below 60% lowers it too.
- The Tracker does not raise it: its propellers do not need a deflector.

Try it: press R to start on the catapult (Skyhawk), hold = to run up to full power, then look back with the chase camera. Press Z to launch.

Still approximate: the size, angle and raise time are game values, not measured from Melbourne's real deflector. The sim does not yet model the exhaust hitting the plate, cooling water, or crew behaviour around it.
