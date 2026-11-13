# ByTechs itemized invoices and the Samtec acknowledgement

Written 2026-11-13T18:10Z. Ben put a folder of ByTechs invoices and a Samtec document in `scratchpad/` on 2026-11-13, and gave one price in chat. Files named below are in `scratchpad/2026-11-13-vpi-assembly-price/`.

## ByTechs invoices: `data/invoices/bytechs/ByTechs-AG-2026/`

27 PDFs, "Invoice 1165.pdf" to "Invoice 1217.pdf", dated 2026-01-06 to 2026-09-30. These are ByTechs' own invoices, the ones the Deel invoices point to ([invoices.md](invoices.md)): each has a line table of product, description, quantity, rate and amount.

Query: `uv run --python 3.15 parse_bytechs_invoices.py data/invoices/bytechs/ByTechs-AG-2026`. Result: `invoice_lines_bytechs.csv`, 282 lines, $89,852.24. The parser asserts that every invoice's lines add up to its printed total, that line numbers run without gaps, and that quantity times rate equals each amount. Two layout cases needed handling: a line number left alone on a line by a page break (invoice 1171), and a credit printed with a typographic minus sign (invoice 1213, a $12.00 credit).

Totals match the Deel invoices where checked: 1217 is $11,716.05, 1213 is $7,091.00, 1206 is $2,798.50, 1205 is $6,602.50, and 1203 plus 1201 are $3,092.50 and $2,127.50.

### Lines used in the roll-up

| ByTechs line | Qty | Rate | Per unit | Invoice, line, date | Roll-up row |
|---|---|---|---|---|---|
| Manufacturing: Compute Stack Units | 41 | $75.00 | $75.00 | 1217 line 5, 2026-09-30 | labour, `AG-CS3-001-000` |
| PCB Assembly Services: PartyHat X5C Assembly (120 units) | 27 h | $100.00 | $22.50 | 1199 line 8, 2026-06-02 | labour, `AG-CS3-002-000_PartyHAT` |
| Manufacturing: USB Bridge Assembly (252 units) | 11 h | $100.00 | $4.37 | 1197 line 2, 2026-05-26 | labour, `AG-CS3-003-000_USBBridge` |
| PCB Assembly Services: Modem Bridge Assembly (32 units) | 2 | $150.00 | $9.38 | 1217 line 27, 2026-09-30 | labour, `AG-CS3-004-000_ModemBridge` |
| PCB Assembly Services: Sensor Bar PCB Assembly (200x units) | 10 h | $100.00 | $5.00 | 1194 line 14, 2026-05-11 | labour, `AG-SEN2-004-000_Breakout` (stale by three days) |
| Manufacturing: Retroreflective Sensor Bar Building | 20 | $30.00 | $30.00 | 1217 line 24, 2026-09-30 | labour, `AG-SEN2-RR-Kit` |
| Manufacturing: 3D Print RetroReflective Rain Covers and install Reflectors | 84 | $6.00 | $6.00 | 1217 line 13, 2026-09-30 | labour, `AG-SEN2-002-000`, two per kit |
| Manufacturing: Dual Camera Kit - 6/4mm | 20 | $35.00 | $35.00 | 1217 line 8, 2026-09-30 | labour, `AG-Dual46-RoundBollard-Kit` |
| Manufacturing: 3D Printing Camera Housings and Parts | 50 | $25.00 | $25.00 | 1205 line 17, 2026-06-26 | adder, `AG-Dual46-RoundBollard-Kit` |
| Manufacturing: Installer kit Packing | 25 | $15.00 | $15.00 | 1217 line 3, 2026-09-30 | labour, `AG-IP-RRBM-DC-Kit` |
| Manufacturing: Enclosure Packing | 23 | $10.00 | $10.00 | 1217 line 4, 2026-09-30 | adder, enclosure base |
| PCB Assembly - General Parts Cost: Sensor Bar Boxes 3.5 x 3.5 x 20" | 50 | $3.19 | $3.19 | 1174 line 6, 2026-02-18 | adder, `AG-SEN2-RR-Kit` (stale) |

The hourly PCB assembly lines give a per-unit figure only through the unit count in their description. The Party HAT figure is supported by an earlier line: "PartyHat x5b 40x units (Hourly)", 9 h at $100.00 on invoice 1165, which is also $22.50 a unit. Two Party HAT X5C lines exist, each 27 h for "(120 units)" (invoices 1184 and 1199); they are read as two batches of 120, not one batch billed twice.

### How rates moved in 2026

- Compute stack build: $50.00 (January to March, with one unit at $60.00), $60.00 (April to early June, starting with "New Cases (Including 3d printing)"), $65.00 (June, "Added FFC bracket"), $75.00 (from the "Week of 7/17" line, "Included all new pricing").
- Sensor bar build: $27.00 (January to May), $30.00 (April kit line, and August on).
- Dual camera build: $30.00 to $32.00 (February to April), $35.00 (May on, "with Heatshrink").
- Rain covers: $4.00 to print (August), $6.00 to print and install reflectors (September).

