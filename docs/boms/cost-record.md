# As-purchased cost record (Ramp)

As of 2026-11-13 (UTC). Window: spend dated 2026-05-13 onward. Not yet matched to BOM lines.

Files (in `scratchpad/2026-11-13-bom-costs/`):

- `out/cost_lines_20260513.csv`: one row per purchased line item.
- `out/cost_records_20260513.csv`: one row per card charge, reimbursement or bill, with its reconciliation.
- Rebuild: `uv run --python 3.15 build_cost_record.py --since 2026-05-13`. Inputs are the Ramp pull in `data/ramp/` ([research/ramp.md](research/ramp.md)) plus `data/ramp/manual_lines.csv` for lines read by hand.

## What is in it

521 records, $231,328.74: 496 card records (498 charges), 18 reimbursements ($1,416.55, one $20 draft), 7 bills ($43,071.85). By person: Monti $93,378, Ben $75,175, Chris $62,776. It includes everything the three spent, not only hardware (Hologram data, Pirate Ship labels, software, travel). The Ramp vendor category, fund and accounting coding are on every row for filtering.

922 line rows:

| Line source | Rows | Landed $ |
|---|---|---|
| Ramp receipt extraction | 774 | 175,785.62 |
| Read by hand (bill invoices, one receipt image, OSH SKUs) | 28 | 43,511.90 |
| Record only (no itemized receipt) | 119 | 11,752.57 |
| Unallocated (OSH Stencils, no prices anywhere) | 1 | 278.65 |

## How costs are landed

- The amount actually charged (card), reimbursed or paid (bill) is the truth. Each record's amount is spread over its priced lines in proportion to line total, so `landed_total` includes the line's share of tax, shipping, tariffs, fees and discounts, and landed totals sum to the record amount (asserted).
- `landed_unit_cost` = `landed_total` / `quantity`. It is blank when quantity is missing or the line cost is zero (backorders).
- Duplicate receipts on one charge: the copy whose total matches the charge and whose lines add up to its own subtotal is used; the rest are ignored.
- Charges that together pay one receipt (split orders) are one record.
- Extraction faults are corrected by a fit test against the receipt subtotal, not by vendor rules. See [research/ramp-receipt-extraction.md](research/ramp-receipt-extraction.md). Lines dropped by these fixes stay in the file with `line_note` and no cost.
- Bills have no line items in Ramp; their lines were typed from the invoice PDFs into `manual_lines.csv`, with file and page.
- Dates are UTC: card transaction time, reimbursement expense date, bill paid date (`receipt_date` holds the invoice date for bills).

## Limits

- 18 records ($9,703.73) have `needs_review`: the receipt does not match the charge (Amazon partial shipments, ULINE, Turo, Apple, Ubiquiti) or the charge is far from lines plus stated tax and fees (missing tariff or tax). Their landed costs are proportional estimates.
- 111 records ($10,519.87) have no receipt at all, so they are one line named from the memo: Pirate Ship 32, Amazon 14, ParkPow 14, Home Depot 6, Digi-Key 5, UPS 5, Ubiquiti 5, JLCPCB 3 and others. Item detail needs those receipts from Ramp's web app or the vendor.
- 8 more records have receipts Ramp could not itemize (mileage, meals, 3 small Amazon orders, a DHL tariff, a Hologram invoice).
- Item names are vendor descriptions. Part numbers are only in some names (McMaster, Digi-Key "PART:" lines) and are not parsed yet.
- Refunds are separate negative records (Home Depot −59.28, ParkPow −250.00, Turo −750.00), not netted against their purchases.
