# vπ full assembly price

As of 2026-11-13 (UTC). Status: nearly complete. Plan and method: [plan.md](plan.md).

Configuration: compute stack kit, RR sensor bar kit, enclosure base and top, dual camera kit (4 mm + 6 mm, round bollard mount), install pack RR bollard mount dual camera, Uline H-2118F bollard. One of each.

Scope (Ben, 2026-11-13): parts, ByTechs labour and packaging. Not freight to site, install labour, cellular data or tooling.

## Where it stands

**The total so far is $2,118.56.** Left out on purpose: filament, and the sensor bar printed parts (see "Flagged and left out"). Still missing: 28 low-value parts, most packaging materials, and freight on the bollard and enclosure.

| Configuration line | Priced |
|---|---|
| Compute stack kit `AG-CS3-Kit` | 850.53 |
| RR sensor bar kit `AG-SEN2-RR-Kit` | 453.38 |
| Dual camera kit `AG-Dual46-RoundBollard-Kit` | 406.96 |
| Install pack `AG-IP-RRBM-DC-Kit` | 172.91 |
| Enclosure base and top | 134.78 |
| Bollard `EXT-H-2118F` | 100.00 |
| **Total** | **2,118.56** |

| Kind of cost | $ |
|---|---|
| Parts | 1,784.74 |
| ByTechs labour (build, PCB assembly, packing) | 208.25 |
| Camera import duty, estimated | 87.38 |
| ByTechs printing, packing and box charges added per kit | 38.19 |

| Basis | Rows | $ |
|---|---|---|
| Purchases and ByTechs invoices inside six months | 61 | 1,041.26 |
| List prices and a quote dated 2026-11-13 | 3 | 204.66 |
| Purchases, invoices and the duty estimate older than six months | 26 | 872.64 |
| Carried at $0: covered by another line, or flagged and left out | 28 | 0.00 |
| Unpriced part rows | 29 | |

$1,245.92 rests on prices inside six months and $872.64 on older ones. Of 124 leaf parts, 74 have a price, 22 are carried at $0 and 28 are unpriced. All 15 labour rows are priced.

Largest rows:

| Part | Qty | Extended | Basis | Dated |
|---|---|---|---|---|
| Raspberry Pi 5 16GB | 1 | 385.00 | MakerBright invoice 1381, 150 units | 2026-11-06 |
| Omron E3Z-R61 | 2 | 256.77 | stale purchase, 200 units | 2026-01-16 |
| ELP camera, 4 mm (KV100IR) | 1 | 127.12 | stale proforma invoice, 50 units | 2026-01-27 |
| ELP camera, 6 mm (KL60IR) | 1 | 127.12 | stale proforma invoice, 400 units | 2026-01-27 |
| Samsung PRO Endurance 256GB | 1 | 114.36 | small-lot purchase, 2 units | 2026-06-21 |
| Omron E39-R1S | 4 | 104.44 | Digi-Key list price, chosen by Ben | 2026-11-13 |
| Uline H-2118F bollard | 1 | 100.00 | list price, no freight or tax | 2026-11-13 |
| Sensor enclosure top (V5, orange) | 1 | 87.70 | stale purchase, 150 units | 2026-04-23 |
| Import duty on the two cameras | 2 | 87.38 | stale estimate, 35% plus processing fee | 2026-04-17 |
| Compute stack build (ByTechs) | 1 | 75.00 | ByTechs invoice 1217, 41 units | 2026-09-30 |
| IPEX junction box | 1 | 68.04 | stale purchase, 150 units | 2026-04-08 |
| Sequent Watchdog HAT | 1 | 45.20 | purchase, 50 units | 2026-06-22 |
| Sixfab base HAT | 1 | 45.20 | purchase, 84 units | 2026-06-11 |
| Sensor enclosure base (V5) | 1 | 37.08 | stale purchase, 150 units | 2026-04-23 |
| Dual camera kit build (ByTechs) | 1 | 35.00 | ByTechs invoice 1217, 20 units | 2026-09-30 |
| I425-GL modem | 1 | 35.00 | purchase, 100 units | 2026-11-06 |

