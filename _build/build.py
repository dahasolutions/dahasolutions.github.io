#!/usr/bin/env python3
"""Build the per-app pages.

    python3 _build/build.py            # write <slug>/index.html for every app in content.py + sitemap.xml
    python3 _build/build.py --shots    # also (re)download the App Store screenshots into <slug>/img/

Content lives in content.py (one dict per app), look in THEMES below. formulabook/ is hand-written and
only listed in the sitemap. GitHub Pages skips directories that start with an underscore, so nothing in
_build/ is published.
"""
import colorsys, html, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://dahasolutions.github.io/"
UPDATED = ("2026-11-09", "November 9, 2026")
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).parent))
from content import APPS  # noqa: E402

FONTS = {
    "sans": '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
    "serif": 'ui-serif, "New York", "Iowan Old Style", Georgia, "Times New Roman", serif',
    "rounded": 'ui-rounded, "SF Pro Rounded", "Nunito", "Varela Round", -apple-system, "Segoe UI", sans-serif',
    "mono": 'ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace',
    "slab": 'Rockwell, "Roboto Slab", "Courier New", Georgia, serif',
    "condensed": '"Avenir Next Condensed", "Roboto Condensed", "Arial Narrow", "Helvetica Neue", Arial, sans-serif',
}
LANGS = {"AR": "Arabic", "BN": "Bengali", "CS": "Czech", "DA": "Danish", "DE": "German", "EL": "Greek", "EN": "English",
         "ES": "Spanish", "FI": "Finnish", "FR": "French", "HE": "Hebrew", "HI": "Hindi", "HU": "Hungarian",
         "ID": "Indonesian", "IT": "Italian", "JA": "Japanese", "KO": "Korean", "MS": "Malay", "NB": "Norwegian",
         "NL": "Dutch", "PA": "Punjabi", "PL": "Polish", "PT": "Portuguese", "RO": "Romanian", "RU": "Russian",
         "SV": "Swedish", "TH": "Thai", "TR": "Turkish", "UK": "Ukrainian", "UR": "Urdu", "VI": "Vietnamese",
         "ZH": "Chinese"}
CATEGORY = {"Medical": "HealthApplication", "Health & Fitness": "HealthApplication", "Finance": "FinanceApplication",
            "Business": "BusinessApplication", "Lifestyle": "LifestyleApplication", "Book": "LifestyleApplication",
            "Food & Drink": "LifestyleApplication", "Utilities": "UtilitiesApplication",
            "Productivity": "UtilitiesApplication", "Games": "GameApplication"}


# ---------- colour helpers ----------
def rgb(h):
    h = h.lstrip("#"); return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def hexs(c):
    return "#" + "".join(f"{round(max(0, min(1, v)) * 255):02X}" for v in c)


def mix(a, b, t):
    a, b = rgb(a), rgb(b); return hexs(tuple(a[i] * (1 - t) + b[i] * t for i in range(3)))


def lum(h):
    return sum(w * (v / 12.92 if v <= .03928 else ((v + .055) / 1.055) ** 2.4) for w, v in zip((.2126, .7152, .0722), rgb(h)))


def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True); return (la + .05) / (lb + .05)


def shift(h, target, want, step):
    """Darken (step<0) or lighten (step>0) h until it reaches `want` contrast against target."""
    hh, ll, ss = colorsys.rgb_to_hls(*rgb(h))
    for _ in range(60):
        if contrast(hexs(colorsys.hls_to_rgb(hh, ll, ss)), target) >= want:
            break
        ll = max(0, min(1, ll + step))
    return hexs(colorsys.hls_to_rgb(hh, ll, ss))


