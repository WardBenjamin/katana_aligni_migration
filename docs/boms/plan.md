# BOMs: export and reconciliation plan

As of 2026-11-13 (UTC). Status: export done; reconciliation in progress.

## Goal

Get one trustworthy BOM per assembly before migrating from Aligni to Katana. Aligni is the starting point; anything missing or out of date there gets found by comparing it with every other place a BOM lives.

## Steps

1. Done. Export Aligni to `boms/` (one CSV per assembly, active revision; other revisions in `boms/revisions/`). Scripts: `scratchpad/2026-11-13-aligni-bom-export/`.
2. Pull the other sources into `scratchpad/2026-11-13-bom-reconciliation/data/<source>/`, read-only:
   - Notion BoM databases and BoM tables under Engineering Home / Tripwire Home (vπ, V4, V3.1, kits).
   - ECAD: KiCad schematics in `repos/tripwire-ecad` (BOMs from symbol fields; two committed BOM CSVs for the sensor board).
   - MCAD: part files per assembly in `repos/tripwire-mcad` (no BOM files; STEP names per release).
   - Shopify: products and SKUs; `aligni-shopify-sync` mirrors SKUs matching `*-Kit`.
3. Compare each source with Aligni, per assembly: missing assemblies, missing or extra lines, quantity differences, part-number and name mismatches.
4. Write `docs/boms/reconciliation.md`: one row per assembly with its status and the fix, plus the decisions that need a person.

## Column standard

`boms/*.csv` columns follow the Notion BoM databases (Part Name, Part Number, Part Number - Mfg, Supplier, Quantity Per Unit, Min Quantity Per Purchase, Cost, Cost Per Unit, Links, Notes), with Aligni fields Katana needs appended (Line, Manufacturer, Supplier Part Number, Unit, Designator, No Load, Part Type, Child Revision). Part numbers follow Aligni: `AG-<family>-<assembly>-<item>[_<suffix>]` for our parts, `EXT-<supplier or mfg PN>` for bought parts.

## Open decisions

- Is the Notion column set the "standard structure" meant, or is there another template? (Assumed Notion's.)
- Which source wins per assembly when they disagree (Aligni, Notion, CAD)?
- V4 / Obelisk and V3.1: migrate to Katana or leave out?
