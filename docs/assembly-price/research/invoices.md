# ByTechs (Deel) and JLCPCB invoices from Ben

Written 2026-11-13T16:50Z. Ben put one archive and three PDFs in `scratchpad/` on 2026-11-13. They are now in `scratchpad/2026-11-13-vpi-assembly-price/data/invoices/`:

- `bytechs/archive-34-files-2026-11-13-16-39-28.zip`: the archive as received.
- `bytechs/pdf/`: its 34 PDFs, extracted.
- `pcb/invoice-5.pdf`, `invoice-6.pdf`, `invoice-7.pdf`: three JLCPCB invoices.

Read with `pdftotext -layout` (archive) and by eye (the JLCPCB PDFs are images with no text layer).

## ByTechs archive

- 25 invoices from Bytechs LLC to AirGarage, issued through Deel under a "Pay As You Go Contract", scope "Hardware assembly and fulfillment". File names start "Chris Williamson_INV-". They run from INV-2025-1 (work 2025-10-24 to 2025-10-31) to INV-nd68x8z-2026-18 (work 2026-10-01 to 2026-10-31) and total $96,421.21.
- 9 invoices from Deel Inc. for its own subscription fee, for example $49.00 for September 2026 (`Deel INV-e9z5g4n-2026-4622842_...pdf`).
- No invoice prints bank details.

The last five carry no line items. Each has one or two lines reading "Task: See invoice" and a total:

| Invoice | Work period | Issued | Total |
|---|---|---|---|
| INV-nd68x8z-2026-14 | 2026-06 | 2026-06-26 | $5,220.00 (two tasks: $3,092.50, $2,127.50) |
| INV-nd68x8z-2026-15 | 2026-07 | 2026-07-29 | $6,602.50 |
| INV-nd68x8z-2026-16 | 2026-08 | 2026-08-31 | $2,798.50 |
| INV-nd68x8z-2026-17 | 2026-09 | 2026-09-30 | $7,091.00 |
| INV-nd68x8z-2026-18 | 2026-10 | 2026-11-09 | $11,716.05 (status "PROCESSING") |

Sum of the five: $33,428.05. The labour, printed-part, cable and packaging lines are on ByTechs' own invoices, which these refer to ("See invoice", once "See invoice #1194" on INV-nd68x8z-2026-11) and which are not in the archive.

Of the 25, 16 say only "See invoice" or "See attached invoice". Task lines that do describe the work, all from 2025-10 to 2026-02:

- INV-2025-4, issued 2025-12-01: "10x Camera Build - See Invoice", $355.00. $35.50 per build, a V3.1-era camera.
- INV-2025-5, issued 2025-12-14: "10x Sensor Bar Assemblies for Inventory", $270.00. $27.00 per assembly.
- INV-2025-6, issued 2025-12-22: "5x PartyHat PCB Prototype Assembly and Onboarding/Assembly", $400.00; prototype run and Slack membership, $693.96.
- INV-2025-7, issued 2025-12-29: "5 Compute Stack builds, local network set up for remote login capabilities, etc. Set up rig for testing power hats", $640.00 (mixed work); burn-in and testing station, $535.56; crimpers, $861.60.
- INV-nd68x8z-2026-1, issued 2026-01-25: "100x 3d printed parts for sensor bar assemblies", $3,060.00 (unclear whether 100 sets or 100 parts); "16x V3.1 6mm Camera Builds 12x V3.1 Sensor Bar Kits 2x hour of labor packing orders", $1,014.00; "Pluggable Harnesses for PartyHat X2B", $87.50; PartyHat X2B build, repairs, parts and labour, $3,502.30.
- INV-2025-3: "Camera Build + Shipping", $280.00; "Shipping @ Box Order", $859.85. INV-nd68x8z-2026-4: "Rush packing, UPS drop off, Rent", $360.00. INV-nd68x8z-2026-5: "Camera Assembly / Packing", $410.00. INV-2025-1: inventory system, cleaning printed parts, onboarding, $1,060.00.

Used in the roll-up: only the sensor bar assembly line ($27.00, stale). The camera builds are a different product, the printed-parts line is ambiguous, and the rest mix several jobs.

## JLCPCB invoices

All ship to ByTechs, DDP. The roll-up spreads each invoice's shipping, tax and import charges over its lines by line total, as the cost record does.

| File | Invoice no. | Invoice date | Line | Qty | Unit | Line total | Invoice total | Landed each |
|---|---|---|---|---|---|---|---|---|
| `invoice-5.pdf` | 3346015A2026111301324297 | 14/11/2026 | 4-layer rigid PCB, `party-hat-x5c_gerbers(Reorder)_Y30` | 50 | $3.92 | $195.90 | $375.32 | $7.51 |
| `invoice-6.pdf` | 3346015A2026100821233800 | 14/10/2026 | 4-layer rigid PCB, `usb-bridge-x3_gerbers(Reorder)_Y29` | 20 | $3.34 | $66.70 | $227.23 | $6.02 |
| `invoice-6.pdf` | same | same | 2-layer flexible PCB, `modem-bridge_x3out(Reorder)_Y31` | 5 | $11.83 | $59.16 | $227.23 | $21.36 |
| `invoice-7.pdf` | 3346015A2026042902074034 | 05/05/2026 | Solder paste stencil, `sensor-bar-io-breakout-x2_gerbers(Reorder)_P5` | 1 | $12.49 | $12.49 | $200.78 | tooling |
| `invoice-7.pdf` | same | same | 2-layer rigid PCB, same file | 50 | $1.21 | $60.50 | $200.78 | $3.33 |

- Charges besides goods: invoice-5 shipping $81.17, sales tax $22.16, import taxes $68.57, disbursement fee $7.52; invoice-6 shipping $36.77, sales tax $13.02, import taxes $51.58; invoice-7 shipping $82.90, sales tax $12.46, import taxes $32.43.
- Shipping, tax and import charges add 81% to 175% to the goods value.
- The roll-up dates each line by the batch number (2026-11-13, 2026-10-08, 2026-04-29), the day the order was placed.
- The modem bridge was bought 5 at a time, so it counts as a small lot. The breakout board order is just over six months old, so it counts as stale.
- Whether these three orders are also among the JLCPCB card charges in the Ramp pull was not checked. No Ramp JLCPCB line is used in the roll-up, so nothing is counted twice.

Typed lines: `scratchpad/2026-11-13-vpi-assembly-price/invoice_lines.csv`. `price_config.py` asserts that each invoice's lines add up to its goods total.
