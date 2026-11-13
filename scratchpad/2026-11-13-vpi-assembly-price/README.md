# vπ full assembly price

Goal: the current landed cost of one complete vπ unit, per configuration. Plan: `docs/assembly-price/plan.md`.

Status: partial roll-up, 2026-11-13. $1,101.22 priced for the first configuration from the Ramp cost record; cameras, enclosure, ByTechs-made parts, most labour and packaging are unpriced. Results: `docs/assembly-price/research/partial-rollup.md`. Nothing promoted.

## Contents

- `configs/rr-bollard-dual46.csv`: the first configuration (top-level part numbers and quantities).
- `price_config.py`: prices one unit of a config (`uv run --python 3.15 price_config.py configs/rr-bollard-dual46.csv --as-of 2026-11-13`). Writes `out/<config>_price_lines.csv`, one row per leaf part and one labour row per assembly, with status, date and source. The rules for picking a price are in its docstring.
- `price_rules.csv`: reviewed patterns that tie a part (or an assembly's labour) to purchase lines that carry no part number, with units per pack. Quote any pattern that contains a comma.
- `manual_prices.csv`: prices read by hand, each with date, basis and source (list prices, quotes, record memos).
- `explode_config.py`: explodes a config through `boms/` into leaf parts and counts part-number matches (`uv run --python 3.15 explode_config.py configs/rr-bollard-dual46.csv`). Writes `out/<config>_leaf_parts.csv`. `price_config.py` imports its explosion.
- `probe_names.py`: finds purchase lines for high-value parts by vendor and item name (`uv run --python 3.15 probe_names.py`). Writes `out/name_probe_lines.csv`. Used for the plan; unreviewed.

All scripts read `scratchpad/2026-11-13-bom-costs/out/cost_lines_20250101.csv`.
