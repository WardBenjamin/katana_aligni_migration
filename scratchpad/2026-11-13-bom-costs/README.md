# BOM costs from Ramp

Goal: pull every Ramp purchase record for Ben, Bryan Monti and Chris Williamson (card transactions, receipts, reimbursements, bills, requests) as the input for a per-item as-purchased BOM cost update. BOMs are not used yet.

Status: pull done (2026-11-13T04:40Z). Cost update not started. Notes: `docs/boms/research/ramp.md`.

## Contents

- `data/ramp/raw/`: Ramp connector output as returned (JSON), except `requests.json` (trimmed).
- `data/ramp/receipts/`: receipt and invoice files downloaded from Ramp, by reimbursement or bill ID. Card-transaction receipt images are not reachable through the connector.
- `flatten_ramp.py`: raw JSON to CSVs (`uv run --python 3.15 flatten_ramp.py`):
  - `data/ramp/spend.csv`: every card, reimbursement and bill record, with memo.
  - `data/ramp/transactions.csv`: card transactions with coding, memo and receipt IDs.
  - `data/ramp/receipt_lines.csv`: one row per receipt line item, joined to its transaction and memo. Duplicate receipts per transaction are not removed (`n_receipts_on_txn`).
  - `data/ramp/reimbursements.csv`: reimbursements, drafts included, with receipt IDs.

Not committed: `data/ramp/receipts/reimbursements/` (236 MB of images and PDFs, gitignored) and the FixturFab bank wire instructions PDF under `data/ramp/receipts/bills/89d333b3-…/` (gitignored).
