# Handoff

As of 2026-11-13 (UTC).

## Goal

Move hardware MRP from Aligni to [Katana](https://katanamrp.com/). Katana was chosen over Odoo; contract signed 2026-11-03; last Aligni bill paid 2026-11-10 (Slack #tripwire-leadership). A 2026-10-27 Katana call set phase 1 as importing items, ingredients and BOMs from CSV templates.

Order of work:

1. Export every BOM from Aligni to `boms/`, one CSV per assembly in our standard structure. Done.
2. Reconcile missing and outdated BOMs across Aligni, the MCAD and ECAD repos, Notion, Shopify, Slack and the install-pack sheet. Done.
3. Build a corrected BOM set with Ben's decisions applied. Done 2026-11-13; part numbers confirmed, placeholders open.
4. Migrate into Katana. Not started.

## Status

- `boms/`: the corrected BOM set, built by `scratchpad/2026-11-13-bom-reconciliation/build_boms.py`. 52 BOMs in Katana scope (vπ, PCBAs, install packs as base set plus add-on, V4 sensor and V4 packs), `legacy-v3.1/` (cleaned, not migrated), `obelisk/` (draft skeleton, not migrated), `index.csv` (scope, source, change, open lines per BOM) and `items.csv` (item master, 277 items, with source and renames).
- `boms/aligni-20261113T0325Z/`: the untouched Aligni export (30 active BOMs, 5 older revisions). Raw snapshot and scripts: `scratchpad/2026-11-13-aligni-bom-export/`.
- Docs: [boms/reconciliation.md](boms/reconciliation.md) (findings and Ben's decisions), [boms/part-numbers.md](boms/part-numbers.md) (confirmed numbers, renumbering, placeholders), [boms/review-later.md](boms/review-later.md) (deferred items), [boms/data-sources.md](boms/data-sources.md) (every source), [boms/plan.md](boms/plan.md).
- Decisions (Ben, 2026-11-13): 4x E39-R1S per RR kit; PCBAs as sub-assemblies; production keeps the I425-GL modem and both current antennas; install packs are base set plus add-on; V4 install packs are real SKUs; V3.1 not migrated but cleaned; V4 sensors migrated; Obelisk not migrated. The authoritative install-pack BOM is ByTechs' sheet (`1zJsQbjP5G1RWWix71tEEHoSLD9x1BxvTSdU-K7LZTec`).
- BOM costs (separate workstream, paused 2026-11-13 by Ben): line-item as-purchased cost record from Ramp for Ben, Monti and Chris, all history (1,608 records, $600,200.04, 2,979 line rows) and last six months. Not matched to BOMs. Method: [boms/cost-record.md](boms/cost-record.md). Remaining scope and open decisions: [bom-costs/plan.md](bom-costs/plan.md). Data and scripts: `scratchpad/2026-11-13-bom-costs/`.
- vπ full assembly price (proposed 2026-11-13, not started): plan in [assembly-price/plan.md](assembly-price/plan.md) for the current landed cost of one complete unit, first configuration RR sensor bar, bollard mount, dual camera. First pass: 124 leaf parts, 29 matched to Ramp by part number; no ELP camera, Haig enclosure or post-2025-08 ByTechs purchases in the Ramp pull. Scripts: `scratchpad/2026-11-13-vpi-assembly-price/`.

## Next

1. Part numbers confirmed by Ben 2026-11-13. Deferred items for later review: [boms/review-later.md](boms/review-later.md).
2. Fill the 39 open lines (`EXT-TBD-*` and blank quantities): ByTechs for cables, Tapcons and connectors; Monti for the V4 X5 BoM and the V4 install kit.
3. Convert `boms/` and `boms/items.csv` to Katana's item and BOM import templates; plan opening stock (renamed parts carry stock from their Aligni numbers).
4. BOM costs: get Ben's answers to the open decisions in `bom-costs/plan.md` (browser access to Ramp receipt images and vendor order histories, cost basis, window), then work its steps in order.
5. Assembly price: get Ben's answers to the six open decisions in `assembly-price/plan.md` (what "price" covers, bollard model, lens pair, cost basis, where ByTechs and Haig invoices are, browser access), then work its steps in order.

## Open items

- Aligni is likely ending; the snapshot above may be the last full pull. Re-run `pull.py` (about 9 requests) before access ends if Aligni changes.
- Unconfirmed: whether Ben meant the Notion column set as the "standard structure", or Katana's import template. Part numbers follow Aligni (`AG-...`, `EXT-...`, `-Kit`) with an `_X<n>` revision tag on CAD files (Ben, 2026-09-21).
- Rerunning `build_boms.py` deletes and rewrites the CSVs in `boms/`, `boms/legacy-v3.1/` and `boms/obelisk/`; edit the script, not the CSVs.
- `repos/` now has `tripwire-ecad`, `tripwire-mcad` and `aligni-shopify-sync` as submodules. `repos/aligni-mcp-server` is still a plain copy with no git history, so it is gitignored.
- `aligni` MCP server: connects and reads live data (checked 2026-11-13T03:18Z). Its `get_bom` tool queries `subparts`, which is not in Aligni's schema; the field is `PartRevision.bomItems`. `mcp__aligni__run_graphql` can run mutations and has no `ask` rule in `.claude/settings.json`.
- Aligni API: 10 requests/min, 1 concurrent, 10,000 complexity per request. Cloudflare rejects Python's default User-Agent (error 1010).
- The Mac's data volume filled up during the MCAD clone on 2026-11-13; Ben freed space (90 GB free afterwards).
- `tripwire-ecad` PR #27 (interposer layout, HW-892) and PR #28 (compute-stack bollard interface, HW-975) are open. Notion's X4A interposer values are in no branch.
