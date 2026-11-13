# BOMs: export and reconciliation plan

As of 2026-11-13 (UTC). Status: steps 1 to 5 done and part numbers confirmed; next is filling placeholders (step 6).

## Goal

Get one trustworthy BOM per assembly before migrating from Aligni to Katana. Aligni is the starting point; anything missing or out of date there gets found by comparing it with every other place a BOM lives.

## Steps

1. Done. Export Aligni (one CSV per assembly, active revision; other revisions in `revisions/`), now in `boms/aligni-20261113T0325Z/`. Scripts: `scratchpad/2026-11-13-aligni-bom-export/`.
2. Done. Pull the other sources into `scratchpad/2026-11-13-bom-reconciliation/data/<source>/`, read-only:
   - Notion BoM databases and BoM tables under Engineering Home / Tripwire Home (vπ, V4, V3.1, kits).
   - ECAD: KiCad schematics in `repos/tripwire-ecad` (BOMs from symbol fields; two committed BOM CSVs for the sensor board).
   - MCAD: part files per assembly in `repos/tripwire-mcad` (no BOM files; STEP names per release).
   - Shopify: products and SKUs; `aligni-shopify-sync` mirrors SKUs matching `*-Kit`.
3. Done. Compare each source with Aligni, per assembly: missing assemblies, missing or extra lines, quantity differences, part-number and name mismatches.
4. Done. Write `docs/boms/reconciliation.md`: one row per assembly with its status and the fix, plus the decisions that need a person.

## Column standard

`boms/*.csv` columns follow the Notion BoM databases (Part Name, Part Number, Part Number - Mfg, Supplier, Quantity Per Unit, Min Quantity Per Purchase, Cost, Cost Per Unit, Links, Notes), with Aligni fields Katana needs appended (Line, Manufacturer, Supplier Part Number, Unit, Designator, No Load, Part Type, Child Revision). Part numbers follow Aligni: `AG-<family>-<assembly>-<item>[_<suffix>]` for our parts, `EXT-<supplier or mfg PN>` for bought parts.

## Open decisions

- Is the Notion column set the "standard structure" meant for the CSVs, or is it Katana's BOM import template? (Assumed Notion's columns with Aligni part numbers.)
- Which source wins per assembly when they disagree (Aligni, Notion, CAD)?
- V4 / Obelisk and V3.1: migrate to Katana or leave out?

## Next

5. Done 2026-11-13. Decisions settled by Ben and applied in a corrected BOM set (`boms/`, `build_boms.py`), with BOMs added for the PCBAs, install packs, V4 sensor and V4 packs, V3.1 (legacy) and Obelisk (draft). Part numbers proposed in `part-numbers.md`.
6. Part numbers confirmed (Ben, 2026-11-13). Fill the `EXT-TBD-*` lines (ByTechs for cables and fasteners, Monti for V4 X5) and work through `review-later.md`.
7. Convert `boms/` and `boms/items.csv` to Katana's item and BOM import templates.
