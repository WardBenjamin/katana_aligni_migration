# vπ full assembly price: plan

As of 2026-11-13 (UTC). Status: proposed, not started. The facts behind this plan are in [research/first-pass.md](research/first-pass.md).

## Goal

The current cost to AirGarage of one complete vπ unit, per configuration, with every line traceable to a purchase, an invoice or a dated quote.

First configuration (`scratchpad/2026-11-13-vpi-assembly-price/configs/rr-bollard-dual46.csv`):

| Line | Part number | Qty |
|---|---|---|
| Compute stack kit | `AG-CS3-Kit` | 1 |
| Retroreflective sensor bar kit | `AG-SEN2-RR-Kit` | 1 |
| Sensor enclosure base and top (V5) | `AG-SEN2-003-001_EnclosureBase`, `AG-SEN2-003-002_EnclosureTop` | 1 each |
| 36 in Uline bollard | Uline H-2118F, not in `boms/items.csv` yet | 1 |
| Dual camera kit | `AG-Dual46-RoundBollard-Kit` (assumed, decision 3) | 1 |
| Install pack | `AG-IP-RRBM-DC-Kit` | 1 |

"Price" is taken to mean our landed cost to buy, build and kit one unit (decision 1).

## What the first pass shows

The configuration explodes to 124 leaf parts. Only 29 match a Ramp purchase line by part number, and those are mostly low-value electronics and fasteners. Most of the money sits in a dozen lines:

| Part | Qty | Latest purchase found | Each | Note |
|---|---|---|---|---|
| Omron E3Z-R61 sensor | 2 | Powermatic, 2026-01-16 | $128.39 landed | |
| Omron E39-R1S reflector | 4 | Powermatic, 2026-01-16 | $20.97 landed | |
| Raspberry Pi 5 16GB | 1 | Amazon, 2025-07-28, 5 units | $132.00, $138.94 landed | 15 months old |
| Samsung PRO Endurance 256GB | 1 | Amazon, 2026-06-21, 2 units | $105.89, $114.36 landed | $29.99 in 2025-07; two Samsung direct orders ($5.9k) have no receipt |
| Sequent Watchdog HAT | 1 | Sequent, 2026-06-22, 50 units | $45.00, $45.20 landed | |
| Sixfab base HAT | 1 | Sixfab, 2026-06-11, 84 units | $45.00, $45.20 landed | |
| I425-GL modem | 1 | Eagle Wireless, 2026-11-06, 100 units | $35.00 | |
| IPEX junction box | 1 | Gordon Electric, 2026-04-08 | $68.04 landed | |
| 12 V power supply | 1 | Digi-Key, 2026-10-28 | $15.09 landed | |
| Bollard washer | 12 | SendCutSend, 2026-07-16, 500 units | $1.59, $1.73 landed | |
| Uline bollard, 36 in | 1 | None. Only 42 in and 60 in bollards were bought | | A page cached in 2025-04 listed H-2118F at $95. Freight and tax added 23% to 46% on the bollards we did buy |
| ELP cameras and USB cables | 2 + 2 | None found | | |
| Enclosure base and top | 1 + 1 | None. No Haig Precision record in the pull | | |
| ByTechs assembly, printed parts, cables | 24 parts plus labour | 2025-06 to 2025-08 only | Party HAT assembly $17.19, breakout $7.76 | Nothing later is in the pull |

These are unreviewed matches from a script, not prices to quote.

Other findings that shape the work:

- **Pack sizes.** McMaster, Fasteners Plus and some Amazon lines are priced per pack. The anchors are $53 to $80 per pack of 25 or 100. Every match needs units per pack before it gives a cost per each.
- **Costs missing from the BOMs.** No BOM carries assembly labour, kitting or packaging. Uline boxes cost $3 to $6 landed each.
- **Printed parts.** The print plates in `tripwire-mcad` are unsliced project files, so they hold no filament weight or print time.
- **Open BOM lines.** Seven `EXT-TBD` placeholders are in this configuration: the 15 ft RJ-12 cable, two anchor lines and four PCB connectors. The BOM says "Tapcon LDT 5/8 x 3in"; the purchases are 1/2 x 3 in Titen HD anchors.
- **Shopify not checked.** The connector returned an error, so I don't know if Shopify holds a price or unit cost for these SKUs.

## Method

