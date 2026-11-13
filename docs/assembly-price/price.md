# vπ full assembly price

As of 2026-11-13 (UTC). Status: partial. Plan and method: [plan.md](plan.md).

Configuration: compute stack kit, RR sensor bar kit, enclosure base and top, dual camera kit (4 mm + 6 mm, round bollard mount), install pack RR bollard mount dual camera, Uline H-2118F bollard. One of each.

Scope (Ben, 2026-11-13): parts, ByTechs labour and packaging. Not freight to site, install labour, cellular data or tooling.

## Where it stands

**$1,706.57 is priced. This is not yet the assembly price**: the enclosure, every ByTechs-made part, most labour and all packaging are missing.

| Basis | Rows | $ |
|---|---|---|
| Purchase at production quantity, inside six months | 48 | 662.24 |
| Small-lot purchase inside six months | 3 | 140.77 |
| List prices dated 2026-11-13 (reflectors, bollard) | 2 | 204.44 |
| Stale purchases and proforma invoices (older than six months) | 20 | 647.17 |
| Stale ByTechs labour | 3 | 51.95 |
| **Priced** | **76** | **1,706.57** |
| Unpriced part rows | 54 | |
| Unpriced labour rows | 12 | |

$1,007.45 rests on prices inside six months and $699.12 on older ones. 71 of 124 leaf parts are priced.

By configuration line:

| Line | Current | Stale | Unpriced rows |
|---|---|---|---|
| `AG-CS3-Kit` | 711.88 | 39.47 | 35 |
| `AG-SEN2-RR-Kit` | 116.59 | 321.14 | 13 |
| `AG-Dual46-RoundBollard-Kit` | 0.00 | 259.58 | 11 |
| `AG-IP-RRBM-DC-Kit` | 78.98 | 78.93 | 5 |
| Enclosure base and top | 0.00 | 0.00 | 2 |
| `EXT-H-2118F` bollard | 100.00 | 0.00 | 0 |

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
| IPEX junction box | 1 | 68.04 | stale purchase, 150 units | 2026-04-08 |
| Sequent Watchdog HAT | 1 | 45.20 | purchase, 50 units | 2026-06-22 |
| Sixfab base HAT | 1 | 45.20 | purchase, 84 units | 2026-06-11 |
| I425-GL modem | 1 | 35.00 | purchase, 100 units | 2026-11-06 |
| Titen HD anchor | 12 | 27.66 | purchase, 20 packs of 25 | 2026-07-16 |
| Sensor bar assembly (labour) | 1 | 27.00 | stale Deel task line, 10 units | 2025-12-14 |
| Modem bridge bare PCB | 1 | 21.36 | small-lot purchase, 5 units | 2026-10-08 |
| Bollard washer | 12 | 20.73 | purchase, 500 units | 2026-07-16 |

The camera price includes its 5 m USB cable, so the two cable rows are priced at $0.00. The Raspberry Pi cooler is $6.50 on the same MakerBright invoice.

Every row, with its source: `scratchpad/2026-11-13-vpi-assembly-price/out/rr-bollard-dual46_price_lines.csv`. Rebuild: `uv run --python 3.15 price_config.py configs/rr-bollard-dual46.csv --as-of 2026-11-13`.

## Still unpriced

- **Enclosure base and top** (Haig Precision).
- **ByTechs-made parts**, 24: printed and cut parts for the compute stack (7), camera module (5), bollard mount (3), sensor bar (5) and reflector cover (1); two cable assemblies; ferrules.
- **Labour** for 12 assemblies: compute stack, camera module, bollard mount, reflector, USB and modem bridge PCBAs, the three kits, the install pack and its two sets.
- **Packaging.** In no BOM. Uline boxes were $3.06 to $5.71 landed each on 2026-06-22.
- **20 Digi-Key parts with no visible purchase**: mostly resistors, capacitors, LEDs and diodes on the PCBAs, plus the Samtec header, the USB 3.0 plugs and one standoff.
- **Others**: four `EXT-TBD` PCB connectors, the padlocks (3), the trash bag and McMaster 92095A210.
- **Bollard freight and tax.** The $100.00 is list price only.

The ByTechs archive does not fill the ByTechs gaps: its last five invoices say only "See invoice" ([research/invoices.md](research/invoices.md)).

## Stale lines that need a quote or a confirmation under the six-month rule

- E3Z-R61 sensors, $256.77: invoice paid 2026-01-16. The order acknowledgement Ben supplied shows the same $128.20 unit price from 2025-10-14 ([research/powermatic-ordack.md](research/powermatic-ordack.md)).
- ELP cameras, $254.25: proforma invoice dated 2026-01-27.
- Junction box, $68.04; the two Misumi bars, $25.30; compression connectors, $10.89; P30B batteries, $9.27; and smaller lines.
- All ByTechs labour figures: the newest is from 2025-12.

## Priced for other configurations

- Wall-mount camera bracket `AG-PIC-005-001_WallBracket`: $49.62 landed ($45.11 plus sales tax), 56 units, Haig invoice 98995 dated 2026-10-06. Not in this configuration.

## Sources

- First pass and coverage: [research/first-pass.md](research/first-pass.md).
- First roll-up, how a price is picked, BOM questions: [research/partial-rollup.md](research/partial-rollup.md).
- ByTechs and JLCPCB invoices: [research/invoices.md](research/invoices.md).
- Powermatic order acknowledgement: [research/powermatic-ordack.md](research/powermatic-ordack.md).
- ELP, Haig and MakerBright documents: [research/elp-haig-makerbright.md](research/elp-haig-makerbright.md).
- E39-R1S at $26.11 (https://www.digikey.com/en/products/detail/omron-automation-and-safety/E39-R1S/761204) was given by Ben on 2026-11-13 as the most recent source; the page was not opened.
