# As-purchased cost record (Ramp)

As of 2026-11-13 (UTC). Not yet matched to BOM lines. Remaining work and open decisions: [../bom-costs/plan.md](../bom-costs/plan.md).

Files (in `scratchpad/2026-11-13-bom-costs/`), one pair per window:

- `out/cost_lines_<since>.csv`: one row per purchased line item, with landed cost, part numbers where known (`vendor_pn`, `manufacturer`, `mpn`, `pn_source`), `vendor_order` and `ships_to_bytechs`.
- `out/cost_records_<since>.csv`: one row per card charge, reimbursement or bill, with its reconciliation, flags and `needs_review`.
- Rebuild: `uv run --python 3.15 build_cost_record.py --since 2026-05-13` (six months) or `--since 2025-01-01` (all history). Inputs are the Ramp pull in `data/ramp/` ([research/ramp.md](research/ramp.md)), `data/ramp/manual_lines.csv` for lines read by hand, and receipt text in `data/ramp/raw/receipt_ocr/search/`.

## What is in it

- Six months (`20260513`): 522 records, $231,555.16: 496 card records (498 charges), 19 reimbursements ($1,642.97, including two drafts, one undated), 7 bills ($43,071.85). 923 line rows.
- All history (`20250101`): 1,608 records, $600,200.04: 1,434 card records, 160 reimbursements (38 drafts), 14 bills. 2,979 line rows. Equals Ramp's spend report plus draft reimbursements.

It includes everything the three spent, not only hardware (Hologram data, Pirate Ship labels, software, travel). Ramp vendor category, fund and accounting coding are on every row for filtering. Undated draft reimbursements appear in every window.

## How costs are landed

- The amount actually charged (card), reimbursed or paid (bill) is the truth. Each record's amount is spread over its priced lines in proportion to line total, so `landed_total` includes the line's share of tax, shipping, tariffs, fees and discounts, and landed totals sum to the record amount (asserted).
- `landed_unit_cost` = `landed_total` / `quantity`. It is blank when quantity is missing or the line cost is zero (backorders).
- Duplicate receipts on one charge: the copy whose total matches the charge and whose lines add up to its own subtotal is used; the rest are ignored.
- Charges that together pay one receipt (split orders) are one record.
- Extraction faults are corrected by a fit test against the receipt subtotal, not by vendor rules. See [research/ramp-receipt-extraction.md](research/ramp-receipt-extraction.md). Lines dropped by these fixes stay in the file with `line_note` and no cost.
- Bills have no line items in Ramp; all 14 were typed from the invoice PDFs into `manual_lines.csv`, with file and page. Powermatic freight-only bills are separate records tied to their goods order by `vendor_order`.
- Lines whose quantity is above 1 but whose total equals the unit price are read as unit price when that fits the receipt subtotal.
- Exact refunds are paired with the purchase they reverse (`refund_of`, `refunded_by` flags).
- Dates are UTC: card transaction time, reimbursement expense date, bill paid date (`receipt_date` holds the invoice date for bills).

## Limits

See the gaps and their sizes in [../bom-costs/plan.md](../bom-costs/plan.md#where-it-stands): records with no receipt, receipts Ramp could not itemize, flagged records, and the few part numbers on electronics lines.
