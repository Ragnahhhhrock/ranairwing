#!/usr/bin/env python3
"""Create a dev-diary post for a new sim feature, with a fresh screenshot recipe.

From the latest commit (used by the GitHub Action; subject must start with "feat"):
    python3 tools/blog/feature_post.py --from-head
By hand / from a Claude session:
    python3 tools/blog/feature_post.py --title "Sea King helicopter" --summary "..." --body-file body.md \
        --shot "cam=chase start=approach hour=16 sea=3 speed=22 advance=20" [--categories dev-diary,aircraft]

Commit-message trailers understood with --from-head (all optional):
    Blog-Skip: true                 do not write a post
    Blog-Summary: one line          post summary (default: first body line)
    Blog-Categories: dev-diary,aircraft
    Blog-Shot: cam=chase start=cat hour=15 sea=3 speed=22 advance=2
    Blog-Try: how to try the feature (one line)
The post is dated now (Perth time) so it publishes immediately. Then run shoot.py and build.py.
"""
import argparse, json, re, subprocess, sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AWST = timezone(timedelta(hours=8))
CATS = {c["slug"] for c in json.loads((ROOT / "content/categories.json").read_text())}

def slugify(s): return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")[:60]

def parse_shot(s):
    r = {}
    for kv in s.split():
        k, _, v = kv.partition("=")
        r[k] = float(v) if re.fullmatch(r"-?\d+(\.\d+)?", v) else v
        if isinstance(r[k], float) and r[k].is_integer() and k != "hour": r[k] = int(r[k])
    r.setdefault("cam", "orbit"); r.setdefault("hour", 15.5); r.setdefault("sea", 3); r.setdefault("speed", 20); r.setdefault("advance", 3)
    return r

def git(*a): return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True, check=True).stdout

def from_head():
    subject = git("log", "-1", "--format=%s").strip()
    body = git("log", "-1", "--format=%b").strip()
    files = git("diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").split()
    if not re.match(r"^feat(\(.+\))?!?:", subject, re.I): sys.exit("not a feat commit: nothing to do")
    if any(f.startswith("content/posts/") for f in files): sys.exit("commit already includes a post: nothing to do")
    tr, text = {}, []
    for line in body.splitlines():
        m = re.match(r"^(Blog-[A-Za-z]+):\s*(.*)$", line)
        if m: tr[m.group(1).lower()] = m.group(2).strip()
        elif not re.match(r"^(Co-Authored-By|Claude-Session):", line): text.append(line)
    if tr.get("blog-skip", "").lower() in ("true", "yes", "1"): sys.exit("Blog-Skip set")
    title = re.sub(r"^feat(\(.+\))?!?:\s*", "", subject, flags=re.I).strip()
    title = title[0].upper() + title[1:]
    body = "\n".join(text).strip()
    return dict(title=title, summary=tr.get("blog-summary") or (body.split("\n\n")[0].replace("\n", " ")[:155] if body else f"New in the sim: {title}."),
                body=body, categories=tr.get("blog-categories", "dev-diary").split(","), shot=tr.get("blog-shot", ""), tryit=tr.get("blog-try", ""))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from-head", action="store_true")
    ap.add_argument("--title"); ap.add_argument("--summary"); ap.add_argument("--body-file"); ap.add_argument("--body")
    ap.add_argument("--shot", default=""); ap.add_argument("--categories", default="dev-diary"); ap.add_argument("--try", dest="tryit", default="")
    a = ap.parse_args()
    d = from_head() if a.from_head else dict(title=a.title, summary=a.summary, categories=a.categories.split(","), shot=a.shot, tryit=a.tryit,
                                              body=Path(a.body_file).read_text() if a.body_file else (a.body or ""))
    if not d["title"]: sys.exit("--title required")
    d["categories"] = [c for c in d["categories"] if c in CATS] or ["dev-diary"]
    now = datetime.now(AWST)
    slug = f"{now:%Y%m%d}-{slugify(d['title'])}"
    shot_id = f"feat-{slug}"
    shots_p = ROOT / "content/shots.json"
    shots = json.loads(shots_p.read_text()); shots[shot_id] = parse_shot(d["shot"]); shots_p.write_text(json.dumps(shots, indent=1))
    body = d["body"] or f"A new feature has been added to the sim: {d['title']}."
    if d["tryit"]: body += f"\n\n## Try it\n\n{d['tryit']}"
    body += "\n\nThis post was drafted automatically when the feature was added. Corrections are welcome on the [project's GitHub page](https://github.com/Ragnahhhhrock/ranairwing/issues)."
    fm = {"title": d["title"], "date": now.isoformat(timespec="minutes"), "categories": d["categories"], "summary": d["summary"], "shot": shot_id, "hero_alt": f"Screenshot of the sim showing the new feature: {d['title']}."}
    out = ROOT / "content/posts" / f"{slug}.md"
    out.write_text("---\n" + "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in fm.items()) + "\n---\n" + body + "\n")
    print(f"wrote {out.relative_to(ROOT)} and shot {shot_id}")

if __name__ == "__main__":
    main()
