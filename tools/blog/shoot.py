#!/usr/bin/env python3
"""Capture blog screenshots from the live sim (index.html) using headless Chrome.

Usage: python3 tools/blog/shoot.py [shot_id ...]   (no ids = every missing shot)
       python3 tools/blog/shoot.py --all            (re-shoot everything)
Recipes live in content/shots.json. Output: blog/img/<id>.jpg (1280x720).
"""
import asyncio, json, os, sys, urllib.request
from pathlib import Path
from io import BytesIO
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
SHOTS = json.loads((ROOT / "content/shots.json").read_text())
OUT = ROOT / "blog/img"
THREE = Path(os.environ.get("THREE_JS", "/tmp/three.min.js"))
THREE_URL = "https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"
CHROME = next((p for p in ("/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser") if os.path.exists(p)), None)

SETUP = """(r) => {
  const S = window.__sim, $ = id => document.getElementById(id);
  const set = (id, v) => { const e = $(id); e.value = v; e.dispatchEvent(new Event('input')); };
  if (r.sea !== undefined) set('sSea', r.sea);
  if (r.speed !== undefined) set('sSpd', r.speed);
  if (r.hour !== undefined) set('sTime', r.hour);
  if (r.type) S.setType(r.type);
  if (r.start) S.resetAircraft(r.start);
  if (r.lesson !== undefined) S.startLesson(r.lesson);
  S.setCam(r.cam || 'orbit');
  if (r.view) Object.assign(S.view, r.view);
  if (r.ac) Object.assign(S.ac, r.ac);
  for (const k of (r.keys || [])) S.pressKey(k);
  if (r.advance) S.advance(r.advance);
  if (r.hideHint) $('hint').style.visibility = 'hidden';
  if (r.uiOff) $('bMenu').click();
  if (r.hidePanels) document.querySelectorAll('.panel').forEach(p => p.style.display = 'none');
}"""

async def main(ids, force):
    from playwright.async_api import async_playwright
    if not THREE.exists():
        THREE.write_bytes(urllib.request.urlopen(THREE_URL, timeout=60).read())
    three = THREE.read_bytes()
    OUT.mkdir(parents=True, exist_ok=True)
    todo = [i for i in ids if force or not (OUT / f"{i}.jpg").exists()]
    if not todo:
        print("nothing to shoot"); return
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME, args=["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist", "--no-sandbox"])
        for sid in todo:
            r = SHOTS[sid]
            pg = await b.new_page(viewport={"width": 1280, "height": 720})
            errs = []
            pg.on("pageerror", lambda e: errs.append(str(e)))
            await pg.route("**/three.min.js", lambda route: route.fulfill(body=three, content_type="application/javascript"))
            await pg.route("**/googletagmanager.com/**", lambda route: route.abort())
            await pg.goto("file://" + str(ROOT / "index.html"))
            await pg.wait_for_function("window.__sim")
            await pg.wait_for_timeout(1200)
            await pg.evaluate(SETUP, r)
            await pg.wait_for_timeout(900)
            png = await pg.screenshot()
            Image.open(BytesIO(png)).convert("RGB").save(OUT / f"{sid}.jpg", quality=84, optimize=True, progressive=True)
            print("shot", sid, "ERR " + "; ".join(errs) if errs else "ok")
            await pg.close()
        await b.close()

if __name__ == "__main__":
    args = sys.argv[1:]
    force = "--all" in args
    ids = [a for a in args if not a.startswith("--")] or list(SHOTS)
    asyncio.run(main(ids, force or bool([a for a in args if not a.startswith("--")])))
