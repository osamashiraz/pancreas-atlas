"""Prepares the atlas images and writes them, with credits, into viewer/src/atlas.json.
  python3 viewer/assets/atlas/provenance/prepare_images.py <folder of downloaded originals>   (needs Pillow)
The originals are not kept in the repository: download each from the source_page in the manifests here, into the
same relative path as its manifest "file". wiring.py says which original goes to which entry, with crop and caption.
Idempotent: rebuilds viewer/assets/atlas/*.jpg, CREDITS.md and every entry's images. A missing original is reported and skipped
(so run it only with the full set, or the entry loses that image)."""
import json, glob, re, sys
from pathlib import Path
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[2]; CAND = Path(sys.argv[1]).resolve(); OUT = ROOT / 'assets' / 'atlas'
MAN = {}
for f in sorted(glob.glob(str(HERE / 'manifest-*.json'))):
    for x in json.load(open(f)): MAN[x['file']] = x
JOURNAL = {'10.1186/s13256': 'J Med Case Rep', '10.1089/crpc': 'Case Rep Pancreat Cancer', '10.1089/pancan': 'J Pancreat Cancer', '10.1186/s40792': 'Surg Case Rep', '10.3389/fonc': 'Front Oncol', '10.3389/fmed': 'Front Med', '10.3390/cimb': 'Curr Issues Mol Biol', '10.1186/s13000': 'Diagn Pathol', '10.7759/cureus': 'Cureus', '10.1055/s-0041-1728651': 'Surg J (N Y)'}
def credit(x):
    if x.get('doi'):
        a = re.split(r',\s*', x['authors'].strip())[0].replace(' et al.', ''); j = x.get('journal') or next((v for k, v in JOURNAL.items() if x['doi'].startswith(k)), '')
        fig = (x.get('figure') or '').split('(')[0].strip(); fig = fig[0].lower() + fig[1:] if fig else ''
        return f"{a} et al. {j} {x.get('year')}, doi:{x['doi']}" + (f", {fig}" if fig.startswith('fig') else '')
    return f"{' '.join(x['authors'].split())}, via Wikimedia Commons"
H = lambda key, caption, mag, credit_, lic: {'src': 'histo:' + key, 'caption': caption, 'mag': mag, 'credit': credit_, 'licence': lic}
DIST = 'Distler et al. Biomed Res Int 2014, doi:10.1155/2014/474905'; CHEN = 'Chen et al. Diagnostics 2023, doi:10.3390/diagnostics13010065'; CHEK = 'Chekmareva et al. Int J Mol Sci 2025, doi:10.3390/ijms262010169'
def C(file, caption, crop=None, mag=None, name=None, credit_=None, lic=None): return {'cand': file, 'caption': caption, 'crop': crop, 'mag': mag, 'name': name, 'credit': credit_, 'lic': lic}
exec(open(HERE / 'wiring.py').read())   # defines WIRING = {entry id: [H(...) or C(...), ...]}
D = json.loads((ROOT / 'src' / 'atlas.json').read_text()); OUT.mkdir(exist_ok=True)
for old in OUT.glob('*.jpg'): old.unlink()
credits = []; missing = []
for e in D['entries']:
    e['images'] = []; e.pop('thumb', None)
    for k, w in enumerate(WIRING.get(e['id'], [])):
        if 'src' in w: e['images'].append(w); continue
        p = CAND / w['cand']
        if not p.exists(): missing.append(w['cand']); continue
        x = MAN.get(w['cand'], {}); im = Image.open(p).convert('RGB')
        if w['crop']: x0, y0, x1, y1 = w['crop']; im = im.crop((int(x0 * im.width), int(y0 * im.height), int(x1 * im.width), int(y1 * im.height)))
        if im.width > 960: im = im.resize((960, round(im.height * 960 / im.width)), Image.LANCZOS)
        name = f"{e['id']}-{k + 1}.jpg"; im.save(OUT / name, quality=80, optimize=True)
        if k == 0: th = im.copy(); s = max(360 / th.width, 270 / th.height); th = th.resize((round(th.width * s), round(th.height * s)), Image.LANCZOS); x0 = (th.width - 360) // 2; y0 = (th.height - 270) // 2; th.crop((x0, y0, x0 + 360, y0 + 270)).save(OUT / ('t-' + name), quality=72, optimize=True); e['thumb'] = 'atlas/t-' + name
        cr = w['credit'] or credit(x); lic = (w['lic'] or x['licence']).split(' (')[0]; mag = w['mag'] if w['mag'] is not None else None
        img = {'src': 'atlas/' + name, 'w': im.width, 'h': im.height, 'caption': w['caption'], 'credit': cr, 'licence': lic}
        if mag: img['mag'] = mag
        e['images'].append(img); credits.append((name, e['name'], w['caption'], cr, lic, x.get('source_page', w.get('page', ''))))
(ROOT / 'src' / 'atlas.json').write_text(json.dumps(D, indent=1, ensure_ascii=False) + '\n')
md = ['# Atlas images', '', 'Micrographs and specimen photographs shown in the atlas, resized (and cropped to one panel where the source was a multi-panel figure). Each keeps the licence of its source. Entries that reuse the lesion views\' images are credited in `../histology/CREDITS.md`.', '', '| File | Entry | Shows | Credit | Licence | Source page |', '|---|---|---|---|---|---|']
md += [f'| `{n}` | {en} | {cap} | {cr} | {lic} | {pg} |' for n, en, cap, cr, lic, pg in credits]
(OUT / 'CREDITS.md').write_text('\n'.join(md) + '\n')
tot = sum(p.stat().st_size for p in OUT.glob('*.jpg'))
print(len(credits), 'files,', round(tot / 1e6, 2), 'MB; entries without image:', [e['id'] for e in D['entries'] if not e['images']]); print('missing candidates:', missing)
