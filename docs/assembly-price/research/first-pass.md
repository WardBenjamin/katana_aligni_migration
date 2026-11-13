# First pass: what the data on hand can price

Written 2026-11-13T14:40Z. Inputs: `boms/` at commit `07b3beb`, `scratchpad/2026-11-13-bom-costs/out/cost_lines_20250101.csv` at commit `c1bbad6`, `repos/tripwire-mcad` at `033bdfb`. Scripts and result files are in `scratchpad/2026-11-13-vpi-assembly-price/`.

## Configuration to BOMs

- The requested lines map to these Katana-scope BOMs in `boms/index.csv`: `AG-CS3-Kit`, `AG-SEN2-RR-Kit`, `AG-SEN2-003-000` (base and top), `AG-Dual46-RoundBollard-Kit` or `AG-Dual68-RoundBollard-Kit`, `AG-IP-RRBM-DC-Kit` (base set `AG-IP-001-000` plus add-on `AG-IP-002-000`).
- Shopify sells the same lines as separate products, including the enclosure top and base as two SKUs (`docs/boms/research/shopify.md`; `scratchpad/2026-11-13-bom-reconciliation/data/shopify/variants_20261113T0400Z.csv`).
- No Uline bollard is in `boms/items.csv`. The Notion PIC-003 and PIC-004 BoMs list it at quantity 0: H-2118F round, H-8264 square, cost $100 (`docs/boms/research/notion-boms.md`, PIC-003 paragraph).
- Uline's page for H-2118F is "Standard Safety Bollard - 4.5 x 36", Fixed". A web search summary of a page cached in 2025-04 gave $95 each, $90 for four or more. Not read from the live page. https://uline.com/Product/Detail/H-2118F/Safety-Guards-Barriers/Standard-Safety-Bollard-45-x-36-Fixed
- Lens pair (4 mm + 6 mm or 6 mm + 8 mm) and mount shape were not stated in the request. The config file assumes 4 mm + 6 mm, round.

## Explosion

Query: `uv run --python 3.15 explode_config.py configs/rr-bollard-dual46.csv`. Result: `out/rr-bollard-dual46_leaf_parts.csv`.

- 124 leaf parts. The one no-load line (EG25-G modem, alternate to I425-GL) is skipped.
- Seven are `EXT-TBD` placeholders: RJ12-15FT, TAPCON-025X125-SS, TAPCON-LDT-0625X3, hat-usb-bridge-J2, modem-bridge-P5, modem-bridge-P6, sensor-bar-io-breakout-J1.
- By listed supplier: DigiKey 44, ByTechs 24, Amazon 9, none listed 8, McMaster 8, JLCPCB 3, ELP 3, Mouser 3, Home Depot 3, Haig 2, Gordon Electric 2, MakerBright 2, Fasteners Plus 2, and one each for eleven others.
- The 24 ByTechs parts are printed or cut plastic parts, two cable assemblies and ferrules. None has a cost in `boms/items.csv`.
- `boms/items.csv` has a cost on 33 of 277 items; 8 of them are leaf parts here (E3Z-R61, the 270 mm Misumi bar, P30B battery, five sensor-bar fasteners), and their sources are Aligni or Notion, undated.

## Ramp coverage by part number

Same query and result file. A part counts as matched when its manufacturer part number, supplier part number or internal number (prefix removed) appears in a costed line's part-number or name text. Unreviewed.

- 29 of 124 leaf parts match. By listed supplier: DigiKey 17 of 44 (one is E39-R1S, bought from Powermatic), McMaster 6 of 8, Gordon Electric 2 of 2, Misumi 1 of 1, Powermatic 1 of 1, Mouser 1 of 3, none listed 1 of 8 (the 455 mm Misumi bar).
- For 10 of the 29 the latest line is on a record flagged `needs_review` (all dated 2026-10-12, Digi-Key).
- McMaster "landed unit cost" is per pack: $8.14 to $19.92 for screws and nuts used 1 to 8 per unit.

## Purchases found by name

Query: `uv run --python 3.15 probe_names.py`. Result: `out/name_probe_lines.csv`. Vendor and item-name patterns are in the script. Unreviewed.

