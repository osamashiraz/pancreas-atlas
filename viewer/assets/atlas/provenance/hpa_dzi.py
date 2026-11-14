"""Fetch a region of the HPA dictionary slide (Deep Zoom). region in full-resolution pixels; level 17 = full."""
import sys, io, time, math, urllib.request
from PIL import Image
B = 'https://images.proteinatlas.org/dictionary_images/fileup5eb986535b8a5956243229_files'; W, H, T, MAXL = 97878, 83415, 254, 17
def tile(L, c, r):
    for k in range(3):
        try: return Image.open(io.BytesIO(urllib.request.urlopen(urllib.request.Request(f'{B}/{L}/{c}_{r}.jpg', headers={'User-Agent': 'pancreas-atlas/1.0 (oshah@unmc.edu)'}), timeout=40).read())).convert('RGB')
        except Exception as e: time.sleep(2)
    raise e
def region(x0, y0, x1, y1, L):
    s = 2 ** (MAXL - L); a0, b0, a1, b1 = int(x0 / s), int(y0 / s), int(x1 / s), int(y1 / s); out = Image.new('RGB', (a1 - a0, b1 - b0), 'white')
    for c in range(a0 // T, (a1 - 1) // T + 1):
        for r in range(b0 // T, (b1 - 1) // T + 1):
            t = tile(L, c, r); ox = c * T - (1 if c else 0); oy = r * T - (1 if r else 0); out.paste(t, (ox - a0, oy - b0)); time.sleep(0.15)
    return out
if __name__ == '__main__':
    x0, y0, x1, y1, L = map(int, sys.argv[1:6]); im = region(x0, y0, x1, y1, L); im.save(sys.argv[6], quality=90); print(im.size)
