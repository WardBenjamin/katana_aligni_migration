# vπ full assembly price

Goal: the current landed cost of one complete vπ unit, per configuration. Plan: `docs/assembly-price/plan.md`.

Status: partial roll-up, 2026-11-13. $1,451.45 priced for the first configuration; cameras, enclosure, ByTechs-made parts, most labour and packaging are unpriced. Current result: `docs/assembly-price/price.md`. Nothing promoted.

## Contents

- `configs/rr-bollard-dual46.csv`: the first configuration (top-level part numbers and quantities).
- `price_config.py`: prices one unit of a config (`uv run --python 3.15 price_config.py configs/rr-bollard-dual46.csv --as-of 2026-11-13`). Writes `out/<config>_price_lines.csv`, one row per leaf part and one labour row per assembly, with status, date and source. The rules for picking a price are in its docstring.
- `price_rules.csv`: reviewed patterns that tie a part (or an assembly's labour) to purchase lines that carry no part number, with units per pack. Quote any pattern that contains a comma.
- `manual_prices.csv`: prices read by hand, each with date, basis and source (list prices, quotes, record memos).
- `invoice_lines.csv`: lines typed from invoices that are not in the Ramp pull, with the invoice's goods total and grand total so the script can land each line.
- `data/invoices/bytechs/`: the archive Ben supplied (25 Bytechs LLC invoices issued through Deel, 9 Deel fee invoices) and its extracted PDFs. `data/invoices/pcb/`: three JLCPCB invoices. Notes: `docs/assembly-price/research/invoices.md`.
- `data/invoices/powermatic/OrdAck1426189.pdf`: Powermatic order acknowledgement of 2025-10-14 for 200 E3Z-R61 and 200 E39-R1S. Notes: `docs/assembly-price/research/powermatic-ordack.md`.
- `explode_config.py`: explodes a config through `boms/` into leaf parts and counts part-number matches (`uv run --python 3.15 explode_config.py configs/rr-bollard-dual46.csv`). Writes `out/<config>_leaf_parts.csv`. `price_config.py` imports its explosion.
- `probe_names.py`: finds purchase lines for high-value parts by vendor and item name (`uv run --python 3.15 probe_names.py`). Writes `out/name_probe_lines.csv`. Used for the plan; unreviewed.

All scripts read `scratchpad/2026-11-13-bom-costs/out/cost_lines_20250101.csv`; `price_config.py` also reads `invoice_lines.csv`.