Each leaf part is priced by one of five routes, then rolled up.

1. **Bought, purchase found.** Latest purchase at the quantity we normally buy, landed, converted to cost per each.
2. **Bought, no purchase found or stale.** Find the purchase (no-receipt records, another buyer, vendor order history). Failing that, a dated quote or list price.
3. **Custom fabricated** (enclosure, washers, bare PCBs). Supplier invoice per piece.
4. **3D printed.** Filament grams times filament price, plus any print charge; or ByTechs' piece price if they bill one.
5. **Labour and kitting.** ByTechs invoice or quote per assembly: PCB assembly, stack, camera and sensor bar assembly, kit packing.

Rule for "most current": take the latest purchase at production quantity, landed (tax, freight and tariffs spread pro rata, as the cost record already does). If it is older than six months, or we only bought ones and twos, replace it with a dated quote. Every line records its basis (purchase, invoice, quote or estimate), date and source.

## Steps

1. **Lock the configuration.** Apply decisions 2 and 3 and add the bollard to `boms/items.csv`. Done when the config file has no assumed lines.
2. **Fill the seven open BOM lines** this configuration uses, with ByTechs. Done when no `EXT-TBD` part is left in the leaf list.
3. **Build the match table.** `matches.csv`: part, cost line, units per pack, note. A script proposes candidates by part number, then by vendor and name; I review each one; you spot-check the 15 highest-value lines. Done when every bought part has a match or is listed as "no purchase found".
4. **Close the gaps outside the Ramp pull** (needs decisions 5 and 6):
   - ByTechs invoices since 2025-08.
   - Haig Precision invoices or a quote for the enclosure base and top.
   - ELP camera and cable purchases.
   - Receipts for the Samsung direct orders.
   - Uline's current H-2118F price and freight to a typical site.
   - Fresh quotes for stale lines: Raspberry Pi 5 16GB, batteries.
5. **Price the printed parts.** Get grams and print hours per part by slicing the plates in `tripwire-mcad`, or take ByTechs' figures; price filament from the Polymaker purchases.
6. **Price the four PCBAs** (Party HAT, USB bridge, modem bridge, sensor breakout): parts from the match table, the bare PCB from its JLCPCB order, and the assembly fee.
7. **Roll up by script.** Leaf to sub-assembly to configuration line to total. Output per line: cost, basis, date, source. Report the total, the share that rests on quotes or estimates, and a low-to-high range where a line is an estimate.
8. **Verify.**
   - Check each purchase-based line in the top 80% of cost against its receipt or invoice.
   - Have a separate agent re-derive the roll-up from the raw files.
   - Compare with any per-unit figure you or finance already use.
9. **Write up and reuse.** Final doc `price.md`; write `Cost Per Unit` into `boms/items.csv` for the Katana import; add config files for through-beam, wall mount, single camera and 6 mm + 8 mm.

Steps 1 to 3 and a partial roll-up with gaps marked can start on the data already here. Steps 4 to 6 wait on decisions 5 and 6.

## Open decisions

1. **What "price" covers.** I assumed parts, ByTechs labour and packaging. Left out unless you say otherwise: freight to the site, install labour, cellular data, tooling and one-off engineering. Is that the number you want, or a sell or transfer price?
2. **Bollard.** Notion lists Uline H-2118F (4.5 x 36 in, fixed, round) and that matches "36 in", but Ramp shows only 42 in and 60 in bollards bought. Is H-2118F right, and does AirGarage buy it or does the site?
3. **Camera.** I assumed 4 mm + 6 mm lenses on the round bollard mount. Correct?
4. **Cost basis.** Latest production-quantity purchase, landed, with a quote when older than six months. This also answers decision 3 in [../bom-costs/plan.md](../bom-costs/plan.md).
5. **ByTechs and Haig invoices.** They are not in Ben's, Monti's or Chris's Ramp spend after 2025-08. Where are they paid from, and may I read them?
6. **Browser access.** May I use Chrome with your signed-in sessions to read Ramp receipt images and vendor order histories, limited to this configuration's parts? Same question as decision 1 in the bom-costs plan.

## Relation to the bom-costs plan

This is step 9 of [../bom-costs/plan.md](../bom-costs/plan.md) narrowed to one configuration. Its steps 1 to 8 get done only where they touch these 124 parts.
