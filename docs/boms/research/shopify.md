# Shopify products and SKUs

Pulled 2026-11-13T04:00Z through the Shopify MCP connector (store "AirGarage", domain 3pl.airgarage.com), query `productVariants(first: 100)`; one page, 67 variants. Saved to `scratchpad/2026-11-13-bom-reconciliation/data/shopify/variants_20261113T0400Z.csv` (transcribed from the tool output).

`repos/aligni-shopify-sync` (commit dcfc009) mirrors inventory between Aligni and Shopify for SKUs matching `SKU_INCLUDE_PATTERN`, default `*-Kit` (`README.md`). Aligni is the source of truth for stock.

## Findings

- All 18 Aligni kit SKUs exist in Shopify and are active: `AG-CS3-Kit`, 6 dual-camera kits, 9 single-camera kits, `AG-SEN2-RR-Kit`, `AG-SEN2-TB-Kit`. Also `AG-SEN2-002-000`, `AG-SEN2-003-001_EnclosureBase`, `AG-SEN2-003-002_EnclosureTop` (not `*-Kit`, so outside the default sync pattern), and `TEST-Kit`.
- The sensor bar kits sit under a product titled "V3.1 Sensor Bar Assembly"; Aligni calls them "vπ RR/TB Sensor Bar Kit". The 9 single-camera kits sit under "Single Camera - Reverse (Assembled)".
- `AG-SEN2-002-000` is titled "E39-R1S Reflector (with hood)"; Aligni's BOM for it uses `EXT-E39-R1` (Omron E39-R1, a different model from E39-R1S).
- Two install-pack SKUs look swapped or shifted: "Install Pack: Through Beam - Dual Camera (TB-IP-DC)" has SKU `RRWMIPDC`, and "Install Pack: Retro Reflective - Wall Mount - Dual Camera (RR-WM-IP-DC)" has SKU `RRBMIPDC`.
- Active hardware products with no SKU and no Aligni part: install packs RR-BM-IP-DC, RR-BM-IP-DCR, RR-WM-IP-DCR, TB-IP-DCR, v4-BM-IP-DC, v4-WM-IP-DCR; "v4 Sensor Bar Assembly"; "Aerial Camera Bundle"; "Aerial Camera Install Pack - Hose Clamps" and "- Screws"; "SIM card"; "E39-R1S Reflector (bare, without hood)"; "RJ12 Cable". Non-hardware active products (tickets, enforcer vests, starter pack) are out of scope.
- Many active variants have negative inventory, e.g. `AG-CS3-Kit` -67, RR-BM-IP-DC -72, enclosure base -55 and top -50, `AG-SEN2-002-000` -42. This matters for opening stock in Katana, not for BOMs.
- Archived products are V3.x (camera modules, compute stack, bare cameras, V4/Tall sensor enclosure, sensors).