def palette(t):
    bg, paper, ink, accent = t["bg"], t.get("paper", "#FFFFFF"), t.get("ink", "#1B1A18"), t["accent"]
    light = {"bg": bg, "paper": paper, "ink": ink, "alt": mix(bg, ink, .045), "line": mix(bg, ink, .12),
             "muted": mix(ink, bg, .34), "accent": shift(accent, bg, 3.2, -.02),
             "accent-ink": shift(accent, bg, 5.2, -.02), "accent-soft": mix(accent, bg, .86)}
    light["on-accent"] = "#FFFFFF" if contrast("#FFFFFF", light["accent"]) >= 3 else ink
    if contrast(light["on-accent"], light["accent"]) < 4.5:
        light["accent"] = shift(light["accent"], light["on-accent"], 4.5, -.02)
    dbg = mix("#121313", accent, .05)
    dark = {"bg": dbg, "paper": mix(dbg, "#FFFFFF", .055), "ink": "#F3F2EF", "alt": mix(dbg, "#FFFFFF", .09),
            "line": mix(dbg, "#FFFFFF", .14), "muted": "#A9A6A1", "accent": shift(accent, dbg, 6.5, .02),
            "accent-ink": shift(accent, dbg, 7.5, .02), "accent-soft": mix(accent, dbg, .8), "on-accent": "#101112"}
    css = lambda d: " ".join(f"--{k}: {v};" for k, v in d.items())
    return css(light), css(dark)


def strip(t):
    kind, cols = t.get("strip", "bands"), t.get("strip_colors") or [t["accent"]]
    if kind == "gradient":
        return f'<div class="strip" style="background:linear-gradient(90deg,{",".join(cols)})" aria-hidden="true"></div>'
    if kind == "ticks":
        return (f'<div class="strip tall" style="background:repeating-linear-gradient(90deg,{cols[1]} 0 2px,transparent 2px 12px),'
                f'repeating-linear-gradient(90deg,{cols[1]} 0 3px,transparent 3px 60px) {cols[0]};background-size:auto 55%,auto 100%;'
                f'background-repeat:repeat-x" aria-hidden="true"></div>')
    if kind == "stripes":
        return (f'<div class="strip tall" style="background:repeating-linear-gradient(-45deg,{cols[0]} 0 14px,{cols[1]} 14px 28px)" '
                'aria-hidden="true"></div>')
    if kind == "dots":
        dots = ",".join(f"radial-gradient(circle at {8 + i * 26}px 50%,{c} 0 5px,transparent 5.5px)" for i, c in enumerate(cols))
        return (f'<div class="strip tall" style="background:{dots};background-size:{len(cols) * 26}px 100%;background-repeat:repeat-x" '
                'aria-hidden="true"></div>')
    return '<div class="strip bands" aria-hidden="true">' + "".join(f'<i style="background:{c}"></i>' for c in cols) + "</div>"


