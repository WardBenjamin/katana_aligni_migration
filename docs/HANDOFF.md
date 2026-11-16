# Handoff

As of 2026-11-16 (UTC).

## Goal

Move hardware MRP from Aligni to [Katana](https://katanamrp.com/). Katana was chosen over Odoo; contract signed 2026-11-03; last Aligni bill paid 2026-11-10 (Slack #tripwire-leadership). A 2026-10-27 Katana call set phase 1 as importing items, ingredients and BOMs from Katana's CSV templates. #temp-katana-onboarding (opened 2026-11-12 by Britney, for HOps, Eng and ByTechs) had no content when last read.

| Step | State |
|---|---|
| 1. Export every Aligni BOM, one CSV per assembly | Done 2026-11-13 |
| 2. Reconcile against MCAD, ECAD, Notion, Shopify, Slack, install-pack sheets | Done 2026-11-13 |
| 3. Corrected BOM set with Ben's decisions; part numbers confirmed | Done 2026-11-13 |
| 4. Close loose ends (placeholders, deferred reviews, data not yet pulled) | Open, below |
| 5. Convert to Katana's templates and import | Not started, below |

## Start here (next session)

1. Read `CLAUDE.md`, then this file, then [boms/part-numbers.md](boms/part-numbers.md) and [boms/review-later.md](boms/review-later.md).
2. The BOM set is generated. Change `scratchpad/2026-11-13-bom-reconciliation/build_boms.py`, never the CSVs, then rebuild: `uv run --python 3.15 build_boms.py` from that folder. A rebuild deletes and rewrites `boms/*.csv`, `boms/legacy-v3.1/` and `boms/obelisk/`; it never touches `boms/aligni-20261113T0325Z/`.
3. Other sessions write in this workspace at the same time. Commit only paths you changed (`git add <paths>`), never `git add -A`. Untracked files under `scratchpad/2026-11-13-bom-costs/out/` belong to the BOM-costs workstream.

## What exists

- `boms/`: corrected BOM set. 52 BOMs in Katana scope (vπ assemblies and kits, PCBAs, install packs as base set plus add-on, V4 sensor and V4 packs), `legacy-v3.1/` (2, cleaned, not migrated), `obelisk/` (2, draft skeleton, not migrated).
  - `boms/index.csv`: one row per BOM with revision, scope, line count, open lines, source and what changed.
  - `boms/items.csv`: item master, 277 items, with source, use count and `Renamed From`. Katana scope uses 227 of them: 52 assemblies and 175 leaf parts.
  - Columns per BOM: the Notion BoM layout (Part Name, Part Number, Part Number - Mfg, Supplier, Quantity Per Unit, Min Quantity Per Purchase, Cost, Cost Per Unit, Links, Notes) plus Line, Manufacturer, Supplier Part Number, Unit, Designator, No Load, Part Type, Child Revision.
- `boms/aligni-20261113T0325Z/`: the untouched Aligni export (30 active BOMs, 5 older revisions). Raw snapshot, client and scripts: `scratchpad/2026-11-13-aligni-bom-export/`.
- Source pulls (Notion, KiCad, Shopify, Slack, install-pack sheets, MCAD file list): `scratchpad/2026-11-13-bom-reconciliation/data/`.
- Docs in [boms/](boms/plan.md):
  - [reconciliation.md](boms/reconciliation.md): findings per assembly and Ben's decisions.
  - [part-numbers.md](boms/part-numbers.md): numbering rules, new families SEN4, IP and OBL, renumbered parts, placeholders.
  - [review-later.md](boms/review-later.md): deferred items.
  - [data-sources.md](boms/data-sources.md): every source and how it was read.
  - `research/`: cited notes.

### Decisions in force (Ben, 2026-11-13)

- Scope: vπ and V4 sensors go to Katana. V3.1 is not migrated, but its BOMs are cleaned. Obelisk is in flux and stays out; its BOM is a draft.
- PCBAs (Party HAT X5C, USB-A bridge X3, modem bridge X3, sensor breakout X2, V4 interposer X4A) are sub-assemblies with their own BOMs.
- Compute stack: keeps the I425-GL modem and both current antennas (cell+GPS combo and diversity). The RG255C 5G change is a placeholder and isn't built. 2 batteries per stack.
- Retroreflector: 2x E39-R1S per assembly, so 4 per RR kit. Sensor bar kits carry 4 pegs, 2 nylocks and 2 caps (`EXT-OLKOS75-100`) per enclosure, and the 15 ft RJ-12.
- Install packs: a full pack is the base set (`AG-IP-001-000`) plus one add-on, and Katana models it that way. The authoritative source is ByTechs' sheet `1zJsQbjP5G1RWWix71tEEHoSLD9x1BxvTSdU-K7LZTec`.
- V4 install packs are real SKUs, each with one vπ pack as a part. The mapping is provisional (review-later #1).
- Part numbers in `part-numbers.md` are confirmed.
- Later BOM corrections, applied in `build_boms.py`:
  - The M3 x 30 mm screw is `EXT-95893A198`.
  - The 3 in install-pack anchor is `EXT-THD50300H` (Titen HD).
  - Wipes are counted as single wipes.
  - Bollard item `EXT-H-2118F` added.

## Loose ends before import

### 1. Open lines in Katana scope (21)

`index.csv` column `Open` counts them. `grep EXT-TBD boms/items.csv` lists every placeholder.

| BOM | Open | What is missing | Ask |
|---|---|---|---|
| AG-SEN4-003-000 V4 install kit | 7 | Every part number: T27 self-drilling screw, T27 impact bit, 7/32 in drill bit, 15 ft RJ-45, 15 ft RJ-12, 1/2 in Tapcon, 1/2 in washer | Monti (the Notion V4 Sensor Kit BoM is his) |
| AG-SEN4-001-000 V4 sensor | 3 | T27 1/4-20 screw, LiDAR thermal pad, quantity of `EXT-95893A198` | Monti; see review-later #2 |
| AG-IP-001/003/004/005/006 install packs | 5 | `EXT-TBD-TAPCON-025X125-SS` (Tapcon 1/4 x 1-1/4 in; the vendor page has no maker number) | ByTechs |
| AG-SEN2-RR-Kit, AG-SEN2-TB-Kit | 2 | `EXT-TBD-RJ12-15FT` (the 8 ft one was `EXT-CS-44050-08`) | ByTechs (Ben ordered 100 in Oct) |
| AG-CS3-004-000 modem bridge | 2 | P5, P6 connectors have no MPN in KiCad | Ben |
| AG-CS3-003-000 USB bridge | 1 | J2 connector has no MPN | Ben |
| AG-SEN2-004-000 sensor breakout | 1 | J1 (6P6C) has no MPN | Ben |

The legacy V3.1 BOM has 1 open line (Party HAT X2B quantity) and the Obelisk draft has 12. Neither blocks the import.

### 2. Deferred reviews ([boms/review-later.md](boms/review-later.md))

1. V4 install-pack mapping: the bollard pack inherits reflector-bollard Tapcons and washers. Owners: Ben, ByTechs.
2. V4 sensor X5 BOM is built from the V4A and X3B Notion BoMs. X5 has design revisions not yet released to `tripwire-mcad`. Owner: Monti.
3. The V4 interposer X4A values in Notion are in no `tripwire-ecad` branch. Open PR #27 changes layout only. Owner: Monti.
4. Modem bridge X3 (flex) design files are not in `tripwire-ecad`; its BOM comes from X2. Owner: Ben.
5. Nylocks: Ben set 2 per enclosure, but both install-pack sheets said 4 per RR pack and 8 per TB pack. Owner: ByTechs.

### 3. BOM details Katana will force a choice on

- **No-load line:** `AG-CS3-001-000` keeps `EXT-EG25-G` as a no-load alternate modem. Katana recipes have no no-load flag, so drop the line or move it to notes.
- **Revisions:** BOM revisions (letters) and PCBA or assembly design revisions (X5C, X4A, X5) live in `index.csv` and `Child Revision`. Decide where they go in Katana: product name, a variant attribute, or notes.
- **Designators:** PCBA lines carry designators. Decide whether to keep them in ingredient notes.
- **Party HAT data error:** C10 (68 pF) shares DigiKey PN `1276-1135-2-ND` with C11, C12 and C16 (22 µF). Fix in KiCad or note it for ByTechs, whose pick-and-place list is the working copy.
- **Costs:** few items carry a cost (Aligni had 12 of 105). Purchase prices exist in the assembly-price roll-up (`scratchpad/2026-11-13-vpi-assembly-price/`) and the Ramp cost record (`scratchpad/2026-11-13-bom-costs/`). Neither is wired into `items.csv`.

### 4. Data not yet pulled from Aligni

Pull these before access ends. The paced client is `scratchpad/2026-11-13-aligni-bom-export/aligni.py`: 10 requests/min, 1 concurrent, 10,000 complexity per request.

- **Inventory balances per part and location:** needed for opening stock. Stock under renamed parts (the ELP cameras, the sensor breakout) moves to the new numbers.
- **Vendors and manufacturers with contacts:** needed for Katana suppliers.
- **Open purchase orders and builds in progress.**
- **Cross-checks for opening stock:** Aligni can't hold negative stock and has drifted from Shopify (Slack 2026-07-13). Many Shopify variants are negative, e.g. `AG-CS3-Kit` -67. Chris planned an inventory audit (Slack 2026-10-15), and a physical count is the safer source for opening stock.

### 5. Shopify and the sync service

These are writes to live systems, so each needs Ben's go-ahead at the time.

- **Set Shopify SKUs to the confirmed numbers before connecting Katana's Shopify integration:**
  - Install packs to `AG-IP-*-Kit`. Today `RRWMIPDC` sits on the TB-IP-DC product and `RRBMIPDC` on RR-WM-IP-DC, and four packs have no SKU.
  - "v4 Sensor Bar Assembly" to `AG-SEN4-Kit`.
  - The v4 install packs to `AG-IP-V4BM-DC-Kit` and `AG-IP-V4WM-DCR-Kit`.
  - The full mapping is in `part-numbers.md`.
- **Retire `aligni-shopify-sync`** (Render service, Aligni webhook, Shopify `orders/fulfilled` webhook) at cutover, so stock isn't decremented twice. Repo: `repos/aligni-shopify-sync`.

## Katana import plan

1. **Get Katana's CSV templates** (materials, products, recipes/BOMs, suppliers, stock), from Katana onboarding or #temp-katana-onboarding. Columns are unverified; don't guess them.
2. **Classify items:**
   - Anything with a BOM in Katana scope is a product: kits, assemblies, PCBAs, install-pack base set and add-ons.
   - Shippable kits (`*-Kit`) are the sold products and carry the Shopify SKUs.
   - Everything else is a material.
   - Decide how to treat parts made by suppliers to our design: printed plastics (ByTechs), machined tubes (Triple B), sheet metal (Haig), custom washers (SendCutSend). Simplest is materials bought from those suppliers.
   - Decide with Britney and ByTechs who runs builds in Katana: ByTechs as the contract manufacturer, or outsourced manufacturing orders.
3. **Write a converter in a new scratchpad task** from `boms/index.csv` (Scope = Katana), the BOM CSVs and `boms/items.csv` to the templates. It should:
   - include only the 227 Katana-scope items;
   - map Part Number to SKU, Part Name to name, Unit to unit, Supplier and Supplier Part Number to the supplier code, Cost Per Unit to purchase price;
   - map each BOM line to an ingredient with quantity, putting designators and notes in notes;
   - leave out legacy and Obelisk BOMs.
4. **Check before import:**
   - no `EXT-TBD-*` or blank quantity left in Katana scope, or a stated decision to import with placeholders;
   - every ingredient SKU exists as a material or product;
   - no circular recipes;
   - Shopify SKUs match `*-Kit` products.
5. **Import order:** suppliers, materials, products, recipes, then opening stock (count-based, with the rename map). Then connect Shopify, and retire the Aligni sync.
6. **Verify:** export recipes from Katana and diff them against `boms/`: line counts, quantities, SKUs.

## Related workstreams (other sessions)

- BOM costs (separate workstream, paused 2026-11-13 by Ben): line-item as-purchased cost record from Ramp for Ben, Monti and Chris, all history (1,608 records, $600,200.04, 2,979 line rows) and last six months. Not matched to BOMs. Method: [boms/cost-record.md](boms/cost-record.md). Remaining scope and open decisions: [bom-costs/plan.md](bom-costs/plan.md). Data and scripts: `scratchpad/2026-11-13-bom-costs/`.
- vπ full assembly price (in progress 2026-11-13): current result in [assembly-price/price.md](assembly-price/price.md), plan in [assembly-price/plan.md](assembly-price/plan.md). Configuration: RR sensor bar, round bollard mount, 4 mm + 6 mm dual camera, Uline H-2118F bollard. Scope and basis (Ben): parts, ByTechs labour, packaging; latest production-quantity purchase, landed; quote when older than six months. $2,118.56 priced ($1,245.92 on prices inside six months), 74 of 124 leaf parts priced and 17 carried at $0, all labour rows priced from ByTechs' itemized invoices, including an estimated $43.69 of import duty per camera ([assembly-price/research/camera-tariffs.md](assembly-price/research/camera-tariffs.md); no duty bill found). Left out on Ben's instruction and flagged in `assembly-price/price.md`: filament (AirGarage supplies Polymaker ASA) and the five sensor bar printed parts (possible ByTechs billing gap). Unpriced: 28 low-value parts (two cables, ferrules, 19 Digi-Key parts, four TBD connectors, padlocks, trash bag), most packaging materials. Reflectors use Digi-Key's $26.11 on Ben's instruction. Scripts and inputs: `scratchpad/2026-11-13-vpi-assembly-price/` (`price_config.py`, `price_rules.csv`, `manual_prices.csv`, `invoice_lines.csv`).
- Invoices from Ben (2026-11-13) are in `scratchpad/2026-11-13-vpi-assembly-price/data/invoices/`: 25 ByTechs invoices issued through Deel (totals only on the last five, "See invoice"), 27 itemized ByTechs invoices for 2026 (parsed by `parse_bytechs_invoices.py`), a Samtec order acknowledgement three JLCPCB board invoices, two Ailipu (ELP) proforma invoices for cameras and lenses, Haig invoices 98995 (wall-mount camera bracket) and 98534 (sensor enclosure top and base), MakerBright invoice 1381 for Raspberry Pis and coolers, and a Powermatic order acknowledgement (E3Z-R61 at $128.20 on 2025-10-14, the same price the roll-up already uses). Notes: [assembly-price/research/invoices.md](assembly-price/research/invoices.md), [assembly-price/research/powermatic-ordack.md](assembly-price/research/powermatic-ordack.md), [assembly-price/research/elp-haig-makerbright.md](assembly-price/research/elp-haig-makerbright.md), [assembly-price/research/bytechs-itemized-samtec.md](assembly-price/research/bytechs-itemized-samtec.md).
- Next steps there: BOM costs waits on Ben's answers in `bom-costs/plan.md` (browser access to Ramp receipt images and vendor order histories, cost basis, window). Assembly price waits on Ben's pricing for the outstanding items in `assembly-price/price.md` and his go-ahead before any Chrome use; then filament, packaging and quotes for stale lines (E3Z-R61 first).

## Reference

- **Sources:** [boms/data-sources.md](boms/data-sources.md).
  - All Notion BoMs are under Tripwire Home.
  - Google Sheets have no connector; they were read in Chrome through `gviz/tq?tqx=out:html&sheet=<tab>`, with link query strings cut.
  - Slack BOM channels: #airgarage-bytechs, #airgarage-bytechs-hardware-chat, #pt-tripwire, #pt-obelisk, #pt-v4-sensors, #airgarage-bytechs-tripleb-v4-hardware.
- **Aligni API:** GraphQL v3 with the token in `.env`. Cloudflare rejects Python's default User-Agent (error 1010). Part has no description field; names come from the active revision's `description`. BOM lines are `PartRevision.bomItems`.
- **`aligni` MCP server:** `get_bom` queries `subparts`, which isn't in the schema. `mcp__aligni__run_graphql` can run mutations and has no `ask` rule in `.claude/settings.json`.
- **`repos/`:** submodules `tripwire-ecad`, `tripwire-mcad`, `aligni-shopify-sync`. `aligni-mcp-server` is a gitignored plain copy.
- **Open `tripwire-ecad` PRs:** #27 (interposer layout, HW-892) and #28 (compute-stack bollard interface, HW-975). PR #28's board is in the Obelisk draft as `AG-OBL-002-000_CSInterface`, with the product assumed.
- **Disk:** the Mac's data volume filled during the MCAD clone on 2026-11-13. Ben freed space (90 GB free afterwards).
