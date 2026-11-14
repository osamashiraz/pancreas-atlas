# Mouse models: text from the eight open-access papers that supply the images (viewer/assets/atlas/provenance/mouse-facts.json).
JOHN = 'Johnson et al. PLoS One 2019, doi:10.1371/journal.pone.0221810'; KARKI = 'Karki et al. PLoS One 2015, doi:10.1371/journal.pone.0145724'; VEITE = 'Veite-Schmahl et al. PLoS One 2017, doi:10.1371/journal.pone.0187552'
MA = 'Ma and Saiyin. PLoS One 2017, doi:10.1371/journal.pone.0176844'; KRAH = 'Krah et al. eLife 2015, doi:10.7554/eLife.07125'; URR = 'Urrutia et al. Front Cell Dev Biol 2021, doi:10.3389/fcell.2021.681153'
GERM = 'Germino et al. PLoS One 2018, doi:10.1371/journal.pone.0194998'; MORR = 'Morris et al. PLoS One 2014, doi:10.1371/journal.pone.0095486'
P = lambda doi: 'https://doi.org/' + doi
GROUPS = [{'key': 'mouse', 'title': 'Mouse models', 'blurb': 'The same sequence in genetically engineered mice, where mutant Kras is switched on in the pancreas: normal tissue, injury, metaplasia, PanIN, carcinoma and spread. Genotypes are given as each paper states them.'}]
E = lambda **k: dict(species='mouse', group='mouse', images=[], **k)
ENTRIES = [
 E(id='mouse-normal', name='Normal mouse pancreas', line='Tightly packed acini with pink granular tips, an islet and a duct: the control for every model.',
   glance=['Acini packed tightly: blue cell bases, pink granular tips', 'A pale islet among them', 'A duct with a thin wall'],
   remember='Controls matter: mice with the Kras allele but no Cre, or Cre alone, keep a normal pancreas.',
   features={'architecture': 'Closely packed acini with islets and ducts; Cre-only and Cre-negative controls show normal structure.', 'cells': 'Pyramidal acinar cells with basal nuclei and apical zymogen granules.'},
   facts={'who': 'Cre-negative littermates carrying lox-stop Kras and Trp53 alleles developed no tumours over up to a year (9 mice); Pdx1-Cre alone gave normal histology at 10 days and 4–6 weeks.'},
   mimics=[{'id': 'normal-acini', 'tell': 'The human counterpart of this entry.'}, {'id': 'mouse-caerulein', 'tell': 'After caerulein the acini swell and vacuolate, the spaces between them widen and inflammatory cells arrive.'}],
   sources=['Johnson et al. 2019, Results and fig. 2B, 3A', 'Urrutia et al. 2021, Results and fig. 1A', 'Morris et al. 2014, fig. 1A', 'Krah et al. 2015, fig. 1']),
 E(id='mouse-caerulein', name='Caerulein pancreatitis', aka='experimental acute pancreatitis', line='Repeated caerulein injections injure the acini: swelling, vacuoles, oedema and inflammatory cells, then recovery.',
   glance=['Spaces between acini widened by oedema', 'Inflammatory cells in the widened stroma', 'Acinar cells swollen and vacuolated, lumina opened up'],
   remember='Acute and reversible: by about ten days most tissue is normal acini again, unless mutant Kras is present.',
   features={'architecture': 'Acini pushed apart by oedema; some turn into duct-like structures (ADM) for a few days.', 'cells': 'Swollen, vacuolated acinar cells; in the first two days some co-express acinar and duct markers.', 'stroma': 'Oedema and an inflammatory infiltrate.'},
   facts={'who': 'A common protocol: eight hourly intraperitoneal injections (50 µg/kg) on each of two consecutive days in mice aged 6–8 weeks. Chronic protocols give one injection a day, five days a week, for four weeks.', 'outlook': 'Most tissue has recovered normal acini by 10 days. The acinar factor Mist1 falls sharply during metaplasia and returns on recovery.'},
   mimics=[{'id': 'mouse-adm', 'tell': 'Injury-induced metaplasia reverses; with mutant Kras it persists and goes on to PanIN.'}, {'id': 'acute-interstitial', 'tell': 'The human counterpart: oedema and inflammation with little necrosis.'}],
   sources=['Karki et al. 2015, Methods, Results and fig. 1B', 'Krah et al. 2015, Methods', 'Urrutia et al. 2021, Methods']),
 E(id='mouse-adm', name='ADM in Kras-mutant mice', aka='acinar-to-ductal metaplasia', line='Acini lose their granules and become small tubes, in an inflamed, fibrous stroma: the first visible step.',
   glance=['Small duct-like tubes where acini should be', 'Inflammatory cells and new stroma round them', 'Normal acini still beside the lesion', 'Some tubes already lined by pale mucinous cells'],
   remember='In the mouse, acinar cells are the usual starting point: ADM first, then PanIN.',
   features={'architecture': 'Acinar tubular complexes and duct-like structures replacing acini; atypical flat lesions and early PanIN alongside.', 'cells': 'Acinar cells that have lost their zymogen granules; the lining of the tubes is often graded with the PanIN scheme.', 'mucin': 'Appears as the tubes turn into PanIN; Alcian-blue-positive area rose over 1, 2 and 3 months after Kras activation in one model.', 'stroma': 'Inflamed and desmoplastic from the start: hyaluronan and activated stellate cells sit beside ADM.'},
   facts={'who': 'Seen within weeks: cohorts of Pdx1-Cre; LSL-KrasG12D mice are examined at 4, 6 and 8 weeks. At 8 weeks every such mouse had neutrophils or histiocytes in the pancreas.', 'molecular': 'Not every PanIN need come from ADM; the older view of an origin in duct epithelium stands beside it.'},
   mimics=[{'id': 'adm', 'tell': 'The human change looks the same, but in people its meaning is unclear and it is common in any injured gland.'}, {'id': 'mouse-panin', 'tell': 'PanIN is a larger duct-like structure lined by tall cells with a mucin cap; ADM tubes are small with low cells.'}],
   sources=['Urrutia et al. 2021, Results and fig. 2B, 7A', 'Johnson et al. 2019, Abstract and fig. 3, 5', 'Veite-Schmahl et al. 2017, Introduction', 'Morris et al. 2014, fig. 1']),
 E(id='mouse-panin', name='Mouse PanIN', aka='mPanIN, in KC mice', line='A duct lined by tall columnar cells with pale mucin and basal nuclei, as in human low-grade PanIN.',
   glance=['One layer of tall columnar cells', 'Pale mucin filling the upper half of each cell', 'Nuclei in a row at the base', 'Normal acini round the lesion'],
   remember='Mutant Kras alone is enough for PanIN; the same grading words are used as in people, and pathologists disagree in the same places.',
   features={'architecture': 'Flat or papillary linings of small ducts, surrounded by normal tissue early on; many lesions do not fit neatly into one grade.', 'cells': 'Tall columnar, mucin-filled.', 'nuclei': 'Basal in PanIN-1; abnormal in PanIN-2; polarity lost, with a cribriform lumen, in PanIN-3.', 'mucin': 'Abundant; Alcian blue is used to measure PanIN burden.'},
   facts={'who': 'KC mice: LSL-KrasG12D with Pdx1-Cre or Ptf1a (p48)-Cre. PanIN are usually minimal at 1 month in Pdx1-Cre KC mice and increase with age; an atlas of Ptf1a-Cre KC mice covers 5 to 16 months.', 'molecular': 'The acinar factor PTF1A, abundant in acinar nuclei, is lost in mouse PanIN and, with rare exceptions, in human PanIN. Ptf1a-Cre keeps tumours to the pancreas; Pdx1-Cre also gives tumours elsewhere.'},
   mimics=[{'id': 'panin-low', 'tell': 'The human lesion; the grading scheme was carried over to the mouse.'}, {'id': 'mouse-adm', 'tell': 'ADM tubes are smaller, with low cells and little mucin, and sit inside a lobule that is breaking down.'}],
   sources=['Krah et al. 2015, Abstract, fig. 1 and 7', 'Veite-Schmahl et al. 2017, Introduction and Methods', 'Germino et al. 2018, fig. 2', 'Urrutia et al. 2021, fig. 2B']),
 E(id='mouse-pda', name='Mouse ductal adenocarcinoma', aka='KPC-type models', line='Adding a second hit to mutant Kras gives invasive, gland-forming carcinoma in dense stroma, like the human tumour.',
   glance=['Irregular glands with open lumina', 'Dense fibrous (desmoplastic) stroma between them', 'Crowded, atypical nuclei lining the glands'],
   remember='Kras starts it; loss of Trp53 or Ink4a speeds it up. Which alleles and which Cre decide latency, so always read the genotype.',
   features={'architecture': 'Infiltrating glands, from well to poorly formed, invading pancreas, fat and duodenal wall.', 'nuclei': 'Marked atypia.', 'mitoses': 'Many, in the model where they are described.', 'stroma': 'Strongly desmoplastic, with few vessels, as in human tumours.'},
   facts={'who': 'KPC: LSL-KrasG12D; LSL-Trp53R172H; Pdx1-Cre. Variants shown here: KPT (tamoxifen-induced Ptf1a-CreER, Trp53 R270H), KPIC (adds Ink4a flox/+; p48-Cre), and Pdx1-Cre; LSL-KrasG12D; Trp53 flox/wt.', 'outlook': 'Median survival 219 days after induction in KPT mice; mean 89 days in KPIC and 62 days in KIC mice; median age at death 159 days in the Trp53 flox/wt model.', 'size': 'Palpable hard masses from about 7 weeks in KPIC mice.'},
   mimics=[{'id': 'pda-well', 'tell': 'The human tumour; mouse tumours in these models are mostly well to moderately differentiated and stroma-rich.'}, {'id': 'mouse-panin', 'tell': 'PanIN stays inside a duct with normal tissue round it; carcinoma is haphazard glands in desmoplastic stroma.'}],
   sources=['Johnson et al. 2019, Results and fig. 2', 'Ma and Saiyin 2017, Methods, Results and fig. 1', 'Germino et al. 2018, Results and fig. 1, 3', 'Kleeff et al. 2016, p. 8']),
 E(id='mouse-met', name='Mouse liver metastasis', line='Tumour glands growing in the liver: the model reproduces spread as well as the primary tumour.',
   glance=['Glands with open lumina that do not belong in liver', 'Plates of pink liver cells round them', 'Fibrous stroma carried with the tumour'],
   remember='Spread depends on the model: liver in 3 of 8 and lung in 1 of 8 KPT mice, but none in the liver in KPIC mice.',
   features={'architecture': 'Neoplastic glands with a desmoplastic reaction inside liver tissue.'},
   facts={'who': 'KPT mice at the humane endpoint: liver metastases in 3 of 8, lung in 1 of 8. KPIC mice invaded neighbouring organs (intestine, kidney) without liver metastases.'},
   mimics=[{'id': 'liver-metastasis', 'tell': 'The human counterpart, usually found as many pale nodules.'}],
   sources=['Johnson et al. 2019, Results and fig. 2D', 'Ma and Saiyin 2017, Results']),
]
I = lambda file, caption, credit, doi, mag='H&E', **k: {**dict(file='mouse/' + file, caption=caption, mag=mag, credit=credit, licence='CC BY 4.0', page=P(doi)), **k}
ADD = {
 'mouse-normal': [I('mouse-normal/dicerhet_3wk_g1A.png', 'Pancreas at 3 weeks: acini (A), an islet (I) and a duct (D), labelled in the source figure. Genotype: Pdx1-CreLate; Dicer flox/+ (a control).', MORR + ', fig. 1A', '10.1371/journal.pone.0095486'),
                  I('mouse-normal/ptf1a_krasG12D_fig1A_acinar.png', 'Normal acinar tissue at high power: basal nuclei, pink granules at the cell tips (letter from the source figure).', KRAH + ', fig. 1A', '10.7554/eLife.07125', mag='H&E, high power')],
 'mouse-caerulein': [I('mouse-caerulein/mist1creert_ap1d_he.png', 'One day after caerulein: widened, oedematous stroma with inflammatory cells beside a congested vessel. Mist1-CreERT/+ mouse. Soft image.', KARKI + ', fig. 1B', '10.1371/journal.pone.0145724'),
                     I('mouse-caerulein/mist1creert_ap6h_he.png', 'Six hours after caerulein: swollen acini with opened lumina and vacuoles. Soft image.', KARKI + ', fig. 1B', '10.1371/journal.pone.0145724')],
 'mouse-adm': [I('mouse-adm/kc_ehmt2wt_F2B.png', 'Pdx1-Cre; LSL-KrasG12D: small tubes replacing acini, inflammatory cells, and ducts lined by pale mucinous cells, beside normal acini.', URR + ', fig. 2B', '10.3389/fcell.2021.681153', licence='CC BY'),
               I('mouse-adm/kpt_B.png', 'Three months after Kras and Trp53 activation in acinar cells (KPT mice): ADM (black arrows) and a PanIN (red arrow) in inflamed stroma; arrows from the source figure.', JOHN + ', fig. 3B', '10.1371/journal.pone.0221810', mag='H&E, ×20')],
 'mouse-panin': [I('mouse-panin-low/ptf1a_krasG12D_fig1B_panin.png', 'Ptf1a-CreERT; LSL-KrasG12D: a duct lined by tall columnar cells with pale mucin and basal nuclei (letter from the source figure). The paper does not give a grade.', KRAH + ', fig. 1B', '10.7554/eLife.07125', mag='H&E, high power'),
                 I('mouse-panin-low/ksr1wt_3mo_g2.png', 'In context at 3 months: a small focus of PanIN among normal acini. Pdx1-Cre; LSL-KrasG12D/+; Trp53 flox/wt.', GERM + ', fig. 2', '10.1371/journal.pone.0194998'),
                 I('mouse-panin-low/mmpca_11mo_B3.png', 'At 11 months in a Ptf1a-Cre; LSL-KrasG12D mouse: dilated, branching ducts lined by tall mucinous cells (number tag from the source atlas).', VEITE + ', fig. 4B', '10.1371/journal.pone.0187552')],
 'mouse-pda': [I('mouse-pda/kpt_pdac_g2C.png', 'KPT mouse: back-to-back glands of columnar cells in dense fibrous stroma.', JOHN + ', fig. 2C', '10.1371/journal.pone.0221810', mag='H&E, ×20'),
               I('mouse-pda/ksr1wt_tumor_g3_hi.png', 'Pdx1-Cre; LSL-KrasG12D/+; Trp53 flox/wt: irregular open glands with secretions; the paper calls these tumours moderately differentiated.', GERM + ', fig. 3', '10.1371/journal.pone.0194998'),
               I('mouse-pda/kpic_he.png', 'KPIC mouse: small, poorly formed glands and single cells in desmoplastic stroma.', MA + ', fig. 1C', '10.1371/journal.pone.0176844')],
 'mouse-met': [I('mouse-met/kpt_liver_met_g2D.png', 'KPT mouse: tumour glands with their stroma inside the liver; pink liver cells at the edges.', JOHN + ', fig. 2D', '10.1371/journal.pone.0221810', mag='H&E, ×20')],
}
for v in ADD.values():
    for w in v:
        if 'licence' not in w: w['licence'] = 'CC BY 4.0'
