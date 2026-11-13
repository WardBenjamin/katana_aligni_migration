# Partial roll-up from the data on hand

Written 2026-11-13T15:15Z. Inputs: `boms/` with the bollard item added (this commit), `scratchpad/2026-11-13-bom-costs/out/cost_lines_20250101.csv` at commit `c1bbad6`. Files named below are in `scratchpad/2026-11-13-vpi-assembly-price/`. No browser was used.

Query: `uv run --python 3.15 price_config.py configs/rr-bollard-dual46.csv --as-of 2026-11-13`. Result: `out/rr-bollard-dual46_price_lines.csv` (142 rows: 127 part rows, 15 labour rows).

## How a price is picked

- Purchases are found by part number (Digi-Key packaging suffixes ignored) and by the reviewed patterns in `price_rules.csv` (31 rules, each checked against its matching lines).
- Pack sizes come from the rule, or from "Packs of N" in the item name.
- Production quantity: a purchase that covers at least 10 units of the configuration.
- Stale: dated before 2026-05-14, 183 days before the as-of date.
- Order of preference among prices inside six months: production purchase, then a price in `manual_prices.csv`, then a small-lot purchase. If nothing is inside six months, the same order among older prices, marked stale.
- A line on a record flagged `needs_review` uses the receipt's unit price instead of the landed cost, and says so in `Flag`.

## Result

| | Rows | $ |
|---|---|---|
| Current purchase (production quantity, inside six months) | 44 | 257.21 |
| Small-lot purchase inside six months | 2 | 119.41 |
| List price read 2026-11-13 (bollard) | 1 | 100.00 |
| Stale purchases and purchase record | 19 | 599.65 |
| Stale labour (ByTechs PCB assembly, 2025-06-04) | 2 | 24.95 |
| **Priced so far** | **68** | **1,101.22** |
| Unpriced part rows | 61 | |
| Unpriced labour rows | 13 | |

- $476.62 rests on prices inside six months; $624.60 on older ones.
- 64 of 124 leaf parts are priced. The ten largest rows are 81% of the priced amount.
- This is not the assembly price: cameras, the enclosure, every ByTechs-made part, most labour, the bare PCBs and packaging are missing.

Largest rows:

| Part | Qty | Each | Extended | Status | Dated |
|---|---|---|---|---|---|
| Omron E3Z-R61 | 2 | 128.39 | 256.77 | stale purchase, 200 units | 2026-01-16 |
| Raspberry Pi 5 16GB | 1 | 120.55 | 120.55 | stale purchase, 40 units | 2025-04-22 |
| Samsung PRO Endurance 256GB | 1 | 114.36 | 114.36 | small-lot purchase, 2 units | 2026-06-21 |
| Uline H-2118F bollard | 1 | 100.00 | 100.00 | list price, no freight or tax | 2026-11-13 |
| Omron E39-R1S | 4 | 20.97 | 83.88 | stale purchase, 200 units | 2026-01-16 |
| IPEX junction box | 1 | 68.04 | 68.04 | stale purchase, 150 units | 2026-04-08 |
| Sequent Watchdog HAT | 1 | 45.20 | 45.20 | purchase, 50 units | 2026-06-22 |
| Sixfab base HAT | 1 | 45.20 | 45.20 | purchase, 84 units | 2026-06-11 |
| I425-GL modem | 1 | 35.00 | 35.00 | purchase, 100 units | 2026-11-06 |
| Titen HD anchor | 12 | 2.30 | 27.66 | purchase, 20 packs of 25 | 2026-07-16 |
| Bollard washer | 12 | 1.73 | 20.73 | purchase, 500 units | 2026-07-16 |
| Party HAT PCB assembly (labour) | 1 | 17.19 | 17.19 | stale purchase, 50 units | 2025-06-04 |

## Unpriced

From `out/rr-bollard-dual46_price_lines.csv`, rows with status `none`:

- ByTechs-made parts, 24: printed and cut parts for the compute stack (7), camera module (5), bollard mount (3), sensor bar (5) and reflector cover (1); two cable assemblies; ferrules.
- ELP: the 4 mm and 6 mm cameras and two USB cables.
- Haig Precision: enclosure base and top.
- Bare PCBs, 4: Party HAT, USB bridge, modem bridge, sensor breakout.
- Digi-Key parts with no visible purchase, 20: resistors, capacitors, LEDs, diodes, the Samtec SSM-120 header (three Samtec records have no lines; the latest is invoice 18438338, 2026-10-20, memo "PARTYHAT X5C"), the JST XA header, three USB 3.0 A plugs, the 16 mm standoff.
- Four `EXT-TBD` PCB connectors.
- Master Lock padlock (3), 13 gal trash bag, McMaster 92095A210.
- Labour, 13 assemblies: compute stack, camera module, bollard mount, sensor bar, reflector, USB and modem bridge PCBAs, the three kits, the install pack and its two sets.
- Packaging is in no BOM, so it has no row at all.

## BOM questions the purchases raise

- **M3 x 30 mm thread-forming screw.** The BOMs list McMaster 95893A197. The purchases named "M3 Size, 30 mm Long, Packs of 25" are 95893A198 (2026-03-20, 2026-04-10). 95893A197 was never bought.
- **Concrete anchors.** `EXT-TBD-TAPCON-LDT-0625X3` is described as Tapcon LDT 5/8 x 3in. Fasteners Plus purchases are Strong-Tie Titen HD 1/2 x 3in, pack of 25. Priced as the Titen HD.
- **Wipes.** `EXT-GOJ902712` is "Alcohol Wipes (Purell, 120 ct)", quantity 2. The purchase is one display box of 120 for $21.06. Priced as 2 single wipes ($0.36); 2 boxes would be $42.92.
- **Amazon parts.** Receipts carry no ASIN, so eight Amazon parts are matched on item name. Each is flagged in the output.

## Bollard

Uline's page for H-2118F, fetched 2026-11-13 (page timestamp 11/13/2026 09:09:48 AM): $100 each, $95 at 4 or more, 22 lb, "SHIPS VIA UPS", in stock. https://www.uline.com/Product/Detail/H-2118F/Safety-Guards-Barriers/Standard-Safety-Bollard-45-x-36-Fixed

Freight and tax are not in the $100. No 36 in bollard was bought, so there is no landed figure; the larger bollards landed 22.8% to 45.5% above list ([first-pass.md](first-pass.md)).

## Not done

- Powermatic freight bills are not added to the sensor and reflector costs (`docs/bom-costs/plan.md`, step 6).
- No quote was sought for any stale line.
- The rules were reviewed by one reader (Claude). Ben has not spot-checked them.
