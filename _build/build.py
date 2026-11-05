# Builds the static prototype into the parent folder: python -I _build/build.py
# Every page shares one layout(). Folk motifs (sprite + hero tree) are our own drawings in the Enjoy Moldova logo style.
import json, os, re, html, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import (SITE, CATEGORIES, TOURS, PAGES, BLOG_CATS, INTERESTS, TRIP_TAGS, TRIP_ORDER, DESTINATIONS, NEW_SLUGS,
                     PAGE_REDIRECTS, CELLAR_TOURS, TRANSNISTRIA_TOURS, HIKING_TOURS, RELATED_TOURS, DEST_KEYWORDS, ITINERARIES, POIS, DEST_KIND,
                     DEST_ROAD_KM)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = lambda f: json.load(open(os.path.join(HERE, 'data', f), encoding='utf8'))
SITE_TOURS = DATA('tours_site.json')
SITE_PAGES = {p['slug']: p for p in DATA('pages.json')}
POSTS = DATA('posts.json')
e = html.escape
BY_SLUG = {t['slug']: t for t in TOURS}
PROTOTYPE = True  # preview copy: keep Google off until launch
REVIEWED = '24 October 2026'
TAGLINE = 'Country shaped like a bunch of grapes · Unique terroir · Passion for wine'  # the brochures' slogan

WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2zm5.3 14.2c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.3 0 .5l-.4.6-.3.4c-.1.1-.2.3 0 .5.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.3 2.4 1.5.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l1.9.9c.3.1.5.2.5.3.1.2.1.7-.1 1.4z"/></svg>'

# Folk icon sprite: thick rounded strokes like the logo; stroke/fill come from CSS (currentColor)
SPRITE = '''<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
<symbol id="f-glass" viewBox="0 0 48 48"><path d="M13 5h22v12a11 11 0 0 1-22 0z" fill="currentColor" stroke="none" opacity=".28"/><path d="M13 5h22v12a11 11 0 0 1-22 0zM24 28v12M15 42h18"/></symbol>
<symbol id="f-tulip" viewBox="0 0 48 48"><path d="M10 10l7 5 7-8 7 8 7-5v14L24 36 10 24z" fill="currentColor" stroke="none" opacity=".28"/><path d="M10 10l7 5 7-8 7 8 7-5v14L24 36 10 24zM24 36v8M24 18l4 4-4 4-4-4z"/></symbol>
<symbol id="f-romb" viewBox="0 0 48 48"><path d="M24 4l20 20-20 20L4 24z"/><path d="M24 16l8 8-8 8-8-8z" fill="currentColor"/></symbol>
<symbol id="f-sun" viewBox="0 0 48 48"><circle cx="24" cy="24" r="8"/><path d="M24 4v6M24 38v6M4 24h6M38 24h6M10 10l4 4M34 34l4 4M38 10l-4 4M10 38l4-4"/></symbol>
<symbol id="f-bird" viewBox="0 0 48 48"><path d="M6 30a18 18 0 0 1 36 0M13 35a11 11 0 0 1 22 0M20 40a4 4 0 0 1 8 0"/></symbol>
<symbol id="f-tree" viewBox="0 0 48 48"><path d="M24 45V10M24 20l-9-9M24 20l9-9M24 31l-12-10M24 31l12-10M24 41l-8-6M24 41l8-6"/><circle cx="24" cy="6" r="3.5" fill="currentColor"/></symbol>
<symbol id="f-tower" viewBox="0 0 48 48"><path d="M12 44V21M36 44V21M7 44h34M12 21h24M12 21v-9h5v4h5v-4h4v4h5v-4h5v9M20 44v-8a4 4 0 0 1 8 0v8"/></symbol>
<symbol id="f-star" viewBox="0 0 48 48"><path d="M24 5l5.6 12.4L43 19l-10 9.3L35.6 42 24 35.3 12.4 42 15 28.3 5 19l13.4-1.6z"/></symbol>
<symbol id="f-flower" viewBox="0 0 48 48"><circle cx="24" cy="13" r="7"/><circle cx="35" cy="24" r="7"/><circle cx="24" cy="35" r="7"/><circle cx="13" cy="24" r="7"/><path d="M21 21h6v6h-6z" fill="currentColor"/></symbol>
<symbol id="f-bowl" viewBox="0 0 48 48"><path d="M6 25h36a18 18 0 0 1-36 0zM18 17c0-4 4-4 4-9M27 17c0-4 4-4 4-9"/></symbol>
<symbol id="f-hook" viewBox="0 0 48 48"><path d="M10 12h24M10 24h24M10 12v26M22 24v14M34 12v6"/></symbol>
<symbol id="f-route" viewBox="0 0 48 48"><path d="M8 40c12 0 6-14 16-14s4-14 16-14"/><circle cx="8" cy="40" r="4"/><circle cx="40" cy="12" r="4" fill="currentColor"/></symbol>
<symbol id="f-leaf" viewBox="0 0 48 48"><path d="M5 34l11-13h27L32 34z" fill="currentColor" stroke="none" opacity=".28"/><path d="M5 34l11-13h27L32 34z"/></symbol>
<symbol id="f-grapes" viewBox="0 0 48 48"><path d="M24 10V3M24 6c4-4 10-3 12 1"/><circle cx="14" cy="16" r="5"/><circle cx="24" cy="16" r="5"/><circle cx="34" cy="16" r="5"/><circle cx="19" cy="26" r="5"/><circle cx="29" cy="26" r="5"/><circle cx="24" cy="36" r="5" fill="currentColor"/></symbol>
<symbol id="f-church" viewBox="0 0 48 48"><path d="M24 3v7M21 6h6M24 10c-6 4-9 8-9 12h18c0-4-3-8-9-12zM15 22h18v22H15zM21 44v-7a3 3 0 0 1 6 0v7M7 44h34"/></symbol>
<symbol id="f-fortress" viewBox="0 0 48 48"><path d="M8 44V18h6v-5h5v5h10v-5h5v5h6v26zM8 27h32M20 44v-9a4 4 0 0 1 8 0v9"/></symbol>
<symbol id="f-heart" viewBox="0 0 48 48"><path d="M24 42L8 26a8.5 8.5 0 0 1 16-12 8.5 8.5 0 0 1 16 12z"/><path d="M24 20l5 5-5 5-5-5z" fill="currentColor"/></symbol>
<symbol id="f-bottle" viewBox="0 0 48 48"><path d="M20 4h8M21 4v9l-5 6v23a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V19l-5-6V4M16 26h16M16 36h16"/></symbol>
</svg>'''


def ic(name, cls='ic'):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#{name}"/></svg>'


# ---------------------------------------------------------------- responsive images
# every /img/*.jpg gets WebP copies at these widths in /img/r/<width>/ (made by make_responsive() at build time)
SIZES = (480, 960, 1600)


def rsrc(path, w):
    """'/img/tours/x.jpg' -> '/img/r/960/tours/x.webp'; external URLs pass through."""
    if not path.startswith('/img/') or path.endswith('.svg'):
        return path
    return f"/img/r/{w}/{path[5:].rsplit('.', 1)[0]}.webp"


def pic(path, alt='', sizes='(max-width: 640px) 90vw, 400px', cls='ph-img', eager=False):
    """<img> with srcset; lazy unless it is the first thing on screen."""
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    if not path.startswith('/img/'):
        return f'<img class="{cls}" src="{path}" alt="{e(alt)}" {load} decoding="async">'
    srcset = ', '.join(f'{rsrc(path, w)} {w}w' for w in SIZES)
    return f'<img class="{cls}" src="{rsrc(path, 960)}" srcset="{srcset}" sizes="{sizes}" alt="{e(alt)}" {load} decoding="async">'


def make_responsive():
    from PIL import Image
    made = 0
    for dp, _, fs in os.walk(os.path.join(ROOT, 'img')):
        if os.sep + 'r' in dp[len(ROOT):] or dp.endswith(os.sep + 'r'):
            continue
        for f in fs:
            if not f.lower().endswith(('.jpg', '.jpeg', '.png')):
                continue
            src = os.path.join(dp, f)
            rel = os.path.relpath(src, os.path.join(ROOT, 'img')).replace('\\', '/').rsplit('.', 1)[0]
            for w in SIZES:
                out = os.path.join(ROOT, 'img', 'r', str(w), rel + '.webp')
                if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(src):
                    continue
                os.makedirs(os.path.dirname(out), exist_ok=True)
                im = Image.open(src).convert('RGB')
                if im.width > w:
                    im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
                im.save(out, 'WEBP', quality=72, method=6)
                made += 1
    return made


# ---------------------------------------------------------------- tour data helpers
def p_for(t, pax):
    return next((p['eur'] for p in (t.get('price_table') or {}).get('prices', []) if p['pax'] == pax), None)


for t in TOURS:
    s = SITE_TOURS.get(t['slug'], {})
    t.setdefault('images', ['/img/tours/' + i for i in s.get('images', [])] or ['/img/hero-vineyard.jpg'])
    t['price_table'] = s.get('price_table')
    if t['price_table']:
        t['price_low'] = min(p['eur'] for p in t['price_table']['prices'])
        t['price2'] = p_for(t, 2)
        t.setdefault('price_from', t['price_low'])
    t.setdefault('duration', 'Multi-day' if t['kind'] == 'multi' else 'Full day')
    if t['kind'] == 'multi':  # site lists the multi-day highlights as <li>
        t.setdefault('highlights', [b[1] for b in s.get('blocks', []) if b[0] == 'li'])
    t['url'] = f"/tours/{NEW_SLUGS.get(t['slug'], t['slug'])}/"

CAT_ICON = {'multi-day-tours': 'f-route', 'day-trips': 'f-sun', 'wine-tours': 'f-glass', 'culture-heritage': 'f-tower', 'nature-countryside': 'f-tree'}
INT_ICON = {'wine': 'f-glass', 'history': 'f-tower', 'soviet': 'f-star', 'nature': 'f-tree', 'villages': 'f-flower', 'food': 'f-bowl'}

SKIP = re.compile(r'^(highlights of the tour|tour package price|choose wine tours|tour details|note\s*:|nb!|book wine tours)', re.I)


def tour_body(t):
    """Site description paragraphs, minus what the page already shows elsewhere (title, prices, notes, highlights)."""
    out, bullets = [], []
    blocks = SITE_TOURS.get(t['slug'], {}).get('blocks', [])
    wineries = bool(t.get('wineries'))
    for i, (tag, s) in enumerate(blocks):
        if tag == 'li' or SKIP.match(s) or (i == 0 and tag.startswith('h')) or (s.isupper() and len(s) < 90) or (wineries and s.isupper()):
            continue
        s = re.sub(r'^([A-Z]) (?=[a-z])', r'\1', s)  # site has drop-cap leftovers like "O n the way"
        if s.startswith('*'):
            bullets.append(s.lstrip('* ').capitalize()); continue
        if bullets:
            out.append('<ul class="ticks">' + ''.join(f'<li>{e(b)}</li>' for b in bullets) + '</ul>'); bullets = []
        out.append(f'<h3>{e(s)}</h3>' if tag in ('h3', 'h4', 'h5') else f'<p>{e(s)}</p>')
    if bullets:
        out.append('<ul class="ticks">' + ''.join(f'<li>{e(b)}</li>' for b in bullets) + '</ul>')
    return '\n'.join(out)


def card_price(t):
    if t.get('price2'):
        return f'<span class="price">€{t["price2"]}<small> /person for 2</small><em>groups from €{t["price_low"]}</em></span>'
    if t.get('price_from'):
        return f'<span class="price"><small>from</small> €{t["price_from"]}<small> /person</small></span>'
    return '<span class="price"><small>Ask for price</small></span>'


def card(t):
    badge = f'<span class="badge">{e(t["badge"])}</span>' if t.get('badge') else ''
    return f'''<a class="card" href="{t['url']}" data-cats="{' '.join(t['cats'])}">
<div class="ph">{pic(t['images'][0], t['title'])}{badge}<span class="dur">{e(t["duration"])}</span></div>
<div class="body"><h3>{e(t['title'])}</h3><p class="meta">{e(t['card'])}</p>
<div class="foot">{card_price(t)}<span class="more">View tour →</span></div></div></a>'''


def wa(msg, label='Chat on WhatsApp', cls='btn btn-wa'):
    return f'<a class="{cls} js-wa" href="#" data-msg="{e(msg)}">{WA_SVG}{e(label)}</a>'


def quote_form(selected=None, compact=False, button='Send my request'):
    opts = ''.join(f'<option{" selected" if t["title"] == selected else ""}>{e(t["title"])}</option>' for t in TOURS)
    opts += f'<option{" selected" if selected == "custom" else ""}>Custom trip / not sure yet</option>'
    return f'''<form class="quote js-form" action="/thank-you/" novalidate>
<div class="full"><label for="f-tour">Which tour?</label><select id="f-tour" name="tour">{opts}</select></div>
<div class="row"><div><label for="f-date">Arrival date</label><input id="f-date" name="date" type="date" data-err="Please choose a date in the future."><small class="hint">Approximate is fine</small></div>
<div><label for="f-pax">Travellers</label><input id="f-pax" name="pax" type="number" min="1" value="2" required data-err="Please enter at least 1 traveller."><small class="hint">Prices depend on group size</small></div></div>
<div class="full"><label for="f-name">Your name</label><input id="f-name" name="name" required autocomplete="name" data-err="Please tell us your name."></div>
<div class="full"><label for="f-email">Email</label><input id="f-email" name="email" type="email" required autocomplete="email" data-err="That email doesn’t look right. Check for typos (e.g. name@gmail.com)."><small class="hint">We’ll send your quote here</small></div>
{'' if compact else '<div class="full"><label for="f-msg">Anything we should know? <span class="opt">(optional)</span></label><textarea id="f-msg" name="msg" rows="3" placeholder="Interests, hotel level, dietary needs…"></textarea></div>'}
<button class="btn btn-primary" type="submit">{e(button)}</button>
<p class="form-note">Free, no obligation. Office hours: {SITE['hours']} (Chișinău time).</p>
</form>'''


# ---------------------------------------------------------------- layout
BEFORE_YOU_GO = [('/plan-your-trip/is-moldova-safe/', 'Is Moldova safe?'), ('/plan-your-trip/moldova-itinerary/', 'Moldova in 3, 5 or 7 days'),
                 ('/plan-your-trip/cricova-vs-milestii-mici/', 'Cricova or Mileștii Mici?'), ('/plan-my-trip/', 'Build my trip')]


