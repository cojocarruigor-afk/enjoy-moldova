# Football / sport travel presentation as a branded PDF for clients and partners.
# Usage: python -I _build/sport_pdf.py  ->  ../prezentari/Enjoy-Moldova-Sport-Travel-2026.pdf (Chrome headless)
import os, sys, html, base64, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); sys.path.insert(0, HERE)
from content_mice import SPORT_LEAD, SPORT_WHO, SPORT_TEAMS_INTRO, SPORT_SERVED, SPORT_SECTIONS, SPORT_WHY_SUB, SPORT_WHY, SPORT_CLOSING
from content_2026 import SPORT_ASSOCIATIONS, SPORT_CLUBS, SPORT_SINCE
e = html.escape
OUT = os.path.join(os.path.dirname(ROOT), 'prezentari'); os.makedirs(OUT, exist_ok=True)

def img(p, w=1600):
    from PIL import Image; import io
    im = Image.open(os.path.join(ROOT, p.lstrip('/'))).convert('RGB'); im.thumbnail((w, w))
    b = io.BytesIO(); im.save(b, 'JPEG', quality=78); return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()

logo = open(os.path.join(ROOT, 'img', 'logo.svg'), encoding='utf8').read() if os.path.exists(os.path.join(ROOT, 'img', 'logo.svg')) else '<b class="wm">ENJOY MOLDOVA</b>'
lst = lambda xs: '<ul>' + ''.join(f'<li>{e(x)}</li>' for x in xs) + '</ul>'
secs = ''.join(f'''<section class="svc"><div class="ph" style="background-image:url({img(im, 900)})"></div><div><h3>{e(t)}</h3><p class="sub">{e(s)}</p>
{''.join(f'<p>{e(p)}</p>' for p in ps)}{lst(items)}{''.join(f'<p>{e(p)}</p>' for p in after)}</div></section>''' for t, s, ps, items, after, im in SPORT_SECTIONS)
t, s, ps, tag = SPORT_CLOSING
doc = f'''<!doctype html><html><head><meta charset="utf-8"><title>Enjoy Moldova · Sports Team Travel & Logistics 2026</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
@page{{size:A4;margin:14mm 16mm 14mm}}@page:first{{margin:0}}*{{box-sizing:border-box;margin:0}}
body{{font:10.5pt/1.5 Inter,Arial,sans-serif;color:#1f1a19;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{position:relative}}.br{{break-before:page}}
.cover{{width:210mm;height:297mm;break-after:page;color:#fff;background:#1d1513 center/cover;display:flex;flex-direction:column;justify-content:flex-end}}
.cover .in{{padding:18mm 16mm;background:linear-gradient(180deg,rgba(20,12,12,0) 0%,rgba(20,12,12,.85) 45%)}}
.cover h1{{font-size:34pt;line-height:1.05;font-weight:800;letter-spacing:-.02em}}.cover .lead{{font-size:15pt;margin:4mm 0 8mm;color:#ffd1bf;font-weight:600}}
.facts{{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid rgba(255,255,255,.35);padding-top:5mm}}.facts b{{display:block;font-size:20pt}}.facts span{{font-size:8.5pt;color:#e8dcd6}}
.wm{{font-size:14pt;letter-spacing:.12em}}.top{{position:absolute;top:14mm;left:16mm;right:16mm;display:flex;justify-content:space-between;font-size:8.5pt;color:#e8dcd6}}
h2{{font-size:18pt;font-weight:800;letter-spacing:-.01em;margin-bottom:2mm;color:#8e0442}}h3{{font-size:12pt;font-weight:700}}
.kick{{font-size:10pt;color:#6b5d59;margin-bottom:5mm}}p{{margin-bottom:2.2mm}}.sub{{font-weight:600;color:#8e0442}}
ul{{padding-left:4.5mm;margin:1mm 0 2.5mm}}li{{margin-bottom:.8mm}}li::marker{{color:#8e0442}}
.grid4{{display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin:4mm 0 7mm}}.card{{border:1px solid #e4e0da;border-radius:3mm;padding:4mm}}
.svc{{display:grid;grid-template-columns:52mm 1fr;gap:6mm;padding:5mm 0;border-top:1px solid #e4e0da;break-inside:avoid}}.svc .ph{{height:40mm;border-radius:2.5mm;background:center/cover}}
.cols{{columns:2;column-gap:8mm;font-size:9.5pt}}.cols li{{break-inside:avoid}}
.why{{display:grid;grid-template-columns:1fr 1fr;gap:3mm 6mm}}.why div{{border-left:2px solid #8e0442;padding-left:3mm;break-inside:avoid}}
.close{{background:#1d1513;color:#fff;border-radius:3mm;padding:7mm;margin-top:7mm}}.close h2{{color:#fff}}.close p{{color:#e8dcd6}}
.foot{{margin-top:6mm;font-size:8pt;color:#6b5d59;display:flex;justify-content:space-between;border-top:1px solid #e4e0da;padding-top:2.5mm}}
.contact b{{color:#fff}}
</style></head><body>
<div class="page cover" style="background-image:url({img('/img/commons/zimbru-stadium.jpg', 2000)})">
<div class="top"><span class="wm">ENJOY MOLDOVA</span><span>by Solei Tourism · Incoming & Business Travel</span></div>
<div class="in"><h1>Sports Team Travel &amp; Logistics in Moldova</h1><p class="lead">{e(SPORT_LEAD)}</p>
<div class="facts"><div><b>{len(SPORT_ASSOCIATIONS)}</b><span>national football associations</span></div><div><b>{len(SPORT_CLUBS)}</b><span>international clubs</span></div><div><b>{SPORT_SINCE}</b><span>first team welcomed</span></div><div><b>24/7</b><span>assistance during the stay</span></div></div></div></div>

<div class="page"><h2>Who We Are</h2>{''.join(f'<p>{e(p)}</p>' for p in SPORT_WHO)}
<h2 style="margin-top:6mm">Sports We Serve</h2><div class="grid4">{''.join(f'<div class="card"><h3>{e(h)}</h3><p>{e(x)}</p></div>' for h, x in SPORT_SERVED)}</div>
</div>
<div class="page br"><h2>International Teams We Have Assisted</h2><p class="kick">{e(SPORT_TEAMS_INTRO)}</p>
<h3>National Football Associations</h3><div class="cols">{lst(SPORT_ASSOCIATIONS)}</div>
<h3 style="margin-top:4mm">International Football Clubs</h3><div class="cols">{lst(SPORT_CLUBS)}</div></div>
<div class="page br"><h2>Complete Team Travel &amp; Logistics</h2>{secs}</div>

<div class="page br"><h2>Why Choose Enjoy Moldova?</h2><p class="kick">{e(SPORT_WHY_SUB)}</p>
<div class="why">{''.join(f'<div><h3>{e(h)}</h3><p>{e(x)}</p></div>' for h, x in SPORT_WHY)}</div>
<div class="close"><h2>{e(t)}</h2><p class="sub" style="color:#ffd1bf">{e(s)}</p>{''.join(f'<p>{e(p)}</p>' for p in ps)}
<p class="contact" style="margin-top:4mm"><b>ENJOY MOLDOVA BY SOLEI TOURISM</b> · {e(tag)}<br>Incoming and Business Travel Department · 9, A. Corobceanu str., MD 2004 Chișinău, Republic of Moldova<br>
incoming@solei.md · +373 22 890 900 · www.moldova.solei.md</p></div>
<div class="foot"><span>“MS Travel Group” SRL | C/F 1007600021047</span><span>Enjoy Moldova by Solei Tourism</span></div></div>
</body></html>'''
h = os.path.join(OUT, 'Enjoy-Moldova-Sport-Travel-2026.html'); open(h, 'w', encoding='utf8').write(doc)
pdf = os.path.join(OUT, 'Enjoy-Moldova-Sport-Travel-2026.pdf')
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
subprocess.run([chrome, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf}', 'file:///' + h.replace(os.sep, '/')], check=True, capture_output=True)
print(pdf, os.path.getsize(pdf))
