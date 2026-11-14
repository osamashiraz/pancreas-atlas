# Normal pancreas from the Human Protein Atlas histology dictionary (whole-slide H&E, CC BY 4.0 per proteinatlas.org/about/licence).
# Crops fetched with hpa_dzi.py (region in full-resolution pixels, level): lobules 30000 46000 54000 64000 L13; acini 56250 30225 57350 31025 L17;
# small duct 54900 29300 56000 30100 L17; large duct 23870 51580 28375 55675 L15. A search of the slide found no clear islet or centroacinar cell.
GROUPS = []; ENTRIES = []
HPA = 'Human Protein Atlas, histology dictionary: normal pancreas (proteinatlas.org); Uhlén et al. Science 2015'; PG = 'https://www.proteinatlas.org/learn/dictionary/normal/pancreas'
I = lambda file, caption, mag, marks: dict(file=file, caption=caption, mag=mag, credit=HPA, licence='CC BY 4.0', page=PG, first=True, marks=marks)
ADD = {
 'normal-lobule': [I('scan-a.jpg', 'Lobules of purple acinar tissue separated by pale septa that carry fat, vessels and the larger ducts.', 'H&E, low power', [[0.45, 0.3, 1], [0.57, 0.115, 3]])],
 'normal-acini': [I('acini-hp.jpg', 'Acini at high power: each cell blue-purple at its base, with red-pink granules at the tip facing the lumen; round basal nuclei.', 'H&E, high power', [[0.41, 0.55, 1], [0.33, 0.5, 2]])],
 'normal-intralobular-duct': [I('smallduct-hp.jpg', 'A small duct among acini: one even ring of cuboidal cells round a clear lumen, inside a thin collar of pink collagen.', 'H&E, high power', [[0.455, 0.53, 1], [0.53, 0.62, 3]])],
 'normal-interlobular-duct': [I('final-interlobular-duct.jpg', 'A large duct in a septum: a single layer of duct cells round a wide lumen, inside a thick wall of collagen, with lobules on every side.', 'H&E', [[0.36, 0.215, 1], [0.17, 0.45, 2]])],
}