def nav():
    cat = lambda k: f'<a href="/tours/{k}/">{ic(CAT_ICON[k])} {CATEGORIES[k]["name"]}</a>'
    pop = ''.join(f'<a href="{BY_SLUG[s]["url"]}">{e(BY_SLUG[s]["title"])}</a>' for s in
                  ['culturewineandgastronomytour', 'milestii-mici-wine-cellars-and-private-gallery-by-petru-costin', 'trip-to-transnistria'])
    links = lambda sec: ''.join(f'<a href="/{k}/">{e(v[1])}</a>' for k, v in PAGES.items() if v[0] == sec)
    byg = ''.join(f'<a href="{u}">{e(n)}</a>' for u, n in BEFORE_YOU_GO)
    return f'''<nav class="main" id="nav" aria-label="Main">
<div class="dd"><a class="dd-top" href="/tours/">Tours</a><div class="dd-panel mega">
<div><h5>By length</h5>{cat('multi-day-tours')}{cat('day-trips')}</div>
<div><h5>By interest</h5>{cat('wine-tours')}{cat('culture-heritage')}{cat('nature-countryside')}</div>
<div><h5>Popular</h5>{pop}<a class="all" href="/tours/">See all tours →</a></div></div></div>
<a href="/destinations/">Destinations</a>
<div class="dd"><a class="dd-top" href="/plan-your-trip/">Plan your trip</a><div class="dd-panel mega">
<div><h5>Before you go</h5>{byg}</div><div><h5>About Moldova</h5>{links('about-moldova')}</div><div><h5>Useful info</h5>{links('useful-info')}</div></div></div>
<a href="/blog/">Blog</a>
<div class="dd"><a class="dd-top" href="/about-us/">About</a><div class="dd-panel"><a href="/about-us/">About us</a><a href="/groups-mice/">Groups, MICE &amp; agents</a><a href="/contact/">Contact</a></div></div>
<a class="btn btn-primary nav-cta" href="/plan-my-trip/">Get a free quote</a>
</nav>'''


def layout(path, title, desc, body, schema=None, wa_msg='Hello! I’d like to plan a trip to Moldova.', noindex=False,
           mobile_cta=('Get a free quote', '/plan-my-trip/')):
    # only English is published: the other languages are listed by their own names, without a link, until their translation exists
    langs = ''.join(f'<a class="on" href="{path}" lang="{c}" aria-current="true">{n}</a>' if c == 'en' else
                    f'<span lang="{c}" aria-disabled="true">{n}<small>soon</small></span>' for c, n in SITE['langs'])
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in (schema or []))
    tours_col = ''.join(f'<li><a href="/tours/{k}/">{v["name"]}</a></li>' for k, v in CATEGORIES.items())
    plan_col = ''.join(f'<li><a href="{u}">{e(n)}</a></li>' for u, n in BEFORE_YOU_GO[:3]) + '<li><a href="/about-moldova/">About Moldova</a></li><li><a href="/useful-info/">Useful info</a></li>'
    page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}">
<link rel="canonical" href="https://moldova.solei.md{path}">{'<meta name="robots" content="noindex">' if noindex or PROTOTYPE else ''}
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<link rel="icon" href="/img/logo.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">{ld}
</head>
<body>
{SPRITE}
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap">
<details class="lang-dd"><summary aria-label="Language: English. Change language">English <span aria-hidden="true">▾</span></summary><div class="lang-list">{langs}</div></details>
<div class="tb-right"><a href="mailto:{SITE['email']}">{SITE['email']}</a><a class="phone" href="{SITE['phone_href']}">☎ {SITE['phone']}</a></div>
</div></div>
<header class="site"><div class="wrap">
<a class="logo" href="/"><img src="/img/logo.svg" alt="Enjoy Moldova by Solei Tourism" width="105" height="43"></a>
{nav()}
<button class="menu-btn" aria-label="Open menu" aria-controls="nav" aria-expanded="false"><span></span><span></span><span></span></button>
</div></header>
<main id="main">
{body}
</main>
<footer><div class="ornament"></div><div class="wrap"><div class="grid fgrid">
<div><img src="/img/logo.svg" alt="Enjoy Moldova" class="flogo"><p class="tagline ftag">{TAGLINE}</p><p>Incoming Tourism &amp; Business Travel Department<br>{e(SITE['address'])}</p>
<p>{SITE['hours']}<br><a href="{SITE['phone_href']}">{SITE['phone']}</a> · <a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
<p><a href="{SITE['facebook']}" rel="noopener">Facebook</a> · <a href="{SITE['instagram']}" rel="noopener">Instagram</a></p></div>
<div><h4>Tours</h4><ul>{tours_col}<li><a href="/destinations/">Destinations map</a></li></ul></div>
<div><h4>Plan your trip</h4><ul>{plan_col}</ul></div>
<div><h4>Company</h4><ul><li><a href="/about-us/">About us</a></li><li><a href="/groups-mice/">Groups, MICE &amp; agents</a></li><li><a href="/blog/">Blog</a></li><li><a href="/contact/">Contact</a></li></ul></div>
</div>
<div class="copy">© 2026 {SITE['legal']} · <a href="/terms/">Terms &amp; Conditions</a> · <a href="/privacy/">Privacy Policy</a> · <a href="/cancellation-policy/">Cancellation policy</a></div>
</div></footer>
<a class="wa-float js-wa" href="#" data-msg="{e(wa_msg)}" aria-label="Chat on WhatsApp">{WA_SVG}</a>
<div class="mobile-bar">{wa(wa_msg, 'WhatsApp')}<a class="btn btn-primary" href="{mobile_cta[1]}">{mobile_cta[0]}</a></div>
<script>window.WA="{SITE['whatsapp']}"</script><script src="/site.js"></script>
</body></html>'''
    write(path, page)


def write(path, page):
    out = os.path.join(ROOT, path.strip('/'), 'index.html') if path != '/404.html' else os.path.join(ROOT, '404.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf8').write(page)


def crumbs(*items):
    parts = ['<a href="/">Home</a>'] + [f'<a href="{u}">{e(n)}</a>' if u else e(n) for n, u in items]
    return '<nav class="crumbs" aria-label="Breadcrumb">' + ' › '.join(parts) + '</nav>'


def crumbs_ld(*items):
    lst = [('Home', '/')] + list(items)
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': 'https://moldova.solei.md' + (u or '')} for i, (n, u) in enumerate(lst)]}


def page_hero(eyebrow, title, intro, img):
    return f'''<section class="phero" style="--hero:url({rsrc(img, 1600)});--hero-sm:url({rsrc(img, 960)})"><div class="wrap">
<p class="eyebrow light">{e(eyebrow)}</p><h1>{e(title)}</h1><p>{e(intro)}</p></div></section><div class="ornament"></div>'''


def cta_band(title='Tell us your dates. We’ll send your itinerary and price.', msg='Hello! I’d like a quote for a Moldova tour.'):
    return f'''<section class="cta-band"><div class="wrap"><div><h2>{e(title)}</h2>
<p>Free, no obligation. Or call {SITE['phone']}.</p></div><div class="ctas">
<a class="btn btn-primary" href="/plan-my-trip/">Get a free quote</a>{wa(msg)}</div></div></section>'''


ORG_LD = {'@context': 'https://schema.org', '@type': 'TravelAgency', 'name': 'Enjoy Moldova by Solei Tourism', 'foundingDate': '2001',
          'url': 'https://moldova.solei.md/', 'telephone': '+37322890900', 'email': SITE['email'],
          'address': {'@type': 'PostalAddress', 'streetAddress': '9 A. Corobceanu str.', 'addressLocality': 'Chișinău', 'postalCode': 'MD-2004', 'addressCountry': 'MD'},
          'sameAs': [SITE['facebook'], SITE['instagram']]}

FQ = {  # question, answer, optional "read more" link
    'change': ('Can I change the itinerary of a tour?', 'Yes. Every tour is a starting point. Tell us what to add or skip and we’ll send an adjusted programme and price.', None),
    'prices': ('How are day trip prices calculated?', 'Day trips are private, so the price per person depends on group size: the more travellers, the lower the price. Transport, a licensed guide and the listed entry fees and tastings are included.', None),
    'safe': ('Is Moldova safe to visit?', 'Official travel advice asks visitors to take care because of the war in neighbouring Ukraine, and several governments advise against travel to Transnistria. Read our guide, with links to official advice, before you book.', '/plan-your-trip/is-moldova-safe/'),
    'cancel': ('Can I cancel?', 'Asking for a quote is free and doesn’t commit you to anything. Cancellation terms for confirmed bookings are in our cancellation policy and in your quote.', '/cancellation-policy/'),
    'pay': ('How do I pay?', 'You pay nothing to get a quote. Payment details are included in the quote we send you.', None),
    'pickup': ('Is pickup included on day trips?', 'Yes. Your guide and driver pick you up from an agreed location in Chișinău. Just tell us where you’re staying.', None),
    'passport': ('Do I need a passport for Transnistria?', 'Yes. Border formalities apply when entering Transnistria, so please bring your passport.', None),
    'languages': ('Which languages do your guides speak?', 'Our guides are licensed and speak English. Other languages are available on request.', None),
    'oneday': ('I only have one day. What do you recommend?', 'Pick one of our wine tours and tastings, for example Mileștii Mici or Cricova, or a day trip combining a winery with a cultural site.', '/plan-your-trip/cricova-vs-milestii-mici/'),
    'quote': ('How do I get a price for my dates?', 'Send a short request with your dates and group size, or build your trip online. We reply by email with your itinerary and package price.', '/plan-my-trip/'),
}


def faq_html(keys):
    return ''.join(f'<details><summary>{e(FQ[k][0])}</summary><p>{e(FQ[k][1])}{f" <a href={chr(34)}{FQ[k][2]}{chr(34)}>Read more →</a>" if FQ[k][2] else ""}</p></details>' for k in keys)


def faq_ld(keys):
    return {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': FQ[k][0], 'acceptedAnswer': {'@type': 'Answer', 'text': FQ[k][1]}} for k in keys]}


TRANSNISTRIA_WARN = ('<div class="note warn"><b>Before you book:</b> check your government’s travel advice for Transnistria. '
                     'Several governments advise against travel there. Bring your passport: border formalities apply. '
                     '<a href="/plan-your-trip/is-moldova-safe/">Read our safety guide →</a></div>')


# ---------------------------------------------------------------- folk hero: our own tree of life
def tree_hero(photos=True):
    """Branches draw themselves on load and end in photo medallions and folk motifs. Pure SVG + CSS.
    photos=False gives the empty-frame version for the motif kit (designers drop their own photos in)."""
    br = lambda d, color, delay, w=9: f'<path class="draw" pathLength="1" d="{d}" stroke="{color}" stroke-width="{w}" style="--d:{delay}s"/>'
    meds = [(150, 200, '/img/cricova.jpg', 'Cricova', '#117799', 1.0), (490, 200, '/img/orheiul-vechi.jpg', 'Orheiul Vechi', '#005e62', 1.1),
            (110, 420, '/img/purcari.jpg', 'Purcari', '#e5592f', 1.2), (530, 420, '/img/besalma.jpg', 'Gagauzia', '#d40025', 1.3)]
    if photos:
        med_svg = ''.join(f'''<g class="pop med" style="--d:{d}s"><clipPath id="mc{i}"><circle cx="{x}" cy="{y}" r="56"/></clipPath>
<image href="{img}" x="{x - 60}" y="{y - 60}" width="120" height="120" preserveAspectRatio="xMidYMid slice" clip-path="url(#mc{i})"><title>{name}</title></image>
<circle cx="{x}" cy="{y}" r="56" fill="none" stroke="{c}" stroke-width="8"/><text x="{x}" y="{y + 84}">{name}</text></g>''' for i, (x, y, img, name, c, d) in enumerate(meds))
    else:
        med_svg = ''.join(f'<circle cx="{x}" cy="{y}" r="56" fill="#faf6f0" stroke="{c}" stroke-width="8"/>' for x, y, _, _, c, _ in meds)
    glass = lambda x, c, d: f'''<g class="pop" style="--d:{d}s"><path d="M{x - 18} 372h36v18a18 18 0 0 1-36 0z" fill="{c}" stroke="#5e0230" stroke-width="7" stroke-linejoin="round"/><path d="M{x} 408v24" stroke="#5e0230" stroke-width="7" stroke-linecap="round"/></g>'''
    arcs = lambda x0, d: f'<path class="draw" pathLength="1" style="--d:{d}s" stroke="#005e62" stroke-width="7" d="M{x0} 170a24 24 0 0 1 48 0M{x0 + 8} 178a16 16 0 0 1 32 0M{x0 + 16} 186a8 8 0 0 1 16 0"/>'
    flower = lambda cx, cy, c, d: f'<g class="pop" style="--d:{d}s" fill="{c}">' + ''.join(
        f'<rect x="{cx + dx - 9}" y="{cy + dy - 9}" width="18" height="18" rx="6"/>' for dx, dy in [(-10, -10), (10, -10), (-10, 10), (10, 10)]) + f'<rect x="{cx - 4}" y="{cy - 4}" width="8" height="8" fill="#f9e1c8"/></g>'
    svg = f'''<svg class="tree" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 610" role="img" aria-label="A Moldovan tree of life with photos of Cricova, Orheiul Vechi, Purcari and Gagauzia">
<g fill="none" stroke-linecap="round" stroke-linejoin="round">
{br('M320 585V150', '#427822', 0, 10)}
{br('M320 560L180 420H168', '#e5592f', .2)}{br('M320 560L460 420H472', '#d40025', .25)}
{br('M320 380L192 252', '#005e62', .35)}{br('M320 380L448 252', '#117799', .4)}
{br('M320 490L262 432', '#a7326b', .45)}{br('M320 490L378 432', '#a7326b', .5)}
{br('M320 300L292 272M282 272h20M292 262v20', '#427822', .55, 7)}{br('M320 300L348 272M338 272h20M348 262v20', '#427822', .6, 7)}
{br('M320 250L262 192', '#005e62', .65, 7)}{br('M320 250L378 192', '#005e62', .7, 7)}
{arcs(238, .9)}{arcs(354, .95)}
{br('M240 480V460', '#117799', .6, 7)}{br('M400 480V460', '#d40025', .6, 7)}
{br('M320 585H236', '#d19a0a', .5, 7)}{br('M320 585H404', '#d19a0a', .5, 7)}
</g>
<g class="pop" style="--d:.8s"><path d="M320 150L268 98l18-18-10-10 20-20 24 18z" fill="#d40025"/><path d="M320 150l52-52-18-18 10-10-20-20-24 18z" fill="#f47e55"/>
<path d="M320 150L268 98l18-18-10-10 20-20 24 18 24-18 20 20-10 10 18 18z" fill="none" stroke="#8e0442" stroke-width="7" stroke-linejoin="round"/>
<path d="M320 90l14 14-14 14-14-14z" fill="none" stroke="#8e0442" stroke-width="6" stroke-linejoin="round"/></g>
{glass(262, '#d40025', .9)}{glass(378, '#427822', .95)}
<circle class="pop" style="--d:1s" cx="240" cy="450" r="10" fill="#117799"/><circle class="pop" style="--d:1s" cx="400" cy="450" r="10" fill="#d40025"/>
<path class="pop" style="--d:1s" d="M250 300l10 10-10 10-10-10z" fill="#a7326b"/><path class="pop" style="--d:1s" d="M390 300l10 10-10 10-10-10z" fill="#a7326b"/>
<path class="pop" style="--d:1.1s" d="M236 585l-26-15-26 15 26 15z" fill="#427822" stroke="#005e62" stroke-width="5" stroke-linejoin="round"/>
<path class="pop" style="--d:1.1s" d="M404 585l26-15 26 15-26 15z" fill="#427822" stroke="#005e62" stroke-width="5" stroke-linejoin="round"/>
{flower(56, 300, '#a7326b', 1.4)}{flower(584, 300, '#e5592f', 1.45)}
{med_svg}</svg>'''
    return svg


# ---------------------------------------------------------------- signature components
GLASS_SVG = '''<svg class="glass" viewBox="0 0 60 92" aria-hidden="true"><defs><clipPath id="{id}"><path d="M11 6h38c0 23-6 35-19 37C17 41 11 29 11 6z"/></clipPath></defs>
<g clip-path="url(#{id})"><rect class="wine" x="0" y="0" width="60" height="44"/></g>
<path class="glass-line" d="M11 6h38c0 23-6 35-19 37C17 41 11 29 11 6zM30 43v32M18 84h24"/></svg>'''


def descent():
    """Scroll from the vineyard down 80 m into the cellar. Without JS / with reduced motion it is a plain fact list."""
    facts = [('Above ground', 'Moldova has the highest density of vineyards in the world, and the country itself is shaped like a bunch of grapes.'),
             ('Into the limestone', 'Cricova is an underground wine city: 120 km of streets with names like Cabernet, Fetească and Aligoté.'),
             ('Perfect conditions', '12–14°C and 97–98% humidity all year round. Down here, wine ages slowly, the way it should.'),
             ('200 km of tunnels', 'The galleries of Mileștii Mici stretch for more than 200 km through old limestone quarries.')]
    items = ''.join(f'<div class="d-fact"><h3>{e(h)}</h3><p>{e(p)}</p></div>' for h, p in facts)
    return f'''<a class="skip skip-anim" href="#after-descent">Skip the cellar animation</a>
