# Install pack BOM from ByTechs (authoritative)

Sheet "ByTechs - AirGarage Install Packs", https://docs.google.com/spreadsheets/d/1zJsQbjP5G1RWWix71tEEHoSLD9x1BxvTSdU-K7LZTec, one tab `SKUs`. Ben, 2026-11-13: "the authoritative install pack BOM forwarded by the contract manufacturer". Read 2026-11-13T05:40Z in Chrome through `gviz/tq?tqx=out:html&sheet=SKUs`, read-only; links cut to hostname. Saved to `scratchpad/2026-11-13-bom-reconciliation/data/sheets/bytechs-install-packs_SKUs.csv`. Column sums match the sheet's totals.

## Findings

- Structure differs from Anthony's "Install Packs" sheet ([install-packs-sheet.md](install-packs-sheet.md)): column `RRWMIPDC` is the "BASE SET TO PACK" (54 items) and the other five SKUs are "ADD ON KIT" columns with incremental quantities: RRBMIPDC 16, TBIPDC 39, RRBMIPDCR 29, RRWMIPDCR 13, TBIPDCR 51. The sheet does not say whether a full RR-BM pack is base plus add-on; the add-on contents (bollard tapcons and washers for RRBM; padlocks, junction box, straps, tapcons, connectors for TB) suggest so.
- Footnote: "Nylocks, 3/4 Plugs, and Nylon pegs are now packed with sensor bar kits." The M6 nylock, "Enclosure Pegs" and "Enclosure 3/4" Caps" rows have no quantity in any pack. These are the enclosure pins (Essentra 27PIF0089) and 3/4 in knock-out seals that Monti said were missing from Aligni (Slack 2026-05-28).
- New items not in Anthony's sheet: 13 gal trash bag (1), microfiber cloth (1), both in the base set only.
- Sizes changed in the first block only: "3/4" one hole straps" (Amazon) and "Topaz 3/4" Rain Tight Connector", where the reverse-camera block still says 1/2". EZ-RJ12/11 connectors and the 8x8x4 junction box have no quantity in the base set.
- The trailing `RR` and `TB` columns (totals 88 and 114) are unchanged from Anthony's sheet and do not match the new layout.
- SKU codes are hyphen-free (`RRBMIPDC`, `RRWMIPDC`, `TBIPDC`, `RRBMIPDCR`, `RRWMIPDCR`, `TBIPDCR`). Shopify has `RRWMIPDC` on the TB-IP-DC product and `RRBMIPDC` on RR-WM-IP-DC; the other four have no Shopify SKU.
- No V4 pack and no part numbers.