Every row, with its source: `scratchpad/2026-11-13-vpi-assembly-price/out/rr-bollard-dual46_price_lines.csv`. Rebuild: `uv run --python 3.15 price_config.py configs/rr-bollard-dual46.csv --as-of 2026-11-13`.

## ByTechs charges in the price

From ByTechs' itemized invoices ([research/bytechs-itemized-samtec.md](research/bytechs-itemized-samtec.md)):

| Charge | Per unit | Invoice, date | Attached to |
|---|---|---|---|
| Compute stack build | $75.00 | 1217, 2026-09-30 | `AG-CS3-001-000` |
| Party HAT X5C PCB assembly | $22.50 (27 h for 120 units) | 1199, 2026-06-02 | `AG-CS3-002-000_PartyHAT` |
| Modem bridge PCB assembly | $9.38 (2 h at $150 for 32 units) | 1217, 2026-09-30 | `AG-CS3-004-000_ModemBridge` |
| USB bridge PCB assembly | $4.37 (11 h for 252 units) | 1197, 2026-05-26 | `AG-CS3-003-000_USBBridge` |
| Sensor breakout PCB assembly | $5.00 (10 h for 200 units), stale | 1194, 2026-05-11 | `AG-SEN2-004-000_Breakout` |
| Retroreflective sensor bar build | $30.00 | 1217, 2026-09-30 | `AG-SEN2-RR-Kit` |
| Print rain cover and install reflectors | $6.00, two per kit | 1217, 2026-09-30 | `AG-SEN2-002-000` |
| Dual camera kit build, 6/4 mm | $35.00 | 1217, 2026-09-30 | `AG-Dual46-RoundBollard-Kit` |
| 3D printing, camera housings and parts | $25.00 | 1205, 2026-06-26 | `AG-Dual46-RoundBollard-Kit` |
| Installer kit packing | $15.00 | 1217, 2026-09-30 | `AG-IP-RRBM-DC-Kit` |
| Enclosure packing | $10.00 | 1217, 2026-09-30 | enclosure base |
| Sensor bar box, 3.5 x 3.5 x 20 in | $3.19, stale | 1174, 2026-02-18 | `AG-SEN2-RR-Kit` |

## Confirmed by Ben, 2026-11-13

- **Camera print charge.** $25.00 is correct. The roll-up applies it once per camera kit.
- **Print labour.** ByTechs' rates cover it. The seven printed compute stack parts, eight printed or cut camera kit parts and the rain cover are carried at $0.

## Flagged and left out

- **Filament.** AirGarage supplies it: Polymaker ASA. Left out of the price for now on Ben's instruction. The Ramp cost record has three Polymaker records, $3,585.60, from 2026-05-04 to 2026-10-30; grams per part are not known.
- **Sensor bar printed parts**, 5 (`AG-SEN2-001-003` to `-007`). ByTechs billed $30.60 a set for 100 sets on invoice 1169 (2026-01-18) and has billed no sensor bar printing since, though about 240 bars were built afterwards. Ben is not sure whether that is correct or a billing error. Carried at $0 and ignored for now. If the $30.60 still applies, the total rises by that amount.

## Assumptions still open

1. **Sub-assembly labour.** ByTechs bills one line per kit, so the sensor bar assembly, camera module, bollard mount, compute stack kit and the two install pack sets are carried at $0 under the kit's rate.
2. **4 mm camera.** The KV100IR ("V100 lens") is taken as the 4 mm camera.
3. **Samtec header freight.** The $8.95 between the acknowledgement ($298.20) and the Ramp charge of 2025-08-06 ($307.15) is taken as freight.

## Still unpriced