# ---------- page ----------
CSS = """
  :root { @@light@@ --head: @@head@@; --sans: @@sans@@; --r: @@radius@@px; --rs: @@radius_s@@px;
    --shadow: 0 1px 2px rgba(20,20,20,.05), 0 14px 40px rgba(20,20,20,.09); }
  @media (prefers-color-scheme: dark) { :root { @@dark@@ --shadow: 0 1px 2px rgba(0,0,0,.4), 0 14px 40px rgba(0,0,0,.45); } }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: var(--sans); background: var(--bg); color: var(--ink); line-height: 1.6; -webkit-font-smoothing: antialiased; }
  a { color: var(--accent-ink); }
  img { max-width: 100%; height: auto; display: block; }
  .wrap { max-width: 1080px; margin: 0 auto; padding: 0 24px; }
  .narrow { max-width: 760px; }
  .strip { height: 6px; } .strip.tall { height: 14px; } .strip.bands { display: flex; } .strip.bands i { flex: 1; }
  header.top { padding: 18px 0; }
  header.top .wrap { display: flex; justify-content: space-between; align-items: center; }
  .brand { font-weight: 700; letter-spacing: -.01em; color: var(--ink); text-decoration: none; }
  .top a.all { font-size: 14px; color: var(--muted); text-decoration: none; }
  .hero { padding: 28px 0 72px; }
  .hero.split .wrap { display: grid; grid-template-columns: 1.05fr .95fr; gap: 56px; align-items: center; }
  .hero.center { text-align: center; padding-bottom: 0; }
  .hero.center .app, .hero.center .stores { justify-content: center; }
  .hero.center .lead { margin-left: auto; margin-right: auto; max-width: 640px; }
  .app { display: flex; align-items: center; gap: 14px; margin-bottom: 22px; text-align: left; }
  .app img { width: 56px; height: 56px; border-radius: 13px; box-shadow: var(--shadow); }
  .app b { display: block; font-size: 17px; letter-spacing: -.01em; }
  .app span { font-size: 14px; color: var(--muted); }
  h1, h2 { font-family: var(--head); font-weight: @@head_weight@@; letter-spacing: @@head_track@@; text-transform: @@head_case@@; }
  h1 { font-size: clamp(@@h1_min@@px, 5.2vw, @@h1_max@@px); line-height: 1.07; }
  h1 em { font-style: @@em_style@@; color: var(--accent-ink); }
  h2 { font-size: clamp(25px, 3.5vw, @@h2_max@@px); line-height: 1.15; margin-top: 8px; }
  .lead { margin-top: 20px; font-size: 18px; color: var(--muted); max-width: 520px; }
  .stores { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 28px; }
  .stores a { display: inline-flex; flex-direction: column; justify-content: center; min-height: 52px; padding: 8px 22px;
    border-radius: var(--rs); text-decoration: none; font-weight: 600; font-size: 16px; line-height: 1.2; text-align: left; }
  .stores a small { font-weight: 500; font-size: 11px; opacity: .8; }
  .stores a.ios { background: var(--accent); color: var(--on-accent); }
  .stores a.play { background: var(--paper); color: var(--ink); border: 1px solid var(--line); }
  .stores a:hover { transform: translateY(-1px); }
  .facts { margin-top: 18px; font-size: 14px; color: var(--muted); }
  .phones { position: relative; height: 560px; }
  .phones img { position: absolute; width: 262px; border-radius: 26px; border: 1px solid var(--line); box-shadow: var(--shadow); background: var(--alt); }
  .phones img:nth-child(1) { right: 6%; top: 44px; transform: rotate(4deg); }
  .phones img:nth-child(2) { left: 6%; top: 0; transform: rotate(-3deg); }
  .row3 { display: flex; justify-content: center; gap: 22px; margin-top: 48px; align-items: flex-end; overflow: hidden; height: 470px; }
  .row3 img { width: 250px; border-radius: 26px 26px 0 0; border: 1px solid var(--line); border-bottom: 0; box-shadow: var(--shadow); background: var(--alt); align-self: flex-start; }
  .row3 img:nth-child(2) { margin-top: 0; } .row3 img:nth-child(1), .row3 img:nth-child(3) { margin-top: 46px; }
  section { padding: 72px 0; }
  section.alt { background: var(--paper); border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); }
  .eyebrow { font-size: 12px; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; color: var(--accent-ink); font-family: var(--sans); }
  .sub { margin-top: 12px; color: var(--muted); font-size: 17px; max-width: 640px; }
  .feat h3, .step h3 { font-size: 17px; letter-spacing: -.01em; }
  .feat p, .step p { color: var(--muted); font-size: 15px; margin-top: 6px; }
  .feat .n { font-family: var(--head); color: var(--accent-ink); font-size: 15px; display: block; margin-bottom: 6px; }
  .feats { display: grid; grid-template-columns: repeat(3, 1fr); margin-top: 40px; }
  .feats.ruled { border-top: 1px solid var(--line); border-left: 1px solid var(--line); }
  .feats.ruled .feat { padding: 26px 24px 28px; border-right: 1px solid var(--line); border-bottom: 1px solid var(--line); }
  .feats.cards { gap: 18px; }
  .feats.cards .feat { padding: 24px; background: var(--bg); border: 1px solid var(--line); border-radius: var(--r); }
  .feats.rows { grid-template-columns: repeat(2, 1fr); gap: 0 56px; }
  .feats.rows .feat { padding: 20px 0; border-top: 1px solid var(--line); display: grid; grid-template-columns: 40px 1fr; }
  .feats.rows .feat .n { grid-row: span 2; font-size: 20px; }
  .extra { margin-top: 40px; display: grid; grid-template-columns: repeat(2, 1fr); gap: 18px; }
  .extra div { border: 1px solid var(--line); border-radius: var(--r); padding: 18px 20px; background: var(--paper); }
  section.alt .extra div { background: var(--bg); }
  .extra b { display: block; font-size: 16px; } .extra span { color: var(--muted); font-size: 15px; }
  .steps { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; margin-top: 40px; counter-reset: s; }
  .step { counter-increment: s; }
  .step::before { content: counter(s); display: grid; place-items: center; width: 34px; height: 34px; border-radius: 50%;
    background: var(--accent-soft); color: var(--accent-ink); font-weight: 700; margin-bottom: 12px; }
  .shots { display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; margin-top: 40px; }
  .shots figure { border-radius: var(--r); overflow: hidden; border: 1px solid var(--line); background: var(--alt); }
  .shots figcaption { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); }
  .ticks { list-style: none; margin-top: 24px; }
  .ticks li { position: relative; padding: 11px 0 11px 30px; border-top: 1px solid var(--line); color: var(--muted); }
  .ticks li:first-child { border-top: 0; }
  .ticks li::before { content: ""; position: absolute; left: 4px; top: 18px; width: 12px; height: 6px;
    border-left: 2px solid var(--accent); border-bottom: 2px solid var(--accent); transform: rotate(-45deg); }
  .ticks b { color: var(--ink); font-weight: 600; }
  .note { margin-top: 24px; font-size: 14px; color: var(--muted); border-left: 3px solid var(--line); padding-left: 14px; }
  .faq { margin-top: 32px; border-top: 1px solid var(--line); }
  .faq details { border-bottom: 1px solid var(--line); }
  .faq summary { cursor: pointer; list-style: none; padding: 18px 36px 18px 0; font-weight: 600; font-size: 17px; position: relative; }
  .faq summary::-webkit-details-marker { display: none; }
  .faq summary::after { content: "+"; position: absolute; right: 6px; top: 14px; font-size: 22px; font-weight: 400; color: var(--accent-ink); }
  .faq details[open] summary::after { content: "–"; }
  .faq p { padding: 0 36px 20px 0; color: var(--muted); }
  .spec { margin-top: 28px; display: grid; grid-template-columns: 160px 1fr; border-top: 1px solid var(--line); font-size: 15px; }
  .spec dt, .spec dd { padding: 12px 0; border-bottom: 1px solid var(--line); } .spec dt { color: var(--muted); }
  .cta { text-align: center; } .cta .stores { justify-content: center; }
  .cta img.icon { width: 72px; height: 72px; border-radius: 17px; margin: 0 auto 18px; box-shadow: var(--shadow); }
  footer { padding: 28px 0 44px; color: var(--muted); font-size: 14px; }
  footer .wrap { display: flex; flex-wrap: wrap; gap: 12px 24px; justify-content: space-between; }
  footer a { color: var(--muted); }
  @media (max-width: 880px) {
    .hero.split .wrap { grid-template-columns: 1fr; gap: 36px; }
    .phones { height: 480px; max-width: 420px; margin: 0 auto; width: 100%; } .phones img { width: 220px; }
    .feats, .feats.rows { grid-template-columns: repeat(2, 1fr); } .feats.rows { gap: 0 32px; }
    .steps { grid-template-columns: 1fr; } .shots { grid-template-columns: repeat(2, 1fr); }
    .row3 { height: 380px; gap: 14px; } .row3 img { width: 200px; }
    section { padding: 56px 0; }
  }
  @media (max-width: 560px) {
    .feats, .feats.rows, .extra { grid-template-columns: 1fr; }
    .spec { grid-template-columns: 1fr; } .spec dt { border-bottom: 0; padding-bottom: 0; }
    .phones { height: 400px; } .phones img { width: 180px; }
    .row3 { height: 300px; } .row3 img { width: 150px; border-radius: 18px 18px 0 0; } .row3 img:nth-child(3) { display: none; }
  }
"""


