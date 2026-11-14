# Mouse models of pancreatic neoplasia, one entry per genotype.
# Text only from the papers named in each entry's sources (facts: mouse-facts.json, mouse-facts2.json).
# Hingorani 2003/2005 and Izeradjene 2007 were read as abstracts only; their figures are under copyright and are not used.
# Image paths are relative to the candidate folder passed to add_images.py (viewer/test/out/atlas-candidates2).
JOHN = 'Johnson et al. PLoS One 2019, doi:10.1371/journal.pone.0221810'
KARKI = 'Karki et al. PLoS One 2015, doi:10.1371/journal.pone.0145724'
VEITE = 'Veite-Schmahl et al. PLoS One 2017, doi:10.1371/journal.pone.0187552'
MA = 'Ma and Saiyin. PLoS One 2017, doi:10.1371/journal.pone.0176844'
KRAH = 'Krah et al. eLife 2015, doi:10.7554/eLife.07125'
URR = 'Urrutia et al. Front Cell Dev Biol 2021, doi:10.3389/fcell.2021.681153'
GERM = 'Germino et al. PLoS One 2018, doi:10.1371/journal.pone.0194998'
MORR = 'Morris et al. PLoS One 2014, doi:10.1371/journal.pone.0095486'
CHENG = 'Cheng et al. Nature 2025, doi:10.1038/s41586-025-08917-z'

GROUPS = [{'key': 'mouse', 'title': 'Mouse models, by genotype',
  'blurb': 'Engineered mice in which mutant Kras is switched on in the pancreas, alone (KC) or with a second hit (KPC, KPIC, KIC, KDC). One entry per model, its pictures in order of progression. Genotypes are given as each paper states them.'}]
E = lambda **k: dict(species='mouse', group='mouse', images=[], **k)
TUM = ['Irregular glands with open lumina', 'Dense pink (desmoplastic) stroma between them', 'Crowded, dark nuclei lining the glands']

