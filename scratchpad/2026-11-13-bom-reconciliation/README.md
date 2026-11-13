# BOM reconciliation

Goal: compare every BOM source with the Aligni export in `boms/` and list what is missing or out of date before the Katana migration. Findings: `docs/boms/reconciliation.md`. Sources: `docs/boms/data-sources.md`.

Status: done 2026-11-13. Decisions open in `docs/boms/reconciliation.md`.

## Contents

- `data/notion/`: 34 Notion BoM databases under Tripwire Home, plus `manifest.csv`. Made by `notion_to_csv.py` from Notion connector output.
- `data/ecad/`: KiCad BOMs per project, `manifest.csv`, committed-vs-schematic diff, a deleted BOM from history. Made by `ecad_bom.py` (`uv run --python 3.15 ecad_bom.py`).
- `data/shopify/`: product variants and SKUs, transcribed from the Shopify connector.
- `data/sheets/`: install-pack BOM tabs from the "Install Packs" Google Sheet, read in Chrome.
- `data/mcad/`: file list of `repos/tripwire-mcad` at 033bdfb.
- `data/slack/`: BOM-relevant Slack events.
- `compare.py`: Aligni vs Notion, line by line (`uv run --python 3.15 compare.py`), writes `out/aligni_vs_notion_*.csv`.