def e(s):
    return html.escape(s, quote=True)


def rich(s):
    """Content strings may carry <b>/<em>; everything else is plain text."""
    return e(s).replace("&lt;b&gt;", "<b>").replace("&lt;/b&gt;", "</b>").replace("&lt;em&gt;", "<em>").replace("&lt;/em&gt;", "</em>")


def shots_for(app):
    d = ROOT / app["slug"] / "img"
    return sorted(p.name for p in d.glob("shot-*.webp")) if d.exists() else []


def langs_text(codes):
    names, seen = [], set()
    for c in codes:
        n = LANGS.get(c, c)
        if n not in seen:
            seen.add(n); names.append(n)
    if "ZH" in codes and codes.count("ZH") > 1:
        names[names.index("Chinese")] = "Chinese (Simplified and Traditional)"
    names = ["English"] + sorted(n for n in names if n != "English")
    return len(codes), ", ".join(names)


def page(app):
    t, slug = app["theme"], app["slug"]
    light, dark = palette(t)
    font = FONTS[t.get("font", "serif")]
    css = CSS
    for k, v in {"light": light, "dark": dark, "head": font, "sans": FONTS["rounded"] if t.get("body") == "rounded" else FONTS["sans"],
                 "radius": t.get("radius", 18), "radius_s": min(t.get("radius", 18), 14),
                 "head_weight": t.get("weight", 700), "head_track": t.get("track", "-.02em"), "head_case": t.get("case", "none"),
                 "h1_min": t.get("h1", (34, 54))[0], "h1_max": t.get("h1", (34, 54))[1], "h2_max": t.get("h2", 36),
                 "em_style": t.get("em", "italic")}.items():
        css = css.replace(f"@@{k}@@", str(v))
    url = BASE + slug + "/"
    ios = f"https://apps.apple.com/app/id{app['ios']}"
    play = f"https://play.google.com/store/apps/details?id={app['play']}&referrer=utm_source%3Ddahasolutions%26utm_medium%3Dsite"
    stores = (f'<div class="stores"><a class="ios" href="{ios}"><small>Download on the</small>App Store</a>'
              f'<a class="play" href="{e(play)}"><small>Get it on</small>Google Play</a></div>')
    icon = f"../assets/icons/{app['icon']}.png"
    shots = shots_for(app)
    alt = lambda i: e(app["shots_alt"][i] if i < len(app.get("shots_alt", [])) else f"{app['name']} screenshot {i + 1}")
    img = lambda i, lazy=True: (f'<img src="img/{shots[i]}" width="660" height="1434" alt="{alt(i)}"'
                                + (' loading="lazy"' if lazy else "") + ">")
    hero_kind = t.get("hero", "split")
    head = (f'<div class="app"><img src="{icon}" alt="{e(app["name"])} app icon" width="56" height="56">'
            f'<div><b>{e(app["name"])}</b><span>{e(app["kind"])}</span></div></div>'
            f'<h1>{rich(app["h1"])}</h1><p class="lead">{rich(app["lead"])}</p>{stores}<p class="facts">{e(app["facts"])}</p>')
    if hero_kind == "center":
        hero = (f'<section class="hero center"><div class="wrap">{head}'
                + (f'<div class="row3">{img(1, False)}{img(0, False)}{img(2, False)}</div>' if len(shots) >= 3 else "") + "</div></section>")
        gallery = shots[3:] and list(range(len(shots)))[:4]
    else:
        hero = (f'<section class="hero split"><div class="wrap"><div>{head}</div>'
                + (f'<div class="phones">{img(1, False)}{img(0, False)}</div>' if len(shots) >= 2 else "") + "</div></section>")
        gallery = list(range(len(shots)))[:4]
    fstyle = t.get("features", "ruled")
    feats = "".join(f'<div class="feat"><span class="n">{i:02d}</span><h3>{rich(a)}</h3><p>{rich(b)}</p></div>'
                    for i, (a, b) in enumerate(app["features"], 1))
    extra = ""
    if app.get("extra"):
        ex = app["extra"]
        extra = (f'<section><div class="wrap"><p class="eyebrow">{e(ex["eyebrow"])}</p><h2>{rich(ex["title"])}</h2>'
                 + (f'<p class="sub">{rich(ex["sub"])}</p>' if ex.get("sub") else "")
                 + '<div class="extra">' + "".join(f"<div><b>{rich(a)}</b><span>{rich(b)}</span></div>" for a, b in ex["items"])
                 + "</div></div></section>")
    steps = ""
    if app.get("steps"):
        steps = ('<div class="steps">' + "".join(f'<div class="step"><h3>{rich(a)}</h3><p>{rich(b)}</p></div>' for a, b in app["steps"])
                 + "</div>")
    figs = "".join(f"<figure>{img(i)}<figcaption>{alt(i)}</figcaption></figure>" for i in (gallery or []))
    how = ""
    if steps or figs:
        how = (f'<section{"" if extra else ""}><div class="wrap"><p class="eyebrow">{e(app.get("how_eyebrow", "How it works"))}</p>'
               f'<h2>{rich(app.get("how_title", "See it in use"))}</h2>{steps}'
               + (f'<div class="shots">{figs}</div>' if figs else "") + "</div></section>")
    ticks = "".join(f"<li>{rich(x)}</li>" for x in app["keep"])
    note = f'<p class="note">{rich(app["note"])}</p>' if app.get("note") else ""
    n_lang, lang_names = langs_text(app["langs"])
    platforms = f"iPhone{' and iPad' if app.get('ipad') else ''} (iOS {app['minos'].rstrip('.0') if app['minos'].endswith('.0') else app['minos']} or later) · Android"
    faq = list(app["faq"]) + [("Which devices and languages does " + app["name"] + " support?",
                               f"{platforms.replace(' · ', ' and ')}. " + (f"The app is available in {n_lang} languages: {lang_names}."
                                                                             if n_lang > 1 else "The app is in English."))]
    faq_html = "".join(f'<details{" open" if i == 0 else ""}><summary>{e(q)}</summary><p>{rich(a)}</p></details>' for i, (q, a) in enumerate(faq))
    priv = "privacy/" if (ROOT / slug / "privacy").exists() else "../privacy-page/"
    supp = "support/" if (ROOT / slug / "support").exists() else "../support/"
    ld_app = {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": app["store_name"], "alternateName": app["name"],
              "description": app["desc"], "applicationCategory": CATEGORY.get(app["genre"], "UtilitiesApplication"),
              "operatingSystem": f"iOS {app['minos']} or later, Android", "url": url, "image": BASE + f"assets/icons/{app['icon']}.png",
              "screenshot": [url + "img/" + s for s in shots[:4]],
              "downloadUrl": [ios, f"https://play.google.com/store/apps/details?id={app['play']}"],
              "inLanguage": sorted(set(c.lower() for c in app["langs"])),
              "audience": {"@type": "Audience", "audienceType": app["audience"]},
              "author": {"@type": "Person", "name": "Ho Van Dai", "url": BASE},
              "featureList": [a for a, _ in app["features"]]}
    strip_tags = lambda s: s.replace("<b>", "").replace("</b>", "").replace("<em>", "").replace("</em>", "")
    ld_faq = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in faq]}
    og = f'<meta property="og:image" content="{url}img/{shots[0]}">' if shots else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(app["title"])}</title>
