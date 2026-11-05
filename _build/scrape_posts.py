# One-off: pull every blog article's body from the live site into _build/data/posts_full.json (clean HTML, no inline styles).
import json, re, html, os, urllib.request
from html.parser import HTMLParser

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
KEEP = {'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'li', 'strong', 'b', 'em', 'i', 'a', 'br', 'table', 'tr', 'td', 'th', 'tbody', 'thead', 'sup'}
BLOCK = {'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'li', 'table', 'tr', 'td', 'th', 'tbody', 'thead'}


def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read().decode('utf8', 'ignore')


class Clean(HTMLParser):
    """Keeps text structure only: headings, paragraphs, lists, links, tables; images and videos become markers."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.stack, self.auto_p, self.images, self.videos = [], [], False, [], []

    def close_auto(self):
        if self.auto_p:
            self.out.append('</p>'); self.auto_p = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('div', 'section', 'figure', 'center') or (tag in BLOCK and tag != 'li'):
            self.close_auto()
        src = a.get('data-src') or a.get('src') or ''  # the theme lazy-loads: the real file sits in data-src
        if tag == 'img':
            src = re.sub(r'^https?://moldova\.solei\.md', '', src)
            if src and not src.startswith('data:') and src not in self.images:  # <noscript> repeats every image
                self.close_auto(); self.images.append(src); self.out.append(f'\x00img{len(self.images) - 1}\x00')
        elif tag == 'iframe':
            if 'youtu' in src and src not in self.videos:
                self.close_auto(); self.videos.append(src.split('?')[0]); self.out.append(f'\x00vid{len(self.videos) - 1}\x00')
        elif tag in KEEP:
            if tag == 'b': tag = 'strong'
            if tag == 'i': tag = 'em'
            attr = ''
            if tag not in BLOCK and tag != 'br' and not self.auto_p and not any(t in BLOCK for t in self.stack if t):
                self.out.append('<p>'); self.auto_p = True  # a bare link or bold line between divs still needs a paragraph
            if tag == 'a':
                href = a.get('href', '')
                if not href or href.startswith('#') or re.search(r'\.(jpe?g|png|webp)$', href, re.I):
                    self.stack.append(None); return  # gallery links to the big photo: keep only the thumbnail
                attr = f' href="{html.escape(href)}"'
            self.stack.append(tag); self.out.append(f'<{tag}{attr}>' if tag != 'br' else '<br>')
            if tag == 'br': self.stack.pop()

    def handle_endtag(self, tag):
        if tag in ('div', 'section', 'figure', 'center'):
            self.close_auto(); return
        if tag == 'b': tag = 'strong'
        if tag == 'i': tag = 'em'
        if tag in KEEP and tag in self.stack or (tag == 'a' and None in self.stack):
            while self.stack:
                t = self.stack.pop()
                if t: self.out.append(f'</{t}>')
                if t == tag or (tag == 'a' and t is None): break
            if tag in BLOCK: self.auto_p = False

    def handle_data(self, d):
        if not d.strip():
            if self.out and not self.auto_p and not self.stack: return
        elif not self.stack and not self.auto_p:
            self.out.append('<p>'); self.auto_p = True
        self.out.append(html.escape(d, quote=False))


def tidy(h):
    h = h.replace('\xa0', ' ')
    h = re.sub(r'<(p|h[234]|li|strong|em)>\s*</\1>', '', h)
    h = re.sub(r'<(p|h[234]|li|strong|em)>\s*</\1>', '', h)
    # a paragraph that is only a short bold line is a heading on the old site
    h = re.sub(r'<p>\s*<strong>([^<]{3,90})</strong>\s*</p>', r'<h3>\1</h3>', h)
    h = re.sub(r'<h2>\s*<strong>(.*?)</strong>\s*</h2>', r'<h2>\1</h2>', h)
    h = re.sub(r'\s+', ' ', h)
    h = re.sub(r'<p>((?:\s*\x00(?:img|vid)\d+\x00)+)\s*</p>', r'\1', h)  # photo-only paragraphs: just the photos
    return re.sub(r'(</(?:p|h[234]|ul|ol|li|table)>)', r'\1\n', h).strip()


posts = json.load(open(os.path.join(DATA, 'posts.json'), encoding='utf8'))
full = {}
for p in posts:
    page = get(p['link'])
    m = re.search(r'<div class="content">\s*<div class="container">(.*?)</main>', page, re.S)
    body = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', m.group(1) if m else '', flags=re.S)
    c = Clean(); c.feed(body); c.close_auto()
    desc = re.search(r'<meta name="description" content="([^"]*)"', page)
    full[p['slug']] = dict(html=tidy(''.join(c.out)), images=c.images, videos=c.videos, desc=html.unescape(desc.group(1)) if desc else '')
    print(p['slug'], len(full[p['slug']]['html']), 'img', len(c.images), 'vid', len(c.videos))
json.dump(full, open(os.path.join(DATA, 'posts_full.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=0)

# files the live site links to but no longer has (404 there too): the build leaves them out
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor
pages = json.load(open(os.path.join(DATA, 'pages.json'), encoding='utf8'))
files = {('https://moldova.solei.md' + i if i.startswith('/') else i) for v in full.values() for i in v['images']}
files |= {html.unescape(h) for v in full.values() for h in re.findall(r'href="(https?://moldova\.solei\.md/wp-content/[^"]+)"', v['html'])}
files |= {i for p in pages for i in p.get('images', []) if i.startswith('http')}


def alive(u):
    try:
        return urllib.request.urlopen(urllib.request.Request(quote(u, safe=':/%'), method='HEAD', headers={'User-Agent': 'Mozilla/5.0'}), timeout=30).status == 200
    except Exception:
        return False

with ThreadPoolExecutor(12) as pool:
    dead = sorted(u for u, ok in zip(sorted(files), pool.map(alive, sorted(files))) if not ok)
json.dump(dead, open(os.path.join(DATA, 'dead_files.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=0)
print('dead files on the live site:', len(dead))