<section class="descent" aria-label="Descend into a Moldovan wine cellar"><div class="d-stage">
<div class="d-layer d-surface"></div><div class="d-layer d-stone"></div><div class="d-layer d-cellar"></div><div class="d-shade"></div>
<div class="d-meter" aria-hidden="true"><span class="d-track"><i></i></span><b class="d-depth">0 m</b></div>
<div class="wrap d-facts"><p class="eyebrow light d-eyebrow">Take a breath. We’re going 80 m down.</p>{items}
<div class="d-fact d-end"><p class="d-big">−80 m</p><h2>1.5 million bottles.<br>One Guinness record.</h2>
<p>The largest wine collection in the world rests in the dark at Mileștii Mici. Come and taste it.</p>
<div class="ctas"><a class="btn btn-primary" href="/tours/wine-tours/">Explore wine tours</a><a class="btn btn-ghost" href="/plan-my-trip/">Build my trip</a></div></div></div>
<p class="d-hint" aria-hidden="true">Scroll to descend ↓</p></div></section><div id="after-descent"></div>'''


MAP_ICON = {'soroca': 'f-fortress', 'tipova-saharna': 'f-route', 'orheiul-vechi': 'f-church', 'capriana': 'f-tree', 'cricova': 'f-glass',
            'transnistria': 'f-star', 'milestii-mici': 'f-bottle', 'castel-mimi': 'f-tower', 'purcari': 'f-grapes', 'gagauzia': 'f-flower'}
GEO = DATA('moldova_geo.json')
K, LAT0, LON0, PAD = 172, 48.55, 26.55, 30
COSLAT = 0.682  # cos(47°): keeps the country's real proportions
KIND_LABEL = {'winery': 'Winery', 'sight': 'Monastery & sights'}


def proj(lon, lat):
    return PAD + (lon - LON0) * COSLAT * K, PAD + (LAT0 - lat) * K


def simplify(pts, tol):
    """Douglas–Peucker: fewer points, so the outline reads as a drawn line."""
    if len(pts) < 3:
        return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1
    norm = (dx * dx + dy * dy) ** .5 or 1
    dist = [abs(dy * (x - x1) - dx * (y - y1)) / norm for x, y in pts[1:-1]]
    i = max(range(len(dist)), key=dist.__getitem__)
    if dist[i] <= tol:
        return [pts[0], pts[-1]]
    return simplify(pts[:i + 2], tol)[:-1] + simplify(pts[i + 1:], tol)


def simplify_ring(pts, tol):
    """A closed ring starts and ends on the same point, so split it at the farthest point and simplify both halves."""
    x0, y0 = pts[0]
    k = max(range(len(pts)), key=lambda i: (pts[i][0] - x0) ** 2 + (pts[i][1] - y0) ** 2)
    return simplify(pts[:k + 1], tol)[:-1] + simplify(pts[k:], tol)[:-1]


def chaikin(pts, closed, rounds=2):
    """Corner cutting: soft, hand-drawn curves."""
    for _ in range(rounds):
        seq = pts + [pts[0]] if closed else pts
        out = [] if closed else [pts[0]]
        for (x1, y1), (x2, y2) in zip(seq, seq[1:]):
            out += [(.75 * x1 + .25 * x2, .75 * y1 + .25 * y2), (.25 * x1 + .75 * x2, .25 * y1 + .75 * y2)]
        pts = out if closed else out + [pts[-1]]
    return pts


def to_path(pts, closed):
    return 'M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + ('Z' if closed else '')


def place_badges(items, W, H):
    """Push overlapping badges apart (Chișinău stays put); each badge keeps a thin line to its real point.
    ponytail: naive O(n²) relaxation, fine for a few dozen points."""
    pos = [[x, y] for _, x, y, _ in items]
    for _ in range(300):
        moved = False
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                dx, dy = pos[j][0] - pos[i][0], pos[j][1] - pos[i][1]
                d = (dx * dx + dy * dy) ** .5 or .01
                need = items[i][3] + items[j][3] + 4
                if d < need:
                    push = (need - d) / 2
                    ux, uy = (dx / d, dy / d) if d > .01 else (1, 0)
                    wi, wj = (0, 2) if items[i][0] == 'chisinau' else (2, 0) if items[j][0] == 'chisinau' else (1, 1)
                    pos[i][0] -= ux * push * wi; pos[i][1] -= uy * push * wi
                    pos[j][0] += ux * push * wj; pos[j][1] += uy * push * wj
                    moved = True
        if not moved:
            break
    return {items[i][0]: (min(max(p[0], 20), W - 20), min(max(p[1], 20), H - 20)) for i, p in enumerate(pos)}


def moldova_map(page_links=False):
    border = chaikin(simplify_ring([proj(*p) for p in GEO['country'][0]], 1.6), True)
    river = [p for p in max(GEO['nistru'], key=len) if p[1] <= 48.47 and 27.56 <= p[0] <= 30.13]  # the Moldovan stretch
    nistru = chaikin(simplify([proj(*p) for p in river], 1.4), False)
    cx = sum(x for x, _ in border) / len(border)
    cy = sum(y for _, y in border) / len(border)
    W, H = 480, int(PAD * 2 + (LAT0 - 45.42) * K)

    # every point: key, name, kind, real x/y, radius, icon
    pts = [(k, n, 'hub' if k == 'chisinau' else DEST_KIND.get(k, 'sight'), *proj(lon, lat), 19 if k == 'chisinau' else 17, MAP_ICON.get(k), True)
           for k, n, (lat, lon), *_ in DESTINATIONS]
    pts += [(k, n, kind, *proj(lon, lat), 12, icon, False) for k, n, kind, (lat, lon), icon, *_ in POIS]
    placed = place_badges([(p[0], p[3], p[4], p[5]) for p in pts], W, H)
    # the Chișinău area holds a third of the points: a zoom box around them, in the map's own proportions
    hx, hy = next((p[3], p[4]) for p in pts if p[0] == 'chisinau')
    near = [placed[p[0]] for p in pts if ((p[3] - hx) ** 2 + (p[4] - hy) ** 2) ** .5 < 50]
    x0, x1 = min(x for x, _ in near) - 34, max(x for x, _ in near) + 34
    y0, y1 = min(y for _, y in near) - 34, max(y for _, y in near) + 34
    zw = max(x1 - x0, (y1 - y0) * W / H)
    zh = zw * H / W
    zx = min(max((x0 + x1 - zw) / 2, 0), W - zw)
    zy = min(max((y0 + y1 - zh) / 2, 0), H - zh)

    badges = []
    for n, (key, name, kind, x, y, r, icon, main) in enumerate(pts):
        bx, by = placed[key]
        size = 22 if main else 15
        inner = ('<text x="0" y="7" class="hub-star">★</text>' if kind == 'hub' else
                 f'<svg class="ic" x="{-size / 2}" y="{-size / 2}" width="{size}" height="{size}"><use href="#{icon}"/></svg>')
        left = bx > W * .62  # labels sit away from the eastern edge
        line = f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{bx:.1f}" y2="{by:.1f}"/>' if abs(bx - x) + abs(by - y) > 3 else ''
        badges.append(f'''<g class="badge k-{kind}{' main' if main else ' poi'}{' hub' if kind == 'hub' else ''}" data-dest="{key}" data-xy="{bx:.0f},{by:.0f}" tabindex="0" role="button" aria-label="{e(name)}" style="--d:{.9 + n * .05:.2f}s">
{line}<circle class="pt" cx="{x:.1f}" cy="{y:.1f}" r="3"/><g transform="translate({bx:.1f} {by:.1f})"><g class="b-in"><circle class="bg" r="{r}"/>{inner}</g>
<text class="lbl" x="{-(r + 8) if left else r + 8}" y="5" text-anchor="{'end' if left else 'start'}">{e(name)}</text></g></g>''')

    sx, sy = proj(28.55, 48.05)
    px, py = proj(27.55, 47.55)
    svg = f'''<svg class="mdmap" viewBox="0 0 {W} {H}" data-zoom="{zx:.0f} {zy:.0f} {zw:.0f} {zh:.0f}" role="group" aria-label="Illustrated map of Moldova with the places we visit">
<text class="ctry" x="40" y="{H * .55:.0f}">ROMANIA</text><text class="ctry" x="{W - 120}" y="70">UKRAINE</text>
<path class="land draw" pathLength="1" d="{to_path(border, True)}"/>
<path class="stitch" d="{to_path(border, True)}" transform="translate({cx:.1f} {cy:.1f}) scale(.955) translate({-cx:.1f} {-cy:.1f})"/>
<path class="river draw" pathLength="1" d="{to_path(nistru, False)}"/>
<text class="rname" x="{sx + 40:.0f}" y="{sy - 18:.0f}">Nistru</text><text class="rname" x="{px - 40:.0f}" y="{py:.0f}">Prut</text>
<g class="compass" transform="translate({W - 50} {H - 60})"><svg class="ic" x="-18" y="-18" width="36" height="36"><use href="#f-sun"/></svg><text y="-26">N</text></g>
{''.join(badges)}</svg>'''

    def legend_item(key, name, kind, icon, main):
        dot = '<span class="hubdot">★</span>' if kind == 'hub' else f'<span class="lg-{kind}">{ic(icon)}</span>'
        return f'<li class="k-{kind}{" main" if main else ""}"><button type="button" data-dest="{key}">{dot}{e(name)}</button></li>'
    legend = ''.join(legend_item(p[0], p[1], p[2], p[6], p[7]) for p in sorted(pts, key=lambda p: (p[2] != 'hub', not p[7])))

    tour_li = lambda slugs: ''.join(f'<li><a href="{BY_SLUG[s]["url"]}">{e(BY_SLUG[s]["title"])}<small>{"from €" + str(BY_SLUG[s]["price_from"]) if BY_SLUG[s].get("price_from") else "ask for price"}</small></a></li>' for s in slugs)
    panels = []
    for key, name, _, blurb, img, slugs in DESTINATIONS:
        if key == 'chisinau':
            extra = '<p class="small">All our tours start here.</p><a class="more" href="/about-moldova/chisinau/">About Chișinău →</a>'
        else:
            extra = (TRANSNISTRIA_WARN if key == 'transnistria' else '') + f'<a class="more" href="/destinations/{key}/">Explore {e(name)} →</a>'
        panels.append(f'''<article class="dest-panel" data-dest="{key}" hidden><div class="ph" style="background-image:url({rsrc(img, 960)})"></div>
<div class="dp-body"><h3>{e(name)}</h3><p>{e(blurb)}</p>{extra}{f'<h4>{len(slugs)} tours go here</h4><ul class="dp-tours">{tour_li(slugs)}</ul>' if slugs else ''}</div></article>''')
    for key, name, kind, _, icon, text, slugs in POIS:
        ask = wa(f'Hello! I’d like a tour and tasting at {name}.', 'Ask for a tasting', 'btn btn-wa') if kind == 'winery' else ''
        panels.append(f'''<article class="dest-panel poi-panel" data-dest="{key}" hidden><div class="dp-body"><div class="dp-ic k-{kind}">{ic(icon, 'ic ic-lg')}</div>
<p class="eyebrow">{KIND_LABEL[kind]}</p><h3>{e(name)}</h3><p>{e(text)}</p><h4>{'Included in' if len(slugs) > 1 else 'Visited on'}</h4><ul class="dp-tours">{tour_li(slugs)}</ul>{ask}</div></article>''')
    intro = '''<article class="dest-panel dp-intro" data-dest=""><div class="dp-body"><h3>Moldova on one map.</h3>
<p>The big points are our destinations, the small ones the wineries and sights on our tours. Tap any of them.</p></div></article>'''
    n_w = sum(1 for p in pts if p[2] == 'winery')
    n_s = sum(1 for p in pts if p[2] == 'sight')
    chips = (f'<div class="chips map-filter" role="group" aria-label="Show on the map"><button class="chip on" type="button" data-show="all">All places</button>'
             f'<button class="chip" type="button" data-show="winery">{ic("f-glass")}Wineries ({n_w})</button>'
             f'<button class="chip" type="button" data-show="sight">{ic("f-church")}Monasteries &amp; sights ({n_s})</button></div>')
    return f'''<div class="moldova-map js-map{' js-hash' if page_links else ''}" data-show="all"><div class="gm-svg">{chips}<div class="gm-draw">{svg}
