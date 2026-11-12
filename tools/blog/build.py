#!/usr/bin/env python3
"""Static blog generator for ranairwing.com.

  python3 tools/blog/build.py            publish only posts whose date has passed (status: ready)
  python3 tools/blog/build.py --all      include future-dated posts (local preview)
  BLOG_NOW=2026-12-01T00:00:00+08:00 python3 tools/blog/build.py   pretend it is that time

Source: content/posts/*.md (front matter + Markdown), content/categories.json, content/shots.json.
Output: blog/ (index, page/N, category/<slug>[/page/N], <slug>/, feed.xml, style.css, share.js) and /sitemap.xml.
Screenshots live in blog/img/ (see tools/blog/shoot.py) and are never deleted by the build.
"""
import html, json, math, os, re, shutil, sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
import markdown, yaml

ROOT = Path(__file__).resolve().parents[2]
SITE = "https://ranairwing.com"
PER_PAGE = 10
AWST = timezone(timedelta(hours=8))
GA = "G-H0ZE9XML6B"
OUT = ROOT / "blog"

CATS = json.loads((ROOT / "content/categories.json").read_text())
CAT = {c["slug"]: c for c in CATS}
SHOTS = json.loads((ROOT / "content/shots.json").read_text())
e = html.escape
_sp = ROOT / "content/schedule.json"
SCHED = {x["slug"]: x["date"] for x in json.loads(_sp.read_text())} if _sp.exists() else {}

def now():
    v = os.environ.get("BLOG_NOW")
    return datetime.fromisoformat(v) if v else datetime.now(timezone.utc)

def parse_post(path):
    raw = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not m: raise SystemExit(f"{path}: missing front matter")
    fm, body = yaml.safe_load(m.group(1)), m.group(2).strip()
    if "date" not in fm:
        fm["date"] = SCHED.get(path.stem) or sys.exit(f"{path}: no date and no schedule slot")
    for k in ("title", "date", "categories", "summary", "shot"):
        if k not in fm: raise SystemExit(f"{path}: front matter needs '{k}'")
    d = fm["date"]
    if isinstance(d, str): d = datetime.fromisoformat(d)
    if d.tzinfo is None: d = d.replace(tzinfo=AWST)
    fm["dt"] = d
    fm["slug"] = path.stem
    for c in fm["categories"]:
        if c not in CAT: raise SystemExit(f"{path}: unknown category {c}")
    if fm["shot"] not in SHOTS: raise SystemExit(f"{path}: unknown shot {fm['shot']}")
    fm["body"] = body
    fm.setdefault("status", "ready")
    return fm

def auto_caption(r):
    cam = {"orbit": "Orbit camera", "deck": "Deck camera", "island": "Island camera", "approach": "Approach camera", "flyby": "Flyby camera", "cockpit": "Cockpit camera", "chase": "Chase camera"}[r.get("cam", "orbit")]
    h = r.get("hour", 15.5); hh = f"{int(h):02d}:{round(h % 1 * 60):02d}"
    return f"Screenshot from the sim. {cam}, {hh}, sea state {r.get('sea', 3)}, ship at {r.get('speed', 20)} kn."

def render_body(p):
    def shot(m):
        sid, cap = m.group(1), (m.group(2) or "").strip()
        r = SHOTS[sid]
        return f'\n<figure class="shot"><img src="/blog/img/{sid}.jpg" width="1280" height="720" loading="lazy" alt="{e(cap or auto_caption(r))}"><figcaption>{e(cap or auto_caption(r))}</figcaption></figure>\n'
    body = re.sub(r"\{\{shot:\s*([\w-]+)\s*(?:\|([^}]*))?\}\}", shot, p["body"])
    return markdown.markdown(body, extensions=["extra", "sane_lists", "md_in_html"])

def fmt_date(d): return d.astimezone(AWST).strftime("%-d %B %Y")
def iso(d): return d.astimezone(AWST).isoformat(timespec="minutes")
def url(path): return SITE + path

GA_SNIPPET = f"""<script async src="https://www.googletagmanager.com/gtag/js?id={GA}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA}');</script>"""

def page(title, desc, path, body, og_img=None, og_type="website", extra_head=""):
    full_title = title if title.startswith("HMAS") else f"{title} · RAN Air Wing"
    og = og_img or "/blog/img/s01-welcome.jpg"
    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url(path)}">
