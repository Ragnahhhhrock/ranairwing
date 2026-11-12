#!/usr/bin/env python3
"""Generate content/schedule.json and docs/content-schedule.md: one post a day for 90 days from 2026-11-13.

Times are Perth time (AWST, UTC+8), seeded-random between 06:10 and 20:50, never on a 5-minute mark,
never the same minute twice, and at least 60 minutes away from the previous day's time.
Re-running keeps existing slots (so published dates never move); only new slugs are added.
"""
import json, random
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
START = date(2026, 11, 13)

# (slug, [categories], title, kind, angle)  kind: ready = written now from the sim/code/project notes;
# brief = needs sourced research before writing (history claims must carry sources, see docs/style-guide.md)
SLOTS = [
("welcome-to-ran-air-wing", ["dev-diary"], "Welcome to RAN Air Wing", "ready", ""),
("phase-1-a-carrier-at-sea", ["dev-diary"], "Phase 1: a carrier at sea, in your browser", "ready", ""),
("hmas-melbourne-by-the-numbers", ["ship-history", "carrier-ops"], "HMAS Melbourne by the numbers", "ready", ""),
("quick-start-launch-and-land", ["how-to-fly"], "Quick start: launch and land in five minutes", "ready", ""),
("how-reference-photos-shaped-the-model", ["dev-diary", "ship-history"], "How reference photos shaped the model", "ready", ""),
("wind-over-deck", ["carrier-ops", "how-to-fly"], "Wind over deck: why the ship turns into the wind", "ready", ""),
("phase-2-a-flyable-skyhawk", ["dev-diary", "aircraft"], "Phase 2: a flyable A-4G Skyhawk", "ready", ""),
("keyboard-controls", ["how-to-fly"], "Keyboard controls cheat sheet", "ready", ""),
("a-4g-livery-and-markings", ["aircraft", "air-wing"], "The A-4G in the sim: livery and markings", "ready", ""),
("what-the-model-gets-wrong", ["dev-diary"], "What the model still gets wrong", "ready", ""),
("seven-cameras", ["how-to-fly", "dev-diary"], "Seven cameras and when to use each", "ready", ""),
("the-angled-deck", ["carrier-ops"], "The angled deck, as drawn in the sim", "ready", ""),
("catapult-launch-step-by-step", ["how-to-fly", "carrier-ops"], "Catapult launch, step by step", "ready", ""),
("deck-sounds", ["dev-diary"], "Making the deck sound right", "ready", ""),
("the-ball", ["carrier-ops", "how-to-fly"], "The ball: how the landing aid works in the sim", "ready", ""),
("approach-and-trap-step-by-step", ["how-to-fly", "carrier-ops"], "Approach and arrested landing, step by step", "ready", ""),
("wires-bolters-and-the-hook", ["carrier-ops"], "Arrestor wires, bolters and the hook", "ready", ""),
("testing-a-flight-sim-without-a-pilot", ["dev-diary"], "Testing a flight sim without a pilot", "ready", ""),
("landing-in-rough-seas", ["how-to-fly", "carrier-ops"], "Landing in rough seas: sea state and ship motion", "ready", ""),
("the-guided-tutorial", ["dev-diary", "how-to-fly"], "The guided tutorial", "ready", ""),
("why-1977-to-1982", ["dev-diary", "ship-history"], "Why the sim is set in 1977-1982", "ready", ""),
("the-catapult-on-the-port-bow", ["carrier-ops"], "The catapult on the port bow", "ready", ""),
("flying-at-dawn-noon-and-dusk", ["how-to-fly", "dev-diary"], "Dawn, noon and dusk: the time-of-day slider", "ready", ""),
("reading-the-hud", ["how-to-fly"], "Reading the HUD", "ready", ""),
("beyond-the-skyhawk-the-air-wing", ["air-wing", "aircraft"], "Beyond the Skyhawk: the rest of the air wing", "ready", ""),
("roadmap-eras-and-aircraft", ["dev-diary", "air-wing"], "Roadmap: eras, aircraft and what comes next", "ready", ""),
("ten-mistakes-new-pilots-make", ["how-to-fly"], "Ten mistakes new pilots make", "ready", ""),
("crashes-and-ejecting", ["how-to-fly", "dev-diary"], "Crashes, ejecting and the counters", "ready", ""),
("flight-deck-layout", ["carrier-ops", "ship-history"], "Flight deck layout in the sim", "ready", ""),
("how-we-write-and-correct", ["dev-diary"], "How we write: sources and corrections", "ready", ""),
("the-stats-panel", ["how-to-fly", "dev-diary"], "Traps, losses and the stats panel", "ready", ""),
("behind-the-blog", ["dev-diary"], "Behind the blog: how posts are scheduled", "ready", ""),
# ---- briefs: history needs sourced research first ----
("from-hms-majestic-to-hmas-melbourne", ["ship-history"], "From HMS Majestic to HMAS Melbourne", "brief", "Origins as a Majestic-class carrier and the sale to Australia. Verify: laying down, launch, sale and name dates; builder."),
("the-long-fit-out", ["ship-history"], "The long fit-out", "brief", "Completion work and design changes before Melbourne entered service. Verify: angled deck, steam catapult and mirror landing aid fits, completion dates."),
("commissioning-and-the-voyage-to-australia", ["ship-history"], "Commissioning and the voyage to Australia", "brief", "Commissioning date, first air group, arrival in Sydney. Verify all dates and the route."),
("fleet-air-arm-before-melbourne", ["air-wing"], "The Fleet Air Arm before Melbourne", "brief", "RAN aviation from 1947: earlier carrier, aircraft, first squadrons."),
("sea-fury", ["aircraft"], "Hawker Sea Fury in RAN service", "brief", "Type profile and squadrons. Verify service dates, numbers, Korean War service."),
("sea-venom", ["aircraft"], "de Havilland Sea Venom in RAN service", "brief", "Type profile, role, squadron, service dates."),
("fairey-gannet", ["aircraft"], "Fairey Gannet in RAN service", "brief", "Type profile, ASW role, squadron, service dates."),
("805-squadron", ["air-wing"], "805 Squadron", "brief", "Squadron history and aircraft types over time."),
("how-the-angled-deck-was-invented", ["carrier-ops"], "How the angled deck was invented", "brief", "Origin, inventor, first trials, why it changed carrier design. Verify dates and people."),
("steam-catapults", ["carrier-ops"], "Steam catapults explained", "brief", "How they work, origin, why Melbourne carried one. Verify."),
("the-mirror-landing-aid", ["carrier-ops"], "The mirror landing aid and its inventor", "brief", "History and operation of the mirror sight. Verify."),
("life-aboard-melbourne", ["ship-history"], "Life aboard Melbourne", "brief", "Crew numbers, messes, routine. Needs oral-history or official sources."),
("flight-deck-crew-and-jersey-colours", ["carrier-ops", "air-wing"], "Flight deck crew and jersey colours", "brief", "Roles and colours as used in RAN practice. Verify RAN conventions."),
("the-landing-signal-officer", ["air-wing", "carrier-ops"], "The Landing Signal Officer", "brief", "Role of the LSO on Melbourne. Verify RAN practice."),
("far-east-deployments", ["ship-history"], "Far East and SEATO deployments", "brief", "Deployments and exercises in the 1950s-60s. Verify."),
("wessex-and-the-anti-submarine-role", ["air-wing", "aircraft"], "Wessex and the anti-submarine role", "brief", "Helicopter ASW on Melbourne. Verify squadron and dates."),
("the-1964-collision-with-voyager", ["ship-history"], "The 1964 collision with HMAS Voyager", "brief", "Handle with care. Verify date, losses, inquiries, memorials from official sources."),
("the-1969-collision-with-frank-e-evans", ["ship-history"], "The 1969 collision with USS Frank E. Evans", "brief", "Handle with care. Verify date, losses, inquiry from official sources."),
("why-the-ran-bought-the-skyhawk", ["air-wing"], "Why the RAN bought the Skyhawk", "brief", "Procurement decision, numbers ordered, delivery. Verify."),
("a-4g-skyhawk-in-ran-service", ["aircraft", "air-wing"], "A-4G Skyhawk in RAN service", "brief", "Type history, variants, side numbers, service dates."),
("ta-4g-trainers", ["aircraft"], "The TA-4G trainers", "brief", "Two-seat Skyhawks. Verify numbers and role."),
("s-2-tracker-in-ran-service", ["aircraft", "air-wing"], "S-2 Tracker in RAN service", "brief", "Type profile and squadron. Verify."),
("troop-transport-voyages", ["ship-history"], "Troop transport voyages to Vietnam", "brief", "Melbourne's role in the Vietnam era. Verify exactly which voyages."),
("the-1967-69-refit", ["ship-history"], "The 1967-69 refit", "brief", "What changed to carry Skyhawks and Trackers. Verify dates and work done."),
("skyhawk-design-lineage", ["aircraft"], "Where the Skyhawk came from", "brief", "Design origin of the A-4 line. Verify."),
("progress-report-1", ["dev-diary"], "Progress report: December", "brief", "Write from the repo commit log and analytics at the time."),
("816-squadron", ["air-wing"], "816 Squadron and the Trackers", "brief", "Verify squadron numbers and types."),
("724-squadron-and-training-at-nowra", ["air-wing"], "724 Squadron and training at Nowra", "brief", "Pilot training pipeline. Verify."),
("hmas-albatross-nowra", ["air-wing"], "HMAS Albatross, Nowra", "brief", "Home of the Fleet Air Arm. Verify."),
("sea-king", ["aircraft"], "Westland Sea King in RAN service", "brief", "Type profile. Verify squadron and dates."),
("sea-king-squadrons", ["air-wing"], "The Sea King squadrons", "brief", "Verify squadron numbers and roles."),
("cyclone-tracy-1974", ["ship-history"], "Cyclone Tracy and the Darwin relief, 1974", "brief", "Melbourne's part in the relief. Verify."),
("night-flying", ["carrier-ops"], "Night flying from a carrier", "brief", "Procedures and risks, general plus RAN-specific sources."),
("planeguard-helicopter", ["carrier-ops", "air-wing"], "The planeguard helicopter", "brief", "Role and practice."),
("keeping-a-carrier-supplied", ["carrier-ops", "ship-history"], "Keeping a carrier supplied", "brief", "Stores, fuel, replenishment at sea."),
("rimpac-and-us-navy-exercises", ["ship-history"], "RIMPAC and exercises with the US Navy", "brief", "Late-1970s exercises. Verify participation and dates."),
("the-air-wing-1977-1982", ["air-wing"], "The air wing in the sim's era, 1977-1982", "brief", "Which squadrons and aircraft embarked in those years. Verify."),
("era-select-design", ["dev-diary", "air-wing"], "Designing an era selector", "brief", "Design note for playing different periods. Write when scoped."),
("the-late-1970s-refit", ["ship-history"], "The late-1970s refit", "brief", "Verify existence, dates and scope before writing."),
("pilot-training-pipeline", ["air-wing"], "How a Skyhawk pilot was trained", "brief", "Verify."),
("the-namesake", ["ship-history"], "Named for a city: earlier ships and the Melbourne name", "brief", "Verify."),
("wessex-profile", ["aircraft"], "Westland Wessex profile", "brief", "Verify."),
("progress-report-2", ["dev-diary"], "Progress report: January", "brief", "Write from the repo and analytics at the time."),
("australia-and-the-invincible-offer", ["air-wing", "ship-history"], "Australia and the offer of HMS Invincible", "brief", "Why Australia did not replace Melbourne. Verify dates and decisions."),
("the-final-years-1981-82", ["ship-history"], "The final years, 1981-82", "brief", "Verify last deployments and flying."),
("decommissioning-june-1982", ["ship-history"], "Decommissioning, June 1982", "brief", "Ceremony and date. Verify."),
("end-of-fixed-wing-flying", ["air-wing"], "The end of RAN fixed-wing flying", "brief", "Verify last flights and dates."),
("sale-to-china-and-the-last-voyage", ["ship-history"], "Sale to China and the last voyage", "brief", "Verify sale, tow, fate."),
("skyhawks-after-the-ran", ["air-wing", "aircraft"], "Where the Skyhawks went", "brief", "Verify sale of the A-4Gs and later careers."),
("fleet-air-arm-museum-nowra", ["air-wing"], "Where to see the history: the Fleet Air Arm Museum", "brief", "Verify what is displayed now."),
("remembering-the-crews", ["ship-history"], "Remembering the crews", "brief", "Memorials and associations. Verify."),
("weather-and-flying-operations", ["carrier-ops"], "Weather and flying operations", "brief", "General explainer tied to the sim's sea states."),
("how-the-flight-model-works", ["dev-diary"], "How the flight model works", "brief", "Write from the code (airStep): lift, drag, stick-commanded angle of attack."),
("advanced-approach-tips", ["how-to-fly"], "Advanced approach tips", "brief", "Write from play-testing."),
("progress-report-3", ["dev-diary"], "Progress report: February", "brief", "Write from the repo and analytics at the time."),
("voices-from-the-deck", ["air-wing"], "Voices from the deck", "brief", "Link to published oral histories only; no quotes beyond fair length."),
("the-escorts", ["ship-history"], "The escorts: ships that sailed with Melbourne", "brief", "Verify ships and eras."),
("ninety-days-and-whats-next", ["dev-diary"], "Ninety days of posts, and what comes next", "brief", "Wrap-up with analytics."),
]
assert len(SLOTS) == 90, len(SLOTS)
assert len({s[0] for s in SLOTS}) == 90

