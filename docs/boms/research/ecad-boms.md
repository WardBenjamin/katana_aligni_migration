# ECAD BOMs (KiCad schematics)

Read 2026-11-13 (UTC). `repos/tripwire-ecad` at `81160fe` (HEAD = main = origin/main, 2026-09-23T00:09Z, merge of PR #26). Paths below are relative to that repo and read at `81160fe` unless another sha is given.

Method: `scratchpad/2026-11-13-bom-reconciliation/ecad_bom.py` parses each `.kicad_sch` (stdlib S-expression parser, no kicad-cli). Outputs in `scratchpad/2026-11-13-bom-reconciliation/data/ecad/`: one `<project>.csv` per project, `manifest.csv`, `committed_bom_diff.csv`, `history/`.

Rules used: power symbols (`#PWR`, `#FLG`, `power:`) skipped; a line is a BOM line if `(in_bom yes)` or `(dnp yes)`; DNP lines stay in with `DNP`, `InBOM`, `OnBoard` columns. Multi-unit symbols count once. Rows grouped by every field except Reference, Datasheet, Description and `Sim.*` (those are joined when they differ). Self-check: summed Quantity equals the symbol count, per project. `pcb_check` in the manifest compares populated on-board symbols with the `.kicad_pcb` footprints (ref, value, footprint, MPN).

## All projects

- No project has hierarchical sheets: zero `(sheet ...)` nodes in all 7 `.kicad_sch` files, and every `.kicad_pro` lists only the root sheet. The sheet-following code path is therefore unexercised.
- No `Manufacturer`, `Mfr`, `LCSC` or `Supplier` field exists anywhere. Supplier fields are `Digikey PN` (party-hat, bollard), `DPN` (bridges, sensor-bar), `ALT DPN` / `ALT MPN` (party-hat J7 only). Party HAT, sensor-bar and bridge MPNs embed the manufacturer name (`Stackpole RMCF0603FT1K00`); bollard MPNs don't (`RC0603FR-072KL`).
- Every DNP symbol is also `(in_bom no)`, so KiCad's own BOM export would omit them.

## party-hat

`party-hat/party-hat.kicad_sch`: title "Party HAT", rev X5C, date 2026-03-11. Last commit `a29dcde` 2026-08-04T16:32Z "[HW-422] Party HAT X5C ..." (also tag `party-hat-x5c`). 37 rows, 82 populated, 0 rows without MPN, PCB check ok.

- DNP: C14, R18, MH3 (off board), C26 (on board, in_bom no).
- Excluded by `(in_bom no)`: TP1 to TP20, MH1, MH2, MH4, FID1 to FID3, NT1.
- C11, C12, C16 (22u, MPN `Samsung CL21A226MAYNNNE`) carry Digikey PN `1276-1135-2-ND`, the same as C10 (68p, `Samsung CL10C680JB8NNNC`). One of the two Digikey PNs is wrong.
- J7: footprint `USB_A_CUI_UJ2-ADH-TH`, MPN `GCT USB1035-GF-P-0-B-B`, ALT MPN `CUI/Same Sky UJ2-ADH-W1-TH`.
- `party-hat.kicad_pro` BOM settings group by Value, Footprint, DNP, MPN and exclude in_bom-no symbols.
- Unmerged branch `origin/monti/hw-892-...` (tip `a6baf8a`, 2026-10-27T16:32Z) carries the same `party-hat.kicad_sch` blob as HEAD; the symbol list is identical.

## sensor-bar-io-breakout

`sensor-bar-io-breakout/sensor-bar-io-breakout.kicad_sch`: "Sensor Bar I/O Breakout", rev X2, 2025-05-27. Last commit `a2ec96b` 2025-05-31T01:15Z "[AG-6048] Party HAT X3 & Sensor Bar I/O Breakout X2 (#18)" (tag `sensor-bar-io-breakout-x2`). 9 rows, 9 populated, PCB check ok.

- Missing MPN: J1 (6P6C, `RJ12_Amphenol_54601-x06` footprint; Party HAT uses `Amphenol FCI 87180-066LF` on the same footprint).
- DNP (in_bom no, off board): D4, D7, D8, R1, R2. D4 is Value `SMAJ12A`, footprint `D_SMA`, but MPN `Littelfuse SMF24A` (an SOD-123F part).
- Excluded: H1, H2 (mounting holes).

## bollard-interposer-board

`bollard-interposer-board/bollard-interposer-board.kicad_sch`: no title block (no title, rev or date); the `.kicad_pcb` has none either. Last schematic commit `ebf6f09` 2026-09-22T22:40Z "Adds protection circuitry, ESD protection, and eFuse to prevent overcurrent"; last PCB commit `62482fe` 2026-09-22T23:24Z "HW-892: ...". Board name from commits: "Bollard Interposer Board X1" (`d96924f` 2026-08-17T17:54Z, tag `bib-x1`). 14 rows, 16 populated.

- Missing MPN: C1 (Value `C`, a placeholder), J4 (Value `RJHSE3085`, no MPN).
- PCB check: MH1 to MH4 are PCB-only footprints with no schematic symbol.
- Unmerged branch commit `a9e4165` (2026-10-27T16:31Z, "Adds updated boards as produced and built for X4B") changes only `.kicad_pcb` and `.kicad_pro`; its PCB matches the HEAD schematic BOM (same MH1 to MH4 note).
- Deleted export: `bollard-interposer-board/bollard-interposer-board_BOM.xlsx`, added `beebfee` (2026-08-04T15:56Z), deleted `85de51c` (2026-08-04T19:52Z, "Remove garbage commit ..."). Extracted to `data/ecad/history/bollard-interposer-board_BOM@beebfee.csv`. It is an early design BOM (J2 `M12A-17PMMP-SF8001`, J3 `MHRJJ66NFV`, J4 `Amphenol 54602-908LF`, R1, D1 `Kingbright APT1608SURCK`, MH1 to MH4; total 9) and predates the protection circuitry; J4 and D1 differ from the current schematic.

## party-hat-usb-bridges, hat-usb-bridge, modem-bridge

- `party-hat-usb-bridges/party-hat-usb-bridges.kicad_sch`: "Compute Stack USB Bridges", rev X1, 2025-07-18; last commit `2656aaf` 2025-11-02T01:51Z "[AG-5914, HW-20] Party HAT X4, Modem Bridge X1, and USB-A (HAT) Bridge X1 (#19)". Its `.kicad_pcb` holds both boards (P1 to P3, J2 and P5, P6) with Amphenol GSB316441CEU USB-A plugs. 6 populated; 14 DNP (C1 to C6, R1 to R6, J1, P7; in_bom no, off board).
- `party-hat-usb-bridges/hat-usb-bridge.kicad_sch`: "Compute Stack USB-A Bridge", rev X2, 2025-10-29; last commit `389171e` 2025-11-06T16:10Z "[HW-184] USB-A (HAT) Bridge X2 ...". Its PCB was last changed in `267ed2a` 2025-12-20T01:51Z "[HW-279] DFM changes: Party HAT X5B, USB Bridge X3, Modem Bridge X2 (#23)" while the schematic and PCB title blocks still say X2. 4 populated (P1 to P3 `Xiamen Jinbelli (JBL-EC) USB-3.0AM-01-D` with DPN `N/A`; J2 without MPN); 8 DNP (C1 to C4, R1 to R4).
- `modem-bridge` has no schematic of its own: `modem-bridge.kicad_sch` exists in no commit on any branch (`git log --all --name-only`). `modem-bridge.kicad_pro` shares the root sheet uuid `394e69b8-...` with the other two projects, and the footprints in `modem-bridge.kicad_pcb` (P5, P6) link to symbol uuids that exist only in `party-hat-usb-bridges.kicad_sch`. The BOM is that schematic filtered to the PCB's symbols: P5 `USB_B_Micro` and P6 `USB_C_Plug_USB2.0`, both without MPN. Board name from commits: "Modem Bridge X2" (`267ed2a`). Neither the PCB nor the shared schematic has a Modem Bridge title block.
- PCB checks ok for all three; PCB footprint fields match the schematic.

## tripwire-v3 (sensor-board rev1)

`sensor-board/rev1/src/tripwire-v3.kicad_sch`: no title block. Last commit `da598aa` 2023-11-20T17:19Z (moved into `rev1/`). 4 rows, 8 populated (H1 to H4 mounting holes are in_bom yes), no MPN fields at all.

- The committed `sensor-board/rev1/outputs/tripwire-BOM.csv` is a PCBWay quotation (product T-1Y8W623647A) from `7ccb6ac` 2023-10-13T06:25Z, updated `7cee3c1` 2023-10-13T06:36Z.
- D1 (LED, Digi-key LSM0805543V) is in the CSV and in the schematic at `7ccb6ac` (`sensor-board/src/tripwire-v3.kicad_sch@7ccb6ac`), but not in the HEAD schematic: it was removed in `1776ee4` 2023-11-01T00:22Z "add next rev" (merged `f3613b6`). The HEAD rev1 schematic and PCB are that later revision, not the board that was ordered.
- J1 footprint: CSV `PhoenixContact_SPT_1.5_4-H-3.5_1x04_P3.5mm_Horizontal`, schematic `footprints:PHOENIX_1984989` (custom footprint added in `8e4e1e8`, after the order). Same part, 1984989.
- Part numbers only in the CSV: R1, R3 `RT0805BRD071KL`; R2 `RT0805BRD073KL`; J1 `1984989`.
- H1 to H4 only in the schematic.

## combined-sensor-board (sensor-board rev2 / rev2.1)

`sensor-board/rev2/src/combined-sensor-board.kicad_sch`: no title block. Last commit `346ed29` 2025-03-04T20:19Z "Remove duplicate files; ...; recover rev2 schematic (#11)"; rev2.1 was added in `d3c46c9` 2023-12-12T02:00Z. 5 rows, 14 populated, no MPN fields.

- Committed `sensor-board/rev2/outputs/tripwire-rev2-bom.csv` (`d3c46c9`) matches the schematic on designators, values and footprints, except H1 to H4 (schematic only). Its Id column starts at 2, so a first line was probably removed by hand.
- Part numbers only in the CSV: R1, R3, R4, R6 `RT0805BRD071KL`; R2, R5 `RT0805BRD073KL`; J1 to J3 Phoenix 1984976; J4 Phoenix 1984989.

## Other committed or deleted exports

- Only BOM-like files ever committed (all branches): the two sensor-board CSVs above, `sensor-board/outputs/tripwire-BOM.csv` (renamed to `rev1/outputs/` in `5b6f21f`), and the deleted bollard xlsx. No BOM files inside any committed `.zip` backup (checked every added zip's file list).
- Not BOMs but list parts: `.pos` centroid files in `sensor-board/rev*/outputs/`, and netlists `sensor-board/rev2/output/combined-sensor-board.net` and `sensor-board/rev2/combined-sensor-board/output/combined-sensor-board.net` (deleted in `346ed29`).
- Not on main: `compute-stack-bollard-interface/` exists only on `origin/monti/hw-975-compute-stack-bollard-interface-1` (`792c0cd` 2026-10-24T03:26Z, `88d20a6` 2026-10-27T21:37Z). Not extracted; a quick parse of its schematic at `88d20a6` gave 9 rows, 12 populated, 1 without MPN, no title block.
