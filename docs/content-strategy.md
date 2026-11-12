# Content strategy: RAN Air Wing dev blog

## Purpose
Give people a reason to find, trust and return to ranairwing.com: a browser flight sim of HMAS Melbourne (R21) and her air wing, set 1977-1982. The blog does three jobs.

1. **Search and discovery.** History queries (HMAS Melbourne, A-4G Skyhawk, Fleet Air Arm, carrier operations) bring in aviation and naval-history readers who have not heard of the sim.
2. **Credibility.** Careful, sourced history shows the sim is built with respect for the ship and the people who served.
3. **Retention.** Dev diary and how-to posts turn visitors into players and returning players.

## Audience
- Naval and aviation history enthusiasts, including veterans and families (accuracy matters most).
- Flight-sim players who like carrier operations and classic jets.
- Browser-game and indie-dev followers.

## Pillars and mix (90 days)
| Category | Share | What it is |
|---|---|---|
| Ship history | 20% | HMAS Melbourne from build to disposal, voyages, events |
| Air wing | 20% | Squadrons, people, aircraft in service by era |
| Aircraft | 10% | One profile per type the sim has or plans |
| Carrier operations | 15% | How catapults, angled decks, mirrors and wires work, and how the sim models them |
| Dev diary | 20% | Each feature, fix and decision, with screenshots |
| How to fly | 15% | Guides and tips |

History pieces are researched and sourced before they are scheduled as ready. Dev diary and how-to pieces come from the sim itself.

## Cadence
One post every day from 13 Nov 2026 to 10 Feb 2027 (90 posts), Perth time. Publish times vary day to day (06:00-21:00, never the same minute twice, at least 45 minutes different from the previous day). See `content/schedule.json` and `docs/content-schedule.md`.

## Workflow
- Posts are Markdown in `content/posts/` with front matter (`date`, `categories`, `shot`, `status`).
- `tools/blog/build.py` generates the static site into `blog/`. Future-dated posts are not published until their time.
- A scheduled GitHub Action rebuilds every 30 minutes, so a post goes live within half an hour of its slot.
- **Every new sim feature gets a post.** The feature commit adds a post in `content/posts/` (a `feat:` commit with no post triggers the fallback workflow that drafts one from the commit message and a fresh screenshot). See `CLAUDE.md`.
- Screenshots are captured from the live sim by `tools/blog/shoot.py` from shot recipes in `content/shots.json`.

## Distribution
Share buttons on every post (Facebook, X, LinkedIn, Reddit, email, copy link, native share on mobile), RSS at `/blog/feed.xml`, sitemap at `/sitemap.xml`, Open Graph images from the hero screenshot. The sim's title panel already links to the blog and an About page.

## Measures
GA4 (already on the sim) is on the blog. Watch: blog to sim click-through, top categories, sessions per post, share-button clicks (`share` events), returning visitors.

## Review
Every 30 days: drop or rework the lowest 20% categories by sessions, move slots to what is working, correct any errors readers report.