<button class="map-zoom" type="button" aria-pressed="false">{ic('f-sun')}<span>Zoom in on Chișinău</span></button></div></div>
<div class="gm-panel">{intro}{''.join(panels)}<ol class="legend" aria-label="Places on the map">{legend}</ol>
<p class="small legend-note">Tap a point on the map, or pick a place from the list. Use the filter to see only wineries or sights.</p></div></div>'''

def builder_data():
    tours = []
    for i, slug in enumerate(TRIP_ORDER):
        t = BY_SLUG[slug]
        tags, group = TRIP_TAGS[slug]
        tours.append(dict(slug=slug, title=t['title'], url=t['url'], img=rsrc(t['images'][0], 480), tags=tags, group=group, order=i,
                          prices=(t['price_table'] or {}).get('prices', []), transnistria=group == 'transnistria'))
    multi = {s: dict(title=BY_SLUG[s]['title'], url=BY_SLUG[s]['url'], price=BY_SLUG[s]['price_from'], duration=BY_SLUG[s]['duration'])
             for s in ['wine-and-gastronomy', 'countryside-tour', 'culturewineandgastronomytour']}
    return json.dumps(dict(tours=tours, multi=multi), ensure_ascii=False)


def builder_page():
    who = [('1', 'Just me', '🧳'), ('2', 'A couple', '💑'), ('4', 'Family', '👨‍👩‍👧'), ('5', 'Friends', '🥂'), ('8', 'A group (7+)', '🚌')]
    who_html = ''.join(f'''<label class="opt"><input type="radio" name="who" value="{v}"{' checked' if v == '2' else ''}><span class="opt-card"><b aria-hidden="true">{i}</b>{e(l)}</span></label>''' for v, l, i in who)
    ints = ''.join(f'''<label class="opt photo"><input type="checkbox" name="interest" value="{k}"><span class="opt-card" style="background-image:url({rsrc(img, 480)})">{ic(INT_ICON[k], 'ic ic-lg')}{e(l)}</span></label>''' for k, l, _, img in INTERESTS)
    months = ''.join(f'<option>{m} 2027</option>' for m in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    body = f'''<section class="builder js-builder-root" style="--fill:0"><div class="wrap">
{crumbs(('Plan my trip', None))}
<div class="b-head"><div class="b-glass">{GLASS_SVG.format(id='bowl-b')}</div>
<div><p class="eyebrow">Build your Moldova trip · <span class="js-stepnum">Step 1 of 4</span></p><h1>Your trip, in 60 seconds.</h1>
<p class="lead">Pick who’s coming, what you love and how long you stay. We’ll suggest an itinerary with an estimated price, and you can send it to us for a free quote.</p></div></div>
<form class="js-builder" action="/thank-you/" novalidate>
<fieldset class="bstep" data-step="1"><legend>Who’s coming?</legend>
<div class="opts who">{who_html}</div>
<div class="pax-row"><label for="b-pax">Exact number of travellers</label><div class="stepper"><button type="button" data-pax="-1" aria-label="Fewer travellers">−</button><input id="b-pax" name="pax" type="number" min="1" max="40" value="2"><button type="button" data-pax="1" aria-label="More travellers">+</button></div></div>
<div class="b-nav"><span></span><button class="btn btn-primary" type="button" data-go="2">Next: interests →</button></div></fieldset>

<fieldset class="bstep" data-step="2" hidden><legend>What makes you curious?</legend><p class="small">Pick as many as you like. Not sure? Skip and we’ll mix a bit of everything.</p>
<div class="opts ints">{ints}</div>
<div class="b-nav"><button class="btn btn-outline" type="button" data-go="1">← Back</button><button class="btn btn-primary" type="button" data-go="3">Next: dates →</button></div></fieldset>

<fieldset class="bstep" data-step="3" hidden><legend>How long will you stay?</legend>
<div class="days"><output class="js-days-out" for="b-days">3 days</output><input id="b-days" name="days" type="range" min="1" max="8" value="3" aria-label="Number of days">
<div class="days-scale" aria-hidden="true"><span>1 day</span><span>8 days</span></div></div>
<div class="full"><label for="b-month">When? <span class="opt-l">(optional)</span></label><select id="b-month" name="month"><option value="">Not sure yet</option>{months}</select></div>
<div class="b-nav"><button class="btn btn-outline" type="button" data-go="2">← Back</button><button class="btn btn-primary" type="button" data-go="4">Show my trip →</button></div></fieldset>

<fieldset class="bstep" data-step="4" hidden><legend>Here’s your Moldova trip</legend>
<div class="b-result" aria-live="polite"></div>
<div class="b-send"><h3>Like it? Send it to us for a free quote.</h3><p class="small">We’ll check availability and reply with the final itinerary and price. Free, no obligation.</p>
<div class="row"><div><label for="f-name">Your name</label><input id="f-name" name="name" required autocomplete="name" data-err="Please tell us your name."></div>
<div><label for="f-email">Email</label><input id="f-email" name="email" type="email" required autocomplete="email" data-err="That email doesn’t look right. Check for typos (e.g. name@gmail.com)."></div></div>
<textarea name="msg" class="js-summary" hidden></textarea>
<div class="b-nav"><button class="btn btn-outline" type="button" data-go="3">← Change</button><button class="btn btn-primary" type="submit">Send me this trip</button></div>
<p class="form-note">Prefer to talk? {wa('Hello! I’d like help planning a trip to Moldova.', 'Chat on WhatsApp', 'link-wa')}</p></div></fieldset>
</form></div></section>
<div class="pop-up" hidden><div class="pop-in">{GLASS_SVG.format(id='bowl-p')}<span class="cork" aria-hidden="true"></span><p>Noroc! 🍷</p></div></div>
<script type="application/json" id="trip-data">{builder_data()}</script>'''
    layout('/plan-my-trip/', 'Plan My Moldova Trip: Free Itinerary & Quote | Enjoy Moldova',
           'Build your Moldova trip in 60 seconds: choose who’s coming, your interests and how many days. Get a suggested itinerary, an estimated price and a free quote.', body)


# ---------------------------------------------------------------- tour pages
def good_to_know(t):
    k = t['slug']
    items = [('f-route', 'Start & finish', 'Your guide and driver pick you up from an agreed location in Chișinău.') if t['kind'] == 'day'
             else ('f-route', 'Programme', 'The full day-by-day programme and inclusions come with your quote.'),
             ('f-bird', 'Guide', 'Licensed English-speaking guide. Other languages on request.'),
             ('f-romb', 'Private tour', 'Only your group, with transport sized to it: car, minivan or minibus.')]
    if k in CELLAR_TOURS:
        items.append(('f-glass', 'Bring a warm layer', 'The underground cellars stay at about 12–14°C all year.'))
    if k in TRANSNISTRIA_TOURS:
        items.append(('f-hook', 'Passport', 'Bring your passport: border formalities apply when entering Transnistria.'))
    if k in HIKING_TOURS:
        items.append(('f-tree', 'Comfortable shoes', 'The route includes a one-way hike to the Țipova waterfalls.'))
    items += [('f-sun', 'Opening days', n) for n in t.get('notes', [])]
    return '<h2>Good to know</h2><ul class="gtk">' + ''.join(f'<li>{ic(i)}<div><b>{e(h)}</b>{e(x)}</div></li>' for i, h, x in items) + '</ul>'


def tour_page(t):
    imgs = t['images'][:5]
    gallery = ''.join('<div>' + pic(i, f'{t["title"]} photo {n + 1}', sizes='(max-width: 640px) 100vw, 50vw', eager=n == 0) + '</div>'
                      for n, i in enumerate(imgs))
    hl = ''.join(f'<li>{e(h)}</li>' for h in t.get('highlights', []))
    pt = t.get('price_table')
    table = ''
    if pt:
        table = f'''<h2>Prices</h2><div class="ptable"><table><thead><tr><th>Travellers</th>{''.join(f'<th data-pax="{p["pax"]}">{p["pax"]}</th>' for p in pt['prices'])}</tr></thead>
<tbody><tr><th>Per person</th>{''.join(f'<td data-pax="{p["pax"]}">€{p["eur"]}</td>' for p in pt['prices'])}</tr></tbody></table></div>
<p class="small">Price per person, depends on group size. 7+ travellers: ask for a group quote.</p>'''
    incl = ''
    if t.get('inclusions'):
        ex = ''.join(f'<li>{e(x)}</li>' for x in t.get('extras', []))
        incl = f'''<h2>What’s included</h2><div class="inc"><div><h3>Included</h3><ul class="ticks">{''.join(f"<li>{e(x)}</li>" for x in t['inclusions'])}</ul></div>
{f'<div><h3>Optional extras</h3><ul class="plus">{ex}</ul></div>' if ex else ''}</div>'''
    elif t['kind'] == 'multi':
        incl = '<h2>What’s included</h2><div class="todo"><b>De completat: incluse / neincluse</b>Pe site nu există încă lista pentru acest tur (cazare, transport, ghid, degustări, mese).</div>'
    wineries = ''
    if t.get('wineries'):
        wineries = '<h2>Choose your winery</h2><div class="wineries-grid">' + ''.join(
            f'<a class="winery js-wa" href="#" data-msg="{e("Hello! I’m interested in a tour and tasting at " + w + ".")}">{ic("f-glass")}{e(w)}<small>Ask for price →</small></a>' for w in t['wineries']) + '</div>'
    related = [r for r in TOURS if r is not t and set(r['cats']) & set(t['cats']) - {'day-trips', 'multi-day-tours'}][:3]
    # booking card: day trips show the price for 2 and update live with the traveller count
    if t.get('price2'):
        prices = json.dumps(pt['prices'])
        price_box = f'''<p class="from js-plabel">Price for 2 travellers</p><p class="big"><span class="js-pp">€{t["price2"]}</span><small> per person</small></p>
<p class="small js-ptotal">€{t["price2"] * 2} in total. The bigger the group, the lower the price.</p>'''
        book_attr = f" data-prices='{prices}'"
    elif t.get('price_from'):
        price_box, book_attr = f'<p class="from">From</p><p class="big">€{t["price_from"]}<small> per person</small></p>', ''
    else:
        price_box, book_attr = '<p class="from">Price</p><p class="big">On request</p><p class="small">Send the form and we’ll reply with the price for your group.</p>', ''
    cat_links = ' · '.join(f'<a href="/tours/{c}/">{CATEGORIES[c]["short"]}</a>' for c in t['cats'])
    msg = f'Hello! I’m interested in the {t["title"]}.'
    tn = t['slug'] in TRANSNISTRIA_TOURS
    faq_keys = ['change', 'prices' if t['kind'] == 'day' else 'quote', 'pickup' if t['kind'] == 'day' else 'languages', 'cancel'] + (['safe'] if tn else [])
    # phones: price + button right under the title (the booking card sits far below on a narrow screen)
    if t.get('price2'):
        quick_label, quick_price = 'Price for 2 travellers', f'€{t["price2"]}<small> per person</small>'
    elif t.get('price_from'):
        quick_label, quick_price = 'From', f'€{t["price_from"]}<small> per person</small>'
    else:
        quick_label, quick_price = 'Price', 'On request'
    # long site descriptions: first two blocks visible, the rest folded
    parts = tour_body(t).split('\n')
    about = '\n'.join(parts) if len(parts) <= 3 else (
        '\n'.join(parts[:2]) + '<details class="readmore"><summary>Read more about this tour</summary>' + '\n'.join(parts[2:]) + '</details>')
    body = f'''<div class="wrap">{crumbs(('Tours', '/tours/'), (CATEGORIES[t['cats'][0]]['name'], f"/tours/{t['cats'][0]}/"), (t['title'], None))}
<div class="gallery-wrap"><div class="gallery n{len(imgs)}" role="region" aria-label="Photos of the tour" tabindex="0">{gallery}</div>
{f'<div class="g-dots" aria-hidden="true">{"<i></i>" * len(imgs)}</div>' if len(imgs) > 1 else ''}</div>
<div class="tour-layout"><div class="tour-main">
<p class="eyebrow">{cat_links}</p>
<h1>{e(t['title'])}</h1>
<div class="chips static"><span class="chip">{ic('f-sun')}{e(t['duration'])}</span><span class="chip">{ic('f-romb')}Private tour</span><span class="chip">{ic('f-bird')}Licensed guide</span>{f'<span class="chip">{ic("f-hook")}Passport needed</span>' if tn else ''}</div>
<p class="lead">{e(t['summary'])}</p>
<div class="quick-book"><div class="qb-price"><span>{quick_label}</span><b>{quick_price}</b></div>
<div class="qb-ctas"><a class="btn btn-primary" href="#book">Get my price</a>{wa(msg, 'WhatsApp')}</div></div>
{TRANSNISTRIA_WARN if tn else ''}
{f'<h2>Highlights</h2><ul class="hl">{hl}</ul>' if hl else ''}
{table}{incl}{wineries}{good_to_know(t)}
<div class="tour-more"><h2>About this tour</h2><div class="prose">{about}</div>
<h2>Questions</h2>{faq_html(faq_keys)}</div>
</div>
<aside class="book" id="book"{book_attr}>{price_box}
{quote_form(t['title'], compact=True, button='Get my price')}
{wa(msg, 'Ask on WhatsApp', 'btn btn-wa wide')}
<ul class="perks"><li>Free request, no obligation</li><li>Itinerary adjusted to you</li><li>Or call {SITE['phone']}</li></ul></aside>
</div></div>
<section class="section pt0"><div class="wrap"><h2 class="mb">You may also like</h2><div class="grid g3">{''.join(card(r) for r in related)}</div></div></section>
{cta_band(f'Want the {t["title"]} on your dates?', msg)}'''
    if pt:
        offer = {'@type': 'AggregateOffer', 'priceCurrency': 'EUR', 'lowPrice': str(t['price_low']), 'highPrice': str(max(p['eur'] for p in pt['prices'])), 'url': 'https://moldova.solei.md' + t['url']}
    else:
        offer = {'@type': 'Offer', 'priceCurrency': 'EUR', 'url': 'https://moldova.solei.md' + t['url'], **({'price': str(t['price_from'])} if t.get('price_from') else {})}
    ld = {'@context': 'https://schema.org', '@type': 'TouristTrip', 'name': t['title'], 'description': t['summary'],
          'image': ['https://moldova.solei.md' + i for i in imgs], 'provider': ORG_LD, 'offers': offer,
          'itinerary': {'@type': 'ItemList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': h} for i, h in enumerate(t.get('highlights', []))]}}
    price_txt = f' €{t["price2"]} per person for 2.' if t.get('price2') else (f' From €{t["price_from"]} per person.' if t.get('price_from') else '')
    layout(t['url'], f"{t['title']} | Moldova Tours | Enjoy Moldova", (t['summary'] + price_txt)[:158], body,
           [ld, crumbs_ld(('Tours', '/tours/'), (t['title'], t['url'])), faq_ld(faq_keys)], wa_msg=msg, mobile_cta=('Get my price', '#book'))


# ---------------------------------------------------------------- listing pages
def post_cat(p):
    t = p['title'].lower() + ' ' + p['slug']
    return next(name for name, keys in BLOG_CATS if any(k in t for k in keys))


def post_img(p):
    img = p['image'] or '/img/hero-vineyard.jpg'
    return img if img.startswith('http') or img.startswith('/img') else 'https://moldova.solei.md' + img  # ponytail: hotlinked from live site


def post_card(p):
    c = post_cat(p)
    return f'''<a class="card post" href="/{p['slug']}/" data-cats="{e(c)}">
