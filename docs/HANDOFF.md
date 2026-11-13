# Handoff

As of 2026-11-13 (UTC).

## Goal

Move hardware MRP from Aligni to [Katana](https://katanamrp.com/). Katana was chosen over Odoo; contract signed 2026-11-03; last Aligni bill paid 2026-11-10 (Slack #tripwire-leadership). A 2026-10-27 Katana call set phase 1 as importing items, ingredients and BOMs from CSV templates.

Order of work:

1. Export every BOM from Aligni to `boms/`, one CSV per assembly in our standard structure. Done.
2. Reconcile missing and outdated BOMs across Aligni, the MCAD and ECAD repos, Notion, Shopify, Slack and the install-pack sheet. Done; decisions open.
3. Migrate everything from Aligni into Katana. Not started.

## Status

- `boms/`: 30 active Aligni BOMs (one CSV per assembly, named by part number), 5 older or draft revisions in `boms/revisions/`, and `boms/index.csv`. Columns follow the Notion BoM databases plus the Aligni fields Katana needs. Scripts and the raw snapshot (2026-11-13T03:25Z): `scratchpad/2026-11-13-aligni-bom-export/`.
- Reconciliation: [boms/reconciliation.md](boms/reconciliation.md). Every source, with where and how it was read: [boms/data-sources.md](boms/data-sources.md). Plan: [boms/plan.md](boms/plan.md).
- Headline findings: Aligni and Notion agree on 140 of 154 lines. The compute stack BOM in both lacks the Party HAT, both bridges and several smaller parts. PCBAs, all V4 hardware and the install packs have no Aligni BOM. The authoritative install-pack BOM is ByTechs' sheet (`1zJsQbjP5G1RWWix71tEEHoSLD9x1BxvTSdU-K7LZTec`), not Anthony's earlier one. Six decisions are listed at the end of `reconciliation.md`.
- Ramp purchase records for Ben, Monti and Chris are pulled for a per-item as-purchased cost update (2026-11-13T04:40Z): 1,437 card transactions with memos, 1,346 receipts with line items, 160 reimbursements with receipt files, 14 bills with invoice files. Data and CSVs: `scratchpad/2026-11-13-bom-costs/`. Notes: [boms/research/ramp.md](boms/research/ramp.md). Bills have no line items in Ramp; card receipt images are not reachable through the connector.

## Next

1. Get answers to the decisions in `reconciliation.md` (reflector part and count, compute-stack antennas, install-pack base plus add-on structure, V4 install packs, part numbers for PCBAs, install packs and V4, scope for V3.1 and Obelisk).
2. Apply the fixes to a corrected BOM set in the workspace (not to Aligni), adding BOMs for the missing items from KiCad, Notion and the install-pack sheet.
3. Convert to Katana's BOM import template and plan the import.
4. Build the per-item cost update from `scratchpad/2026-11-13-bom-costs/data/ramp/receipt_lines.csv`: de-duplicate repeat receipts per transaction, split tax, shipping and fees, and match items to BOM lines. Bill prices come from the invoice PDFs.

## Open items

- Aligni is likely ending; the snapshot above may be the last full pull. Re-run `pull.py` (about 9 requests) before access ends if Aligni changes.
- Unconfirmed: whether Ben meant the Notion column set as the "standard structure", or Katana's import template. Part numbers follow Aligni (`AG-...`, `EXT-...`, `-Kit`) with an `_X<n>` revision tag on CAD files (Ben, 2026-09-21).
- `repos/` now has `tripwire-ecad`, `tripwire-mcad` and `aligni-shopify-sync` as submodules. `repos/aligni-mcp-server` is still a plain copy with no git history, so it is gitignored.
- `aligni` MCP server: connects and reads live data (checked 2026-11-13T03:18Z). Its `get_bom` tool queries `subparts`, which is not in Aligni's schema; the field is `PartRevision.bomItems`. `mcp__aligni__run_graphql` can run mutations and has no `ask` rule in `.claude/settings.json`.
- Aligni API: 10 requests/min, 1 concurrent, 10,000 complexity per request. Cloudflare rejects Python's default User-Agent (error 1010).
- The Mac's data volume filled up during the MCAD clone on 2026-11-13; Ben freed space (90 GB free afterwards).
- `tripwire-ecad` PR #27 (interposer layout, HW-892) and PR #28 (compute-stack bollard interface, HW-975) are open. Notion's X4A interposer values are in no branch.