ENTRIES = [
 E(id='mouse-control', name='Controls', aka='wild-type, Cre only, or a lox-stop allele without Cre',
   line='Tightly packed acini with pink tips, an islet and a duct: what every model is read against.',
   glance=['Acini packed tight: blue bases, pink granular tips', 'A pale islet among them', 'A thin-walled duct'],
   remember='A lox-stop allele does nothing without Cre, and Cre alone does nothing: both controls keep a normal pancreas.',
   features={'architecture': 'Closely packed acini with islets and ducts.', 'cells': 'Pyramidal acinar cells, basal nuclei, apical granules.'},
   facts={'who': 'Cre-negative littermates with lox-stop Kras/Trp53 alleles made no tumours over up to a year; Pdx1-Cre alone gave normal histology at 10 days and 4-6 weeks.'},
   mimics=[{'id': 'normal-acini', 'tell': 'The human counterpart of this entry.'},
           {'id': 'mouse-caerulein', 'tell': 'After caerulein the acini swell, the gaps between them widen and inflammatory cells arrive.'}],
   sources=['Johnson et al. 2019, fig. 3A', 'Urrutia et al. 2021, fig. 1A', 'Morris et al. 2014, fig. 1A', 'Krah et al. 2015, fig. 1']),
 E(id='mouse-caerulein', name='Caerulein pancreatitis', aka='injury model, no oncogene',
   line='Repeated caerulein injections injure the acini: swelling, oedema and inflammatory cells, then recovery.',
   glance=['Gaps between acini widened by oedema', 'Inflammatory cells in the widened stroma', 'Swollen, vacuolated acinar cells'],
   remember='Acute and reversible: by about ten days the tissue is normal acini again, unless mutant Kras is present.',
   features={'architecture': 'Acini pushed apart by oedema; some form duct-like tubes (ADM) for a few days.', 'stroma': 'Oedema and an inflammatory infiltrate.'},
   facts={'who': 'A common protocol: eight hourly injections (50 ug/kg) on each of two days, in mice aged 6-8 weeks.', 'outlook': 'Most tissue recovers by 10 days; the acinar factor Mist1 falls during metaplasia and returns on recovery.'},
   mimics=[{'id': 'mouse-kc', 'tell': 'Injury metaplasia reverses; with mutant Kras it persists and goes on to PanIN.'},
           {'id': 'acute-interstitial', 'tell': 'The human counterpart: oedema and inflammation with little necrosis.'}],
   sources=['Karki et al. 2015, Methods and fig. 1B', 'Krah et al. 2015, Methods']),
 E(id='mouse-kc', name='KC', aka='LSL-KrasG12D with Pdx1-Cre or Ptf1a (p48)-Cre',
   line='Mutant Kras alone: acinar-to-ductal metaplasia, then PanIN of rising grade; cancer is late and uncommon.',
   glance=['Small duct-like tubes replacing acini (ADM)', 'New stroma and inflammatory cells round them', 'Tall, pale mucinous cells lining a duct (PanIN)', 'Normal acini still beside the lesion'],
   remember='Kras alone starts PanIN, but most KC mice stay cancer-free for months: the model of the preinvasive stages.',
   features={'architecture': 'ADM, atypical flat lesions and PanIN among normal tissue; many lesions do not fit one PanIN grade.', 'cells': 'ADM: acinar cells that have lost their granules. PanIN: tall columnar cells, basal nuclei; polarity lost in PanIN-3.', 'mucin': 'Abundant in PanIN; Alcian blue measures PanIN burden.', 'stroma': 'Inflamed early: at 8 weeks every Pdx1-Cre KC mouse had neutrophils or histiocytes.'},
   facts={'who': 'Endogenous KrasG12D switched on in pancreatic progenitors (Hingorani et al. 2003). Ptf1a-Cre keeps tumours to the pancreas; Pdx1-Cre also gives tumours elsewhere.', 'size': 'PanIN minimal at 1 month, the main finding at about 4 months, covering the human PanIN range.', 'outlook': 'A few progress on their own to invasive cancer; visible terminal cancer at about 10 months. Over 76% were cancer-free at 6 months in one series.', 'molecular': 'PTF1A is lost in mouse PanIN and, with rare exceptions, in human PanIN.'},
   mimics=[{'id': 'panin-low', 'tell': 'The human lesion; its grading was carried over to the mouse.'},
           {'id': 'adm', 'tell': 'In people ADM looks the same, but its meaning is unclear and it is common in injured glands.'},
           {'id': 'mouse-kpc', 'tell': 'Adding mutant Trp53 turns the same start into invasive, metastatic cancer within months.'}],
   sources=['Hingorani et al. 2003, abstract (Cancer Cell 4:437-50)', 'Hurwitz et al. 2023, fig. 1, 3', 'Krah et al. 2015, fig. 1, 7', 'Veite-Schmahl et al. 2017, Introduction', 'Urrutia et al. 2021, fig. 2B, 7A']),
 E(id='mouse-kpc', name='KPC', aka='LSL-KrasG12D; LSL-Trp53R172H; Pdx1-Cre',
   line='Mutant Kras with mutant Trp53: PanIN within weeks, then invasive, widely metastatic ductal carcinoma.',
   glance=TUM, remember='The standard model of metastatic pancreatic cancer: gland-forming tumours in dense stroma, with unstable chromosomes.',
   features={'architecture': 'Normal tissue, PanIN and carcinoma side by side in one pancreas; invasive glands in desmoplastic stroma.', 'nuclei': 'Atypical; tumours carry many chromosomal translocations without obvious telomere erosion.'},
   facts={'who': 'Described by Hingorani et al. 2005; some groups use Ptf1a-Cre and keep the name.', 'size': 'PanIN appear after 6 weeks.', 'outlook': 'Median survival about 187 days in one series; metastases to liver, diaphragm and bowel.', 'molecular': 'The other main tumour-suppressor pathways were unmutated, taken to mean separate genetic routes to carcinoma.'},
   mimics=[{'id': 'pda-moderate', 'tell': 'The human tumour it was built to reproduce.'},
           {'id': 'mouse-kpt', 'tell': 'KPT uses a different Trp53 mutation (R270H) and switches on in adult acinar cells, so it is slower.'},
           {'id': 'mouse-kpflox', 'tell': 'There one Trp53 copy is deleted rather than point-mutated.'}],
   sources=['Hingorani et al. 2005, abstract (Cancer Cell 7:469-83)', 'Nikolaou et al. 2024, fig. 1-4', 'Cheng et al. 2025, fig. 1']),
 E(id='mouse-kpt', name='KPT', aka='Ptf1a-CreER; LSL-KrasG12D; LSL-Trp53R270H, tamoxifen-induced',
   line='Kras and Trp53 switched on in adult acinar cells: ADM and PanIN by 3 months, then fibrotic carcinoma.',
   glance=TUM, remember='An adult-onset KPC: same sequence, slower, and shown to start in acinar cells.',
   features={'architecture': 'Infiltrating glands, well to poorly formed, invading pancreas, fat and duodenum.', 'mitoses': 'Many.', 'stroma': 'Strongly desmoplastic; hyaluronan and activated stellate cells sit beside ADM.'},
   facts={'who': 'Tamoxifen at 4-5 weeks; the paper writes the Trp53 allele as R270H.', 'size': 'ADM and PanIN by 3 months; mucin-positive area rises month by month.', 'outlook': 'Median survival 219 days after tamoxifen; liver metastases in 3 of 8, lung in 1 of 8.'},
   mimics=[{'id': 'mouse-kpc', 'tell': 'Classic KPC carries Trp53 R172H and switches on in the embryo.'},
           {'id': 'liver-metastasis', 'tell': 'The human counterpart of the last picture.'}],
   sources=['Johnson et al. 2019, fig. 2, 3, 5']),
 E(id='mouse-kpflox', name='Kras with one Trp53 copy deleted', aka='Pdx1-Cre; LSL-KrasG12D; Trp53 flox/wt',
   line='Mutant Kras with loss of one Trp53 copy: PanIN among normal tissue at 3 months, then carcinoma.',
   glance=TUM, remember='Deleting Trp53 is not the same as mutating it: check whether a paper’s "KPC" carries R172H, R270H or a floxed allele.',
   features={'architecture': 'Open, irregular glands with secretions; the paper calls the tumours moderately differentiated.', 'stroma': 'Desmoplastic.'},
   facts={'size': 'PanIN among normal tissue at 3 months.', 'outlook': 'Median age at death or sacrifice 159 days.'},
   mimics=[{'id': 'mouse-kpc', 'tell': 'KPC carries a point-mutant Trp53 (R172H), not a deleted copy.'}],
   sources=['Germino et al. 2018, fig. 1-3']),
 E(id='mouse-kpic', name='KPIC', aka='LSL-KrasG12D; LSL-Trp53R172H/+; Ink4a flox/+; Ptf1a (p48)-Cre',
   line='KPC with one Ink4a copy also removed: hard tumours by 7 weeks, stroma-rich and locally invasive.',
   glance=TUM[:2], remember='Faster than KPC and locally invasive, but without liver metastases in the series described.',
   features={'architecture': 'Ductal carcinoma: tumour cells as ducts in dense stroma; of 5 mice, 3 had carcinoma and 2 high-grade PanIN.', 'stroma': 'Rich, with few small vessels, like human tumours.'},
   facts={'size': 'Palpable hard masses from about 7 weeks.', 'outlook': 'Mean survival 89 days; invasion of intestine and kidney; no liver metastases seen.'},
   mimics=[{'id': 'mouse-kic', 'tell': 'KIC has no Trp53 mutation but loses both Ink4a copies, and is faster.'},
           {'id': 'mouse-kpc', 'tell': 'KPC keeps both Ink4a copies and metastasises to the liver.'}],
   sources=['Ma and Saiyin 2017, fig. 1']),
 E(id='mouse-kic', name='KIC', aka='Ptf1a (p48)-Cre; LSL-KrasG12D; Ink4a flox/flox',
   line='Mutant Kras with both Ink4a copies removed: the fastest of these models, tumours well differentiated and stroma-rich.',
   glance=TUM[:2], remember='No Trp53 change at all: losing Ink4a is enough to turn Kras-driven lesions into carcinoma within two months.',
   features={'architecture': 'Well-differentiated carcinoma: tumour cells as ducts in dense stroma.'},
   facts={'outlook': 'Mean survival 62 days.'},
   mimics=[{'id': 'mouse-kpic', 'tell': 'KPIC adds mutant Trp53 and keeps one Ink4a copy; it lives about a month longer.'}],
   sources=['Ma and Saiyin 2017, fig. 1']),
 E(id='mouse-kdc', name='KDC', aka='KrasG12D with Smad4 (Dpc4) loss; also written KSC',
   line='Mutant Kras with Smad4 loss gives cystic mucinous tumours instead of PanIN, and slower, less metastatic cancer.',
   glance=['Large cystic spaces, not small ducts', 'A mucinous lining, mucin-rich (Muc5AC)', 'Slow growth; little spread'],
   remember='A different route: Kras with Smad4 loss makes cystic (MCN/IPMN-like) lesions, not the PanIN sequence of KC.',
   features={'architecture': 'Mostly macroscopic cystic lesions; Izeradjene 2007 calls them mucinous cystic neoplasm (MCN), Hurwitz 2023 calls the cystic, Muc5AC-rich lesions IPMN-like.', 'mucin': 'Abundant; Alcian blue and Muc5AC positive.'},
   facts={'who': 'Pdx1-Cre; LSL-KrasG12D with Smad4 flox (Hurwitz "KSC"); Izeradjene 2007 used Smad4/Dpc4 haploinsufficiency.', 'outlook': 'Slower than KC and KPC; 90% of Hurwitz KSC mice had no cancer or death to about 4 months, and no metastases were seen even in terminal cancer.', 'molecular': 'In Izeradjene 2007, progression came with loss of the second Dpc4 copy and mutation of p53 or p16.'},
   mimics=[{'id': 'mcn', 'tell': 'The human cystic tumour; whether these mice model MCN or IPMN is itself debated (Izeradjene vs Hurwitz).'},
           {'id': 'mouse-kc', 'tell': 'KC takes the PanIN route; swapping Trp53 loss for Smad4 loss changes the lesion to a cyst.'}],
   sources=['Izeradjene et al. 2007, abstract (Cancer Cell 11:229-43)', 'Hurwitz et al. 2023, Introduction and fig. 4']),
]