<div class="ph">{pic(post_img(p), p['title'])}<span class="badge">{e(c)}</span></div>
<div class="body"><p class="meta">{e(p['date'])}</p><h3>{e(p['title'])}</h3><div class="foot"><span class="more">Read article →</span></div></div></a>'''


HOME_FAQ = ['prices', 'safe', 'cancel', 'pickup', 'quote']
BESTSELLERS = ['culturewineandgastronomytour', 'milestii-mici-wine-cellars-and-private-gallery-by-petru-costin', 'trip-to-transnistria',
               'old-orhei-complex-and-chateau-vartely-winery', 'wine-and-gastronomy', 'purcari-winery-and-the-medieval-church']


def home():
    best = [BY_SLUG[s] for s in BESTSELLERS]
    cat_chips = ''.join(f'<a class="chip" href="/tours/{k}/">{ic(CAT_ICON[k])}{v["name"]} <small>{sum(k in t["cats"] for t in TOURS)}</small></a>' for k, v in CATEGORIES.items())
    n_places = len(DESTINATIONS) + len(POIS)
    proof = [('2001', 'organising trips in Moldova, from Chișinău'), ('Awarded', 'Best Inbound Travel Agency in the Republic of Moldova, more than once'),
             ('13', 'partner wineries for tastings, from Guinness-record cellars to family estates'), (str(n_places), 'places on our map: wineries, monasteries, fortresses')]
    benefits = [('f-tree', 'Your itinerary', 'Dates, pace and places chosen around you.'), ('f-romb', 'Private, always', 'Only your group, with your own guide and transport.'),
                ('f-route', 'Everything handled', 'Transfers, tastings, entry fees and meals.'), ('f-tower', 'Beyond the wine', 'Cave monasteries, Gagauz culture, Soviet heritage.')]
    body = f"""
<section class="hero" style="--hero:url({rsrc('/img/hero-river.jpg', 1600)});--hero-sm:url({rsrc('/img/hero-river.jpg', 960)})"><div class="wrap">
<p class="eyebrow light">Wine · Culture · Gastronomy</p>
<h1>Discover Moldova, <em>one glass at a time</em></h1>
<p>Private tours to the world’s biggest wine cellars, cave monasteries, Gagauz villages and the Soviet time capsule of Transnistria, planned around your dates.</p>
<div class="ctas"><a class="btn btn-primary" href="/plan-my-trip/">Get a free quote</a>{wa('Hello! I’d like to plan a trip to Moldova.')}</div>
<div class="trust"><span>Local tour operator since 2001</span><span>Awarded Best Inbound Travel Agency in Moldova</span><span>Licensed guides</span></div>
</div></section>
<div class="wrap quote-bar"><a class="teaser" href="/plan-my-trip/"><span class="t-glass">{GLASS_SVG.format(id='bowl-t')}</span>
<span class="t-text"><b>Not sure where to start?</b>Build your Moldova trip in 60 seconds: who’s coming, what you love, how many days.</span>
<span class="btn btn-primary">Build my trip</span></a></div>

<section class="section"><div class="wrap">
<div class="head-row"><div><p class="eyebrow">Most booked</p><h2>Our bestsellers</h2></div><a class="more" href="/tours/">All {len(TOURS)} tours →</a></div>
<div class="grid g3 rail">{''.join(card(t) for t in best)}</div>
<div class="chips cat-chips" aria-label="Browse tours by type"><span>Browse:</span>{cat_chips}</div>
</div></section>

<section class="section pt0"><div class="wrap">
<div class="head-row"><div><p class="eyebrow">Explore the map</p><h2>Where we’ll take you</h2></div><a class="more" href="/destinations/">All destinations →</a></div>
{moldova_map()}</div></section>

{descent()}

<section class="proof"><div class="wrap">
<p class="eyebrow light">Why travel with us</p><h2>Moldova, organised by locals</h2>
<p class="tagline">{TAGLINE}</p>
<div class="proof-nums">{''.join(f'<div><b>{n}</b><span>{e(t)}</span></div>' for n, t in proof)}</div>
<div class="benefits">{''.join(f'<div>{ic(i)}<b>{h}</b><span>{x}</span></div>' for i, h, x in benefits)}</div>
<div class="todo dark"><b>De completat: recenzii reale</b>Aici vin 3 recenzii scurte Google / TripAdvisor (nume, țară, stele) și ratingul total.</div>
</div></section>

<section class="section"><div class="wrap">
<div class="center head"><p class="eyebrow">How it works</p><h2>From idea to trip in 3 steps</h2></div>
<div class="grid g3 steps">
<div class="step"><h3>Tell us what you like</h3><p>Build your trip online, send a short request or message us on WhatsApp.</p></div>
<div class="step"><h3>Get your itinerary &amp; price</h3><p>We reply by email with a tailored programme and a clear package price.</p></div>
<div class="step"><h3>Enjoy Moldova</h3><p>Your guide and driver pick you up. Transport, guide and tastings are all set.</p></div>
</div></div></section>

<section class="section pt0"><div class="wrap narrow">
<div class="center head"><p class="eyebrow">Good to know</p><h2>Frequently asked questions</h2></div>{faq_html(HOME_FAQ)}
<p class="center mt"><a class="more" href="/plan-your-trip/">More travel tips →</a></p></div></section>
{cta_band()}"""
    layout('/', 'Private Moldova Tours: Wine, Culture & Food | Enjoy Moldova',
           'Private wine, culture and gastronomy tours in Moldova since 2001: Cricova, Mileștii Mici, Purcari, Orheiul Vechi, Gagauzia and Transnistria. Get a free quote.',
           body, [ORG_LD, faq_ld(HOME_FAQ)])

def tours_index():
    chips = '<button class="chip on" data-filter="all">All tours</button>' + ''.join(
        f'<button class="chip" data-filter="{k}">{ic(CAT_ICON[k])}{v["name"]}</button>' for k, v in CATEGORIES.items())
    body = page_hero('Tours', 'All tours in Moldova', 'Multi-day tours and private day trips from Chișinău. Every tour can be adjusted to your dates and interests.', '/img/cricova.jpg') + f'''
<section class="section"><div class="wrap">{crumbs(('Tours', None))}
<div class="chips js-filter" role="group" aria-label="Filter tours">{chips}</div>
<div class="grid g3 js-items">{''.join(card(t) for t in TOURS)}</div>
<p class="empty" hidden><b>No tours match this filter.</b> Try another category or <a href="/tours/">see all tours</a>.</p>
</div></section>{cta_band('Not sure which tour fits? We’ll suggest one.')}'''
    layout('/tours/', 'Moldova Tours: Multi-day Tours & Day Trips | Enjoy Moldova',
           'All tours in Moldova: wine tours and tastings, culture and heritage, nature and countryside. Private day trips from €75 per person and multi-day tours from €655.',
           body, [crumbs_ld(('Tours', '/tours/'))])


def category(k, c):
    items = [t for t in TOURS if k in t['cats']]
    other = ''.join(f'<a class="chip" href="/tours/{o}/">{ic(CAT_ICON[o])}{v["name"]}</a>' for o, v in CATEGORIES.items() if o != k)
    # tours first; on the wine page the cellar descent comes after the list, not before it
    body = page_hero('Tours', c['name'], c['intro'], c['img']) + f'''
<section class="section"><div class="wrap">{crumbs(('Tours', '/tours/'), (c['name'], None))}
<p class="count">{len(items)} tours</p>
<div class="grid g3">{''.join(card(t) for t in items)}</div>
<div class="chips more-cats"><span>Other categories:</span>{other}</div>
</div></section>{descent() if k == 'wine-tours' else ''}{cta_band()}'''
    lows = [t['price_from'] for t in items if t.get('price_from')]
    desc = f"{c['name']} in Moldova with Enjoy Moldova: {', '.join(t['title'] for t in items[:4])}" + (f'. From €{min(lows)} per person.' if lows else '.')
    layout(f'/tours/{k}/', f"{c['name']} in Moldova | Enjoy Moldova", desc, body, [crumbs_ld(('Tours', '/tours/'), (c['name'], f'/tours/{k}/'))])


# ---------------------------------------------------------------- destinations
def km_between(a, b):
    """Straight-line km between two (lat, lon) points; fine at Moldova's size."""
    return (((a[1] - b[1]) * 111.32 * COSLAT) ** 2 + ((a[0] - b[0]) * 111.32) ** 2) ** .5


def dest_info(key, latlon, slugs):
    """Facts of the destination's own (no tour paragraphs copied): distance, time, price, what to combine, what is nearby."""
    tours = [BY_SLUG[s] for s in slugs]
    day, multi = [t for t in tours if t['kind'] == 'day'], [t for t in tours if t['kind'] == 'multi']
    prices = [t['price_from'] for t in day if t.get('price_from')]
    plural = lambda n, w: f'{n} {w}{"s" if n != 1 else ""}'
    facts = [('f-route', 'From Chișinău', f'≈ {DEST_ROAD_KM[key]} km by road'),
             ('f-sun', 'Time needed', 'A full day from Chișinău' if day else 'Part of a multi-day tour'),
             ('f-glass', 'Price', f'Day tours from €{min(prices)} per person' if prices else 'On request, for your group'),
             ('f-romb', 'Tours', ' · '.join(x for x in (plural(len(day), 'day trip') if day else '', plural(len(multi), 'multi-day tour') if multi else '') if x))]
    facts_html = '<dl class="dest-facts">' + ''.join(f'<div>{ic(i)}<dt>{h}</dt><dd>{e(v)}</dd></div>' for i, h, v in facts) + '</dl>'
    combine = []
    for k, n, _, _, _, s2 in DESTINATIONS:
        shared = [s for s in slugs if s in s2]
        if k not in (key, 'chisinau') and shared:
            best = min(shared, key=lambda s: BY_SLUG[s]['kind'] != 'day')  # name a day trip when there is one
            combine.append((len(shared), k, n, best))
    combine = sorted(combine, key=lambda c: -c[0])[:3]
    combine_html = ('<h2>Good to combine with</h2><ul class="gtk">' + ''.join(
        f'<li>{ic(MAP_ICON.get(k, "f-romb"))}<div><b><a href="/destinations/{k}/">{e(n)}</a></b>Together on <a href="{BY_SLUG[s]["url"]}">{e(BY_SLUG[s]["title"])}</a></div></li>'
        for _, k, n, s in combine) + '</ul>') if combine else ''
    near = sorted(((km_between(latlon, ll), n, kind, icon, text) for _, n, kind, ll, icon, text, _ in POIS if km_between(latlon, ll) < 30))
    near_html = ('<h2>Also nearby</h2><ul class="gtk">' + ''.join(
        f'<li>{ic(icon)}<div><b>{e(n)}</b><span class="small">{KIND_LABEL[kind]} · ≈ {max(1, round(d))} km away</span><br>{e(text)}</div></li>'
        for d, n, kind, icon, text in near[:4]) + '</ul>') if near else ''
    return facts_html, combine_html, near_html, day + multi


def destinations_page():
    cards = ''.join(f'''<a class="card dest-card" href="{'/about-moldova/chisinau/' if k == 'chisinau' else f'/destinations/{k}/'}"><div class="ph">{pic(img, n)}</div>
<div class="body"><h3>{e(n)}</h3><p class="meta">{e(b)}</p><div class="foot"><span class="more">{f'{len(s)} tours →' if s else 'Start here →'}</span></div></div></a>''' for k, n, _, b, img, s in DESTINATIONS)
    body = page_hero('Destinations', 'Explore Moldova on the map', 'From the fortress of Soroca in the north to Gagauzia in the south: every place we take you, on one map.', '/img/orheiul-vechi.jpg') + f'''
<section class="section"><div class="wrap">{crumbs(('Destinations', None))}{moldova_map(page_links=True)}</div></section>
<section class="section pt0"><div class="wrap"><h2 class="mb">All destinations</h2><div class="grid g3">{cards}</div></div></section>{cta_band()}'''
    layout('/destinations/', 'Moldova Destinations Map: Wineries, Monasteries & Regions | Enjoy Moldova',
           'Interactive map of Moldova’s best places: Cricova, Mileștii Mici, Orheiul Vechi, Soroca, Purcari, Gagauzia and Transnistria, with the tours that go there.', body)
    for key, name, latlon, blurb, img, slugs in DESTINATIONS:
        if key == 'chisinau':
            continue
        facts, combine, near, tours = dest_info(key, latlon, slugs)
        body = page_hero('Destinations', name, blurb, img) + f'''
<section class="section"><div class="wrap">{crumbs(('Destinations', '/destinations/'), (name, None))}
<div class="side-layout"><aside class="side"><h4>Destinations</h4>{''.join(f'<a class="{"on" if k == key else ""}" href="/destinations/{k}/">{e(n)}</a>' for k, n, *_ in DESTINATIONS if k != 'chisinau')}</aside>
<article class="prose">{TRANSNISTRIA_WARN if key == 'transnistria' else ''}{facts}
<h2>Tours that go to {e(name)}</h2><div class="grid g2">{''.join(card(t) for t in tours)}</div>
{combine}{near}<p class="mt"><a class="more" href="/destinations/#{key}">See {e(name)} on the map →</a></p></article></div>
</div></section>{cta_band(f'Want to see {name}? Tell us your dates.', f'Hello! I’d like to visit {name}.')}'''
        layout(f'/destinations/{key}/', f'{name}, Moldova: Tours & Travel Guide | Enjoy Moldova', f'{blurb} Private tours to {name} from Chișinău with Enjoy Moldova.'[:158], body,
               [crumbs_ld(('Destinations', '/destinations/'), (name, f'/destinations/{key}/'))])


# ---------------------------------------------------------------- content pages (About Moldova, Useful info)
def text_to_html(slug, text):
    """Scraped page text → simple HTML: short title-like lines become headings."""
    out, rows = [], []
    lines = [l.strip() for l in text.split('\n') if l.strip()][1:]  # first line repeats the title
    if slug == 'emmergency-calls':  # alternating label / number lines
        lines = lines[1:]
        i = 0
        while i < len(lines):
            a, b = lines[i], lines[i + 1] if i + 1 < len(lines) else ''
            if re.match(r'^[\d(+][\d\s(),+-]+$', b):
                rows.append(f'<tr><td>{e(a)}</td><td><a href="tel:{re.sub(r"[^0-9+]", "", b.split(",")[0])}">{e(b)}</a></td></tr>'); i += 2
            else:
                if rows: out.append('<table class="info">' + ''.join(rows) + '</table>'); rows = []
                out.append(f'<h3>{e(a)}</h3>'); i += 1
        if rows: out.append('<table class="info">' + ''.join(rows) + '</table>')
        return '\n'.join(out)
    for l in lines:
        if '<iframe' in l or ('”' in l and 'youtube' in l):
            out.append('<div class="video"><iframe src="https://www.youtube.com/embed/liVLOQKsHe8" title="Chișinău" loading="lazy" allowfullscreen></iframe></div>'); continue
        if 'Harta Serviciului Vamal' in l:
            out.append('<p>See the official map of border crossing points on the website of the Customs Service: <a href="https://www.customs.gov.md" rel="noopener">customs.gov.md</a>.</p>'); continue
        if l.startswith('Sursa'): continue
        heading = (len(l) < 70 and not l.endswith(('.', ':', ',', ';')) and not re.search(r'\d{3}', l)) or l.startswith('RM Embassy')
        out.append(f'<h3>{e(l)}</h3>' if heading else f'<p>{e(l)}</p>')
    return '\n'.join(out)


def content_page(key, section, title, intro, src_slug):
    src = SITE_PAGES.get(src_slug, {})
    sec_name = 'About Moldova' if section == 'about-moldova' else 'Useful info'
    siblings = ''.join(f'<a class="{"on" if k == key else ""}" href="/{k}/">{e(v[1])}</a>' for k, v in PAGES.items() if v[0] == section)
    # the live site only keeps the resized copies of these old uploads (the full-size files return 404)
    imgs = [i for i in src.get('images', []) if re.search(r'-\d+x\d+\.\w+$', i) and i not in DEAD][:3]
    pics = ''.join(f'<img src="{i}" alt="{e(title)}" loading="lazy">' for i in imgs)  # ponytail: hotlinked from live site
    rel = RELATED_TOURS.get(key)
    rel_html = f'<h2>Tours that include this</h2><div class="grid g3">{"".join(card(BY_SLUG[s]) for s in rel)}</div>' if rel else ''
    hero = {'about-moldova': '/img/orheiul-vechi.jpg', 'useful-info': '/img/capriana.jpg'}[section]
    body = page_hero(sec_name, title, intro, hero) + f'''
