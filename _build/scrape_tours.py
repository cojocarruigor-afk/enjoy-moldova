# One-off: pull tour text (as paragraphs), price tables and photos from the live site into _build/data.
import json, re, html, os, io, urllib.request
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get(u, raw=False):
    b = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})).read()
    return b if raw else b.decode('utf8', 'ignore')


def txt(h):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h))).strip()


def parse_price_table(table):
    """Site tables: header row (1..6 pax), price row, 'Inclusions' rows, optional 'Supplement' row."""
    # each <td> holds one or more <h5> lines: keep every line as its own cell
    rows = [[txt(line) for c in re.findall(r'<td[^>]*>(.*?)</td>', tr, re.S)
             for line in (re.findall(r'<h5[^>]*>(.*?)</h5>', c, re.S) or [c]) if txt(line)]
            for tr in re.findall(r'<tr[^>]*>(.*?)</tr>', table, re.S)]
    res = dict(prices=[], inclusions=[], supplements=[])
    mode = None
    for i, cells in enumerate(rows):
        if any(re.search(r'\d\s*pax', c) for c in cells) and i + 1 < len(rows):
            pax = [int(m) for c in cells for m in re.findall(r'(\d+)\s*pax', c)]
            eur = [int(m) for c in rows[i + 1] for m in re.findall(r'(\d+)\s*[€.]', c)]
            res['prices'] = [{'pax': p, 'eur': e} for p, e in zip(pax, eur)]
            continue
        if cells and cells[0].lower().startswith('inclusion'):
            mode, cells = 'inclusions', cells[1:]
        elif cells and cells[0].lower().startswith('supplement'):
            mode, cells = 'supplements', cells[1:]
        if mode:
            res[mode] += cells
    return res if res['prices'] else None


tours = json.loads(get('https://moldova.solei.md/wp-json/wp/v2/tours?per_page=50&_fields=slug,link,title'))
out = {}
for t in tours:
    h = get(t['link'])
    m = re.search(r'<main.*?</main>', h, re.S)
    body = m.group(0) if m else h
    body = re.sub(r'<(script|style|noscript)[^>]*>.*?</\1>', '', body, flags=re.S)
    price = None
    for table in re.findall(r'<table.*?</table>', body, re.S):
        price = price or parse_price_table(table)
    body_no_tables = re.sub(r'<table.*?</table>', '', body, flags=re.S)
    blocks = []
    for tag, inner in re.findall(r'<(h[1-5]|p|li)[^>]*>(.*?)</\1>', body_no_tables, re.S):
        s = txt(inner)
        if len(s) > 2 and s.lower() not in ('more info', 'tour description….', 'tour description…'):
            blocks.append([tag, s])

    urls = re.findall(r'https?://moldova\.solei\.md/wp-content/uploads/[^"\'\s)]+?\.(?:jpe?g|png|webp)', body)
    full = []
    for u in urls:
        base = re.sub(r'-\d+x\d+(?=\.\w+$)', '', u)
        if base not in full and 'wine-tour-packages' not in base:
            full.append(base)
    imgs = []
    for u in full[:6]:
        name = f"{t['slug']}-{len(imgs) + 1}.jpg"
        path = os.path.join(ROOT, 'img', 'tours', name)
        if not os.path.exists(path):
            try:
                im = Image.open(io.BytesIO(get(u, raw=True))).convert('RGB')
            except Exception:
                continue
            if min(im.size) < 300:
                continue
            im.thumbnail((1600, 1600))
            im.save(path, quality=80, optimize=True, progressive=True)
        imgs.append(name)

    out[t['slug']] = dict(title=html.unescape(t['title']['rendered']), link=t['link'], blocks=blocks, price_table=price, images=imgs)
    print(t['slug'], len(blocks), 'blocks', len(imgs), 'imgs', 'prices' if price else '-')

json.dump(out, open(os.path.join(ROOT, '_build', 'data', 'tours_site.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
