# BOM data sources

As of 2026-11-13 (UTC). Every place a hardware BOM, or a decision about one, lives. Snapshots are under `scratchpad/2026-11-13-bom-reconciliation/data/` unless noted; research notes are in `research/`.

| Source | Where | Access used | What it holds | Snapshot | Notes |
|---|---|---|---|---|---|
| Aligni | `<org>.aligni.com`, GraphQL API v3 | API token in `.env`, read-only; 10 req/min | System of record being replaced: 105 parts, 112 revisions, 36 BOM revisions (vπ only) | `scratchpad/2026-11-13-aligni-bom-export/data/20261113T0325Z/`; CSVs in `boms/` | [research/aligni.md](research/aligni.md) |
| Notion | Tripwire Home, https://app.notion.com/p/0afdeb167ec24c0a82661e860449cfa0 | Notion connector, read-only | Per-assembly BoM databases for vπ, V3.1, V4 (X1, X2, X3B, X4B/V4A), V4 sensor install kit, X4A interposer PCB; Engineering Change Notices page | `data/notion/` (34 CSVs, `manifest.csv`) | All BoMs are under Tripwire Home (Ben). [research/notion-boms.md](research/notion-boms.md) |
| Google Sheet "Install Packs" | https://docs.google.com/spreadsheets/d/1Qsc5gxIf8g-M4u9SausMnXMgNn1OOJiesQ50L1Hw7uI | Chrome, read-only HTML view | Install-pack BOMs for 6 v3.14 packs (RR/TB, bollard/wall, with and without reverse camera) | `data/sheets/` | Links cut to hostname. [research/install-packs-sheet.md](research/install-packs-sheet.md) |
| ECAD | GitHub `airgarage/tripwire-ecad`, submodule `repos/tripwire-ecad` | git, read-only | KiCad schematics: Party HAT X5C, USB-A bridge, modem bridge, sensor bar I/O breakout X2, bollard interposer, sensor boards rev1/rev2; open PRs #27 (interposer) and #28 (compute stack bollard interface) | `data/ecad/` | [research/ecad-boms.md](research/ecad-boms.md), [research/ecad-open-prs.md](research/ecad-open-prs.md) |
| MCAD | GitHub `airgarage/tripwire-mcad`, submodule `repos/tripwire-mcad` | git, read-only | STEP, 3MF and PDF per release (V3.1, vπ, V4 X1 to X5, installer kits); no BOM files | `data/mcad/files_at_HEAD.txt` | [research/mcad.md](research/mcad.md) |
| OnShape | vπ camera assembly document, linked from Notion "vπ Camera" | Not read | Native CAD for the camera; may carry assembly BOMs | none | Not accessed. |
| Shopify | Store "AirGarage", 3pl.airgarage.com | Shopify connector, read-only | Kit SKUs (mirror Aligni `-Kit` part numbers), install packs, v4 products, inventory | `data/shopify/variants_20261113T0400Z.csv` | [research/shopify.md](research/shopify.md) |
| aligni-shopify-sync | GitHub `airgarage/aligni-shopify-sync`, submodule `repos/aligni-shopify-sync` | git, read-only | Inventory sync Aligni ↔ Shopify for SKUs matching `*-Kit` | none | Deployed on Render (not read). |
| Slack | #airgarage-bytechs, #airgarage-bytechs-hardware-chat, #pt-tripwire, #pt-obelisk, #pt-v4-sensors, #airgarage-bytechs-tripleb-v4-hardware | Slack connector, read-only | Discussion and decisions: BOM changes, builds and POs with ByTechs, TripleB, V4 | `data/slack/` | [research/slack.md](research/slack.md) |
| Katana | katanamrp.com | Not accessed | Target system; BOM import by CSV template | none | 2026-10-27 call: phase 1 imports items, ingredients and BOMs. |

## Mentioned but not found

- A Party HAT BoM "on Josiah's hard drive" and an install-kit BoM "managed by Anthony" (Notion meeting note 2026-04-07, outside Tripwire Home). The install-kit BoM is the Google Sheet above. The Party HAT BoM can be regenerated from `tripwire-ecad` (`data/ecad/party-hat.csv`).
- V3 Materials Inventory (Google Sheet linked from Tripwire Home, v3.0 section): retired generation, not read.
- Attachment `bollard-hybrid-cable.bom.tsv` on Notion "V4 X4B Assembly SOP and BoM": not downloaded.