<section class="section"><div class="wrap">{crumbs(('Plan your trip', '/plan-your-trip/'), (sec_name, f'/{section}/'), (title, None))}
<div class="side-layout"><aside class="side"><h4>{sec_name}</h4>{siblings}<h4>Before you go</h4>{''.join(f'<a href="{u}">{e(n)}</a>' for u, n in BEFORE_YOU_GO)}</aside>
<article class="prose">{text_to_html(src_slug, src.get('text', ''))}{f'<div class="pics">{pics}</div>' if pics else ''}</article></div>
{f'<div class="mt">{rel_html}</div>' if rel_html else ''}
</div></section>{cta_band()}'''
    layout(f'/{key}/', f'{title} | Enjoy Moldova', intro, body, [crumbs_ld(('Plan your trip', '/plan-your-trip/'), (sec_name, f'/{section}/'), (title, f'/{key}/'))])


def section_index(section, title, intro, img):
    items = ''.join(f'<a class="card link-card" href="/{k}/"><div class="body"><h3>{e(v[1])}</h3><p class="meta">{e(v[2])}</p><div class="foot"><span class="more">Read more →</span></div></div></a>'
                    for k, v in PAGES.items() if v[0] == section)
    body = page_hero(title, title, intro, img) + f'''<section class="section"><div class="wrap">{crumbs(('Plan your trip', '/plan-your-trip/'), (title, None))}
{('<div class="prose narrow-prose">' + text_to_html('about-moldova', SITE_PAGES['about-moldova']['text']) + '</div>') if section == 'about-moldova' else ''}
<div class="grid g3 mt">{items}</div></div></section>{cta_band()}'''
    layout(f'/{section}/', f'{title} | Enjoy Moldova', intro, body)


# ---------------------------------------------------------------- plan your trip: guides
def article(path, eyebrow, title, intro, img, html_body, related=None, schema=None):
    rel = f'<h2>Tours to consider</h2><div class="grid g3">{"".join(card(BY_SLUG[s]) for s in related)}</div>' if related else ''
    side = ''.join(f'<a class="{"on" if u == path else ""}" href="{u}">{e(n)}</a>' for u, n in BEFORE_YOU_GO)
    body = page_hero(eyebrow, title, intro, img) + f'''
<section class="section"><div class="wrap">{crumbs(('Plan your trip', '/plan-your-trip/'), (title, None))}
<div class="side-layout"><aside class="side"><h4>Before you go</h4>{side}<h4>More</h4><a href="/about-moldova/">About Moldova</a><a href="/useful-info/">Useful info</a></aside>
<article class="prose">{html_body}</article></div>{f'<div class="mt">{rel}</div>' if rel else ''}</div></section>{cta_band()}'''
    layout(path, f'{title} | Enjoy Moldova', intro, body, [crumbs_ld(('Plan your trip', '/plan-your-trip/'), (title, path))] + (schema or []))


def plan_hub():
    group = lambda h, items: f'<h2 class="mb">{h}</h2><div class="grid g3 mb2">' + ''.join(
        f'<a class="card link-card" href="{u}"><div class="body">{ic(i, "ic ic-lg ic-c")}<h3>{e(n)}</h3><p class="meta">{e(d)}</p><div class="foot"><span class="more">Read →</span></div></div></a>' for u, n, d, i in items) + '</div>'
    before = [('/plan-your-trip/is-moldova-safe/', 'Is Moldova safe?', 'Official travel advice, Transnistria and everyday tips.', '/img/capriana.jpg'),
              ('/plan-your-trip/moldova-itinerary/', 'Moldova in 3, 5 or 7 days', 'Ready-made itineraries with real prices.', '/img/monastery-aerial.jpg'),
              ('/plan-your-trip/cricova-vs-milestii-mici/', 'Cricova or Mileștii Mici?', 'The two underground wine cities, compared.', '/img/milestii-mici.jpg'),
              ('/plan-my-trip/', 'Build my trip', 'Get a suggested itinerary and price in 60 seconds.', '/img/wine-tasting-table.jpg')]
    # the four guides get photos in a 2×2 grid (no lone card in a row); the reference pages stay text cards
    guides = '<h2 class="mb">Before you go</h2><div class="grid g2 mb2">' + ''.join(
        f'<a class="card guide-card" href="{u}"><div class="ph">{pic(img, "", sizes="(max-width: 640px) 90vw, 560px")}</div><div class="body"><h3>{e(n)}</h3><p class="meta">{e(d)}</p><div class="foot"><span class="more">Read →</span></div></div></a>'
        for u, n, d, img in before) + '</div>'
    about = [(f'/{k}/', v[1], v[2], 'f-tulip') for k, v in PAGES.items() if v[0] == 'about-moldova']
    useful = [(f'/{k}/', v[1], v[2], 'f-hook') for k, v in PAGES.items() if v[0] == 'useful-info']
    body = page_hero('Plan your trip', 'Plan your trip to Moldova', 'Everything to know before you go: safety, itineraries, wine cellars, food, money and useful contacts.', '/img/saharna.jpg') + f'''
<section class="section"><div class="wrap">{crumbs(('Plan your trip', None))}
{guides}{group('About Moldova', about)}{group('Useful info', useful)}</div></section>{cta_band()}'''
    layout('/plan-your-trip/', 'Plan Your Trip to Moldova: Safety, Itineraries & Tips | Enjoy Moldova',
           'Plan your Moldova trip: is it safe, 3/5/7-day itineraries, Cricova vs Mileștii Mici, food, customs, embassies and useful numbers.', body)


def safety_page():
    src = lambda u, n: f'<a href="{u}" rel="noopener">{n}</a>'
    body = f'''<p class="small">Last reviewed: {REVIEWED}. Travel advice changes: always check your own government’s latest advice before you travel.</p>
<h2>The short answer</h2>
<p>Tourism to Moldova is growing, and Chișinău and the wine regions are the focus of most trips. Official advice still asks visitors to be careful because of the war in neighbouring Ukraine: Australia advises a <em>“high degree of caution”</em> and the United States rates Moldova <em>Level 2: exercise increased caution</em>.</p>
<h2>Transnistria</h2>
<p>Transnistria is a breakaway region on the left bank of the Nistru that is not controlled by the Moldovan government. Advice here is stricter: Australia says <em>“do not travel”</em> to Transnistria and the US lists unrest there as a risk. Travel guides note that consular help there is limited.</p>
<div class="note warn"><b>If you’re thinking about one of our Transnistria tours:</b> read your government’s advice first and ask us about current conditions. You can always swap it for another day trip, for example <a href="{BY_SLUG['purcari-winery-and-the-medieval-church']['url']}">Purcari</a> or <a href="{BY_SLUG['old-orhei-complex-and-chateau-vartely-winery']['url']}">Old Orhei</a>.</div>
<h2>Everyday safety</h2>
<ul class="ticks"><li>Violent crime against tourists is rare. The most common problems are taxi overcharging and petty theft in crowded places.</li>
<li>Use arranged transfers or app-based taxis. We can organise your airport transfer.</li>
<li>Keep valuables close in markets and on public transport.</li>
<li>Cards are widely accepted; carry some cash in Moldovan lei for small places.</li></ul>
<h2>How we help</h2>
<p>All our tours are private, with a licensed guide and your own transport. Our team has worked in Chișinău since 2001: ask us anything before you book.</p>
<p>{wa('Hello! I have a question about travel safety in Moldova.', 'Ask us on WhatsApp')}</p>
<h2>Official advice and sources</h2>
<ul class="plus"><li>{src('https://www.smartraveller.gov.au/destinations/europe/moldova', 'Australia: Smartraveller, Moldova')}</li>
<li>{src('https://travel.state.gov/en/international-travel/travel-advisories/moldova.html', 'United States: Moldova travel advisory')}</li>
<li>{src('https://www.roafly.com/blog/is-moldova-safe', 'Roafly: Is Moldova safe for tourists?')}</li>
<li>{src('https://bestofmoldova.com/is-moldova-safe-for-tourists/', 'Best of Moldova: safety guide')}</li></ul>'''
    article('/plan-your-trip/is-moldova-safe/', 'Plan your trip', 'Is Moldova safe to visit?', 'An honest answer, with links to official travel advice.', '/img/capriana.jpg', body,
            ['purcari-winery-and-the-medieval-church', 'old-orhei-complex-and-chateau-vartely-winery', 'milestii-mici-wine-cellars-and-private-gallery-by-petru-costin'],
            [faq_ld(['safe', 'passport'])])


def itinerary_page():
    blocks = []
    for name, intro, slugs in ITINERARIES:
        days = ['<li class="free"><span class="day">Day 1</span><h4>Arrive in Chișinău</h4><p class="small">We can arrange your airport transfer. Evening in the city.</p></li>']
        for n, s in enumerate(slugs, start=2):
            t = BY_SLUG[s]
            note = ' <span class="small">· passport needed</span>' if s in TRANSNISTRIA_TOURS else ''
            days.append(f'''<li><span class="pimg" style="background-image:url('{rsrc(t['images'][0], 480)}')"></span><div><span class="day">Day {n}</span>
<h4><a href="{t['url']}">{e(t['title'])}</a>{note}</h4><p class="small">{e(t['summary'])}</p></div><span class="pp">€{t['price2']}<small>per person for 2</small></span></li>''')
        if name == '7 days':
            days.append('<li class="free"><span class="day">Day 7</span><h4>Free day and departure</h4><p class="small">Markets, cafés and a last glass in Chișinău.</p></li>')
        total = sum(BY_SLUG[s]['price2'] for s in slugs)
        blocks.append(f'''<h2 id="{name.split()[0]}-days">Moldova in {name}</h2><p>{e(intro)}</p><ol class="plan">{''.join(days)}</ol>
<div class="est"><div><small>Day trips for 2 travellers</small><b>€{total} per person</b><small>Private transport, licensed guide, listed entry fees and tastings. Hotels not included.</small></div>
<a class="btn btn-primary" href="/plan-my-trip/">Customise this trip</a></div>''')
    alt = BY_SLUG['wine-and-gastronomy']
    body = f'''<p>Three ready-made plans built from our private day trips, with real prices for two travellers. Each one starts and ends in Chișinău, so you keep the same hotel.</p>
<p class="toc"><a href="#3-days">3 days</a> · <a href="#5-days">5 days</a> · <a href="#7-days">7 days</a></p>
{''.join(blocks)}
<div class="alt">Prefer everything arranged, hotels included? Take the <a href="{alt['url']}">{e(alt['title'])}</a> ({e(alt['duration'])}), from €{alt['price_from']} per person.</div>
<p class="small">Opening days: the Petru Costin Gallery is open Wednesday to Sunday; the Purcari tour runs Tuesday to Sunday. We plan the order around them.</p>'''
    article('/plan-your-trip/moldova-itinerary/', 'Plan your trip', 'Moldova in 3, 5 or 7 days', 'Ready-made itineraries from Chișinău, with real prices.', '/img/orheiul-vechi.jpg', body)


def cricova_vs_milestii():
    c, m = BY_SLUG['cricova-winery-and-orheiul-vechi-tour'], BY_SLUG['milestii-mici-wine-cellars-and-private-gallery-by-petru-costin']
    rows = [('What it is', 'An underground wine city: you drive along streets named after wines', 'The largest underground wine galleries in Moldova'),
            ('Size', '120 km of underground streets', 'More than 200 km of limestone tunnels (about 55 km in use)'),
            ('Famous for', 'Wine and sparkling wine production, and luxurious tasting halls', 'The largest wine collection in the world: about 1.5 million bottles (Guinness record, 2005)'),
            ('Down there', '12–14°C and 97–98% humidity all year', 'Bottles rest about 80 m underground; the oldest wine dates from 1969'),
            ('Our tour', f'<a href="{c["url"]}">{e(c["title"])}</a>', f'<a href="{m["url"]}">{e(m["title"])}</a>')]
    table = '<div class="ptable cmp"><table><thead><tr><th></th><th>Cricova</th><th>Mileștii Mici</th></tr></thead><tbody>' + ''.join(
        f'<tr><th>{a}</th><td>{b if "<a" in b else e(b)}</td><td>{x if "<a" in x else e(x)}</td></tr>' for a, b, x in rows) + '</tbody></table></div>'
    body = f'''<p>Moldova has two famous underground wine cities, both a short drive from Chișinău. Travellers often ask which one to choose. Here’s how they compare, using the facts from our tours.</p>
{table}
<h2>Choose Cricova if…</h2><ul class="ticks"><li>you love sparkling wine and want to see how it’s made</li><li>you’d like elegant tasting halls</li><li>you want to combine it with the cave monastery of Orheiul Vechi on the same day</li></ul>
<h2>Choose Mileștii Mici if…</h2><ul class="ticks"><li>you want to see a Guinness record with your own eyes</li><li>you’re curious about the Soviet past: the trip includes the Petru Costin Gallery</li><li>you’d like to add Căpriana, the oldest monastery in Moldova</li></ul>
<h2>Why not both?</h2><p>They complement each other well. Our <a href="{BY_SLUG['culturewineandgastronomytour']['url']}">Culture, Wine &amp; Gastronomy Tour</a> includes both, or ask us to fit both into your stay.</p>
<p><a class="btn btn-primary" href="/plan-my-trip/">Build my trip</a></p>'''
    article('/plan-your-trip/cricova-vs-milestii-mici/', 'Plan your trip', 'Cricova or Mileștii Mici?', 'The two underground wine cities of Moldova, compared.', '/img/milestii-mici.jpg', body,
            ['cricova-winery-and-orheiul-vechi-tour', 'milestii-mici-wine-cellars-and-private-gallery-by-petru-costin', 'culturewineandgastronomytour'])


# ---------------------------------------------------------------- company & legal
BLOG_PER_PAGE = 12
cat_slug = lambda c: re.sub(r'[^a-z]+', '-', c.lower()).strip('-')


def blog():
    """12 articles per page; page 1 opens with the 3 newest as featured; one listing per category; every article its own page."""
    cats = list(dict.fromkeys(post_cat(p) for p in POSTS))
    blog_listing('/blog/', None, POSTS, cats)
    for c in cats:
        blog_listing(f'/blog/category/{cat_slug(c)}/', c, [p for p in POSTS if post_cat(p) == c], cats)
    for p in POSTS:
        blog_post(p)


POSTS_FULL = DATA('posts_full.json')  # article bodies, from _build/scrape_posts.py
DEAD = set(DATA('dead_files.json'))  # photos and PDFs the live site links to but no longer has
MONTHS = 'January February March April May June July August September October November December'.split()
human_date = lambda d: f'{int(d[8:10])} {MONTHS[int(d[5:7]) - 1]} {d[:4]}'


def known_paths():
    return ({t['url'] for t in TOURS} | {f'/tours/{k}/' for k in CATEGORIES} | {f'/{p["slug"]}/' for p in POSTS} | {f'/{k}/' for k in PAGES}
            | set(PAGE_REDIRECTS.values()) | {'/', '/tours/', '/blog/', '/about-us/', '/contact/', '/destinations/', '/plan-your-trip/', '/plan-my-trip/'})


def local_link(m, known):
    """Links inside the old articles: the live site's own URLs become prototype paths; anything else opens outside."""
    href = html.unescape(m.group(1))
    path = re.sub(r'^https?://(www\.)?moldova\.solei\.md', '', href)
    if path == href:
        return f'href="{e(href)}" rel="noopener"'
    path = (path.split('?')[0].split('#')[0] or '/').rstrip('/') + '/'
    path = {f'/tours/{o}/': f'/tours/{n}/' for o, n in NEW_SLUGS.items()}.get(path) or PAGE_REDIRECTS.get(path) or path
    return f'href="{e(path)}"' if path in known else f'href="{e(href)}" rel="noopener"'


def blog_post(p):
    full, c, slug = POSTS_FULL.get(p['slug'], {}), post_cat(p), p['slug']
    known = known_paths()
    imgs = ['https://moldova.solei.md' + i if i.startswith('/') else i for i in full.get('images', [])]
    vids = full.get('videos', [])

    def media(m):  # each run of photos in the old article becomes one grid; videos stay embedded
        out, pics = '', []
        for kind, n in re.findall(r'\x00(img|vid)(\d+)\x00', m.group(0)):
            if kind == 'vid':
                out += f'<div class="video"><iframe src="{e(vids[int(n)])}" title="{e(p["title"])}" loading="lazy" allowfullscreen></iframe></div>'
            elif imgs[int(n)] not in DEAD:
                pics.append(f'<img src="{imgs[int(n)]}" alt="{e(p["title"])}, photo {int(n) + 1}" loading="lazy" decoding="async">')
        return out + (f'<div class="post-pics n{min(len(pics), 3)}">{"".join(pics)}</div>' if pics else '')

    body = re.sub(r'<a href="([^"]*)">(.*?)</a>', lambda m: m.group(2) if html.unescape(m.group(1)) in DEAD else m.group(0), full.get('html', ''))
    body = re.sub(r'href="([^"]*)"', lambda m: local_link(m, known), body)
    body = re.sub(r'(?:\s*\x00(?:img|vid)\d+\x00)+', media, body)
    body = re.sub(r'<li>\s*[–-]\s*', '<li>', body)  # old lists typed their own dashes on top of the bullets
    body = re.sub(r'(<a [^>]*>)\s*https?://(?:www\.)?([^/<\s]+)[^<]*</a>', r'\1Read on \2 →</a>', body)  # bare long URLs as link text
    if not re.sub(r'<[^>]+>|\s', '', body) and '<iframe' not in body:
        body = '<div class="todo"><b>De completat: textul articolului</b>Pe site-ul actual articolul are doar titlul și poza, fără text.</div>'
    text = re.sub(r'<[^>]+>', ' ', body) + ' ' + p['title']
    # tours for the places the article talks about; the bestsellers fill the rest
    dest_slugs = {k: s for k, *_, s in DESTINATIONS}
    rel = [s for k, kws in DEST_KEYWORDS.items() if any(w in text for w in kws) for s in dest_slugs.get(k, [])]
    rel = sorted(dict.fromkeys(rel + BESTSELLERS), key=lambda s: BY_SLUG[s]['kind'] != 'day')[:3]
    more = [q for q in POSTS if post_cat(q) == c and q is not p][:3]
    desc = full.get('desc') or re.sub(r'\s+', ' ', text).strip()
    hero = f'''<section class="phero post-hero" style="--hero:url({post_img(p)})"><div class="wrap">
