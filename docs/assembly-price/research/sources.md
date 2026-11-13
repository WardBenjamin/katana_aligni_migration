# Sources opened

- `boms/index.csv`, `boms/items.csv` and the BOM CSVs for this configuration (`AG-CS3-Kit`, `AG-CS3-001-000`, `AG-SEN2-RR-Kit`, `AG-SEN2-001-000`, `AG-SEN2-002-000`, `AG-SEN2-003-000`, `AG-Dual46-RoundBollard-Kit`, `AG-Dual68-RoundBollard-Kit`, `AG-Dual46-SquareBollard-Kit`, `AG-PIC-001-000_Dual46`, `AG-PIC-003-000`, `AG-PIC-004-000`, `AG-IP-RRBM-DC-Kit`, `AG-IP-001-000`, `AG-IP-002-000`) at commit `07b3beb` — read 2026-11-13
- `scratchpad/2026-11-13-bom-costs/out/cost_lines_20250101.csv` and `cost_records_20250101.csv` at commit `c1bbad6` — read 2026-11-13
- `scratchpad/2026-11-13-bom-costs/README.md`, `docs/bom-costs/plan.md`, `docs/boms/cost-record.md` — read 2026-11-13
- `docs/boms/research/notion-boms.md` (PIC-003/PIC-004 paragraph, V4 page paragraph, "Hardware Stock tables" bullet), `docs/boms/research/shopify.md` — read 2026-11-13
- `scratchpad/2026-11-13-bom-reconciliation/data/shopify/variants_20261113T0400Z.csv` — read 2026-11-13
- `repos/tripwire-mcad` at `033bdfb`: list of `.3mf` files; `Metadata/slice_info.config` in `vπ-release/cameras/bollard-mount-camera/Bambu Print Plates/Round Bollard Dual Cam Plate (ASA - 0.4mm).3mf` — read 2026-11-13
- Web search "Uline H-2118F safety bollard 4 1/2 x 36"; result title and summary for https://uline.com/Product/Detail/H-2118F/Safety-Guards-Barriers/Standard-Safety-Bollard-45-x-36-Fixed (page itself not opened) — 2026-11-13
- Shopify Admin GraphQL (read-only) for six product variants' price and unit cost: HTTP 500 twice, no data — 2026-11-13
- Uline product page for H-2118F, fetched with the web-fetch agent (HTTP 200): price, weight, shipping method https://www.uline.com/Product/Detail/H-2118F/Safety-Guards-Barriers/Standard-Safety-Bollard-45-x-36-Fixed — read 2026-11-13
- `scratchpad/2026-11-13-bom-reconciliation/build_boms.py` (item definitions and how `boms/items.csv` is written) — read 2026-11-13
- `scratchpad/2026-11-13-vpi-assembly-price/data/invoices/bytechs/pdf/`: 25 Bytechs LLC invoices issued through Deel (text of all 25 for task lines and totals; the last five and INV-2025-1, -3, -4, -5, -6, -7 and INV-nd68x8z-2026-1 in full) and one of 9 Deel fee invoices — read 2026-11-13
- `scratchpad/2026-11-13-vpi-assembly-price/data/invoices/pcb/invoice-5.pdf`, `invoice-6.pdf`, `invoice-7.pdf`: JLCPCB invoices, read by eye (no text layer) — read 2026-11-13
- `scratchpad/2026-11-13-vpi-assembly-price/data/invoices/powermatic/OrdAck1426189.pdf`: Powermatic order acknowledgement 1426189, 1 page — read 2026-11-13
- `scratchpad/2026-11-13-bom-costs/data/ramp/manual_lines.csv` (Powermatic rows) and the Powermatic rows of `cost_records_20250101.csv` and `cost_lines_20250101.csv` — read 2026-11-13
- `scratchpad/2026-11-13-vpi-assembly-price/data/invoices/elp/Ailipu PI NO.ELPFP2026012704C-1.pdf` and `Ailipu PI NO.ELPFP2026011501C-1.pdf`: Shenzhen Ailipu proforma invoices — read 2026-11-13
- `scratchpad/2026-11-13-vpi-assembly-price/data/invoices/haig/Inv.98995.pdf`: Haig Precision invoice 98995 — read 2026-11-13
- `scratchpad/2026-11-13-vpi-assembly-price/data/invoices/makerbright/Invoice_1381.pdf`: MakerBright invoice 1381 — read 2026-11-13
- `boms/AG-PIC-005-000.csv` and the ELP rows of `boms/items.csv` — read 2026-11-13

