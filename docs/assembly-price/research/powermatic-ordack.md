# Powermatic order acknowledgement 1426189

Written 2026-11-13T16:56Z. Ben put `OrdAck1426189.pdf` in `scratchpad/` on 2026-11-13 as the Powermatic (Omron) document to take the E3Z-R61 price from. It is now `scratchpad/2026-11-13-vpi-assembly-price/data/invoices/powermatic/OrdAck1426189.pdf`. Read with `pdftotext -layout`; one page.

## What it is

An order acknowledgement, not an invoice. Order number 1426189, order date 10/14/2025 13:32:08, PO number PO-POWERMATIC-003, terms Net 30, ordered by Benjamin Ward, bill to and ship to AirGarage in San Francisco.

| Item | Qty | Unit price | Extended |
|---|---|---|---|
| E3Z-R61 (Omron sensor) | 200 | $128.20 | $25,640.00 |
| E39-R1S (Omron sensor) | 200 | $20.94 | $4,188.00 |

Sub-total $29,828.00, tax $2,572.67, amount due $32,400.67. Both lines are marked NC/NR, expected dock date 10/27/2025, ship UPS Ground.

## E3Z-R61 price

$128.20 each at 200 units, before tax and freight.

## How it relates to what the roll-up already uses

- The roll-up prices the E3Z-R61 from Powermatic invoice 3675147: 200 at $128.20, plus a share of $43.34 freight, $128.39 landed. That invoice is order 1426667, PO-POWERMATIC-003-1, shipped to ByTechs, with no tax, invoice dated 2025-11-18 and paid 2026-01-16 (`scratchpad/2026-11-13-bom-costs/data/ramp/manual_lines.csv`, bill `0e46bef4-515c-4a14-897d-eaa7e3231e99`).
- Same quantities and unit prices on both documents, and the PO numbers are -003 and -003-1. This acknowledgement looks like the first version of that order, re-entered as 1426667 with the ship-to changed. Not confirmed: the order numbers differ and nothing on either document names the other.
- Only one Powermatic bill of this size is in the Ramp pull, so the acknowledgement is not treated as a second purchase and is not added to `invoice_lines.csv`.
- The unit price is the same, so the roll-up does not change. The acknowledgement is older than the invoice (2025-10-14 against 2026-01-16), so the E3Z-R61 line is still stale under the six-month rule.

## E39-R1S

The same document has the E39-R1S at $20.94 for 200 units. The roll-up uses $26.11, the Digi-Key single-unit price Ben gave on 2026-11-13.