- **Two cable assemblies and the ferrules** made by ByTechs.
- **19 Digi-Key parts with no visible purchase**: resistors, capacitors, LEDs and diodes on the PCBAs, the JST XA header, the USB 3.0 plugs and one standoff. ByTechs billed $7,935.64 on 2026-01-21 as "Cost for Parts for 250x Compute Stack Vπ units" ($31.74 a stack) with no breakdown; some of these parts may be in it.
- **Four `EXT-TBD` PCB connectors**, the padlocks (3) and the trash bag.
- **Packaging materials** other than the sensor bar box: boxes for the compute stack, camera kit, enclosure and install pack. Uline boxes were $3.06 to $5.71 landed each on 2026-06-22.
- **Freight and tax on the bollard; freight on the enclosures.**

Not allocated to a unit: ByTechs' monthly rent ($250), ordering and inventory hours, troubleshooting of returned units, and Deel's $49 monthly fee.

## Stale lines that need a quote or a confirmation under the six-month rule

- E3Z-R61 sensors, $256.77: invoice paid 2026-01-16. The order acknowledgement Ben supplied shows the same $128.20 unit price from 2025-10-14 ([research/powermatic-ordack.md](research/powermatic-ordack.md)).
- ELP cameras, $254.25, and their estimated duty, $87.38: proforma invoice dated 2026-01-27, entered the US about 2026-04-17.
- Sensor enclosure top and base, $124.78: Haig invoice 98534 dated 2026-04-23, three weeks past the six-month line.
- Junction box, $68.04; the two Misumi bars, $25.30; compression connectors, $10.89; P30B batteries, $9.27; the Samtec header, $5.12 (2025-08); and smaller lines.

## Camera import duty

Estimate for the 600-camera order that entered the US about 2026-04-17 ([research/camera-tariffs.md](research/camera-tariffs.md), checked in [research/camera-tariffs-review.md](research/camera-tariffs-review.md)). No duty bill was found.

| Case | Rate on $74,160 | Order | Per camera |
|---|---|---|---|
| Low: classified as a digital still image video camera | 17.5% | $12,978 | $21.63 |
| Likely: Section 301 at 25% plus Section 122 at 10% | 35% | $25,956 | $43.26 |
| High: same rates with freight in the customs value | 35% | $26,689 | $44.48 |

The roll-up uses the likely case plus a $0.43 processing fee, $43.69 per camera. The UPS entry summary or duty invoice for that shipment would replace the estimate. Section 122 expired at the close of 2026-07-23, so the next order will face a different rate; that was not researched.

## Priced for other configurations

- Wall-mount camera bracket `AG-PIC-005-001_WallBracket`: $49.62 landed ($45.11 plus sales tax), 56 units, Haig invoice 98995 dated 2026-10-06. Not in this configuration.

## Sources

- First pass and coverage: [research/first-pass.md](research/first-pass.md).
- First roll-up, how a price is picked, BOM questions: [research/partial-rollup.md](research/partial-rollup.md).
- ByTechs (Deel) and JLCPCB invoices: [research/invoices.md](research/invoices.md).
- ByTechs itemized invoices and the Samtec acknowledgement: [research/bytechs-itemized-samtec.md](research/bytechs-itemized-samtec.md).
- Powermatic order acknowledgement: [research/powermatic-ordack.md](research/powermatic-ordack.md).
- ELP, Haig and MakerBright documents: [research/elp-haig-makerbright.md](research/elp-haig-makerbright.md).
- Sensor enclosure: [research/haig-enclosure.md](research/haig-enclosure.md).
- Camera import duty: [research/camera-tariffs.md](research/camera-tariffs.md), [research/camera-tariffs-review.md](research/camera-tariffs-review.md).
- E39-R1S at $26.11 (https://www.digikey.com/en/products/detail/omron-automation-and-safety/E39-R1S/761204) and McMaster 92095A210 at $10.91 per pack of 50 were given by Ben on 2026-11-13; neither page was opened.
