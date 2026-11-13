# Haig invoice 98534: sensor enclosure

Written 2026-11-13T17:23Z. Ben put `Inv.98534.pdf` in `scratchpad/` on 2026-11-13. It is now `scratchpad/2026-11-13-vpi-assembly-price/data/invoices/haig/Inv.98534.pdf`. One page, read with `pdftotext -layout`.

Haig Precision Mfg. Corp. invoice 98534, dated 23-Apr-26, bill to AirGarage, ship to ByTechs (will call), packing list 136733, shipped 23-Apr-26.

| Line | Description | Qty | Unit | Amount | Landed each |
|---|---|---|---|---|---|
| 1 | SENSOR ENCLOSURE ASSY V5, Cardinal Orange T009-OG26 (job 42088D) | 150 | $79.73 | $11,959.50 | $87.70 |
| 2 | SENSOR ENCLOSURE BASE V5 (job 42088E) | 150 | $33.71 | $5,056.50 | $37.08 |

Sub-total $17,016.00; Santa Clara Co. sales tax $1,701.60 (10.0%); invoice total $18,717.60; amount paid $0.00 on the invoice as printed.

- Line 1 is `AG-SEN2-003-002_EnclosureTop`, whose item name in `boms/items.csv` is "SENSOR ENCLOSURE ASSY V5 CARDINAL ORANGE T009-OG26". Line 2 is `AG-SEN2-003-001_EnclosureBase`, "SENSOR ENCLOSURE BASE V5".
- Landed cost spreads the sales tax by line total: one top plus one base is $124.78.
- No freight on the invoice. The parts went from San Jose to ByTechs in South Carolina by will call, so any freight was paid elsewhere and is not in this figure.
- The invoice is dated before 2026-05-14, so the roll-up marks both rows stale.

Effect on the roll-up (`uv run --python 3.15 price_config.py configs/rr-bollard-dual46.csv --as-of 2026-11-13`, result `out/rr-bollard-dual46_price_lines.csv`): priced $1,918.73 (was $1,793.95), of which $1,007.45 on prices inside six months and $911.28 on older ones; 73 of 124 leaf parts priced; 52 part rows and 12 labour rows unpriced.