def make():
    sched_path = ROOT / "content/schedule.json"
    old = {s["slug"]: s for s in json.loads(sched_path.read_text())} if sched_path.exists() else {}
    rng = random.Random(20261113)
    used, prev, out = set(), None, []
    for i, (slug, cats, title, kind, angle) in enumerate(SLOTS):
        d = START + timedelta(days=i)
        while True:
            m = rng.randint(6 * 60 + 10, 20 * 60 + 50)
            if m % 5 == 0 or m in used: continue
            if prev is not None and abs(m - prev) < 60: continue
            break
        used.add(m); prev = m
        slot = old.get(slug, {"slug": slug, "date": f"{d.isoformat()}T{m // 60:02d}:{m % 60:02d}:00+08:00"})
        slot.update({"title": title, "categories": cats, "kind": kind, "angle": angle})
        out.append(slot)
    sched_path.write_text(json.dumps(out, indent=1, ensure_ascii=False))
    ready = {p.stem for p in (ROOT / "content/posts").glob("*.md")}
    cname = {c["slug"]: c["name"] for c in json.loads((ROOT / "content/categories.json").read_text())}
    lines = ["# Content schedule: 90 days from 13 Nov 2026", "",
             "Perth time (AWST). Generated by `tools/blog/make_schedule.py` from `content/schedule.json`. Times are randomised: no two posts share a minute and consecutive days are at least an hour apart.", "",
             "Status: **written** = Markdown exists in `content/posts/`; **brief** = needs sourced research first (history claims need sources).", "",
             "| # | Date | Time | Category | Title | Status |", "|---|---|---|---|---|---|"]
    for i, s in enumerate(out, 1):
        dt = s["date"]
        status = "written" if s["slug"] in ready else "brief"
        lines.append(f"| {i} | {dt[:10]} | {dt[11:16]} | {', '.join(cname[c] for c in s['categories'])} | {s['title']} | {status} |")
    (ROOT / "docs/content-schedule.md").write_text("\n".join(lines) + "\n")
    times = [s["date"][11:16] for s in out]
    print(len(out), "slots;", len(set(times)), "distinct times;", out[0]["date"], "to", out[-1]["date"])

if __name__ == "__main__":
    make()
