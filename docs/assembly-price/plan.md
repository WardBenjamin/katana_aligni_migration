# vπ full assembly price: plan

As of 2026-11-13 (UTC). Status: in progress. Steps 1 and 3 are done as a first pass and step 7's script exists. The current result is in [price.md](price.md): $1,918.73 priced, with ByTechs-made parts, most labour and packaging still missing. The facts behind the plan are in [research/first-pass.md](research/first-pass.md).

## Goal

The current cost to AirGarage of one complete vπ unit, per configuration, with every line traceable to a purchase, an invoice or a dated quote.

First configuration (`scratchpad/2026-11-13-vpi-assembly-price/configs/rr-bollard-dual46.csv`):

| Line | Part number | Qty |
|---|---|---|
| Compute stack kit | `AG-CS3-Kit` | 1 |
| Retroreflective sensor bar kit | `AG-SEN2-RR-Kit` | 1 |
| Sensor enclosure base and top (V5) | `AG-SEN2-003-001_EnclosureBase`, `AG-SEN2-003-002_EnclosureTop` | 1 each |
| 36 in Uline bollard | Uline H-2118F, not in `boms/items.csv` yet | 1 |
| Dual camera kit | `AG-Dual46-RoundBollard-Kit` | 1 |
| Install pack | `AG-IP-RRBM-DC-Kit` | 1 |

"Price" means our landed cost of parts, ByTechs labour and packaging for one unit.

## Decisions (Ben, 2026-11-13)

1. **Scope.** Parts, ByTechs labour and packaging. Not included: freight to the site, install labour, cellular data, tooling and one-off engineering.
2. **Bollard.** Uline H-2118F (4.5 x 36 in, fixed, round).
3. **Camera.** 4 mm + 6 mm lenses on the round bollard mount.
4. **Cost basis.** Latest production-quantity purchase, landed, replaced by a dated quote when it is older than six months. This also settles decision 3 in [../bom-costs/plan.md](../bom-costs/plan.md).
5. **Browser access.** Agreed in principle; on hold until Ben says go. No Chrome use before then.
6. **BOM corrections.** The M3 x 30 mm screw is McMaster 95893A198. The 3 in anchor is the Strong-Tie Titen HD 1/2 x 3 in (`EXT-THD50300H`). The wipes quantity is single wipes. All three are in `boms/`.
7. **Prices given.** Raspberry Pi 5 16GB is $385.00 (MakerBright invoice 1381). Omron E39-R1S is $26.11 each at Digi-Key; use it over Powermatic's $20.94 because it is the most recent source.

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

How the script reads that rule (my choices, change them if they are wrong):

- Production quantity is a purchase that covers at least 10 units.
- Six months is 183 days before the as-of date.
- A small purchase inside six months counts as the dated quote when the last production purchase is stale.
- A line on a record flagged for review uses the receipt's unit price, without tax or freight.

## Steps

1. **Lock the configuration.** Done 2026-11-13: the bollard is `EXT-H-2118F` in `boms/items.csv` and the config file has no assumed lines.
2. **Fill the seven open BOM lines** this configuration uses, with ByTechs. Done when no `EXT-TBD` part is left in the leaf list. The three BOM questions in [research/partial-rollup.md](research/partial-rollup.md) were answered by Ben on 2026-11-13 and one of the seven lines (the 3 in anchor) is now a real part, leaving six.
3. **Build the match table.** First pass done 2026-11-13 as `price_rules.csv`: part, vendor pattern, item pattern, units per pack, flag. Part-number matches are automatic; 31 name-based rules were each checked against their lines. Left to do: your spot-check of the highest-value lines, and the 20 Digi-Key parts with no visible purchase.
4. **Close the gaps outside the Ramp pull** (needs open decision 1 and the go-ahead for browser access):
   - ByTechs' own itemized invoices (open decision 1).
   - The enclosure base and top are priced from Haig invoice 98534 (2026-04-23).
   - ELP cameras are priced from a proforma invoice dated 2026-01-27, which is stale under the rule.
   - Receipts for the Samsung direct orders.
   - Freight and tax on the bollard. The list price is in: $100 on 2026-11-13.
   - Fresh quotes for stale lines: E3Z-R61 sensors (last bought 2026-01-16), junction box, batteries. Ben gave current prices for the Raspberry Pi and the E39-R1S.
   - The Samtec header invoice (18438338). The four bare PCBs are priced from JLCPCB invoices Ben supplied.
5. **Price the printed parts.** Get grams and print hours per part by slicing the plates in `tripwire-mcad`, or take ByTechs' figures; price filament from the Polymaker purchases.
6. **Price the four PCBAs** (Party HAT, USB bridge, modem bridge, sensor breakout): parts from the match table, the bare PCB from its JLCPCB order, and the assembly fee.
7. **Roll up by script.** Leaf to sub-assembly to configuration line to total. Output per line: cost, basis, date, source. Report the total, the share that rests on quotes or estimates, and a low-to-high range where a line is an estimate. `price_config.py` does this now for what can be priced; the range and the sub-assembly subtotals are not built.
8. **Verify.**
   - Check each purchase-based line in the top 80% of cost against its receipt or invoice.
   - Have a separate agent re-derive the roll-up from the raw files.
   - Compare with any per-unit figure you or finance already use.
9. **Write up and reuse.** Final doc `price.md`; write `Cost Per Unit` into `boms/items.csv` for the Katana import; add config files for through-beam, wall mount, single camera and 6 mm + 8 mm.

Steps 1 to 3 and a partial roll-up with gaps marked can start on the data already here. Steps 4 to 6 wait on open decision 1 and the browser go-ahead.

## Open decisions

1. **Itemized ByTechs invoices.** ByTechs is paid through Deel. The archive Ben supplied holds the Deel invoices, and the last five say only "See invoice" with a total ([research/invoices.md](research/invoices.md)). The labour, printed-part, cable and packaging prices are on ByTechs' own invoices, which Deel attaches. Those are needed, at least for 2026-06 to 2026-10.
2. **Stale lines.** The E3Z-R61 sensors were last bought 2026-01-16. Get a quote, or accept that price?

Ben supplied camera, wall-bracket and Raspberry Pi documents on 2026-11-13 ([research/elp-haig-makerbright.md](research/elp-haig-makerbright.md)) and is getting pricing for more of the missing items.
## Relation to the bom-costs plan

This is step 9 of [../bom-costs/plan.md](../bom-costs/plan.md) narrowed to one configuration. Its steps 1 to 8 get done only where they touch these 124 parts.
