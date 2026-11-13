# vπ full assembly price

As of 2026-11-13 (UTC). Status: partial. Plan and method: [plan.md](plan.md).

Configuration: compute stack kit, RR sensor bar kit, enclosure base and top, dual camera kit (4 mm + 6 mm, round bollard mount), install pack RR bollard mount dual camera, Uline H-2118F bollard. One of each.

Scope (Ben, 2026-11-13): parts, ByTechs labour and packaging. Not freight to site, install labour, cellular data or tooling.

## Where it stands

**$1,918.73 is priced. This is not yet the assembly price**: every ByTechs-made part, most labour and all packaging are missing.

| Basis | Rows | $ |
|---|---|---|
| Purchase at production quantity, inside six months | 48 | 662.24 |
| Small-lot purchase inside six months | 3 | 140.77 |
| List prices dated 2026-11-13 (reflectors, bollard) | 2 | 204.44 |
| Stale purchases and proforma invoices (older than six months) | 22 | 771.95 |
| Stale ByTechs labour | 3 | 51.95 |
| Estimated import duty on the two cameras (entered about 2026-04-17) | 2 | 87.38 |
| **Priced** | **80** | **1,918.73** |
| Unpriced part rows | 52 | |
| Unpriced labour rows | 12 | |

$1,007.45 rests on prices inside six months and $911.28 on older ones. 73 of 124 leaf parts are priced.

By configuration line:

| Line | Current | Stale | Unpriced rows |
|---|---|---|---|
| `AG-CS3-Kit` | 711.88 | 39.47 | 35 |
| `AG-SEN2-RR-Kit` | 116.59 | 321.14 | 13 |
| `AG-Dual46-RoundBollard-Kit` | 0.00 | 346.96 | 11 |
| `AG-IP-RRBM-DC-Kit` | 78.98 | 78.93 | 5 |
| Enclosure base and top | 0.00 | 124.78 | 0 |
| `EXT-H-2118F` bollard | 100.00 | 0.00 | 0 |

Largest rows:

| Part | Qty | Extended | Basis | Dated |
|---|---|---|---|---|
| Raspberry Pi 5 16GB | 1 | 385.00 | MakerBright invoice 1381, 150 units | 2026-11-06 |
| Omron E3Z-R61 | 2 | 256.77 | stale purchase, 200 units | 2026-01-16 |
| ELP camera, 4 mm (KV100IR) | 1 | 127.12 | stale proforma invoice, 50 units | 2026-01-27 |
| ELP camera, 6 mm (KL60IR) | 1 | 127.12 | stale proforma invoice, 400 units | 2026-01-27 |
| Import duty on the two cameras | 2 | 87.38 | stale estimate, 35% plus processing fee | 2026-04-17 |
| Samsung PRO Endurance 256GB | 1 | 114.36 | small-lot purchase, 2 units | 2026-06-21 |
| Omron E39-R1S | 4 | 104.44 | Digi-Key list price, chosen by Ben | 2026-11-13 |
| Uline H-2118F bollard | 1 | 100.00 | list price, no freight or tax | 2026-11-13 |
| Sensor enclosure top (V5, orange) | 1 | 87.70 | stale purchase, 150 units | 2026-04-23 |
| IPEX junction box | 1 | 68.04 | stale purchase, 150 units | 2026-04-08 |
| Sequent Watchdog HAT | 1 | 45.20 | purchase, 50 units | 2026-06-22 |
| Sixfab base HAT | 1 | 45.20 | purchase, 84 units | 2026-06-11 |
| Sensor enclosure base (V5) | 1 | 37.08 | stale purchase, 150 units | 2026-04-23 |
| I425-GL modem | 1 | 35.00 | purchase, 100 units | 2026-11-06 |
| Titen HD anchor | 12 | 27.66 | purchase, 20 packs of 25 | 2026-07-16 |
| Sensor bar assembly (labour) | 1 | 27.00 | stale Deel task line, 10 units | 2025-12-14 |
| Modem bridge bare PCB | 1 | 21.36 | small-lot purchase, 5 units | 2026-10-08 |
| Bollard washer | 12 | 20.73 | purchase, 500 units | 2026-07-16 |

The camera price includes its 5 m USB cable, so the two cable rows are priced at $0.00. With the estimated duty, one camera lands at about $170.81. The Raspberry Pi cooler is $6.50 on the same MakerBright invoice.

Every row, with its source: `scratchpad/2026-11-13-vpi-assembly-price/out/rr-bollard-dual46_price_lines.csv`. Rebuild: `uv run --python 3.15 price_config.py configs/rr-bollard-dual46.csv --as-of 2026-11-13`.

## Still unpriced

- **ByTechs-made parts**, 24: printed and cut parts for the compute stack (7), camera module (5), bollard mount (3), sensor bar (5) and reflector cover (1); two cable assemblies; ferrules.
- **Labour** for 12 assemblies: compute stack, camera module, bollard mount, reflector, USB and modem bridge PCBAs, the three kits, the install pack and its two sets.
- **Packaging.** In no BOM. Uline boxes were $3.06 to $5.71 landed each on 2026-06-22.
- **20 Digi-Key parts with no visible purchase**: mostly resistors, capacitors, LEDs and diodes on the PCBAs, plus the Samtec header, the USB 3.0 plugs and one standoff.
- **Others**: four `EXT-TBD` PCB connectors, the padlocks (3), the trash bag and McMaster 92095A210.
- **Bollard freight and tax.** The $100.00 is list price only.

The ByTechs archive does not fill the ByTechs gaps: its last five invoices say only "See invoice" ([research/invoices.md](research/invoices.md)).

## Stale lines that need a quote or a confirmation under the six-month rule

- E3Z-R61 sensors, $256.77: invoice paid 2026-01-16. The order acknowledgement Ben supplied shows the same $128.20 unit price from 2025-10-14 ([research/powermatic-ordack.md](research/powermatic-ordack.md)).
- ELP cameras, $254.25, and their estimated duty, $87.38: proforma invoice dated 2026-01-27, entered the US about 2026-04-17.
- Sensor enclosure top and base, $124.78: Haig invoice 98534 dated 2026-04-23, three weeks past the six-month line.
- Junction box, $68.04; the two Misumi bars, $25.30; compression connectors, $10.89; P30B batteries, $9.27; and smaller lines.
- All ByTechs labour figures: the newest is from 2025-12.

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
- ByTechs and JLCPCB invoices: [research/invoices.md](research/invoices.md).
- Powermatic order acknowledgement: [research/powermatic-ordack.md](research/powermatic-ordack.md).
- ELP, Haig and MakerBright documents: [research/elp-haig-makerbright.md](research/elp-haig-makerbright.md).
- Sensor enclosure: [research/haig-enclosure.md](research/haig-enclosure.md).
- Camera import duty: [research/camera-tariffs.md](research/camera-tariffs.md), [research/camera-tariffs-review.md](research/camera-tariffs-review.md).
- E39-R1S at $26.11 (https://www.digikey.com/en/products/detail/omron-automation-and-safety/E39-R1S/761204) was given by Ben on 2026-11-13 as the most recent source; the page was not opened.
