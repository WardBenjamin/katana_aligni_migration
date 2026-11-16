# Ramp: purchase records for Ben, Monti and Chris

Started 2026-11-13T04:01Z. Read-only pull through the Ramp MCP connector (token is user-level, business 4c411bd8; scopes include transactions, receipts, reimbursements, bills, purchase_orders, reporting read). Purpose: inputs for a per-item as-purchased BOM cost update. BOMs not read for this note. Data: `scratchpad/2026-11-13-bom-costs/data/ramp/`.

## People

From `ramp_get_org_chart` (current user), 2026-11-13:

- Benjamin Ward, 01954cee-c726-7b10-b069-c9c9b450ee6c, manager Josiah Lapolla.
- Bryan Monti, 01954cee-c717-707b-a6d2-fd8f365f01ac, reports to Ben.
- Chris Williamson, 019c9064-3541-72df-bab0-c9322d9fe100, chris@bytechsllc.com (ByTechs), reports to Ben.
- Lorenzo Allas also reports to Ben. Not in scope; his 2 card transactions came back in the team pull and are left out of the CSVs (still in the raw pages).

## Card transactions

`ramp_get_transactions`, scope `transactions_made_by_my_team`, state `all` (cleared and pending, never declines), sorted by date ascending, 200 per page, `submitted_items` details. 8 pages, `next_page_cursor` null on page 8. Raw: `data/ramp/raw/transactions/page_01..08.json`.

- 1,439 records, 1,439 unique IDs, 2025-03-04 to 2026-11-12. All USD. 1,434 cleared, 5 pending.
- Ben 693 (500 with receipts, 683 receipt IDs), Monti 439 (311, 382), Chris 305 (267, 281), Lorenzo 2.
- Ben's 693 also matches `my_transactions` total_count 693.
- The list view leaves `reason_or_justification` null even when a memo exists (Digi-Key 3ce938db: list null, `ramp_get_full_transaction_metadata` memo "Tripwire R&D - 3x Party HAT X1 build materials"). Memos come from the spend report below.
- Card receipts have no file link in any connector tool tried (`ramp_get_transactions`, `ramp_get_full_transaction_metadata`, `ramp_get_receipt_details`, `ramp_search_receipts`). Only Ramp's extraction is available; images would need the Ramp web app or API.

## Spend report (memos, all spend types)

`ramp_reporting_query` on dataset `spend`, detail rows, filter `user in` the three IDs, no date bound, `page_size` 1000, 2 pages. Raw: `data/ramp/raw/spend_report/page_01..02.json`.

- 1,573 rows: card 1,437 (Ben 693, Monti 439, Chris 305), reimbursements 122 (Ben 120, Monti 2), bills 14 (Ben 11, Monti 3).
- The 1,437 card IDs match the transaction pull exactly.
- 946 rows have a memo.
- Reimbursement drafts are not in this dataset (see below).

## Receipts on card transactions

1,346 distinct receipt IDs across the three users' card transactions. `ramp_get_receipt_details` returns merchant, date, total, subtotal, taxes, fees, discounts and line items (name, quantity, unit price, total). Batches of 100 and 250 worked. Raw: `data/ramp/raw/receipt_details/batch_*.json`.

- Several transactions carry the same order more than once (Digi-Key 3ce938db has 3 receipts: two itemized copies, one with 10 of the 17 lines, one not itemized). Line items must be de-duplicated per transaction before costing.
- Item names are the vendor's description (Digi-Key "RES 10K OHM 1% 1/10W 0603"), not part numbers. Part numbers appear in the OCR text, which `ramp_search_receipts` returns as `ocr_excerpt` (Digi-Key PART and MFG lines), but that search is capped at 100 candidates per query, so it is not a full export.

## Reimbursements

`ramp_get_reimbursements`, scope all, `user` tag per person, page 200, comments on. Raw: `data/ramp/raw/reimbursements/{ben,monti,chris}_page_01.json`.

- Ben 158 (120 paid, 38 drafts), Monti 2 (paid), Chris 0. Mostly travel and meals; some Home Depot (12) and Lowe's (4).
- Records have no receipt IDs. `ramp_get_reimbursement_receipts` per reimbursement returns `receipt_url` (signed, expires about 1 hour) and `pdf_preview_url`. Raw: `data/ramp/raw/reimbursement_receipts.jsonl`; files in `data/ramp/receipts/reimbursements/<reimbursement>/`.

## Bills

14 paid bills, all found with `ramp_search_bills` by payee: Eagle Wireless 4 (INV2621, INV2209, INV1104, INV1103), Powermatic 5 (3680202, 3675147, 3661292, 3660264, 1417784), PTC 2 (10628199, INV00036107), Quectel 1 (D265070387, $18,652.50, SWIFT), FixturFab 1 (INV/2026/00065), 3D Hubs 1 (LLC-IN150553). Details and invoice files: `data/ramp/raw/bills/`, `data/ramp/receipts/bills/`.

## Purchase orders, requests, unmatched receipts

- `ramp_search_purchase_orders` with the three as owners: 0.
- `ramp_search_unified_requests` by owner or requester: 10 fund requests (REQ-66 to REQ-194), no item lines. Saved trimmed to `data/ramp/raw/requests.json`.
- `ramp_list_unmatched_receipts` (Ben only; the tool has no user filter): 0.

## Results (2026-11-13T04:40Z)

- Card receipt extraction: 1,346 of 1,346 receipts pulled, 1,264 itemized, 2,630 line items. One receipt has no extraction (`dad7b5c5-2e65-4d2c-a9dc-bb59b81f4ab7`, `structured_data` null). Most item lines: Amazon 743, Pirate Ship 472 (shipping labels), Digi-Key 445, McMaster-Carr 165, Hologram 97, Mouser 80.
- Reimbursement receipts: 160 reimbursements queried, 160 receipts (2 reimbursements have none: d1ca9cd7, a3a5ac60; 2 have two: a41af7ab, 935da35f). 160 files downloaded, 75 PDF, 73 JPEG, 12 PNG, 236 MB. Links came from two Ramp hosts, customer-documents.ramp.com and receipts.ramp.com. `pdf_preview_url` was null on all. Files are gitignored for size.
- Bills: `ramp_get_bill_details` returns `line_items: []` with `line_items_status: "omitted"` on all 14; the only per-line text is in `accounting_field_codings`, with no amounts. Per-item prices for bills must be read from the 23 invoice files (16 PDF, 1 PNG, 6 email text). The FixturFab bill includes the vendor's bank wire instructions PDF; it is kept local and gitignored.
- CSVs from `flatten_ramp.py`: `spend.csv` 1,573, `transactions.csv` 1,437, `receipt_lines.csv` 2,712 (2,630 item rows plus one row per receipt with no items), `reimbursements.csv` 160. The script asserts the pull counts above.

- 2026-11-16: at Ben's request the reimbursement receipt files, the bill text and the FixturFab bank wire instructions PDF are now committed to the workspace repo (the `.gitignore` rules for them were removed). The repo has no remote.