## camera-tariffs (read 2026-11-13)
- https://airgarage.slack.com/archives/C09FF4GLH9R/p1775837057811809 (#airgarage-bytechs, 2026-04-10T16:04Z, cameras shipped, UPS tracking; thread ts 1775836387.012279 read in full, 2026-04-15 to 2026-04-23 replies)
- https://airgarage.slack.com/archives/C08EUD1T2US/p1771615984347319 (group DM, 2026-02-20T19:33Z, ELP order tariffs not yet paid; surrounding messages read)
- https://airgarage.slack.com/archives/C08EUD1T2US/p1776295590373499 (group DM, 2026-04-15T23:26Z, "last tariff bill on the cameras like $35K")
- Slack search results (concise) for "tariff", "ELP", "duties", "customs", "UPS" Jan-Jul 2026; DM Ben Ward / Chris Williamson 2026-06-05T15:43Z (57.5% cable tariff)
- Ramp connector: ramp_search_vendors (Ailipu, ELP, DHL Express, FedEx, UPS), ramp_search_bills ("Ailipu"), ramp_get_transactions (duty text; UPS 2026-03-25..06-01; amount > $20,000 2026-01-20..04-15). No match.
- scratchpad/2026-11-13-bom-costs/out/cost_records_20250101.csv (filtered Jan-Aug 2026: DHL duties $176.59 on 2026-03-31 and 2026-06-11 only)
- https://hts.usitc.gov/reststop/search?keyword=8525.89 , keyword=9903.03 , keyword=9903.88.03 (saved data/tariffs/hts_*.json)
- https://hts.usitc.gov/reststop/file?release=currentRelease&filename=Chapter%2099 (HTS Revision 23 (2026) ch. 99, saved data/tariffs/hts_ch99.pdf, ch99.txt)
- https://www.whitehouse.gov/presidential-actions/2026/02/imposing-a-temporary-import-surcharge-to-address-fundamental-international-payments-problems/ (saved data/tariffs/s122_proclamation.html)
- https://www.federalregister.gov/documents/2026/02/25/2026-03824/imposing-a-temporary-import-surcharge-to-address-fundamental-international-payments-problems (data/tariffs/fr_2026-03824.xml; annex tables not in the XML)
- https://www.federalregister.gov/documents/2026/02/25/2026-03832/ending-certain-tariff-actions (EO 14389; data/tariffs/fr_2026-03832.xml)
- https://rulings.cbp.gov/ruling/H332743 and /H331315 (via rulings.cbp.gov/api/ruling/<id>, data/tariffs/r_*.json)
- https://www.federalregister.gov/documents/2025/07/23/2025-13869/customs-user-fees-to-be-adjusted-for-inflation-in-fiscal-year-2026-cbp-dec-25-10 (MPF FY2026, from search snippet only, not opened)
- Web searches (pointers only, not cited as authority): flexport, wiley, bakerdonelson, freshfields Section 122 summaries; customsmobile NY N018295

## camera-tariffs-review (read 2026-11-13)
- `data/tariffs/hts_8525.89.json`, `hts_9903.88.03.json`, `hts_9903.03.json`, `ch99.txt`, `s122_proclamation.txt` under `scratchpad/2026-11-13-vpi-assembly-price/` (the agent's saved copies)
- Slack thread C09FF4GLH9R, parent ts 1775836387.012279, via `slack_read_thread`