<p class="eyebrow light"><a href="/blog/category/{cat_slug(c)}/">{e(c)}</a> · <time datetime="{p['date']}">{human_date(p['date'])}</time></p><h1>{e(p['title'])}</h1></div></section><div class="ornament"></div>'''
    page = hero + f'''<section class="section"><div class="wrap">{crumbs(('Blog', '/blog/'), (c, f'/blog/category/{cat_slug(c)}/'), (p['title'], None))}
<article class="prose narrow-prose post-body">{body}</article>
<p class="post-back"><a class="more" href="/blog/">← All articles</a></p></div></section>
<section class="section pt0"><div class="wrap"><h2 class="mb">See it with us</h2><div class="grid g3">{''.join(card(BY_SLUG[s]) for s in rel)}</div></div></section>
{f'<section class="section pt0"><div class="wrap"><h2 class="mb">More in {e(c)}</h2><div class="grid g3">{"".join(post_card(q) for q in more)}</div></div></section>' if more else ''}{cta_band()}'''
    title = next(t for t in (f'{p["title"]} | Enjoy Moldova Blog', f'{p["title"]} | Enjoy Moldova', p['title']) if len(t) <= 60 or t == p['title'])
    ld = {'@context': 'https://schema.org', '@type': 'BlogPosting', 'headline': p['title'], 'datePublished': p['date'], 'image': post_img(p),
          'publisher': ORG_LD, 'mainEntityOfPage': f'https://moldova.solei.md/{slug}/', 'articleSection': c}
    layout(f'/{slug}/', title, desc[:158], page, [ld, crumbs_ld(('Blog', '/blog/'), (c, f'/blog/category/{cat_slug(c)}/'), (p['title'], f'/{slug}/'))])


def blog_listing(base, cat, posts, cats):
    pages = max(1, -(-len(posts) // BLOG_PER_PAGE))
    chips = (f'<a class="chip{" on" if cat is None else ""}" href="/blog/">All articles</a>' +
             ''.join(f'<a class="chip{" on" if c == cat else ""}" href="/blog/category/{cat_slug(c)}/">{e(c)} <small>{sum(post_cat(p) == c for p in POSTS)}</small></a>' for c in cats))
    for n in range(pages):
        path = base if n == 0 else f'{base}page/{n + 1}/'
        chunk = posts[n * BLOG_PER_PAGE:(n + 1) * BLOG_PER_PAGE]
        featured = ''
        if cat is None and n == 0:
            featured = f'<div class="grid feat-posts">{"".join(post_card(p) for p in chunk[:3])}</div><h2 class="mb mt">More articles</h2>'
            chunk = chunk[3:]
        link = lambda i: base if i == 0 else f'{base}page/{i + 1}/'
        pager = '' if pages == 1 else ('<nav class="pager" aria-label="Pages">' +
                 (f'<a href="{link(n - 1)}">← Newer</a>' if n else '<span></span>') +
                 '<span class="nums">' + ''.join(f'<a class="{"on" if i == n else ""}" href="{link(i)}"{" aria-current=page" if i == n else ""}>{i + 1}</a>' for i in range(pages)) + '</span>' +
                 (f'<a href="{link(n + 1)}">Older →</a>' if n < pages - 1 else '<span></span>') + '</nav>')
        title = cat or 'News, events & wine festivals'
        page_lbl = f' · page {n + 1}' if n else ''
        body = page_hero('Blog', title, 'What’s happening in Moldova: wine festivals, traditions, travel tips and news from our team.', '/img/gagauzia-festival.jpg') + f'''
<section class="section"><div class="wrap">{crumbs(('Blog', '/blog/' if cat or n else None), *(((cat, None),) if cat else ()))}
<div class="chips" aria-label="Blog categories">{chips}</div>
{featured}<div class="grid g3">{''.join(post_card(p) for p in chunk)}</div>{pager}
</div></section>{cta_band()}'''
        layout(path, f'{"Blog: " + cat if cat else "Blog: Moldova News, Events & Wine Festivals"}{page_lbl} | Enjoy Moldova',
               f'{title}: articles about Moldova from the Enjoy Moldova team{page_lbl}.', body)


def about_us():
    src = SITE_PAGES['about-us']['text']
    # milestones: each one is told in an article of the site's own blog
    timeline = [('2001', 'Founded in Chișinău', 'Solei-Turism starts as a tour operator for travel to and within Moldova.', 'happy-anniversary-solei-turism'),
                ('2016', 'First-degree diplomas', 'At the “Tourism. Leisure. Hotels” fair in Chișinău: for inbound tourism, for domestic tourism and for the best website promoting Moldova.', 'solei-turism-diplomas'),
                ('2018', 'Moldova at the big fairs', 'Our stand at ITB Berlin, MITT Moscow and COTTM Beijing, presenting Moldova as a new destination.', 'itb-berlin-2018-the-perfect-holiday-starts-here'),
                ('2023', 'Back at ITB Berlin', 'New itineraries for our partners, at stand 206 in hall 1.1.', 'tourist-fair-itb-berlin-2023'),
                ('2024', 'Best travel agency for inbound tourism', 'Moldova Tourism Awards 2024: first place in inbound tourism in the Republic of Moldova.', 'moldova-tourism-awards')]
    tl = ''.join(f'<li><span class="tl-year">{y}</span><div><h3>{e(h)}</h3><p>{e(t)}</p><a class="more" href="/{s}/">Read the story →</a></div></li>' for y, h, t, s in timeline)
    team = ''.join(f'<div class="team-slot">{ic(i, "ic ic-lg")}<b>{r}</b><span>Photo, name, languages</span></div>' for i, r in
                   [('f-bird', 'Your guide'), ('f-glass', 'Wine expert'), ('f-route', 'Trip planner'), ('f-heart', 'Groups & MICE')])
    body = page_hero('About us', 'Enjoy Moldova by Solei Tourism', 'A Chișinău-based travel company since 2001, repeatedly awarded Best Inbound Travel Agency in the Republic of Moldova.', '/img/besalma.jpg') + f'''
<section class="facts section"><div class="wrap"><div class="grid g4">
<div><b>2001</b><span>founded in Chișinău</span></div><div><b>20+ years</b><span>organising football team travel and events</span></div>
<div><b>13</b><span>partner wineries for tastings</span></div><div><b>FIT &amp; groups</b><span>individual travellers and groups, tours and MICE</span></div></div></div></section>
<section class="section"><div class="wrap">{crumbs(('About us', None))}
<div class="about-intro"><h2>Your local team in Moldova</h2>
<p class="lead">We plan the logistics and every detail of your trip, so you can simply enjoy it. Our guides help you understand local life, not just see the sights.</p></div>
<h2 class="mt mb">Our story</h2><ol class="timeline">{tl}</ol>
<h2 class="mt">The people you’ll travel with</h2>
<div class="todo"><b>De completat: echipa</b>3–6 oameni: o fotografie, numele, rolul și limbile vorbite. Oamenii reali sunt ce lipsește cel mai mult de pe site.</div>
<div class="team">{team}</div>
<article class="prose narrow-prose mt"><details class="readmore"><summary>Read our full company profile</summary>{text_to_html('about-us', src)}</details>
<p><a class="more" href="/groups-mice/">Groups, MICE &amp; travel agents →</a></p></article></div></section>{cta_band()}'''
    layout('/about-us/', 'About Enjoy Moldova by Solei Tourism | Since 2001', 'Enjoy Moldova by Solei Tourism: Moldova DMC since 2001, awarded Best Inbound Travel Agency. Tours, transfers, guides, business travel and MICE.', body, [ORG_LD])


def groups_page():
    services = [('f-route', 'Transfers & transport', 'Airport transfers and any vehicle: VIP cars, minivans, minibuses and coaches, plus rent-a-car.'),
                ('f-tulip', 'Accommodation', 'Hotels in Chișinău and across Moldova, countryside guest houses and Tiraspol.'),
                ('f-tree', 'Tailor-made programmes', 'FIT and group tours, combined tours with Romania and city breaks (Bucharest, Iași, Chișinău, Tiraspol).'),
                ('f-star', 'Events & sport', 'MICE, festivals and special event tours. More than 20 years of travel arrangements for football teams.'),
                ('f-bowl', 'Catering', 'Group meals, wine dinners and tastings at partner wineries.'),
                ('f-bird', 'Guides', 'Licensed guides; English and other languages on request.')]
    body = page_hero('For groups & partners', 'Groups, MICE & travel agents', 'Your local partner in Moldova since 2001: transport, hotels, guides, events and tailor-made programmes.', '/img/cricova.jpg') + f'''
<section class="section"><div class="wrap">{crumbs(('About', '/about-us/'), ('Groups, MICE & agents', None))}
<div class="grid g3">{''.join(f'<div class="feat">{ic(i, "ic ic-lg ic-c")}<h3>{h}</h3><p>{p}</p></div>' for i, h, p in services)}</div>
<div class="contact-layout mt"><div class="prose"><h2>Why work with us</h2><ul class="ticks">
<li>A DMC based in Chișinău since 2001, repeatedly awarded Best Inbound Travel Agency in Moldova</li>
<li>Relationships with airlines, hotels, wineries and travel companies</li><li>Individual and corporate clients, FIT and groups</li>
<li>One local contact for logistics, so your group can focus on the trip</li></ul>
<p>Call {SITE['phone']} or write to <a href="mailto:{SITE['email']}">{SITE['email']}</a>.</p></div>
<div class="form-card" id="quote"><h2>Request a group proposal</h2><p class="small">Tell us the dates, group size and what the group needs.</p>{quote_form('custom', button='Request a proposal')}</div></div>
</div></section>'''
    layout('/groups-mice/', 'Groups, MICE & Travel Agents in Moldova | Enjoy Moldova DMC', 'Moldova DMC since 2001: group tours, MICE, events, transfers, hotels and guides for travel agents and companies.', body, [ORG_LD])


def contact():
    q = 'Alexei Corobceanu 9, Chisinau, Moldova'
    body = page_hero('Contact', 'Plan your trip with us', 'Tell us your dates and group size. We’ll reply by email with your itinerary and price.', '/img/orheiul-vechi.jpg') + f'''
<section class="section"><div class="wrap">{crumbs(('Contact', None))}
<div class="contact-layout"><div>
<h2>Get in touch</h2>
<ul class="contact-list">
<li>{ic('f-route')}<div><b>Office</b>Incoming Tourism &amp; Business Travel Department<br>{e(SITE['address'])}</div></li>
<li>{ic('f-bird')}<div><b>Phone</b><a href="{SITE['phone_href']}">{SITE['phone']}</a></div></li>
<li>{ic('f-romb')}<div><b>Email</b><a href="mailto:{SITE['email']}">{SITE['email']}</a></div></li>
<li>{ic('f-sun')}<div><b>Office hours</b>{SITE['hours']} (Chișinău time, GMT+2)</div></li></ul>
<p>{wa('Hello! I’d like to plan a trip to Moldova.')}</p>
<div class="map"><iframe title="Office map" loading="lazy" src="https://maps.google.com/maps?q={q.replace(' ', '+')}&amp;output=embed"></iframe></div>
</div>
<div class="form-card" id="quote"><h2>Get a free quote</h2><p class="small">Takes about 1 minute. Or <a href="/plan-my-trip/">build your trip step by step</a>.</p>{quote_form()}</div>
</div></div></section>'''
    layout('/contact/', 'Contact Enjoy Moldova | Get a Free Tour Quote', f'Contact Enjoy Moldova in Chișinău: {SITE["phone"]}, {SITE["email"]}. Get a free quote for your tour of Moldova.', body, [ORG_LD])


def legal(path, title, intro, html_body):
    body = page_hero('Legal', title, intro, '/img/capriana.jpg') + f'''<section class="section"><div class="wrap">{crumbs((title, None))}
