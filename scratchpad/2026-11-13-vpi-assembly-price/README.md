# vπ full assembly price

Goal: the current landed cost of one complete vπ unit, per configuration. Plan: `docs/assembly-price/plan.md`.

Status: first pass only, 2026-11-13. The configuration is exploded to leaf parts and probed against the Ramp cost record. Nothing is priced yet. Nothing promoted.

## Contents

- `configs/rr-bollard-dual46.csv`: the first configuration (top-level part numbers and quantities). Two lines are assumptions: lens pair and mount shape, and the bollard model.
- `explode_config.py`: explodes a config through `boms/` into leaf parts and counts part-number matches in the all-history Ramp cost lines (`uv run --python 3.15 explode_config.py configs/rr-bollard-dual46.csv`). Writes `out/<config>_leaf_parts.csv`. The match is a substring test, for coverage only.
- `probe_names.py`: finds purchase lines for high-value parts by vendor and item name (`uv run --python 3.15 probe_names.py`). Writes `out/name_probe_lines.csv`. Unreviewed.

Both scripts read `scratchpad/2026-11-13-bom-costs/out/cost_lines_20250101.csv`.
