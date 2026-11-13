# Aligni BOM snapshot

Snapshot `scratchpad/2026-11-13-aligni-bom-export/data/20261113T0325Z/` (pulled 2026-11-13T03:25Z, GraphQL `https://<org>.aligni.com/api/v3/graphql`). Exported to `boms/` at workspace commit e13d88b.

## Counts

- 105 parts: 48 Mechanical, 30 Assembly, 16 Module, 5 Cable, 4 Other, 2 Power. 112 revisions: 105 released-active, 6 released-inactive, 1 draft (`data/20261113T0325Z/part_revisions.json`).
- 36 revisions have BOM lines, across 31 parts. All 30 Assembly-type parts have a BOM; `AG-SEN2-002-000` (Module) also has one. Every part is used in at least one BOM.
- Part numbers: `AG-<family>-<assembly>-<item>_<suffix>` for our parts (families CS3, PIC, SEN2, plus `-Kit` SKUs), `EXT-<supplier or mfg PN>` for bought parts. One test object, `TEST-Kit` ("TEST object"), excluded from `boms/`.
- Top-level BOMs (used in no other BOM): 18 kits plus `AG-SEN2-003-000` (sensor enclosure). `boms/index.csv`.

## Findings

- Draft `AG-CS3-001-000` rev C, reason "Adding electronics", has the same 28 lines as active rev B. Nothing in any Aligni BOM is a Party HAT, USB bridge, modem bridge or sensor board. Rev B lists `EXT-SM-I-003` (Sequent Microsystems) and a line note "OLED to PartyHAT connection" on `EXT-5623`. `boms/AG-CS3-001-000.csv`, `boms/revisions/AG-CS3-001-000_RevC.csv`.
- Item code `PIC-001-005` is used by four different parts: `_DualWinMount`, `_ELPCam4`, `_ELPCam6`, `_ELPCam8`. `parts.json`.
- `SEN2-001-002` is unused (sensor bar items run 001, 003 to 007).
- Several `EXT-` parts store a DigiKey part number as the manufacturer part number, for example `EXT-732-10422-ND` (manufacturer Würth Elektronik, MPN field `732-10422-ND`), `EXT-952-3964-ND` (Harwin), `EXT-1168-TG-A1250-15-15-1.0-ND`, `EXT-2073-05-12-A-0030-A-4-06-4-T-ND`. Amazon ASINs are used as MPNs for `EXT-B07H18YDYB`, `EXT-B0BZKG6DBZ`, `EXT-B0CTCQN775`. `EXT-W3906XXXX` has MPN `W3906B0100`.
- `EXT-SC1113` (Raspberry Pi 5 model number) has manufacturer MakerBright, a reseller.
- Revision history: `AG-SEN2-RR-Kit` B to C removed the 12V/6W power supply (the TB kit still has one); A to B doubled the retroreflectors. `AG-SEN2-002-000` B to C replaced 1x `EXT-E39-R2` with 4x `EXT-E39-R1`. `AG-CS3-001-000` A to B added an M2 nut and an M2x20 screw.
- 12 of 105 parts have a standard cost; none have lead time, attrition or reorder quantity. 20 have a preferred vendor; 79 have a vendor part number.
- API: Part has no description field; names come from the revision `description`. The `aligni` MCP server's `get_bom` uses `subparts`, which is not in the schema (`data/schema.json`); the field is `PartRevision.bomItems`.
