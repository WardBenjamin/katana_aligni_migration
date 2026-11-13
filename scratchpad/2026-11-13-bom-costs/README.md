# BOM costs from Ramp

Goal: pull every Ramp purchase record for Ben, Bryan Monti and Chris Williamson (card transactions, receipts, reimbursements, bills, requests) as the input for a per-item as-purchased BOM cost update. BOMs are not used yet.

Status: paused 2026-11-13. Line-item cost record built for all history and the last six months; not matched to BOMs. Method: `docs/boms/cost-record.md`. Remaining scope: `docs/bom-costs/plan.md`. Notes: `docs/boms/research/ramp.md`.

## Contents

- `data/ramp/raw/`: Ramp connector output as returned (JSON), except `requests.json` (trimmed).
- `data/ramp/receipts/`: receipt and invoice files downloaded from Ramp, by reimbursement or bill ID. Card-transaction receipt images are not reachable through the connector.
- `flatten_ramp.py`: raw JSON to CSVs (`uv run --python 3.15 flatten_ramp.py`):
  - `data/ramp/spend.csv`: every card, reimbursement and bill record, with memo.
  - `data/ramp/transactions.csv`: card transactions with coding, memo and receipt IDs.
  - `data/ramp/receipt_lines.csv`: one row per receipt line item, joined to its transaction and memo. Duplicate receipts per transaction are not removed (`n_receipts_on_txn`).
  - `data/ramp/reimbursements.csv`: reimbursements, drafts included, with receipt IDs.
- `data/ramp/manual_lines.csv`: lines read by hand, with source file and page: the window's 7 bill invoices, the Home Depot reimbursement receipt image, OSH Stencils SKUs from receipt OCR (`raw/receipt_ocr/`).
- `data/ramp/raw/reimbursement_receipt_details/`: Ramp extraction for all 160 reimbursement receipts.
- `data/ramp/raw/receipt_ocr/`: receipt text from Ramp's receipt search. `targets.csv` lists every receipt with its upload time; `search/` holds results (only receipts uploaded since 2026-04-02 are indexed); `targeted_calls.json` is the planned narrow-window search list (ids 0 to 14 run, 15 to 138 not yet).
- `build_cost_record.py`: per-line cost record (`uv run --python 3.15 build_cost_record.py --since 2026-05-13`, or `--since 2025-01-01` for all history):
  - `out/cost_lines_<since>.csv`: one row per line item with landed cost (tax, shipping, fees spread pro rata so lines sum to the amount paid) and part numbers where known.
  - `out/cost_records_<since>.csv`: one row per card charge, reimbursement or bill, with reconciliation and `needs_review`.
  - `out/*_20250301.csv` are a superseded intermediate run, not committed.

Not committed: `data/ramp/receipts/reimbursements/` (236 MB of images and PDFs), the FixturFab bank wire instructions PDF under `data/ramp/receipts/bills/89d333b3-…/`, and `data/ramp/raw/bill_text/` (pdftotext output; rebuild with `pdftotext -layout`). All gitignored.