<article class="prose narrow-prose legal"><div class="todo"><b>Șablon: de verificat juridic</b>Textul de mai jos e o structură de pornire. Câmpurile din [paranteze] trebuie completate, iar textul final verificat de un jurist.</div>{html_body}</article></div></section>'''
    layout(path, f'{title} | Enjoy Moldova', intro, body)


def legal_pages():
    legal('/privacy/', 'Privacy Policy', 'How we collect and use your personal data.', f'''
<p class="small">Last updated: [date]</p>
<h2>Who we are</h2><p>[Full legal name of the company], trading as Enjoy Moldova by Solei Tourism, {e(SITE['address'])}, [company registration number / IDNO]. Contact: <a href="mailto:{SITE['email']}">{SITE['email']}</a>.</p>
<h2>What we collect</h2><ul class="ticks"><li>Details you send in our forms: name, email, travel dates, number of travellers, interests and your message.</li>
<li>Messages you send us by WhatsApp, phone or email.</li><li>Website usage data through cookies, only with your consent (for example Google Analytics).</li></ul>
<h2>Why we use it</h2><p>To answer your request, prepare your quote and organise your trip; to meet legal and accounting obligations; and, only if you agree, to send you news and offers.</p>
<h2>Who we share it with</h2><p>Only the partners needed to deliver your trip (hotels, transport, guides, wineries) and service providers who host our website and email. [List processors and any transfers outside Moldova / the EU.]</p>
<h2>How long we keep it</h2><p>[Retention period] after your request or trip, unless the law requires longer.</p>
<h2>Your rights</h2><p>You can ask to access, correct or delete your data, object to its use or withdraw consent at any time by writing to <a href="mailto:{SITE['email']}">{SITE['email']}</a>. [Applicable law: Law no. 133/2011 on personal data protection of the Republic of Moldova and, for travellers in the EU, the GDPR: to be confirmed by a lawyer.]</p>''')
    legal('/terms/', 'Terms & Conditions', 'The terms for our quotes, bookings and tours.', '''
<p class="small">Last updated: [date]</p>
<h2>Quotes and bookings</h2><p>Requesting a quote is free and doesn’t commit you. A booking is confirmed when you accept our quote and [pay the deposit / receive our written confirmation].</p>
<h2>Prices</h2><p>Prices are in euro, per person, and depend on group size. Day trip prices include the items listed under “What’s included”. Optional extras are paid separately. [Validity of prices, currency and taxes.]</p>
<h2>Payment</h2><p>[Deposit, balance, payment methods and deadlines.]</p>
<h2>Changes and cancellations</h2><p>See our <a href="/cancellation-policy/">cancellation policy</a>. We may adjust an itinerary for safety, weather or closures and will offer a comparable alternative.</p>
<h2>Your responsibilities</h2><p>You are responsible for valid travel documents (passport, visas where needed) and for following local rules, including at border crossings. We recommend travel insurance.</p>
<h2>Liability and law</h2><p>[Limits of liability, force majeure, complaints procedure, governing law and jurisdiction.]</p>''')
    legal('/cancellation-policy/', 'Cancellation policy', 'What happens if your plans change.', '''
<p>Asking for a quote is free and doesn’t commit you to anything. For confirmed bookings the following terms apply:</p>
<div class="ptable"><table><thead><tr><th>When you cancel</th><th>Day trips</th><th>Multi-day tours</th></tr></thead><tbody>
<tr><th>[X] days or more before</th><td>[free / % refund]</td><td>[free / % refund]</td></tr>
<tr><th>[Y–X] days before</th><td>[%]</td><td>[%]</td></tr>
<tr><th>Less than [Y] days / no-show</th><td>[%]</td><td>[%]</td></tr></tbody></table></div>
<h2>If we have to change or cancel</h2><p>If a tour can’t run (for example because of a border closure, weather or safety), we offer another date, a comparable tour or [a full refund].</p>
<h2>How to cancel</h2><p>Write to <a href="mailto:incoming@solei.md">incoming@solei.md</a> or message us on WhatsApp. We confirm every cancellation in writing.</p>''')


def thank_you():
    body = f'''<section class="section center thanks"><div class="wrap narrow">
<div class="ty-ic">{ic('f-tulip', 'ic ic-xl')}</div><h1>Thank you, your request is in!</h1>
<p class="lead">Here’s what happens next.</p>
<ol class="next-steps"><li><b>We read your request</b>during office hours, {SITE['hours']} (Chișinău time).</li>
<li><b>You get your itinerary and price</b>by email, tailored to your dates and group.</li>
<li><b>You decide.</b>The quote is free and doesn’t commit you to anything.</li></ol>
<div class="trip-summary js-trip-summary" hidden><h3>Your trip request</h3><pre></pre></div>
<p class="small">Need it sooner? Call <a href="{SITE['phone_href']}">{SITE['phone']}</a>.</p>
<div class="ctas center-ctas">{wa('Hello! I just sent a request on your website.')}<a class="btn btn-outline" href="/plan-your-trip/">Read our travel tips</a></div>
</div></section>'''
    layout('/thank-you/', 'Thank you | Enjoy Moldova', 'Your request has been sent.', body)


def not_found():
    body = f'''<section class="section center thanks"><div class="wrap narrow"><div class="ty-ic">{ic('f-route', 'ic ic-xl')}</div>
<h1>You’ve wandered 80 m underground and got lost in the tunnels.</h1><p class="lead">The page you’re looking for may have moved.</p>
<div class="ctas center-ctas"><a class="btn btn-primary" href="/tours/">See all tours</a><a class="btn btn-outline" href="/">Back to the surface</a></div></div></section>'''
    layout('/404.html', 'Page not found | Enjoy Moldova', 'Page not found.', body)


# ---------------------------------------------------------------- motif kit: SVG files for social media, print and Canva
KIT_COLORS = {'vin': '#8e0442', 'verde': '#427822', 'albastru': '#117799', 'alb': '#ffffff'}
ICON_NAMES = {'glass': 'Pahar', 'tulip': 'Lalea', 'romb': 'Romb', 'sun': 'Soare', 'bird': 'Păsări', 'tree': 'Pomul vieții', 'tower': 'Mănăstire',
              'star': 'Stea', 'flower': 'Floare', 'bowl': 'Bucate', 'hook': 'Cârlig (covor)', 'route': 'Drum', 'leaf': 'Frunză', 'grapes': 'Struguri',
              'church': 'Biserică', 'fortress': 'Cetate', 'heart': 'Inimă', 'bottle': 'Sticlă'}
ORN_TILE = ("<path d='M0 9h9M23 9h14M51 9h13' stroke='#427822' stroke-width='2.5' stroke-linecap='round'/>"
            "<path d='M16 2l7 7-7 7-7-7z' fill='none' stroke='#8e0442' stroke-width='2.5' stroke-linejoin='round'/>"
            "<path d='M16 6.5l2.5 2.5-2.5 2.5-2.5-2.5z' fill='#d40025'/><path d='M44 3.5l5.5 5.5-5.5 5.5-5.5-5.5z' fill='#f47e55'/>"
            "<circle cx='30' cy='3.5' r='1.8' fill='#117799'/><circle cx='30' cy='14.5' r='1.8' fill='#117799'/>")
PALETTE = [('Vișiniu', '#8e0442'), ('Roșu', '#d40025'), ('Coral', '#f47e55'), ('Verde', '#427822'), ('Verde închis', '#005e62'),
           ('Albastru', '#117799'), ('Roz', '#a7326b'), ('Galben', '#d19a0a'), ('Text', '#2a1f1d'), ('Crem', '#faf6f0')]


def design_kit():
    kit = os.path.join(ROOT, 'motive')
    symbols = dict(re.findall(r'<symbol id="f-([\w-]+)" viewBox="0 0 48 48">(.*?)</symbol>', SPRITE, re.S))
    for cname, col in KIT_COLORS.items():
        os.makedirs(os.path.join(kit, cname), exist_ok=True)
        for sid, inner in symbols.items():
            open(os.path.join(kit, cname, f'{sid}.svg'), 'w', encoding='utf8').write(
                f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="512" height="512" fill="none" stroke="{col}" '
                f'stroke-width="4" stroke-linecap="round" stroke-linejoin="round" color="{col}">{inner}</svg>')
    open(os.path.join(kit, 'pomul-vietii.svg'), 'w', encoding='utf8').write(tree_hero(photos=False))
    open(os.path.join(kit, 'bordura.svg'), 'w', encoding='utf8').write(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 18" width="1920" height="54"><defs><pattern id="o" width="64" height="18" patternUnits="userSpaceOnUse">{ORN_TILE}</pattern></defs><rect width="640" height="18" fill="url(#o)"/></svg>')
    # Instagram frame (1080×1080, transparent middle): bands top and bottom, a tulip in each corner
    corner = lambda x, y: f'<g transform="translate({x} {y}) scale(1.6)" fill="none" stroke="#8e0442" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" color="#d40025">{symbols["tulip"]}</g>'
    open(os.path.join(kit, 'rama-instagram.svg'), 'w', encoding='utf8').write(
        f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1080" width="1080" height="1080"><defs><pattern id="o" width="64" height="18" patternUnits="userSpaceOnUse">{ORN_TILE}</pattern></defs>
<g transform="translate(0 30) scale(2)"><rect x="60" width="420" height="18" fill="url(#o)"/></g><g transform="translate(0 1014) scale(2)"><rect x="60" width="420" height="18" fill="url(#o)"/></g>
{corner(24, 6)}{corner(980, 6)}{corner(24, 990)}{corner(980, 990)}</svg>''')

    tiles = ''.join(f'''<div class="kit-tile"><div class="kit-ic">{ic('f-' + sid, 'ic')}</div><b>{e(ICON_NAMES.get(sid, sid))}</b>
<small>{' · '.join(f'<a href="/motive/{c}/{sid}.svg" download>{c}</a>' for c in KIT_COLORS)}</small></div>''' for sid in symbols)
    swatches = ''.join(f'<div class="sw"><span style="background:{h}"></span><b>{n}</b><code>{h}</code></div>' for n, h in PALETTE)
    body = page_hero('Kit de brand', 'Motive tradiționale Enjoy Moldova', 'Desenate în stilul logo-ului: linii groase, capete rotunjite, motive de broderie. Gata de folosit pe site, în social media și în print.', '/img/gagauzia-festival.jpg') + f'''
<section class="section"><div class="wrap">
<h2 class="mb">Iconițe ({len(symbols)})</h2><p class="small mb">Fiecare se descarcă în 4 culori, ca SVG (se mărește fără pierderi și se deschide în Canva, Figma, Illustrator). Pe poze folosiți varianta albă.</p>
<div class="kit-grid">{tiles}</div>
<h2 class="mb mt">Pomul vieții</h2>
<div class="kit-tree"><div>{tree_hero()}</div><div class="prose"><p>Elementul principal al brandului: ramurile se termină în medalioane cu poze și în motive tradiționale. Pe site se desenează singur la încărcare.</p>
<p><a class="btn btn-primary" href="/motive/pomul-vietii.svg" download>Descarcă varianta cu rame goale</a></p><p class="small">Ramele rotunde sunt goale: puneți pozele voastre în ele (de exemplu în Canva).</p></div></div>
<h2 class="mb mt">Bordura tradițională</h2><div class="ornament kit-orn"></div><p><a class="more" href="/motive/bordura.svg" download>Descarcă bordura (SVG) →</a> · <a class="more" href="/motive/rama-instagram.svg" download>Ramă pentru postări Instagram 1080×1080 →</a></p>
<h2 class="mb mt">Paleta de culori</h2><div class="kit-sw">{swatches}</div>
<h2 class="mb mt">Reguli simple</h2><ul class="ticks"><li>Grosimea liniei e mereu 1/12 din mărimea iconiței, cu capete rotunjite, ca la logo.</li>
<li>Maximum 3 culori pe o grafică, pe fundal crem sau alb. Pe poze: varianta albă.</li><li>Nu deformați și nu rotiți motivele; mărimea minimă e 24 px.</li>
<li>Bordura separă secțiuni; nu o puneți peste text.</li></ul>
</div></section>'''
    layout('/design-kit/', 'Kit de motive tradiționale | Enjoy Moldova', 'Motivele tradiționale ale brandului Enjoy Moldova: iconițe, pomul vieții, bordura și paleta de culori.', body, noindex=True)
    return len(symbols)


# ---------------------------------------------------------------- 301 redirects (old WordPress URLs)
def redirects():
    pairs = [(f'/tours/{old}/', f'/tours/{new}/') for old, new in NEW_SLUGS.items()] + list(PAGE_REDIRECTS.items())
    for old, new in pairs:  # prototype: meta-refresh stubs so old links still work locally
        write(old, f'<!doctype html><meta charset="utf-8"><title>Moved</title><link rel="canonical" href="https://moldova.solei.md{new}">'
                   f'<meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url={new}"><a href="{new}">This page has moved</a>')
    open(os.path.join(ROOT, 'REDIRECTS-301.csv'), 'w', encoding='utf8').write('source,target\n' + ''.join(f'{o},{n}\n' for o, n in pairs))
    open(os.path.join(ROOT, 'redirects.htaccess'), 'w', encoding='utf8').write(
        '# 301 redirects from the old WordPress URLs. Paste into .htaccess above the WordPress block, or import REDIRECTS-301.csv into the Redirection plugin.\n'
        + ''.join(f'Redirect 301 {o} {n}\n' for o, n in pairs))
    return len(pairs)


if __name__ == '__main__':
    print('responsive images made:', make_responsive())
    home(); tours_index()
    for k, c in CATEGORIES.items(): category(k, c)
    for t in TOURS: tour_page(t)
    section_index('about-moldova', 'About Moldova', 'Facts, the capital, food and why Moldova is worth the trip.', '/img/orheiul-vechi.jpg')
    section_index('useful-info', 'Useful info', 'Practical information for your trip: phone numbers, customs, borders and embassies.', '/img/capriana.jpg')
    for k, v in PAGES.items(): content_page(k, *v)
    plan_hub(); safety_page(); itinerary_page(); cricova_vs_milestii()
    blog(); about_us(); groups_page(); contact(); legal_pages(); thank_you(); not_found()
    builder_page(); destinations_page()
    n = redirects()
    k = design_kit()
    print('built', len(TOURS), 'tours,', len(DESTINATIONS) - 1, 'destinations,', n, 'redirects,', k, 'motifs')
