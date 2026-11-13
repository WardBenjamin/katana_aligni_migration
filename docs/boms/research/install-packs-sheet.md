# Install pack BOMs (Google Sheet)

Sheet "Install Packs", https://docs.google.com/spreadsheets/d/1Qsc5gxIf8g-M4u9SausMnXMgNn1OOJiesQ50L1Hw7uI (link from Ben, 2026-11-13). Read 2026-11-13T05:10Z in Chrome through the sheet's `gviz/tq?tqx=out:html` view, read-only. Purchase links were cut to their hostname (`link:<host>`) because the browser tool blocks URLs with query strings; the sheet has the full links.

Tabs: `SKUs`, `40 unit costs`, `First ORDER / 40 units`, `v3.14 Dual Camera`, `v3.14 Dual Camera + Reverse`. Saved: `SKUs` and the two `v3.14` tabs to `scratchpad/2026-11-13-bom-reconciliation/data/sheets/install-packs_*.csv`. Not saved: the two cost and order tabs (purchase quantities and prices for a 40-unit first order, same 13 parts).

## Findings

- `SKUs` is the install-pack BOM: 13 consumables and fasteners (wipes, padlocks, tape, Lexel glue, RJ12 connectors, IPEX junction boxes 12x12x6 and 8x8x4, conduit straps, M6 nylock nuts, Tapcon 1/4" and 5/8", Topaz rain-tight connectors, custom SendCutSend washers) across six packs: RR-BM-IP-DC, RR-WM-IP-DC, TB-IP-DC and the reverse-camera variants RR-BM-IP-DCR, RR-WM-IP-DCR, TB-IP-DCR. Per-pack totals 76, 60, 102, 88, 72, 114 items; the transcribed quantities sum to these totals.
- No part numbers: parts are named and linked to retail pages (Home Depot, Amazon, Gordon Electric, Fasteners Plus). Washers are "SendCutSend Custom - Monti to assist"; MCAD has `Installer Kits/Bollard Washers/Bollard Washer.step`.
- SKU codes are written two ways in one header row: `RR-BM-IP-DC` and `RRWMIPDC`, `TBIPDC`, `RRIPDC`. Shopify assigns `RRWMIPDC` to the TB-IP-DC product and `RRBMIPDC` to RR-WM-IP-DC (`data/shopify/variants_20261113T0400Z.csv`), so the Shopify SKUs are shifted by one product against this sheet; the other four packs have no Shopify SKU.
- The tabs are labelled "v3.14". No v4 pack (Shopify has v4-BM-IP-DC and v4-WM-IP-DCR) is in this sheet; Notion's "V4 Sensor Kit BoM" (`data/notion/v4-sensor-install-kit.csv`) has 8 rows with no part numbers.
- None of these packs or parts exist in Aligni.
