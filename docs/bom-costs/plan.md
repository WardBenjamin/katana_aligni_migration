# BOM costs from Ramp: remaining scope

As of 2026-11-13 (UTC). Status: paused by Ben. Line-item cost record built for all Ramp spend by Ben, Monti and Chris; not matched to BOMs. What exists and how it was built: [../boms/cost-record.md](../boms/cost-record.md). Pull notes: [../boms/research/ramp.md](../boms/research/ramp.md), [../boms/research/ramp-receipt-extraction.md](../boms/research/ramp-receipt-extraction.md).

## Where it stands

Files in `scratchpad/2026-11-13-bom-costs/out/`, built by `build_cost_record.py --since <date>`:

| Window | Records | $ | Line rows | Flagged for review | No receipt | Receipt not itemized |
|---|---|---|---|---|---|---|
| 2026-05-13 on (`*_20260513.csv`) | 522 | 231,555.16 | 923 | 17 ($9.6k) | 112 ($10.7k) | 8 ($1.2k) |
| All, 2025-02 on (`*_20250101.csv`) | 1,608 | 600,200.04 | 2,979 | 97 ($26.5k) | 361 ($79.8k) | 45 ($21.7k) |

- The full-history total equals Ramp's spend report plus draft reimbursements, to the cent.
- All 14 bills are typed in from their invoices (`data/ramp/manual_lines.csv`).
- Part numbers are on 194 of 2,979 lines: 149 parsed from item names, 32 from typed invoices, 13 from receipt text.
- Vendor order numbers are on 127 records and the ByTechs ship-to flag on 66.
- Not committed: the receipt-text pass (step 3 below) stopped at 15 of 139 searches.

## Remaining work

In the order I'd do it. Steps 1 and 2 need your go-ahead (open decisions below).

1. **Itemize the large hardware records Ramp couldn't read.** 45 records ($21.7k) have a receipt that Ramp didn't itemize. Most of the value is three Digi-Key orders:
   - 2025-04-25, $8,826.45, Omron E3Z sensors
   - 2025-06-17, $4,256.51
   - 2025-08-09, $1,707.95

   The receipt files exist in Ramp but the connector can't return card receipt images. Source: open each transaction in the Ramp web app (Chrome) and read the receipt, or use Digi-Key order history. Done when each is itemized in `manual_lines.csv` with its source.

2. **Find receipts for hardware bought with no receipt.** There are 361 such records ($79.8k). The hardware vendors, which matter for BOM cost:

   | Vendor | Records | $ |
   |---|---|---|
   | Sixfab | 3 | 14.1k |
   | Sequent | 4 | 12.0k |
   | Ubiquiti | 19 | 8.7k |
   | Samsung | 2 | 5.9k |
   | JLCPCB | 14 | 2.6k |
   | Home Depot | 14 | 2.7k |
   | Amazon | 83 | 2.4k |
   | MISUMI | 2 | 2.2k |
   | Hubs | 4 | 1.7k |
   | Digi-Key | 14 | 1.2k |
   | McMaster | 13 | 0.7k |

   The rest is not BOM material: Pirate Ship labels $6.2k, ParkPow $6.1k, software and travel. Sources, in order: vendor order histories (Chrome, your sessions), order-confirmation emails, then asking whoever bought it. Done when hardware records over a threshold you pick are itemized or marked unrecoverable.

3. **Finish the receipt-text pass.** Ramp's receipt search returns the first ~2,000 characters of a receipt's text. That gives order numbers, ship-to, and Digi-Key, Mouser and McMaster part numbers. It only covers receipts uploaded since 2026-04-02; earlier ones are not in its index. 124 targeted searches are left in `data/ramp/raw/receipt_ocr/targeted_calls.json` (ids 15 to 138, ~170 part-relevant receipts). About two agent runs. Long orders still lose lines past the cut-off.

4. **Get part numbers for electronics lines.** 297 Digi-Key lines exist; most carry only a description ("RES 10K OHM 1% 1/10W 0603"). Matching to BOMs needs Digi-Key or manufacturer part numbers. Best source: Digi-Key and Mouser order-history exports, which list part numbers on every line. Step 3 covers only recent, short orders.

5. **Work the review queue.** 97 records ($26.5k) are flagged; their landed costs are proportional estimates. Causes:
   - Amazon receipts that cover a whole order when the charge is one shipment.
   - Tax or tariff missing from Ramp's extraction.
   - A few garbled extractions (Delta two × $565, an Amazon quantity of 733).

   Fix from receipt images or receipt text, or accept the estimates for non-hardware vendors.

6. **Link records that belong together.**
   - Powermatic freight bills ($62.33, $24.34) to the $21,185 sensor prepayment, via `vendor_order`.
   - The 8 partial refunds to their purchases. Home Depot −$59.28 and Turo −$750 are two of them.
   - Amazon orders split across charges.

   Needed so per-part landed cost includes freight and excludes refunds.

7. **Tag each line's spend type** (BOM material, tooling, consumables, shipping, software, travel) from vendor category, vendor and memo. The cost update can then filter to BOM material without reading every line. This is pre-filtering, not BOM matching.

8. **Verify independently.** An agent re-derives about 60 records (stratified by vendor and source) from the raw files and compares them with the outputs, plus 20 receipt images checked by eye. An outside-model review would need anonymized data, since receipts carry names and addresses.

9. **Then the cost update itself** (not started; out of scope until you say): match lines to BOM parts, pick the cost basis, roll up per assembly.

## Open decisions

1. May I use Chrome, with your signed-in sessions, to read Ramp receipt images and vendor order histories (Digi-Key, Mouser, JLCPCB, Sixfab, Sequent, Ubiquiti)? Which vendors, and is downloading their order-history exports OK?
2. For no-receipt spend: chase hardware only, above what dollar amount?
3. Cost basis for the update: last purchase, weighted average, or by quantity break? Should landed cost include tax and freight?
4. Window for the update: the last six months only, or everything since 2025-03?
5. FixturFab bank wire instructions PDF: keep local (gitignored now) or delete? The committed invoice PDFs also print vendor remittance details.

## Caveats

- Card receipt images aren't reachable through the Ramp connector; only Ramp's extraction and, since 2026-04-02, the first ~2,000 characters of text.
- Every record's landed lines sum to what was paid. Where the receipt and the charge disagree, the split is proportional and the record is flagged.
- Item names are vendor descriptions. Amazon names are often cut short; the full name is recovered from receipt text on 25 lines so far.
- Refunds are separate negative records. Only exact refunds are paired (3 of 11).
