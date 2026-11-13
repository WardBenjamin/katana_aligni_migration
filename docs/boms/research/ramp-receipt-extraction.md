# Ramp receipt extraction: faults found while building the cost record

2026-11-13 (UTC). Window 2026-05-13 onward, card receipts from `scratchpad/2026-11-13-bom-costs/data/ramp/raw/receipt_details/batch_*.json` (pulled 2026-11-13T04:0xZ). Checked by comparing each receipt's line sum with its subtotal and with the card charge (`build_cost_record.py` at this commit).

- 373 of 387 card transactions with receipts have a receipt whose total equals the charge within 2 cents. The other 14: Amazon partial shipments (charge below the order total), ULINE (receipt is a $145 product line without freight or tax), JetBlue and one Amazon order split across two charges, Ubiquiti, Apple, Turo.
- Split orders: Amazon 275.20 + 140.20 = receipt 415.40 (one charge on 2026-05-02, before the window); JetBlue 446.80 + 58.00 = 504.80. Both charges carry an identical receipt.
- "N of:" lines: Amazon receipts put the unit price in `item_total_price` when the line reads "4 of: ...". Example: Joyfay edge trim, qty 4, total 26.99, subtotal 107.96 = 4 × 26.99. Other Amazon receipts give the true line total (UGREEN adapter qty 2, total 9.44, subtotal 83.32). Which reading fits has to be decided per receipt against the subtotal.
- Repeated lists: Pirate Ship 14.81 lists its one label twice (29.62).
- Header and adder lines: FixturFab card receipt 1305.05 lists section headers "Materials" 475.99 and "Design" 788.01 above the detail lines that make up the 1264.00 subtotal. Mouser and Digi-Key list "Tariff" as qty-less lines that are also in `fees`, or that are the only record of the tariff.
- Negative lines: Pirate Ship lists label batches as negative amounts on positive charges (11 records).
- Zero lines: Digi-Key 3536.56 has a 1000 × 0.82701 line with total 0.00 (backordered, not charged).
- Discounts: `discounts` is listed whether or not line prices already include it (Hologram 3875.60, Sequent 250.00, 18650 Battery Store 816.00 are already in the line prices).
- Missing tax: many Amazon receipts extract no tax, so the charge exceeds lines plus stated adders.
- No prices: OSH Stencils 278.65 lists 5 items with no prices; its OCR (`ramp_search_receipts`, saved in `raw/receipt_ocr/`) has SKUs but only the order total.
- Unreadable: Home Depot reimbursement 440.05 (receipt 52e8cf45) has no extraction; read from the image instead.
