# Copy of the built site for GitHub Pages, which serves it under /<repo>/ instead of the domain root.
# Usage: python -I _build/pages.py OUT_DIR /enjoy-moldova
import os, re, sys, shutil
SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT, BASE = sys.argv[1], sys.argv[2].rstrip('/')
SKIP = {'_build', '.git'}
# root-absolute URLs in attributes, url(), srcset lists and JSON strings: "/x" -> "/enjoy-moldova/x"
ABS = re.compile(r'(?:(?<==")|(?<==\')|(?<=url\()|(?<=, )(?=/img/)|(?<=": ")|(?<=":"))/(?![/\s>])')

for dp, dirs, fs in os.walk(SRC):
    dirs[:] = [d for d in dirs if d not in SKIP and os.path.join(dp, d) != os.path.abspath(OUT)]
    for f in fs:
        s = os.path.join(dp, f)
        t = os.path.join(OUT, os.path.relpath(s, SRC))
        os.makedirs(os.path.dirname(t), exist_ok=True)
        if f.endswith(('.html', '.css')):
            txt = open(s, encoding='utf8').read()
            txt = ABS.sub(BASE + '/', txt)
            open(t, 'w', encoding='utf8').write(txt)
        else:
            shutil.copy2(s, t)
print('pages copy ->', OUT)
