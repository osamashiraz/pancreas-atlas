# Backlog

## Open issues
1. Some nuclei in cut acinar cells render as rings rather than solid dots (cause not found; cut-face shading works for cells and islet nuclei).
2. The 4 mm piece in Cell types colours was not visually checked (same code path as the acinus, which was).
3. Narration offers Google UK English Female (default) and Male, which exist only in Chrome; other browsers fall back to standard UK narrators (Microsoft Sonia/Libby/Ryan, Apple Daniel/Serena/Kate). Audio was never testable in headless runs.
4. Islet | Acinus split preset: in software rendering, the islet half was still in flight when checked; Beta cell | Acinar cell was confirmed.
5. Organ slices: cut faces are filled by shading back faces (a capping trick), not by true section geometry; seen edge-on the fill can look flat.
6. Verify Gray's Anatomy 42nd ed. (vessel anatomy). The Japan Pancreas Society stations were checked against the eighth edition (2024); the model still divides 13 and 17 into a/b (earlier editions) and does not split 14 by tumour side.
7. Report the HRA crosswalk error (male superior mesenteric vein mapped to UBERON:0001182, the artery).

8. Layers opened in place: turning the view far from the line going in while deep in the opening looks into the wall of the lobule column; names behind that wall are hidden. Around 2 mm from the site the duct tree near the line can crowd the view (the large interlobular duct may pass close to it).

9. Marker data (`repo/data/human-pancreas-markers.json`) was extracted by one-off scripts (provenance, URLs and checksums are in the file); add a builder script to reproduce it from the pinned ASCT+B file and the HPA release.
10. HPA lumps human islet endocrine cells; beta and alpha HPA lists come from bulk-derived cell-type enrichment intersected with the islet list and are noisy. Delta granule size: Brereton 2015 (read in full) gives 250 nm, smaller than alpha and beta granules, as drawn. Primary sources for delta-cell process length (Grube & Bohn 1983; Baskin 1984) not checked.
11. Secretion in motion is not yet shown at the islet level (hormones into the islet capillaries) or as glucose-dependent switching between insulin and glucagon.

12. Books checked (literature/, kept out of git): none of Beger 4th ed., Gorelick & Williams 2021 or Golson 2024 gives cell-level sizes (acinar cell, nucleus, acinus, duct radii, capillary, lobule, septum), so these stay not yet sourced. They differ from the model on organ length (14–23/25 cm against the HRA organ's ~15 cm), islet composition by region (beta 75–80% in the dorsal part; PP 54–94% of islet volume in the uncinate), islet cell size (9–10 µm against 11 µm), and main duct lumen (1–2.5 mm on EUS). Beger Fig 2.7 names the dorsal, great, inferior and transverse pancreatic arteries and the pancreaticoduodenal arcades (vessel names now checkable; caudal not found); Beger ch. 135 Table 135.2 has the Japan Pancreas Society classification (to verify the lymph node stations). Page references: docs/book-notes/
13. Precursor views: PanIN location sources disagree (Beger ch. 126 head > tail; ch. 119 table head = tail); IPMN multifocality 10–20% (Robbins) vs 20–40% (Beger ch. 81); MCN size by chapter (median 3.5–5 cm; mean 6.5 cm; range 2–35 cm). Marker positions on the micrographs were placed by eye; worth a pathologist's check. A normal intralobular duct micrograph (e.g. Berkshire Community College CC0 series) could be added beside PanIN.

14. Organs round the pancreas: male model only (the female united model is a 76 MB 7z archive not yet fetched); the neighbours file is not yet registered in the module's loader or tests. The HRA v2.0 model has no stomach or adrenals.
15. Pancreatitis and PDA: placement and sizes on the organ are simulated; the PDA head/body/tail split comes from Robbins (9th ed.), whose survival figure (under 5%) is older than Beger's (about 10%). An open-licensed H&E of chronic pancreatitis was later found (Chekmareva 2025, CC BY) and is now shown.

16. Atlas and pages:
    - Atlas and histology-view pins were placed by eye (IPMN pins 3, 6, 7 corrected 2026-11-16); worth a pathologist's check.
    - Mouse-model images: the original KC/KPC/KDC paper figures are copyright, so images come from later CC BY papers using the same models; the one real KPC image (Trp53 R172H, Nature 2025, CC BY) is small (366 px) and flagged, and KDC has no open image yet.
    - The duct + islet + vessel "triad" the user asked about is only partly supported by the sources (no source uses the word "triad"); it is rendered instead as the accurate sourced note that islets lie alongside ducts and are richly vascularised (insulo-acinar portal system). Revisit if a primary source names a formal triad.
    - The PDA "spread" view orders metastatic sites (liver → peritoneum, lung, nodes) without per-organ percentages; add sourced frequencies only if an open dataset supports them.

## Next steps (agreed or proposed)
- **Glossary** (proposed 2026-11-16, awaiting the user's go-ahead): a Glossary page of about 40 plain-language terms (cells and tissue, secretion, histology words, lesions, genes, microenvironment, mouse models), opened from a button beside the theme switch, with terms underlined on first use per page; plus "How to read the figure" keys like the KRAS one for the desmoplasia and progression figures only.
- **Lesion figures**: the user will supply figures to replace the removed histology cartoons in the lesion views.
- Open items from the 2026-11-15 review: one figure manifest and one numbers table with a source test; per-tab tests with the smoke test served over http; figure folder renames and older figures light-default; content gaps (WHO 2019 terms, chronic pancreatitis vs PDA pitfall box, IPMN risk features).
- The TypeScript module and its 23 tests were removed (2026-11-16). Port the tissue-rule checks to a small Python test (one intercalated duct per acinus, no overlapping acini or acini in the islet, reach, packing above 45%, capillary reach, islet composition, manifest checksums) so the rules stay enforced.
- Disease states still to add: type 1 diabetes (beta-cell loss, insulitis), type 2 (islet amyloid, reduced beta cells).
- Overlay user data (single-cell, spatial, CODEX) onto cell types.
- Nerves (coeliac plexus, splanchnic, vagal, intrapancreatic ganglia) — needs more of the HRA body model.
- Superior pancreaticoduodenal veins, minor papilla.
- Measured human sizes to replace not-yet-sourced values (stereology literature, electron microscopy full texts).
- Measuring ruler; image and video export.