<link rel="alternate" type="application/rss+xml" title="RAN Air Wing dev blog" href="/blog/feed.xml">
<link rel="stylesheet" href="/blog/style.css">
<meta property="og:site_name" content="RAN Air Wing">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url(path)}">
<meta property="og:image" content="{SITE}{og}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b1622">
{extra_head}
{GA_SNIPPET}
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="/blog/">RAN Air Wing<small>HMAS Melbourne (R21) flight sim · dev blog</small></a>
<nav class="nav" aria-label="Site"><a href="/blog/">Blog</a><a href="/about.html">About</a><a href="/blog/feed.xml">RSS</a><a class="btn" href="/">Fly the sim</a></nav>
</div></header>
<main><div class="wrap">
{body}
</div></main>
<footer><div class="wrap">RAN Air Wing is an independent fan project. Screenshots are from the sim. <a href="/">Fly the sim</a> · <a href="/about.html">About</a> · <a href="/blog/feed.xml">RSS</a> · <a href="mailto:contact@ranairwing.com">contact@ranairwing.com</a> · <a href="https://malgordon.com" rel="noopener">Another Mal Gordon creation</a></div></footer>
<script src="/blog/share.js" defer></script>
</body></html>"""

def chips(cats, link=True):
    return '<p class="chips">' + "".join(f'<a class="chip" href="/blog/category/{c}/">{e(CAT[c]["name"])}</a>' for c in cats) + "</p>"

def card(p):
    return f"""<article class="card"><a href="/blog/{p['slug']}/" tabindex="-1" aria-hidden="true"><img src="/blog/img/{p['shot']}.jpg" width="1280" height="720" loading="lazy" alt=""></a>