def I(file, caption, credit, page, mag='H&E', licence='CC BY 4.0', marks=None):
    d = dict(file='mouse/' + file, caption=caption, credit=credit, licence=licence, page=page, mag=mag)
    if marks: d['marks'] = marks
    return d

DOI = 'https://doi.org/'
ADD = {
 'mouse-control': [
   I('mouse-normal/dicerhet_3wk_g1A.png', 'Pancreas at 3 weeks: acini (A), an islet (I) and a duct (D), labelled in the source figure. A Dicer-heterozygous control.', MORR + ', fig. 1A', DOI + '10.1371/journal.pone.0095486'),
   I('mouse-normal/ptf1a_krasG12D_fig1A_acinar.png', 'Normal acinar tissue at high power: basal nuclei, pink granules at the tips (letter from the source figure).', KRAH + ', fig. 1A', DOI + '10.7554/eLife.07125', mag='H&E, high power')],
 'mouse-caerulein': [
   I('mouse-caerulein/mist1creert_ap1d_he.png', 'One day after caerulein: oedematous stroma with inflammatory cells beside a congested vessel. Soft image.', KARKI + ', fig. 1B', DOI + '10.1371/journal.pone.0145724'),
   I('mouse-caerulein/mist1creert_ap6h_he.png', 'Six hours after caerulein: swollen acini with opened lumina and vacuoles. Soft image.', KARKI + ', fig. 1B', DOI + '10.1371/journal.pone.0145724')],
 'mouse-kc': [
   I('mouse-adm/kc_ehmt2wt_F2B.png', 'Pdx1-Cre; LSL-KrasG12D: small tubes replacing acini (ADM) and ducts lined by pale mucinous cells, beside normal acini.', URR + ', fig. 2B', DOI + '10.3389/fcell.2021.681153', licence='CC BY'),
   I('mouse-panin-low/ptf1a_krasG12D_fig1B_panin.png', 'A duct lined by tall columnar cells with pale mucin and basal nuclei (PanIN). The paper gives no grade. Letter from the source figure.', KRAH + ', fig. 1B', DOI + '10.7554/eLife.07125', mag='H&E, high power'),
   I('mouse-panin-low/mmpca_11mo_B3.png', 'At 11 months in a Ptf1a-Cre KC mouse: dilated, branching ducts lined by tall mucinous cells. Number tag from the source atlas.', VEITE + ', fig. 4B', DOI + '10.1371/journal.pone.0187552')],
 'mouse-kpc': [
   I('kpc/kpc_panin_borderline.png', 'KPC PanIN: a duct lined by one layer of columnar cells in fibrous stroma. Small image (366 px); scale bar from the source figure.', CHENG + ', fig. 1a', DOI + '10.1038/s41586-025-08917-z'),
   I('kpc/kpc_pdac_borderline.png', 'KPC carcinoma: irregular small glands and single cells in desmoplastic stroma. Small image (366 px).', CHENG + ', fig. 1a', DOI + '10.1038/s41586-025-08917-z')],
 'mouse-kpt': [
   I('mouse-adm/kpt_B.png', 'Three months after induction (KPT): ADM (black arrows) and a PanIN (red arrow) in inflamed stroma; arrows from the source figure.', JOHN + ', fig. 3B', DOI + '10.1371/journal.pone.0221810', mag='H&E, x20'),
   I('mouse-pda/kpt_pdac_g2C.png', 'KPT carcinoma: back-to-back glands of columnar cells in dense fibrous stroma.', JOHN + ', fig. 2C', DOI + '10.1371/journal.pone.0221810', mag='H&E, x20'),
   I('mouse-met/kpt_liver_met_g2D.png', 'KPT liver metastasis: tumour glands with their stroma inside the liver; pink liver cells at the edges.', JOHN + ', fig. 2D', DOI + '10.1371/journal.pone.0221810', mag='H&E, x20')],
 'mouse-kpflox': [
   I('mouse-panin-low/ksr1wt_3mo_g2.png', 'At 3 months: a small focus of PanIN among normal acini. Pdx1-Cre; LSL-KrasG12D; Trp53 flox/wt.', GERM + ', fig. 2', DOI + '10.1371/journal.pone.0194998'),
   I('mouse-pda/ksr1wt_tumor_g3_hi.png', 'Carcinoma: irregular open glands with secretions, called moderately differentiated by the paper.', GERM + ', fig. 3', DOI + '10.1371/journal.pone.0194998')],
 'mouse-kpic': [
   I('mouse-pda/kpic_he.png', 'KPIC carcinoma: small, poorly formed glands and single cells in desmoplastic stroma.', MA + ', fig. 1C', DOI + '10.1371/journal.pone.0176844')],
 'mouse-kic': [
   I('mouse-pda/kic_he.png', 'KIC carcinoma: well-formed glands in dense desmoplastic stroma.', MA + ', fig. 1C', DOI + '10.1371/journal.pone.0176844')],
}
