# RAN Air Wing

A browser flight simulator of HMAS Melbourne (R21) and her air wing, set 1977-1982. Play it at https://ranairwing.com.

- `index.html` is the whole sim (Three.js r128 from cdnjs).
- `content/` holds the dev blog: posts, categories, screenshot recipes and the 90-day schedule.
- `tools/blog/` builds the blog (`build.py`), captures screenshots from the sim (`shoot.py`), makes the schedule and drafts feature posts.
- `docs/` has the style guide, content strategy and content schedule.
- `blog/` is generated output. Do not edit it by hand.

Blog build: `pip install markdown pyyaml pillow playwright`, then `python3 tools/blog/build.py` (`--all` previews future posts).

Found a mistake in the sim or a post? Open an issue.