<div>{chips(p['categories'])}<h2><a href="/blog/{p['slug']}/">{e(p['title'])}</a></h2><div class="meta"><time datetime="{iso(p['dt'])}">{fmt_date(p['dt'])}</time> · {p['mins']} min read</div><p>{e(p['summary'])}</p></div></article>"""

def pager(base, n, total):
    def href(i): return base if i == 1 else f"{base}page/{i}/"
    if total <= 1: return ""
    out = ['<nav class="pager" aria-label="Pagination">']
    out.append(f'<a href="{href(n-1)}" rel="prev">&larr; Newer</a>' if n > 1 else '<span class="off">&larr; Newer</span>')
    shown = sorted({1, total, *range(max(1, n - 2), min(total, n + 2) + 1)})
    last = 0
    for i in shown:
        if i - last > 1: out.append("<span class=\"off\">…</span>")
        out.append(f'<span class="cur" aria-current="page">{i}</span>' if i == n else f'<a href="{href(i)}">{i}</a>')
        last = i
    out.append(f'<a href="{href(n+1)}" rel="next">Older &rarr;</a>' if n < total else '<span class="off">Older &rarr;</span>')
    out.append("</nav>")
    return "".join(out)

def write(rel, content):
    f = ROOT / rel.lstrip("/"); f.parent.mkdir(parents=True, exist_ok=True); f.write_text(content)

EMPTY = '<p class="panel">The first post goes live soon. <a href="/">Fly the sim</a> in the meantime.</p>'

def listing(posts, base, title, intro_html, desc, counts, active=None):
    pages = max(1, math.ceil(len(posts) / PER_PAGE))
    nav = '<p class="chips">' + f'<a class="chip{" on" if active is None else ""}" href="/blog/">All<small>{len(P)}</small></a>' + "".join(
        f'<a class="chip{" on" if active == c["slug"] else ""}" href="/blog/category/{c["slug"]}/">{e(c["name"])}<small>{counts.get(c["slug"], 0)}</small></a>' for c in CATS if counts.get(c["slug"])) + "</p>"
    for n in range(1, pages + 1):
        chunk = posts[(n - 1) * PER_PAGE: n * PER_PAGE]
        t = title if n == 1 else f"{title} · page {n}"
        links = ""
        if n > 1: links += f'<link rel="prev" href="{url(base if n == 2 else f"{base}page/{n-1}/")}">'
        if n < pages: links += f'<link rel="next" href="{url(f"{base}page/{n+1}/")}">'
        body = f'<section class="intro">{intro_html}</section>{nav}<div class="cards">{"".join(card(p) for p in chunk) or EMPTY}</div>{pager(base, n, pages)}'
        path = base if n == 1 else f"{base}page/{n}/"
        write(path + "index.html", page(t, desc, path, body, og_img=f"/blog/img/{chunk[0]['shot']}.jpg" if chunk else None, extra_head=links))
    return pages

def share_bar(p):
    u = url(f"/blog/{p['slug']}/"); q = lambda s: __import__("urllib.parse").parse.quote(s, safe="")
    t = p["title"]
    links = [("facebook", "Facebook", f"https://www.facebook.com/sharer/sharer.php?u={q(u)}"),
             ("x", "X", f"https://twitter.com/intent/tweet?url={q(u)}&text={q(t)}"),
             ("linkedin", "LinkedIn", f"https://www.linkedin.com/sharing/share-offsite/?url={q(u)}"),
             ("reddit", "Reddit", f"https://www.reddit.com/submit?url={q(u)}&title={q(t)}"),
             ("email", "Email", f"mailto:?subject={q(t)}&body={q(u)}")]
    a = "".join(f'<a data-method="{m}" href="{h}" target="_blank" rel="noopener noreferrer" aria-label="Share on {n}">{n}</a>' for m, n, h in links)
    return f'<div class="share" data-url="{e(u)}" data-title="{e(t)}" data-slug="{p["slug"]}"><span class="label">Share</span>{a}<button type="button" data-copy>Copy link</button><button type="button" data-native hidden>Share…</button></div>'

def post_page(p, newer, older, related):
    path = f"/blog/{p['slug']}/"
    src = ""
    if p.get("sources"):
        src = '<section class="sources"><h3>Sources</h3><ul>' + "".join(
            f'<li><a href="{e(s["url"])}" rel="noopener">{e(s["title"])}</a></li>' if isinstance(s, dict) else f"<li>{e(str(s))}</li>" for s in p["sources"]) + "</ul></section>"
    cta = ""
    if p.get("cta", True):
        cta = '<aside class="panel cta"><p>Launch from the catapult, fly the pattern and land on the angled deck, in your browser.</p><a class="btn" href="/">Fly the sim</a></aside>'
    hero_alt = p.get("hero_alt") or p.get("hero_caption") or auto_caption(SHOTS[p["shot"]])
    cap = p.get("hero_caption") or auto_caption(SHOTS[p["shot"]])
    adj = '<nav class="adj" aria-label="More posts">' + (
        f'<a class="prev" href="/blog/{older["slug"]}/"><span class="label">&larr; Previous</span><span>{e(older["title"])}</span></a>' if older else "<span></span>") + (
        f'<a class="next" href="/blog/{newer["slug"]}/"><span class="label">Next &rarr;</span><span>{e(newer["title"])}</span></a>' if newer else "<span></span>") + "</nav>"
    rel = ""
    if related:
        rel = '<section class="related"><h3>More like this</h3><ul>' + "".join(f'<li><a href="/blog/{r["slug"]}/">{e(r["title"])}</a> <span class="meta">· {fmt_date(r["dt"])}</span></li>' for r in related) + "</ul></section>"
    ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"], "description": p["summary"], "datePublished": iso(p["dt"]), "dateModified": iso(p.get("updated_dt") or p["dt"]),
          "image": f"{SITE}/blog/img/{p['shot']}.jpg", "mainEntityOfPage": url(path), "author": {"@type": "Person", "name": "Mal Gordon"}, "publisher": {"@type": "Organization", "name": "RAN Air Wing"}}
    body = f"""<article class="post">
{chips(p['categories'])}
<h1>{e(p['title'])}</h1>
<div class="meta"><time datetime="{iso(p['dt'])}">{fmt_date(p['dt'])}</time> · {p['mins']} min read</div>
<p class="lede">{e(p['summary'])}</p>
<figure class="hero"><img src="/blog/img/{p['shot']}.jpg" width="1280" height="720" alt="{e(hero_alt)}"><figcaption>{e(cap)}</figcaption></figure>
{p['html']}
{cta}
{src}
{share_bar(p)}
<p class="meta">Filed under {", ".join(f'<a href="/blog/category/{c}/">{e(CAT[c]["name"])}</a>' for c in p["categories"])}</p>
{adj}
{rel}
</article>"""
    head = f'<script type="application/ld+json">{json.dumps(ld)}</script><meta property="article:published_time" content="{iso(p["dt"])}">' + "".join(f'<meta property="article:tag" content="{e(CAT[c]["name"])}">' for c in p["categories"])
    write(path + "index.html", page(p["title"], p["summary"], path, body, og_img=f"/blog/img/{p['shot']}.jpg", og_type="article", extra_head=head))

def main():
    global P
    allp = [parse_post(f) for f in sorted((ROOT / "content/posts").glob("*.md"))]
    t = now()
    show_all = "--all" in sys.argv
    P = sorted([p for p in allp if p["status"] == "ready" and (show_all or p["dt"] <= t)], key=lambda p: p["dt"], reverse=True)
    for p in P:
        p["html"] = render_body(p)
        p["mins"] = max(1, round(len(re.sub(r"<[^>]+>", " ", p["html"]).split()) / 200))
    # clean generated output but keep screenshots
    for child in OUT.iterdir() if OUT.exists() else []:
        if child.name == "img": continue
        shutil.rmtree(child) if child.is_dir() else child.unlink()
    OUT.mkdir(exist_ok=True)
    shutil.copy(ROOT / "tools/blog/blog.css", OUT / "style.css")
    shutil.copy(ROOT / "tools/blog/share.js", OUT / "share.js")
    global EMPTY
    nxt = sorted(p["dt"] for p in allp if p["status"] == "ready" and p["dt"] > t)
    if nxt: EMPTY = f'<p class="panel">The first post goes live on {fmt_date(nxt[0])}. <a href="/">Fly the sim</a> in the meantime.</p>'
    counts = {c["slug"]: sum(c["slug"] in p["categories"] for p in P) for c in CATS}
    intro = f'<h1>RAN Air Wing dev blog</h1><p class="lede">The history of HMAS Melbourne (R21) and her air wing, and the making of a browser flight sim set in 1977&ndash;1982. A new post most days.</p>'
    pages = listing(P, "/blog/", "HMAS Melbourne flight sim dev blog", intro, "History of HMAS Melbourne and her air wing, carrier operations explained, and the dev diary of a browser flight sim.", counts)
    urls = [("/", None), ("/about.html", None), ("/blog/", P[0]["dt"] if P else None)] + [(f"/blog/page/{n}/", None) for n in range(2, pages + 1)]
    for c in CATS:
        cp = [p for p in P if c["slug"] in p["categories"]]
        if not cp: continue
        base = f"/blog/category/{c['slug']}/"
        n = listing(cp, base, f"{c['name']}", f'<h1>{e(c["name"])}</h1><p class="lede">{e(c["description"])}</p>', c["description"], counts, active=c["slug"])
        urls += [(base, cp[0]["dt"])] + [(f"{base}page/{i}/", None) for i in range(2, n + 1)]
    for i, p in enumerate(P):
        newer = P[i - 1] if i > 0 else None
        older = P[i + 1] if i + 1 < len(P) else None
        related = [r for r in P if r is not p and set(r["categories"]) & set(p["categories"])][:3]
        post_page(p, newer, older, related)
        urls.append((f"/blog/{p['slug']}/", p.get("updated_dt") or p["dt"]))
    # RSS
    items = "".join(f"<item><title>{e(p['title'])}</title><link>{url('/blog/'+p['slug']+'/')}</link><guid isPermaLink=\"true\">{url('/blog/'+p['slug']+'/')}</guid><pubDate>{p['dt'].astimezone(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S +0000')}</pubDate>{''.join('<category>'+e(CAT[c]['name'])+'</category>' for c in p['categories'])}<description>{e(p['summary'])}</description></item>" for p in P[:20])
    write("/blog/feed.xml", f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>RAN Air Wing dev blog</title><link>{SITE}/blog/</link><description>HMAS Melbourne (R21) flight sim: history, carrier operations and dev diary.</description><language>en-au</language>{items}</channel></rss>')
    sm = "".join(f"<url><loc>{url(u)}</loc>" + (f"<lastmod>{d.astimezone(AWST).date().isoformat()}</lastmod>" if d else "") + "</url>" for u, d in urls)
    write("/sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>')
    if not (ROOT / "robots.txt").exists():
        write("/robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    missing = [p["shot"] for p in P if not (OUT / "img" / f"{p['shot']}.jpg").exists()]
    print(f"{len(P)} published of {len(allp)} posts ({len(allp)-len(P)} unpublished/future); {pages} pages; at {t.astimezone(AWST):%Y-%m-%d %H:%M} AWST")
    if missing: print("WARNING missing screenshots:", ", ".join(missing))

if __name__ == "__main__":
    main()
