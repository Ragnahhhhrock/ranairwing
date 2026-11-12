---
title: "Behind the blog: how posts are scheduled"
categories: [dev-diary]
summary: "Markdown files, a small generator and a scheduled job: how this blog publishes a post at a different time each day."
shot: s32-behind
hero_alt: "HMAS Melbourne seen from the orbit camera at a distance, on a sea at sea state 4."
---
This blog has no database and no server. It is a set of static pages on the same host as the sim.

## The pieces

- **Posts.** Markdown files in the project, each with a title, summary, categories and a screenshot.
- **A generator.** A small script turns the files into HTML pages: the home page, category pages, the posts, an RSS feed and a sitemap.
- **A schedule.** Each post has a publish time, in Perth time. The generator leaves out any post whose time is still ahead.
- **A timer.** A scheduled job runs the generator every 30 minutes and commits the result, so a post appears within half an hour of its time.

## Different times each day

The 90 publish times were chosen at random between 06:10 and 20:50, never on a 5-minute mark and never twice. Consecutive days are at least an hour apart. The full list is in the project's content schedule.

## Pagination and categories

The home page shows 10 posts per page, with newer and older links and numbered pages. Each category has its own paginated list. Every post carries its category tags and a row of share buttons: Facebook, X, LinkedIn, Reddit, email and a copy-link button, plus the phone's own share sheet where one is available.

## Screenshots

Each post's screenshot is taken from the live sim by a script, from a recipe that names the camera, time, sea state and ship speed. See [testing a flight sim without a pilot](/blog/testing-a-flight-sim-without-a-pilot/).

## New features get posts

When a new feature is added to the sim, a post about it is added in the same change, with a fresh screenshot. If a feature change arrives without a post, the timer job drafts one from the change description. A blog that does not keep up with the sim is not much use.