<meta name="description" content="{e(app["desc"])}">
<link rel="canonical" href="{url}">
<meta name="apple-itunes-app" content="app-id={app["ios"]}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(app["title"])}">
<meta property="og:description" content="{e(app["desc"])}">
<meta property="og:url" content="{url}">
{og}
<link rel="icon" href="{icon}">
<script type="application/ld+json">{json.dumps(ld_app, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(ld_faq, ensure_ascii=False)}</script>
<style>{css}</style>
</head>
<body>
{strip(t)}
<header class="top"><div class="wrap"><a class="brand" href="../">Ho Van Dai</a><a class="all" href="../">All apps</a></div></header>
<main>
{hero}
<section class="alt"><div class="wrap"><p class="eyebrow">{e(app.get("feat_eyebrow", "What it does"))}</p><h2>{rich(app["feat_title"])}</h2>
{f'<p class="sub">{rich(app["feat_sub"])}</p>' if app.get("feat_sub") else ""}
<div class="feats {fstyle}">{feats}</div></div></section>
{extra}
{how}
<section class="alt"><div class="wrap narrow"><p class="eyebrow">{e(app.get("keep_eyebrow", "Your data"))}</p><h2>{rich(app["keep_title"])}</h2>
<ul class="ticks">{ticks}</ul>{note}</div></section>
<section><div class="wrap narrow"><p class="eyebrow">Questions</p><h2>Before you download</h2>
<div class="faq">{faq_html}</div>
<dl class="spec"><dt>Made for</dt><dd>{e(app["audience"])}</dd><dt>Platforms</dt><dd>{e(platforms)}</dd>
<dt>Languages</dt><dd>{e(lang_names if n_lang <= 8 else f"{n_lang}, including " + ", ".join(lang_names.split(", ")[:6]))}</dd>
<dt>Category</dt><dd>{e(app["genre"])}</dd><dt>Developer</dt><dd>Ho Van Dai</dd>
<dt>Page updated</dt><dd><time datetime="{UPDATED[0]}">{UPDATED[1]}</time></dd></dl></div></section>
<section class="alt cta"><div class="wrap narrow"><img class="icon" src="{icon}" alt="" width="72" height="72" loading="lazy">
<h2>{rich(app["cta"])}</h2>{stores}</div></section>
</main>
<footer><div class="wrap"><div>© 2026 Ho Van Dai</div><div><a href="../">Home</a> &nbsp;·&nbsp; <a href="{priv}">Privacy Policy</a> &nbsp;·&nbsp; <a href="{supp}">Support</a></div></div></footer>
</body>
</html>
"""


def fetch_shots(app, raw):
    d = ROOT / app["slug"] / "img"; d.mkdir(parents=True, exist_ok=True)
    for i, u in enumerate(raw["shots"][:4], 1):
        src = u.rsplit("/", 1)[0] + "/660x1434bb.webp"
        out = d / f"shot-{i}.webp"
        subprocess.run(["curl", "-s", "-m", "60", "-o", str(out), src], check=True)
        print("  ", out.relative_to(ROOT), out.stat().st_size // 1024, "KB")


def main():
    raw = {}
    if "--shots" in sys.argv:
        ids = ",".join(a["ios"] for a in APPS)
        out = subprocess.run(["curl", "-s", "-m", "40", f"https://itunes.apple.com/lookup?country=us&id={ids}"], capture_output=True, text=True).stdout
        raw = {str(r["trackId"]): {"shots": r.get("screenshotUrls", [])} for r in json.loads(out)["results"]}
    for app in APPS:
        if raw:
            fetch_shots(app, raw[app["ios"]])
        (ROOT / app["slug"]).mkdir(exist_ok=True)
        (ROOT / app["slug"] / "index.html").write_text(page(app))
        print("built", app["slug"], len(shots_for(app)), "shots")
    pages = ["", "formulabook/"] + [a["slug"] + "/" for a in APPS] + ["privacy-page/", "support/"]
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                      + "".join(f"  <url><loc>{BASE}{u}</loc><lastmod>{UPDATED[0]}</lastmod></url>\n" for u in pages) + "</urlset>\n")


main()