- Uline bollards, 13 lines, none 36 in: 4.5 x 60 in (H-6290F) at $140 to $145, 2026-06-09 to 2026-08-14; 4.5 x 42 in at $115, 2026-01-23; square 4.5 x 42 in at $115 to $120, 2025-05 to 2025-08; heavy duty 5.5 and 6.5 x 42 in at $130 and $160. Landed cost is 22.8% to 45.5% above the unit price (for example 10 units at $115 landed $141.17; 1 unit at $145 landed $208.97).
- Bollard washer: SendCutSend 316 stainless 1.496 x 1.496 in, 500 at $1.59 (landed $1.73) on 2026-07-16 and 500 at $1.56 on 2026-06-05. The 2026 item names start "Uline_Bollard_Drill_Jig"; the 2025-09-18 line with the same size is named "Bollard_Washer.step".
- Raspberry Pi 5 16GB: Amazon 5 at $132.00 (landed $138.94) on 2025-07-28; MakerBright 40 at $120.00 on 2025-04-22. Nothing later.
- Sequent Watchdog HAT: 50 at $45.00 (landed $45.20) on 2026-06-22; 61 at $45.00 on 2026-01-28.
- Sixfab base HAT: 84 at $45.00 (landed $45.20) on 2026-06-11; 110 on 2026-04-02; 50 on 2026-02-27.
- I425-GL modem: Eagle Wireless 100 at $35.00 on 2026-11-06; 150 and 100 and 50 at $35.00 in 2026-09 (typed from invoices).
- Samsung PRO Endurance 256GB, 16 lines: $29.99 in 2025-07; $55.45 for 29 on 2025-10-25; $81.99 for 1 on 2026-03-30; $105.89 for 2 (landed $114.36) on 2026-06-21. The 2025-11-17 lines (100 and 43 units at $27.58) are flagged and their landed costs are wrong. Samsung Electronics America has two records with no receipt, $5.9k (`docs/bom-costs/plan.md`, step 2 table).
- Molicel P30B: 20 at $3.90 (landed $4.63) on 2025-09-17. One line.
- Concrete anchors, Fasteners Plus, 8 lines: Tapcon 1/4 x 1-1/4 in 410 stainless, pack of 100, $73.60 to $79.99; Strong-Tie Titen HD 1/2 x 3 in, pack of 25, $53.35 to $57.99. No 5/8 x 3 in Tapcon LDT line.
- JLCPCB bare boards: 9 costed lines, for example 50 at $1.55 (landed $3.22) on 2026-04-30. Which board each order is for is not on the line.
- Uline boxes: 14 x 14 x 14 in at $1.72 (landed $3.06), 24 x 14 x 10 in at $3.07 (landed $5.46), 24 x 14 x 12 in at $3.21 (landed $5.71), all 2026-06-22.
- ByTechs, 9 lines, 2025-06-04 to 2025-08-13 only: PCB assembly Party Hat VX2B 50 at $17.19; Sensor Bar IO Breakout 80 at $7.76; cable harness 50 at $3.50; packaging design 10 at $100.00; shipping; 3% card fee. Three records have no lines.
- ELP camera: 0 lines. Haig Precision: 0 lines, and no vendor of that name in `out/cost_records_20250101.csv`.

## Other sources checked

- ByTechs labour quotes exist in Notion ("Quantity: 5 units ... $24/unit"), on the Contract Manufacturing page; not pulled (`docs/boms/research/notion-boms.md`, "Hardware Stock tables" bullet).
- Print plates: 13 `.3mf` files in `repos/tripwire-mcad`, 11 under `vπ-release/`. `Metadata/slice_info.config` in "Round Bollard Dual Cam Plate (ASA - 0.4mm).3mf" has only a header (205 bytes): no filament weight or print time.
- Shopify price and unit cost for the six variants: not checked. The Shopify connector returned HTTP 500 on two read queries at about 2026-11-13T14:35Z.
- The Ramp pull covers spend by Ben, Monti and Chris only (`scratchpad/2026-11-13-bom-costs/README.md`), so invoices paid by anyone else are not in it.
