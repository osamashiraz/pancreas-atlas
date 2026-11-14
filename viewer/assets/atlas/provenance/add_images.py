"""Adds images (and, optionally, new entries) to the atlas without touching what is already there.
  python3 viewer/assets/atlas/provenance/add_images.py <folder of downloaded originals> <additions.py>   (needs Pillow)
additions.py defines GROUPS (new groups, may be empty), ENTRIES (new entries, text only) and ADD = {entry id: [image, ...]},
each image a dict: file (relative to the folder), caption, mag, credit, licence, page (source page), crop (fractions or None),
first (True to put it before the existing images, which then drops the entry's pins). Appends to CREDITS.md."""
import json, sys
from pathlib import Path
from PIL import Image
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[2]; CAND = Path(sys.argv[1]).resolve(); OUT = ROOT / 'assets' / 'atlas'
ns = {}; exec(open(sys.argv[2]).read(), ns)
D = json.loads((ROOT / 'src' / 'atlas.json').read_text()); have = {g['key'] for g in D['groups']}; ids = {e['id'] for e in D['entries']}
D['groups'] += [g for g in ns.get('GROUPS', []) if g['key'] not in have]; D['entries'] += [e for e in ns.get('ENTRIES', []) if e['id'] not in ids]
rows = []
for e in D['entries']:
    for w in ns['ADD'].get(e['id'], []):
        if any(im.get('caption') == w['caption'] for im in e['images']): continue
        im = Image.open(CAND / w['file']).convert('RGB')
        if w.get('crop'): x0, y0, x1, y1 = w['crop']; im = im.crop((int(x0 * im.width), int(y0 * im.height), int(x1 * im.width), int(y1 * im.height)))
        if im.width > 960: im = im.resize((960, round(im.height * 960 / im.width)), Image.LANCZOS)
        k = 1 + max([int(p.stem.rsplit('-', 1)[1]) for p in OUT.glob(e['id'] + '-*.jpg') if not p.name.startswith('t-')] or [0]); name = f"{e['id']}-{k}.jpg"; im.save(OUT / name, quality=80, optimize=True)
        rec = {'src': 'atlas/' + name, 'w': im.width, 'h': im.height, 'caption': w['caption'], 'credit': w['credit'], 'licence': w['licence']}
        if w.get('mag'): rec['mag'] = w['mag']
        first = w.get('first') or not e['images']
        if first:
            th = im.copy(); s = max(360 / th.width, 270 / th.height); th = th.resize((round(th.width * s), round(th.height * s)), Image.LANCZOS); x0 = (th.width - 360) // 2; y0 = (th.height - 270) // 2
            old = e.get('thumb'); th.crop((x0, y0, x0 + 360, y0 + 270)).save(OUT / ('t-' + name), quality=72, optimize=True); e['thumb'] = 'atlas/t-' + name
            if old and old != e['thumb'] and (OUT / old[6:]).exists(): (OUT / old[6:]).unlink()
            e['images'].insert(0, rec)
        else: e['images'].append(rec)
        rows.append(f"| `{name}` | {e['name']} | {w['caption']} | {w['credit']} | {w['licence']} | {w.get('page', '')} |")
(ROOT / 'src' / 'atlas.json').write_text(json.dumps(D, indent=1, ensure_ascii=False) + '\n')
with open(OUT / 'CREDITS.md', 'a') as f: f.write('\n'.join(rows) + ('\n' if rows else ''))
print(len(rows), 'images added;', len(D['entries']), 'entries')
