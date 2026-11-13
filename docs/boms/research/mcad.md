# MCAD repo

`repos/tripwire-mcad` at 033bdfb (2026-10-23T16:53Z, "Adds the coupler interlock mechanisms sent out for prototyping to TripleB"). Read from git objects; the working-tree checkout is incomplete (disk full during clone). File list: `scratchpad/2026-11-13-bom-reconciliation/data/mcad/files_at_HEAD.txt` (114 STEP, 3MF, DXF and PDF files).

## Findings

- No BOM files (CSV, XLSX) anywhere in the tree. Releases: `V3.1-release/`, `vπ-release/`, `V4-release/{X1,X2,X3B,X5 Release}`, `Installer Kits/`.
- `vπ-release/README.md` lists CAD files per assembly with "[Add description]" placeholders, no part numbers.
- Documentation PDFs are Notion exports: `vπ-release/compute-stack/Documentation/vπ Compute Stack 2a2dcb3d06b28056be62fa9b1aa03f2d.pdf` (Notion page id in the name), sensor bar and bollard dual camera packages.
- vπ STEP names map to Aligni fabricated parts by name, with gaps:
  - Compute stack: `Antenna Wing Left Arm`, `V3` and `V4` variants of the left arm, right arm and mount all present; Aligni has one `AG-CS3-001-003_WingBase`, `-004_WingLeft`, `-005_WingRight` at rev A, so which CAD version is in production isn't recorded.
  - Wall mount: CAD has `Camera Yaw Pitch Mount (2)` and `(3)`; no Aligni part with that name in `AG-PIC-005-000`.
  - Sensor bar: CAD has `Tuning Fork Mount` and two rain-cover variants (`Mounting Holes`, `Round & Flat`); Aligni has `RollMnt` and the Round & Flat cover only.
  - Sensor enclosure: CAD has base, front hood and rear hood (V5); Aligni has base and "ENCLOSURE ASSY V5" top, bought from Haig Precision.
- V4 / Obelisk (X1 to X5) and V3.1 have CAD here and no parts in Aligni.
- 2026-11-13T04:30Z: after disk space was freed, `git -C repos/tripwire-mcad status` reports a clean working tree at 033bdfb; the checkout is complete.