### Readings that are assumptions

- **Camera printing.** Invoice 1205 bills 50 "3D Printing Camera Housings and Parts" at $25.00 and invoice 1199 bills 50 "3D Printing Camera Cases" at $25.00; invoice 1193 bills 100 "Camera Housings" at $23.00. Invoice 1217 bills 30 "3D Print Dual Camera Mounts" at $6.00 and no housings. The roll-up takes one $25.00 set per camera kit. Whether the $6.00 line replaces it or is a different part is not stated.
- **Compute stack printing.** No line bills printing of compute stack parts except invoice 1187, "Assembled VPi Compute Stack New Cases (Including 3d printing)" at $60.00. The seven printed stack parts are carried at $0 on the reading that the build rate has included printing since then.
- **Sensor bar printing.** Invoice 1169 bills 100 sets at $30.60: "3D printing of Sensor bar parts. 2x Reflector Housings 1x Base 1x Fork 1x Left Sensor Mount 1x Right Sensor Mount 1x Pivot". No later line bills sensor bar printing, though about 240 bars were built after it. The five printed sensor bar parts are left unpriced.
- **One line per kit.** No invoice bills the sensor bar assembly, camera module, bollard mount or install pack sets separately from their kit, so those labour rows are carried at $0.
- **Filament.** No invoice line bills filament. The Ramp cost record has three Polymaker records, $3,585.60, from 2026-05-04 to 2026-10-30 (`scratchpad/2026-11-13-bom-costs/out/cost_records_20250101.csv`), presumably filament; not examined. Print material is not in the price.

### Not used

- "Cost for Parts for 250x Compute Stack Vπ units", $7,935.64 (invoice 1170 line 5, 2026-01-21): $31.74 a stack, no breakdown. It may cover the PCBA parts the roll-up cannot find a purchase for. Not added, because it would also overlap parts already priced from Ramp.
- "Costs for parts, PCBs, etc to complete assembly of boards", $1,642.30 (invoice 1165).
- Parts ByTechs bought early in 2026 that the roll-up prices from later AirGarage purchases: M5 x 8 mm screws ($0.10), M5 heat-set nuts ($0.17), M5 T-nuts ($41.76 per 500), terminal blocks.
- "Cable Harness - 2 Pin Wire w/ Ferrules each end installed into pluggable terminal", 25 at $3.50 (invoice 1167): for the older Party HAT X2B, not matched to the current power cable `AG-CS3-001-007_PowerCab`.
- "14 x 14 x 14 Boxes (50 Count)", $52.20, and packing paper, $52.59 (invoice 1174): which kit they pack is not stated.
- Overhead: shop rent ($100.00 to $250.00 a month), ordering supplies, inventory work, troubleshooting returned units, V4 and aerial kit lines, vest and ticket kit packing.

## Samtec: `data/invoices/samtec/34804506_Acknowledgment_20250801123454.pdf`

Order acknowledgement, job 34804506, entry date 8/1/2025, credit card, ship to Chris Williamson at ByTechs by UPS 2nd Day Air, billing option "Prepay and Add", probable country of origin VN.

- 60 x SSM-120-L-DV-BE-LC at $4.970, $298.20. This is the Party HAT's Pi GPIO header, `EXT-SSM-120-L-DV-BE-LC`.
- The Ramp pull has a Samtec card charge of $307.15 on 2025-08-06, memo "Tripwire Build Materials - headers for production", with no receipt (`scratchpad/2026-11-13-bom-costs/out/cost_records_20250101.csv`, record `c149d753-c845-40c9-99c7-e0611fce4e87`). The roll-up takes that as this order with $8.95 freight: $5.12 landed each. The link between the two is inferred from the date and amount.
- It is from 2025-08, so the row is stale. A later Samtec charge of $1,295.49 on 2026-10-20 (invoice 18438338) has no line items; 260 headers at $4.97 would be $1,292.20.

## McMaster 92095A210

Ben, 2026-11-13: "$10.91 per pack of 50". $0.2182 each, entered in `manual_prices.csv` as a quote with no source document.

## Effect on the roll-up

Query: `uv run --python 3.15 price_config.py configs/rr-bollard-dual46.csv --as-of 2026-11-13`. Result: `out/rr-bollard-dual46_price_lines.csv`.

- Priced: $2,118.56 (was $1,918.73): parts $1,784.74, ByTechs labour $208.25, adders $125.57.
- $1,245.92 on prices inside six months, $872.64 on older ones.
- Of 124 leaf parts: 74 priced, 17 carried at $0, 33 unpriced. All 15 labour rows priced, six of them at $0 under a kit rate.
