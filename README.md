# Pancreas: Organ to Disease

*An open learning atlas of H&E, mechanisms and 3D anatomy, from the normal gland to PDA*

**[Open the learning tool →](https://osamashiraz.github.io/pancreas-atlas/)** (runs in the browser; Chrome or Edge recommended)

[![Watch a one-minute tour of the tool](docs/images/video-poster.jpg)](https://osamashiraz.github.io/pancreas-atlas/video/pancreas-atlas-showcase.mp4)

A free, open learning tool that walks from the normal human pancreas, its exocrine and endocrine parts, to its diseases: pancreatitis, the precursor lesions of pancreatic cancer, and pancreatic ductal adenocarcinoma (PDA). Every step is shown three ways: an interactive illustrated figure of the mechanism, real H&E micrographs of what it looks like under the microscope, and an interactive 3D model that zooms from the whole organ down to single cells.

## A note on terms

Pancreatic ductal adenocarcinoma is written several ways in the literature: **PDAC** (the most common abbreviation), **PDA**, "pancreatic adenocarcinoma", "ductal adenocarcinoma of the pancreas" and, loosely, "pancreatic cancer". All mean the same tumour, the ductal-type adenocarcinoma that makes up most pancreatic cancers. This repository uses **PDA** throughout.

## How it relates to other resources

This is not a reference work. For depth, use the comprehensive resources, for example:

- [PathologyOutlines.com](https://www.pathologyoutlines.com/pancreas.html), for the full surgical pathology of the pancreas: every entity, its criteria, its differential diagnosis, its stains and the WHO terms;
- [Pancreatlas](https://pancreatlas.org) (Vanderbilt), for large collections of high-resolution human pancreas and islet images.

This tool is for quick, simple learning. It links the normal histology, biology and cell biology of the pancreas to its main diseases on one page each, so you can get oriented before going deeper.

## Why I built this

I am a bioinformatician working on spatial profiling of pancreatic cancer. To read these data well, I needed to understand the biology behind them: the molecular and cancer biology, and the histology and pathology of the pancreas and its diseases. I made this resource for others in the same position: students, trainees and computational biologists new to the pancreas. I am still learning myself, so corrections and suggestions are very welcome (see [Feedback, collaboration and contributions](#feedback-collaboration-and-contributions)).

**That understanding starts with H&E.** Haematoxylin and eosin were first combined in 1876. About 150 years later, H&E is still the standard stain in medicine. Pathologists use it to see what a disease looks like, to diagnose it, and to grade and stage tumours, which informs prognosis.

I gathered what I learned from papers, textbooks and open resources. But I could not find one open resource that linked the normal pancreas, with its exocrine and endocrine functions, to the diseases of each part in a single overview. So I built one as a learning tool, using Claude Code and agentic pipelines. I picked up these skills recently in my Agentic AI course at The Johns Hopkins University. I wanted to apply them to something worth learning from.

Understanding the biology and pathology of the pancreas has directly improved my own data analyses. Seeing histology beside spatial data is how I connect the two. In the clinic, diagnosis, grading and staging still rest on H&E. Spatial transcriptomics may one day add to that. Putting them side by side shows me where H&E is already enough (recognising tissue, lesions, grade and invasion) and where spatial data may add more: cell states and neighbourhoods that look alike on H&E. If you are new to the pancreas, start with the [suggested route](#a-suggested-route) below.

## What is inside

Watch the [video](https://osamashiraz.github.io/pancreas-atlas/video/pancreas-atlas-showcase.mp4) for a tour. The bar at the top left switches pages; the button at the top right switches between light and dark themes.

- **Atlas**: 51 entries with 79 openly licensed H&E images, from the normal gland to PDA and its look-alikes, with pins, side by side comparison, a features table and a quiz.
- **Pancreas**: the organ, its exocrine tissue and islets, how it secretes, and each cell's job beside its H&E.
- **Pancreatitis**: how the gland injures itself, from acute to chronic, with real H&E.
- **PDA precursors**: the PanIN to PDA progression model, its genetic changes, KRAS, and PanIN vs IPMN vs MCN.
- **PDA**: desmoplasia, grades and variants, and where PDA spreads.
- **Interactive 3D model** (button on the Pancreas page): zoom from the whole organ to one cell, at true scale, in H&E or cell-type colours, with a 16-step narrated journey.

Each page and the 3D model are described in full in [`docs/GUIDE.md`](docs/GUIDE.md).

### A suggested route

1. **Pancreas**: the organ, then exocrine tissue and islets, then each cell's job beside its H&E.
2. **Atlas → Normal pancreas**: learn the normal patterns with the pins on.
3. **Pancreatitis**, then **PDA precursors**, then **PDA**, following the disease from injury to invasion.
4. Back to the **Atlas** for look-alikes (side by side) and the **quiz** to test yourself.
5. The **3D model** and its journey, whenever you want to see how the scales fit together.

In every figure, hover over or tap a part to see its name and a short sourced explanation. **Sources & notes** under each figure open the full references.

### Tips

- Any view can be linked: the address follows what you see, e.g. [`#atlas=pda-poor`](https://osamashiraz.github.io/pancreas-atlas/#atlas=pda-poor) or [`#site=9&view=islet&stain=if`](https://osamashiraz.github.io/pancreas-atlas/#site=9&view=islet&stain=if).
- In the 3D model, **Esc** steps back a level, the **Stain** switch toggles H&E and cell-type colours, and the **seek bar** under the journey jumps to any step.
- Click any cell or structure to name it, isolate it or fade it. **Marker genes** link to the Human Protein Atlas.

## What is real, what is drawn, and limits

Every structure in the 3D model has one of three labels, and the viewer shows it:

- **source**: drawn by the Human Reference Atlas from the Visible Human Project (organ shape, main ducts, large vessels);
- **traced**: followed from a published image;
- **simulated**: placed by a written rule from published measurements (small vessels, lymph nodes, lobules, acini, islets, cells).

Every number either names its source or is marked *not yet sourced* in the data; those still awaiting a source are listed in [`docs/SPEC.md`](docs/SPEC.md) §9. The organ comes from one male and one female reference body; everything below the organ scale is simulated from published descriptions. The illustrated figures are simplified drawings of mechanisms, not to scale. The micrographs are examples chosen to show a feature, not a measure of how common it is. Known issues are in [`docs/BACKLOG.md`](docs/BACKLOG.md).

## Main sources

- **Organ, ducts, large vessels and nearby organs**: HRA 3D Reference Object Library v2.0 (HuBMAP), from the Visible Human Project (U.S. National Library of Medicine); CC BY 4.0.
- **Cell types, ontology terms and markers**: HRA ASCT+B pancreas table v1.3 and crosswalk; Human Protein Atlas v26.0 (CC BY 4.0).
- **Tissue and islet measurements**: Hahn et al. 2021, Wang et al. 2013, Cabrera et al. 2006, Kiemen et al. (CODA) 2022, and others.
- **Disease**: Beger et al., *The Pancreas*, 4th ed., 2023; *Robbins and Cotran*, 9th ed., 2015; Hingorani 2007; Rodriguez et al. 2007.
- **Images**: openly licensed micrographs, mostly from Wikimedia Commons, each credited on the page.
- **Teaching text**: StatPearls (CC BY 4.0), Columbia and Basel histology notes, Human Protein Atlas, paraphrased in my own words.

The full table with what each source is used for is in [`docs/GUIDE.md`](docs/GUIDE.md#datasets-and-sources-in-full); references with DOIs are in [`docs/SOURCES.md`](docs/SOURCES.md).

## How it is built

- **Organ**: meshes extracted unchanged from the HRA united body models. Small arteries (gastroduodenal, pancreaticoduodenal arcades, dorsal/great/caudal pancreatic) are routed by shortest path around drawn structures. Lymph nodes are placed at the Japan Pancreas Society stations, checked against its eighth edition (2024). Gray's Anatomy, cited for vessel anatomy, is still to be checked.
- **Tissue**: deterministic Python builders grow a duct tree, bud acini on their own intercalated ducts, route capillaries so every acinus is within reach, and add stroma and one islet. Cells then grow until they meet a neighbour. The builders hold to these rules: no overlapping acini, one duct per acinus, packing above 45%, islet composition and size.
- **Figures**: interactive isometric SVG figures built with the anima figure kit. Each has its own source script and a sources block, and an automatic layout audit checks every figure.
- **Viewer**: a single self-contained HTML page (three.js) with the models embedded, so it can be hosted anywhere static. In the layered openings, each opening grows with the zoom to nearly half the height of the view, outer layers stay as rings, and vessels and ducts of the organ are left uncut.

## Repository layout

| Path                               | What                                                                                                                                                                                                                     |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `dist/pancreas-organ-to-cell.html` | The built viewer (published to GitHub Pages)                                                                                                                                                                             |
| `dist/atlas/`                      | The atlas images, loaded by the page only when the atlas is opened                                                                                                                                                       |
| `dist/figures/`                    | The interactive illustrated figures, embedded in the pages                                                                                                                                                               |
| `viewer/`                          | Viewer sources (`template.html`, `src/app.js`, `src/atlas.json`, `src/figure-embed.html`), images (`assets/`), build script, tests (`test/smoke.py`, `test/atlas_check.py`, `test/profile.py`), earlier versions in `legacy/` |
| `repo/`                            | Model data and the Python builders                                                                                                                  |
| `docs/`                            | Specification, backlog, change history, sources, the full guide, README images                                                                                                                                                           |

### Run it locally

Open `dist/pancreas-organ-to-cell.html` in a browser (it needs internet for three.js and fonts). To rebuild it, run from the repository folder:

```bash
python3 viewer/build_viewer.py repo dist/pancreas-organ-to-cell.html   # writes the page; dist/atlas and dist/figures are copied beside it
python3 viewer/test/atlas_check.py                                       # checks the atlas sources, credits and licences
```

Python builders need `numpy` and `scipy`; the smoke test needs `playwright`. Pushing a new `dist/` to `main` republishes the GitHub Pages site.

## Feedback, collaboration and contributions

This work is evolving. Corrections, suggestions and contributions are very welcome: better or openly licensed images, errors in the biology, new topics (for example diabetes, or overlays of spatial data), or ideas for teaching with it. If you would like to contribute or collaborate, email me at **osamashirazshah@gmail.com**, or open an issue on this repository.

## Disclaimer

- **For education and research only. Not for medical use.** It is not a diagnostic tool, it gives no medical advice, and it is no substitute for a pathology textbook, a pathologist or a clinician.
- **It reflects my understanding** from what I have read and learned. I have tried to source and check every statement, but errors are possible. Please tell me if you find one.
- **Images are limited to open licences** (CC BY, CC BY-SA, CC0, public domain), each credited. Some entries therefore have small images, images with the source figure's arrows, or no image yet. Textbook and journal figures under copyright are not reproduced.

## Licence and credit

- Code: MIT (see [`LICENSE`](LICENSE)).
- Model data derived from the HRA 3D Reference Object Library: CC BY 4.0 (see [`repo/public/atlas-human/NOTICE.md`](repo/public/atlas-human/NOTICE.md)). Cite: Börner K, et al. *Nat Methods* 2025;22:845–860. doi:10.1038/s41592-024-02563-5.
- Visible Human Project, U.S. National Library of Medicine.
- Narration and page text are in my own words, paraphrased from open sources (StatPearls CC BY 4.0, university histology notes, Human Protein Atlas) with credit.
