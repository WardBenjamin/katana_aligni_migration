# Notion BoMs: research notes

Started 2026-11-13 (UTC). Read-only pulls from Notion via the Notion MCP (fetch, query-data-sources, search). Exports land in `scratchpad/2026-11-13-bom-reconciliation/data/notion/`. Times are UTC as Notion returns them.

## Tripwire Home

https://app.notion.com/p/0afdeb167ec24c0a82661e860449cfa0, last edited 2026-10-05T16:26:56Z. Index page under Engineering Home. No BoM itself. Links to BoM pages under "V4 BoM's and SOP's" (V4 X3B BoM, V4 X3B Assembly SOP, V4 Installation SOP, V4 X4B Assembly SOP and BoM, V4 Sensor Install Kit BoM), "v3.x" (Tripwire V3.1 BoM), "vπ" (Compute Stack, SOP, Camera, Sensor Bar, Bollard Mount Dual Camera Manufacturing Package, Sensor Enclosure, Wall Mount Dual Camera), "Deployment Kit" (Standard Deployment Kit), "Manufacturing" (Engineering Change Notices, Hardware Stock, Purchasing Documentation). Also lists a full-page database "Materials Inventory (OLD, v2)" (collection://91655b71-cc5f-46a0-846c-eed4ae4d8ad2) under v2, and for v3.0 a "V3 Materials Inventory" Google Sheet (not Notion, not read). The v3.0 callout says v3.0 was "the state of the hardware as of Q1 '25"; v2 callout says Q1 '24; v1 Q1 '23.

## vπ Compute Stack (page)

https://app.notion.com/p/2a2dcb3d06b28056be62fa9b1aa03f2d, last edited 2026-05-13T21:25:44Z. Holds two inline databases: "vπ Compute Stack Kit BoM" (collection://33ddcb3d-06b2-810d-8668-000b3a50727d) and "vπ Compute Stack (CS3-001-000) BoM" (collection://2a8dcb3d-06b2-8175-a573-000bb4a5faf4). Header callout says "Last Updated by Bryan Monti on 2025-11-05", which is older than the page's real last edit (2026-05-13), so the callout is stale. "Assembly Instructions (WIP)" section started 2026-04-02; its only parts list is the Antenna Wing ("2x M3x30mm T8 Torx Self Threading Screw, 1x Antenna Wing Back, 1x Antenna Wing"), a sub-step of the compute stack that the CS3-001-000 database covers, so not exported as a separate SOP table.

## vπ Camera (page)

https://app.notion.com/p/2f5dcb3d06b2803ca07fd4033314b01d, last edited 2026-08-05T16:26:01Z. Holds 11 inline databases: six kit BoMs (Round/Square Bollard and Wall Mount, Dual and Single) and five assembly BoMs (PIC-001-000 Dual Camera Module, PIC-002-000 Single Camera Module, PIC-003-000 Round Bollard Mount, PIC-004-000 Square Bollard Mount, PIC-005-000 Wall Mount).

Part-numbering scheme stated on the page ("Part Naming Legend"): PIC = vPi Camera; PIC-001 Camera Body (Dual); PIC-002 Camera Body (Single); PIC-003 Round Bollard Mount; PIC-004 Square Bollard Mount; PIC-005 Wall Mount.

Three "Materials:" plain tables in the assembly instructions (Camera Body Assembly, 7 rows; Assemble the Bollard Mount, 7 rows; Wall Mount Camera Assembly, 5 rows plus one blank row). Databases cover all three assemblies (PIC-001, PIC-003/004, PIC-005), so per the brief they were not exported. Things they show that may matter for comparison: Camera Body table lists "ELP Cameras" qty 2 with note "Configuration chosen here (4/6mm or 6/8mm)"; the Bollard Mount table says the instructions are the same for round and square and lists "Round Bollard Base" only; the Wall Mount table lists "M3 30mm Torx" x8 and "M3 8mm Torx" x6. A callout says "Pictures of camera cable routing required!" (open TODO). A checklist under OnShape Resources has all three GitHub release items checked. "Part Manufacturing Docs" is an alias block the API could not render.

## vπ Sensor Bar (page)

https://app.notion.com/p/33ddcb3d06b280e08303dd10b52f4ac2, last edited 2026-09-09T19:05:34Z. Not in the brief's known list; holds six inline databases:

- vπ TB Sensor Bar Kit (SEN2-TB-Kit) BoM, collection://33ddcb3d-06b2-8109-bac3-000b87b32a89
- vπ RR Sensor Bar Kit (SEN2-RR-Kit) BoM, collection://33ddcb3d-06b2-8190-b816-000b360d7f41
- vπ Sensor Bar (SEN2-001-000) BoM, collection://33ddcb3d-06b2-817e-8e0f-000b828bc44f
- vπ Sensor Retroreflector (SEN2-002-000) BoM, collection://33ddcb3d-06b2-811e-a6fc-000ba3c42e5f
- vπ Sensor Enclosure (SEN2-003-000) BoM, collection://f19dcb3d-06b2-8239-9c0b-874d2f27ac16 (database block https://app.notion.com/p/38edcb3d06b280cb9fcef3cdc80fc7ff; its data source ID has a different pattern from the others, so it may be a newer or moved database)
- vπ Sensor Retroreflector (SEN2-002-000) BoM (1), collection://36edcb3d-06b2-80e5-882f-000b1d171610. The "(1)" suffix is Notion's duplicate naming: a second database with the same title as SEN2-002-000.

TB = through-beam (E3Z-T61 emitter/receiver), RR = retroreflective (E3Z-R61), per the page's "Part Preparation" text. Plain "Parts Required" tables in the SOP: sensors into mounts (4 rows, includes "Sensors (Pair)(E3Z-XXX)" qty 2), heat-set inserts into Pitch Roll Mount (3 rows, includes a jig), Sensor Bar Assembly (7 rows, includes "Center Alignment Pitch Mount Jig"), Base Bar Assembly (6 rows: 2020 Base Bar Extrusion 455mm, Base Mount, Tuning Fork Mount, Sensor IO Breakout PCB, M5x8mm Button Head Screw x5, M5 T-nut x4). The SEN2 databases cover these assemblies, so the tables were not exported. Text mentions an M5x12mm screw for the angled insert that no SOP table lists. Tables mix jigs (tooling) with parts.

## vπ Sensor Enclosure (page)

https://app.notion.com/p/36edcb3d06b28090be34e1045b392cde, last edited 2026-05-28T20:19:56Z. Empty page (one blank paragraph). The SEN2-003-000 Sensor Enclosure BoM lives on the vπ Sensor Bar page instead.

## Wall Mount Dual Camera (page)

https://app.notion.com/p/3b3dcb3d06b2805e91beda3c2a1d95b7, last edited 2026-08-07T16:00:13Z. Says it "includes all BoM and assembly information for the wall mount cameras" but the body is only that sentence and a callout ("This assembly re-uses the main dual camera module from the bollard mounted dual cameras"). No BoM. The wall mount BoMs are the PIC-005-000 and Wall Mount Dual/Single Cam Kit databases on the vπ Camera page.

## Bollard Mount Dual Camera Manufacturing Package (page)

https://app.notion.com/p/30ddcb3d06b2804e89f5d2cc690a7bae, last edited 2026-04-09T18:20:46Z. 3D-printing package for the camera plastics. Has two numbered lists headed as BoMs ("There exist two forms of the dual camera. The BoM for each is the following"), printed parts only, qty 1 each, named by STEP file: Single = Single Lens Mount, Single Camera Body Mount, Base Pivot Mount, Slip Ring, Round Bollard Base; Dual = Dual Lens Mount, Dual Camera Body Mount, Base Pivot Mount, Slip Ring, Round Bollard Base. Lists, not tables, and covered by the PIC databases, so not exported. Odd: both variants list only the Round Bollard Base (no square), and the STEP names differ between sections ("Dual Camera Body Mount.step" vs "Dual Camera Mount Body.step"). Mentions a `.zip` with Bambu project files (attachment, not downloaded).

## SOP: Tripwire vπ Assembly (page)

https://app.notion.com/p/2cddcb3d06b28015933cf371470c13fa, last edited 2026-05-28T20:19:34Z. Callout: written by Ben Ward 2025-12-15, "Last updated" 2025-12-18 (stale relative to the page edit time). Its "Materials" section is a linked view of the CS3-001-000 database ("View of vπ Compute Stack (CS3-001-000) BoM", https://app.notion.com/p/2cddcb3d06b28059bd91ddd9bcef0cf5, data source collection://2a8dcb3d-06b2-8175-a573-000bb4a5faf4), so no separate export. Open "TODO:" list right under it: "Power supply cable", "OLED cable" (both have comment threads). Per-layer "Materials Needed" are bullet lists, not tables (Layer 1: Pi 5, Active Cooler, 4x M2.5x5mm SHCS, 4x M2.5x14mm F/F standoff, microSD; Layer 2: SixFab Modem HAT, LTE modem, antennas, Antenna Wing, 4x M2.5x10mm M/F standoff, Hologram SIM; Layer 3: tall riser, Party HAT X5, USB-A Bridge, Modem Bridge, FFC, thermal pad, 4x M2.5x15mm M/F standoff; Layer 4: Sequent Watchdog HAT, 2x 18650 Li-ion, 4x M2.5x5mm SHCS, JST-XA to ferrule cable; Final: Case Body, Faceplate, 2x plastic-threading screws, OLED, OLED cable). "Final Assembly" instructions are just "TODO". Differences from the CS3-001-000 database worth checking: SOP names a Raspberry Pi Active Cooler, Party HAT X5, USB-A Bridge, Modem Bridge and 2x 18650 batteries, none of which appear in the database rows; SOP says 15mm M/F standoffs, database has 16mm M-F.

## vπ Compute Stack (CS3-001-000) BoM (database)

collection://2a8dcb3d-06b2-8175-a573-000bb4a5faf4, database https://app.notion.com/p/2a8dcb3d06b280df9f62c6b35dc8e3db on the vπ Compute Stack page (page last edited 2026-05-13T21:25:44Z). 27 rows. Exported to `vpi-compute-stack-cs3-001-000.csv`. Columns: Part Name, Manufacturer Part Number, Quantity Per Unit, Supplier, Links, Alternate Link, Cost, Min Quantity Per Purchase, Cost Per Unit (formula), Notes, Part Number - Mfg, Internal Part Number.

- "Cost Per Unit" is a formula. The Notion MCP returns it only as a `formulaResult://` reference in rows mode, view mode and row-page fetch, and `formulaCode://` cannot be fetched, so the column is exported blank. Only 2 of 27 rows have a Cost (OLED $6.99, JST-PH cable $2.33).
- Two part-number columns: "Manufacturer Part Number" is filled, "Part Number - Mfg" is blank on every row (leftover column).
- Internal part numbers: bought parts `EXT-<supplier or mfg PN>`, our parts `CS3-001-00N_<Name>` (001 CaseBody, 002 Faceplate, 003 WingBase, 004 WingLeft, 005 WingRight, 006 PDisp, 007 PowerCab). No `AG-` prefix, unlike Aligni.
- "2x JST-XA to Ferrule cable" (CS3-001-007_PowerCab) has no Quantity Per Unit.
- "LTE Modem" row holds two alternates in one cell each (MPN "I425-GL / EG25-G", internal "EXT-I425-GL / EXT-EG25-G", supplier "Eagle Wireless (2026) / Digikey (Quectel) (2025)").
- "Pulse Electronics LTE + GPS Antenna": internal PN is a placeholder `EXT-W3906XXXX` while MPN is W3906B0100. "Antenova" antenna internal `EXT-SRFL029` vs MPN SRFL029-100.
- "M2x20mm Socket Head Screw" has a blank Supplier. "Modem HAT" MPN is a product name, not a PN. Raspberry Pi MPN "SC1113 / 9036-Pi5-16GB" holds two codes.
- OLED note: "Find alternative supplier".

## Export method (applies to every database below)

Rows pulled with the Notion MCP `query-data-sources` in rows mode (limit 100; every database returned `has_more: false`). Written with `scratchpad/2026-11-13-bom-reconciliation/notion_to_csv.py`, which keeps Notion column names, appends the row page URL as "Notion URL", strips `<p>` wrappers, turns `<br />` into a newline and removes Markdown backslash escapes (Notion returns `PIC-001-004\_LensGrom` for `PIC-001-004_LensGrom`). "Cost Per Unit" is a formula on every BoM database; the API gives only a `formulaResult://` reference (rows mode, view mode and row-page fetch all tried on 2026-11-13, and `formulaCode://` and `formulaResult://` URLs are refused by fetch), so that column is blank in every CSV. Column order follows the database's default view where I fetched it; for databases where I only read the data source or rows, I used the order of the sibling database with the same schema. Notion does not return a per-database last-edited time; manifest dates are the parent page's `page_last_edited_at`.

## vπ Compute Stack Kit BoM (database)

https://app.notion.com/p/33ddcb3d06b2802db1dec699ade71125, collection://33ddcb3d-06b2-810d-8668-000b3a50727d, on the vπ Compute Stack page (last edited 2026-05-13T21:25:44Z). 3 rows: vπ Compute Stack (CS3-001-000), 12V/36W Power Supply (EXT-L6R36-120), 3ft Barrel Jack Extension (EXT-P0101E). Schema has three part-number columns: "Internal Part Number" (filled), "Part Number" (holds "MPN / DigiKey PN", e.g. "L6R36-120 / 364-1282-ND"), "Part Number - Mfg" (blank). The kit's title has no part number on the page; Aligni calls it AG-CS3-Kit. Power supply Cost 9.42521 (unrounded).

## vπ Dual Camera Module (PIC-001-000) BoM (database)

https://app.notion.com/p/2f5dcb3d06b280f3a3a1d4431b4bcecb, collection://2f5dcb3d-06b2-8145-a714-000b9fbad53f, on vπ Camera (last edited 2026-08-05T16:26:01Z). 9 rows. Columns: Part Name, Part Number, Quantity Per Unit, Supplier, Links, Cost, Min Quantity Per Purchase, Cost Per Unit, Notes, Part Number - Mfg (blank throughout).

- Part number PIC-001-005 is used twice: `PIC-001-005_DualWinMount` (Dual Lens Window Mount) and `PIC-001-005_ELPCam[4,6,8]` (ELP Camera). The next row, ELP USB cable, is PIC-001-006, so the camera probably should be its own number.
- One row "ELP Camera (4/6/8mm)" qty 2 covers every lens option; there is no 4/6 vs 6/8 split (Aligni has AG-PIC-001-000_Dual46 and _Dual68). The vπ Camera SOP table says the lens configuration is chosen at camera-body assembly.
- Bought camera parts (ELP camera, ELP USB cable) carry internal PIC- numbers, not EXT-, and have no link or MPN.
- Has "M3x30mm Thread Forming Screw" qty 4, which the SOP "Camera Body Assembly" table does not list; SOP lists 6x M3x8mm (matches).

## vπ Single Camera Module (PIC-002-000) BoM (database)

https://app.notion.com/p/33ddcb3d06b280c08c6ee3ef3f335672, collection://33ddcb3d-06b2-81f1-8f5d-000be7a351d6 (title has a trailing space). 9 rows; schema identical to PIC-001. Reuses PIC-001 parts (LensGrom, InnerWindow, ELPCam, ELPCamUSB) at qty 1, plus PIC-002-001 SMainBody, -002 SingleWindow, -003 SingleWinMount. Keeps 6x M3x8mm and 4x M3x30mm, the same screw counts as the dual module.

## vπ Round Bollard Mount (PIC-003-000) and Square Bollard Mount (PIC-004-000) BoMs (databases)

PIC-003: https://app.notion.com/p/33ddcb3d06b280398c37f9686f20d5b1, collection://33ddcb3d-06b2-815b-b84c-000b74bc8f76. PIC-004: https://app.notion.com/p/33ddcb3d06b2805bb8d7c8edd8c5df6e, collection://33ddcb3d-06b2-81ac-978c-000b56c6848b. 5 rows each. Both list the ULINE bollard itself (H-2118F round, H-8264 square, Cost $100) at **Quantity Per Unit 0** — present for reference, not consumed. Both use 8x M3x30mm thread-forming screws. Square reuses `PIC-003-003_SlipRing` and `PIC-003-002_PivotMount`. The vπ Camera SOP bollard table lists different fasteners (6x M3x16mm, 2x M3x25mm, 2x M4x8mm CS, plus 2x M3x8mm in the text), none of which are in either database.

## vπ Wall Mount (PIC-005-000) BoM (database)

https://app.notion.com/p/33ddcb3d06b280309cace4e2098b5f8f, collection://33ddcb3d-06b2-8158-a88f-000b2c5a40fe. 7 rows: 8x M3x30mm TF, 6x M3x8mm TF, 2x M3x8mm button head (EXT-92095A181), Wall Bracket (PIC-005-001, supplier Haig Precision, "Sheet Metal"), Wall Cam Base A/B (-002/-003), 2x Face Cover Plate (-004). The vπ Camera SOP wall table has "Wall Mount Camera Lower/Upper", "M3 30mm Torx" x8, "M3 8mm Torx" x6: names differ from the database and the SOP has no bracket, covers or button-head screws.

## vπ camera kit BoMs (six databases)

On vπ Camera, each 2 rows: one camera module + one mount, qty 1 each, with "Links" pointing at the module/mount database view. Columns: Part Name, Part Number, Quantity Per Unit, Links, Supplier, Cost, Min Quantity Per Purchase, Cost Per Unit, Notes, Part Number - Mfg (schema fetched for Round Bollard Dual; the other five show the same keys in rows). None of the kits has a part number of its own in Notion, and none carries the lens option (Aligni has 6 single and 3+3 dual lens-specific kit SKUs, e.g. AG-Dual46-WallMount-Kit).

- Round Bollard Dual (collection://33ddcb3d-06b2-81d9-9750-000baeb951a6): PIC-001-000 + PIC-003-000.
- Square Bollard Dual (collection://33ddcb3d-06b2-8138-8e78-000b11b7d673): PIC-001-000 + PIC-004-000.
- **Wall Mount Dual (collection://33ddcb3d-06b2-812c-866b-000b44aa76de): PIC-002-000 "Single Camera Module" + PIC-005-000.** A dual kit that calls for the single camera module; looks like a copy-paste error from the single kit (identical to Wall Mount Single).
- Round Bollard Single (collection://33ddcb3d-06b2-8183-b3e6-000b430ae5d4): PIC-002-000 + PIC-003-000.
- Square Bollard Single (collection://33ddcb3d-06b2-8100-9f45-000ba8541fca): PIC-002-000 + PIC-004-000.
- Wall Mount Single (collection://33ddcb3d-06b2-8116-86d8-000b5ad12bdd): PIC-002-000 + PIC-005-000.

The Round Bollard Dual database's ancestor path has two untitled pages between it and vπ Camera (https://app.notion.com/p/33ddcb3d06b280dbb2ede2c251292fc9, https://app.notion.com/p/33ddcb3d06b280b89e1df8e141f18fca), likely the column-layout blocks.

## vπ Sensor Bar (SEN2-001-000) BoM (database)

https://app.notion.com/p/33ddcb3d06b281988bc2f872cd740ee8, collection://33ddcb3d-06b2-817e-8e0f-000b828bc44f, on vπ Sensor Bar (page last edited 2026-09-09T19:05:34Z). 14 rows. Columns: Part Name, Part Number - Internal, Part Number, Quantity Per Unit, Supplier, Links, Cost, Min Quantity Per Purchase, Cost Per Unit, Notes (no "Part Number - Mfg" column here, unlike its siblings).

- Internal numbers SEN2-001-001 to -013 (001 Breakout, 002 SenMount, 003 SenMntR, 004 SenMntL, 005 BaseMnt, 006 PitchRoll, 007 RollMnt, 008 M5Insert, 009 SetScrew, 010 ExtScrew, 011 2020Nut, 012 SensorBar, 013 SensorBase) plus EXT-22AWGFERRULE. Bought fasteners use SEN2- numbers, not EXT-, and have "Part Number" "N/A" (four Amazon/McMaster parts), even where a McMaster PN is in the link (92095A210).
- "M3x8mm Button Head Screw" is numbered SEN2-001-002_SenMount, a name that reads like the sensor mount part.
- Links for Pitch Roll Mount and Base Mount are the GitHub release URL pasted twice end-to-end (`...v31-mcad-releasehttps://...v31-mcad-release`). Printed parts link to the **v3.1** MCAD release (`v31-mcad-release`) though this is the vπ BoM.
- 3D-printed rows: Supplier "In-House", Cost 0, note "3D Printed in-house"; Sensor I/O Breakout supplier "ByTechs LLC" (underlined in Notion).
- 22AWG Ferrules: link text "Amazon (according to Chris @ Bytechs LLC)", no Cost.
- Compared with the SOP tables on the same page: SOP says 4x M5 T-nut in the base bar plus 2 in the sensor bar (database 4) and 6 + 5 + 4 M5x8mm screws across steps (database 12). Not reconciled here.

## vπ Sensor Retroreflector (SEN2-002-000) BoM (database)

https://app.notion.com/p/33ddcb3d06b280989ef9edf9c57b4d98, collection://33ddcb3d-06b2-811e-a6fc-000ba3c42e5f. 2 rows: Dual Retro Reflective Rain Cover (SEN2-002-001_DualRRCov, supplier ByTechs LLC, note "3D Printed in-house", Cost 0) and Omron E39-R2 Retroreflector (EXT-E39-R2, Part Number "E39-R2 / Z11478-ND", supplier Powermatic, Cost $26). Columns: Part Name, Part Number - Internal, Part Number, Quantity Per Unit, Supplier, Links, Cost, Min Quantity Per Purchase, Cost Per Unit, Notes, Part Number - Mfg.

## vπ Sensor Retroreflector (SEN2-002-000) BoM (1) (database, duplicate)

https://app.notion.com/p/36edcb3d06b28053aed3cb8307958cf0, collection://36edcb3d-06b2-80e5-882f-000b1d171610. Exported as `vpi-sensor-retroreflector-sen2-002-000-copy.csv`. 4 rows. A copy of SEN2-002-000 that someone started turning into a sensor-enclosure BoM: row 1 renamed "Sensor Enclosure" but still SEN2-002-001_DualRRCov; row 2 renamed "Sensor Enclosure Base" but still EXT-E39-R2 / Powermatic / $26; plus "Pins" (qty 4, Essentra via Mouser 27PIF0089, no part number) and "3/4” Knock-out Seal" (qty 2, Amazon short link, no supplier or part number). Treat as a draft, not a BoM of record.

## vπ Sensor Enclosure (SEN2-003-000) BoM (database)

https://app.notion.com/p/38edcb3d06b280cb9fcef3cdc80fc7ff, collection://f19dcb3d-06b2-8239-9c0b-874d2f27ac16. 2 rows, half-edited: part numbers are SEN2-003-002_EnclosureTop and SEN2-003-001_EnclosureBase with supplier Haig Precision, but the **Part Names are still the retroreflector's** ("Dual Retro Reflective Rain Cover (Round & Flat)", "Omron E39-R2 Retroreflector"), the top row still says "3D Printed in-house" while the supplier is a sheet-metal shop, and the links are the v3.1 MCAD release. Its view ID (view://001dcb3d-...) and row IDs (ae8dcb3d-..., 82adcb3d-...) follow a different pattern from every other vπ database, so it was probably created or moved recently. The Pins and Knock-out Seal rows from the "(1)" copy are not in it.

## vπ TB Sensor Bar Kit (SEN2-TB-Kit) and RR Sensor Bar Kit (SEN2-RR-Kit) BoMs (databases)

TB: https://app.notion.com/p/33ddcb3d06b280489a18d0d12ab1b564, collection://33ddcb3d-06b2-8109-bac3-000b87b32a89, 4 rows. RR: https://app.notion.com/p/33ddcb3d06b28007ac1be87bdedf11ce, collection://33ddcb3d-06b2-8190-b816-000b360d7f41, 5 rows. Same columns as SEN2-002.

- TB kit: 2x vπ Sensor Bar (SEN2-001-000), 2x E3Z-T61-D/L (EXT-E3Z-T61, $128.20), 1x RJ-12 cable 8ft (EXT-CS-44050-08, "Via PO"), 1x 12V/6W PSU (EXT-L6R06H-120).
- RR kit: 1x vπ Sensor Bar, 2x E3Z-R61 (EXT-E3Z-R61, $148.70), RJ-12 cable, 12V/6W PSU, 2x vπ Sensor Retroreflector (SEN2-002-000).
- The "vπ Sensor Bar" row in both kits carries the 455mm extrusion's Mfg PN (HFSB5-2020-455-TPW) and its note ("cut to length spec'd (455mm here)"), copied from the SEN2-001-013 row, though the row is the whole assembly.
- RR kit's E3Z-R61 "Part Number" is "44" (looks like a typo); both sensor rows have "Part Number - Mfg" "E3Z-R61, E3Z-T61" (both models in one cell).
- Neither kit includes the Sensor Enclosure (SEN2-003-000); Aligni has an AG-SEN2-003-000 assembly.

## Tripwire V3.1 BoM (page) and its three linked views

https://app.notion.com/p/299dcb3d06b28079a42fe3b0cd846ddc, last edited 2025-12-31T20:56:00Z. Callout: "This page is to hold all resources pertaining to the manufacturing of all Tripwire components. This does not include hardware required for site installation (ie, EMT, tapcons, etc)", with a link to https://app.notion.com/p/28edcb3d06b280a98930cde0d9416f81 for install hardware. Three sections, each a **linked view** of a database that lives on an older v3.1 design page (found via row-page ancestor paths):

| Section | View on V3.1 page | Source database | Source page |
|---|---|---|---|
| Camera Assembly BoM | https://app.notion.com/p/299dcb3d06b280a28836e86935f844ce | "BoM", https://app.notion.com/p/1bcdcb3d06b28040bc4cf6e2bf9d344b, collection://1bcdcb3d-06b2-80a3-8f40-000be4417ee4 | Camera Glow Up (Cam Housing), https://app.notion.com/p/1addcb3d06b280e98fb6dd259781b8db |
| Sensor Bar Assembly BoM | https://app.notion.com/p/299dcb3d06b28012bde3e8073126c8f7 | "BoM", https://app.notion.com/p/1ebdcb3d06b280c38593d858644168c3, collection://1ebdcb3d-06b2-809a-a0ca-000b125aa95e | Sensor Bar (Rescue), https://app.notion.com/p/1aedcb3d06b280cbb36dce8ae617e1b5 |
| Compute Stack BoM | https://app.notion.com/p/29bdcb3d06b280e78ff5eb5d511756ec | "Compute Stack BoM", https://app.notion.com/p/299dcb3d06b28075bea3f483a029cff8, collection://299dcb3d-06b2-81aa-9fae-000bb92c9964 | Compute Stack Case, https://app.notion.com/p/1c0dcb3d06b280bb8377cb3cfaf055fb |

None of the three views shows a filter, so each CSV is the full source database. The page also has an "ai_block" the API could not render.

### V3.1 Camera Assembly BoM → `tripwire-v3-1-camera-assembly.csv`

14 rows. Columns: Name, Part Number - Mfg, Part Number - Internal, Quantity Per Unit, Supplier, Links, Notes, Cost, Quantity Per Purchase, Cost Per Unit (formula). Title column is "Name" (not "Part Name") and it has "Quantity Per Purchase" instead of "Min Quantity Per Purchase": an older template. Internal numbers are **CAM4-001-001 to -013** (Housing, RearCap, LensClamp, RearGasket, LensGasket, LensWindow, LensGasket again as -007, Grommet, M25Insert, FrontScrew, RearScrew, HingeBolt, CamAnchor). Odd: "CAM4" prefix on a v3.1 BoM; "LensGasket" suffix used for both -005 (Lens Window Gasket, printed TPE) and -007 (Camera Lens Gasket, O-ring); "M2x4mm Socket Head Screw" with note "M2x5mm" and MPN 91292A004; ELP camera row lists three MPNs in the internal-PN cell (KV100IR, KV60IR, KV80IR) and supplier "ELP - Cecilia ()"; two gasket rows have supplier "Bryan Monti" (a person); "Links" values are Markdown "[Link](url)" text or "Github Release"; acrylic note says laser cutting is done by "a friend ... for free". Row pages last edited as early as 2025-10-30.

### V3.1 Sensor Bar Assembly BoM → `tripwire-v3-1-sensor-bar-assembly.csv`

15 rows. Columns: Part Name, Part Number - Mfg, Part Number - Internal, Quantity Per Unit, Supplier, Links, Cost, Min Quantity Per Purchase, Cost Per Unit, Notes. Uses the **same SEN2-001-001…013 numbers as the vπ SEN2-001-000 database**, with near-identical rows (the vπ database looks like a copy of this one). Differences: this one has the sensor row ("E3Z-R61 or E3Z-T61-D/L", internal PN cell "E3Z-R61, E3Z-T61", qty 2, $148.70), which vπ moved into the TB/RR kits; ferrules are SEN2-001-014_22Ferrule here vs EXT-22AWGFERRULE in vπ; the two extrusion rows have no Cost here. Same doubled GitHub link on Pitch Roll and Base Mount. Ferrule row page last edited 2026-04-08.

### V3.1 Compute Stack BoM → `tripwire-v3-1-compute-stack.csv`

18 rows. Columns: Part Name, Part Number - Mfg, Part Number, Quantity Per Unit, Supplier, Links, Cost, Min Quantity Per Purchase, Cost Per Unit, Notes. Internal numbers **COM4-001-001 to -011** (HoloSIM, RPiCooler, SAM256G, BattP30B, PartyX2B, SWDv9, Sixfab4G, RPI516GB, HousingB, HousingA, AntBracket). Seven fastener/standoff rows have a blank "Part Number" and a DigiKey PN in "Part Number - Mfg". "Party HAT X2B" has no Quantity Per Unit. Includes Active Cooler and 2x Molicel P30B 18650 batteries, which the vπ CS3-001-000 database lacks (the vπ SOP still lists both). Row pages last edited 2025-10-30.

## V4 X3B BoM (page) and its three databases

https://app.notion.com/p/3c0dcb3d06b2804ea759f49224c82a4f, last edited 2026-08-21T19:50:23Z. Opens with an instruction-style line "Include costs for the powder coating, assembly of the stack, and the packaging of the stack" (an open to-do). Callouts define the split: "Manufacturing BoM includes all raw materials required to produce parts for the final assembly"; "Powder coating BoM includes all metal parts that are required to be power coated". Powder-coating price tiers from IR Fabrication Inc are in page text (25/50/100 extension tubes at $25/$20/$17 each, couplers +$12/+$10/+$8), not in the database, and the database lists Triple B as the coater. A warning callout says other mounting options for the aluminium parts are being explored (McMaster 95015A450 self-tapping screws, 29045A743 drill bit). All three databases share columns Part Name, Part Number - Internal, Part Number, Quantity Per Unit, Supplier, Links, Cost, Min Quantity Per Purchase, Cost Per Unit, Notes, Part Number - Mfg. **No V4 row has an internal part number**; the only text in that column is the placeholder "Existing part - put reference here" (RJ12 Cable row). No Aligni assembly exists for V4 (none in `boms/index.csv`).

- V4 X3B Manufacturing BoM (collection://342dcb3d-06b2-8244-9c93-07762aae2bf3), `v4-x3b-manufacturing.csv`, 3 rows: aluminium stock that becomes the bollard coupler (McMaster 7392T42), LiDAR tube adapter (9056K42-9056K164) and extension tube (24" Sch 40 pipe, Metals4UOnline, PN "N/A").
- V4 X3B Powder Coating BoM (collection://9d2dcb3d-06b2-8347-9cc0-87152c8a7e46), `v4-x3b-powder-coating.csv`, 3 rows: Prismatic Powders HSS-1336 satin black, Bollard Coupler (Unpainted) $25 and Bollard Extension (Unpainted) $12 from Triple B, no part numbers.
- V4 X3B Assembly BoM (collection://450dcb3d-06b2-8209-a793-0795ab94075b, title has trailing space), `v4-x3b-assembly.csv`, 15 rows: 12x M3x10 thread-forming (96817A322), 7x M3x8 SHCS (91292A112), 18x #10 3/4" tamper-resistant drilling screws (94625A423, blank supplier), Seyond D1R LiDAR ($800, no supplier/PN), printed/machined parts linked to STEP files under `tripwire-mcad/V4-release/X3B-release/CAD Files/`, RJ12 and RJ45 cables 8ft (no PN), M12 17-pin cable (Mouser MSAS17ML-SASFL-SB001). Eight rows have neither a part number nor a supplier. No PCB rows although the notes mention the "sensor interposer X1".

## V4 Sensor Install Kit BoM (page) and V4 Sensor Kit BoM (database)

Page https://app.notion.com/p/3f0dcb3d06b28127ac28ce13354bea62, last edited 2026-11-04T20:13:30Z (most recent of all BoM pages). Callout: "Kit BoM includes all installation hardware, tooling, and consumables packed with each V4 sensor kit"; a second callout (❌ icon) says they may ship installers 5 drill bits to start and resupply.

Database https://app.notion.com/p/001212f48c6e41508dec256b6a975aab, collection://a3f53fcc-7a37-4b05-845b-389f8f115d4e, `v4-sensor-install-kit.csv`, 8 rows. Different schema from the others: Part Name, Quantity Per Unit, Links, Part Number - Internal, Part Number - Mfg, Min Quantity Per Purchase, Cost Per Unit, Cost, Notes, Supplier (no "Part Number" column). **Every row has blank part numbers, supplier and cost.** Rows: 6x T27 security Torx self-drilling screw (note: "P/N not finalized. Candidates from Fastener Testing: McMaster 95015A278 (used on first V4 install), 95015A314 (listed in V4A LiDAR Assembly BoM)"), 2x T27 impact bit, alcohol wipes, 7/32" drill bit, 15ft RJ45, 15ft RJ12 (link "N/A"), 4x 1/2" TAPCONs, 4x 1/2" washers (link "SendCutSend"). The note names a "V4A LiDAR Assembly BoM" not linked from Tripwire Home; searched for below.

## V4 X4B Assembly SOP and BoM (page) and its three databases

https://app.notion.com/p/3cedcb3d06b2800c86ebfb6ea25181f6, last edited 2026-10-21T22:12:17Z. Callout: created by Bryan Monti 2026-09-01, "Last updated 2026-09-13" (stale versus the page edit). A callout under "BoMs": "We need to include the machining tools that Triple B purchased to build the below parts" (open to-do). "Assembly Instructions" has three empty headings (Coupler, LiDAR Housing, Final) and a stray word "Digikey" at the end: the SOP part is unwritten. Attachments not downloaded: a SendCutSend heatsink invoice PDF (SA97S389.pdf) and WireViz cable files including `bollard-hybrid-cable.bom.tsv`, a cable BoM attachment (not read; it would need a download). Naming is mixed on one page: page title says X4B, databases say "V4A" and "X4A", and a row in the LiDAR BoM says "Sensor Interposer PCB - X4B". Internal part numbers in these databases are just the vendor PN copied over, or blank; no AG/V4 numbering scheme.

- **V4A Machining BoM** (collection://988dcb3d-06b2-82b2-ba2e-870c16c8e70d), `v4a-machining.csv`, 5 rows; columns Part Name, Part Number - Internal, Part Number, Quantity Per Unit, Links, Supplier, Cost, Min Quantity Per Purchase, Cost Per Unit, Notes. Raw aluminium stock. McMaster 5" OD tube (7392T42-7392T423, "Bollard Coupler") at **qty 0**, apparently replaced by Nox Metals 5.5" OD round stock (qty 1) whose note says "5” OD" while its name says 5.5"; 4.5" OD round stock from SpeedyMetals at qty 0.33 with no cost. Overlaps the X3B Manufacturing BoM (same 9056K42-9056K164 tube and 24" Sch 40 pipe, now with Metals4U PN API61440 and $82.20 vs $75.92).
- **V4A LiDAR Assembly BoM** (collection://263dcb3d-06b2-83f0-9669-875032b7b548), `v4a-lidar-assembly.csv`, 14 rows, same columns. Does **not** list the Seyond D1R LiDAR itself (X3B Assembly BoM does, $800). T27 security self-tapping screw is 94625A131 here, but the V4 Sensor Kit note says this BoM lists 95015A314: the note or this row is out of date. "T10x10mm Thread-Forming Screws" carries PN 96817A322, the same PN X3B calls "M3x10mm". Conformal coating qty 0; "Plastic Threading Screws 30mm" (McMaster 95893A198) has no quantity; epoxy supplier "N/A"; three printed parts have no supplier or PN; M12 cable note: "Need to find replacement part due to availability and Chris’ request for a 2.5ft cable (vs current 1m length)".
- **X4A Sensor Interposer PCB** (collection://fcfdcb3d-06b2-824c-8916-8716c9d898d0), `x4a-sensor-interposer-pcb.csv`, 18 rows, same columns. Electrical BoM with reference designators in Notes (J2, J3, J4, D1, D2, C1–C5, R1, R3–R6, U1, U2). Notes read like a recent design review: several rows "Changed from" earlier values (R1 2.0k→6.8k, D2 SMAJ15A→SMAJ28A, R3 2.0k→1M, C1 0603→1206 1kV), costs "carried over ... not re-verified", "confirm at order", and a known defect: "With the non-shielded body, J2 pin 18 has no physical pin, so R3/C1 currently connect to nothing." 0603 Red LED kept at **qty 0** "for reference". No resistor R2 row. The bare PCB (OSHPark, $43, min 3) has no PN. Worth checking against `repos/tripwire-ecad` (not done here).

## Standard Deployment Kit (page)

https://app.notion.com/p/1c0dcb3d06b280e58948d1f539d06b11, last edited 2025-07-29T19:33:07Z. No table or database. "Recommended Tools" (ES15 electric screwdriver, RJ45/RJ11/12 crimper, M12/18 Milwaukee impact driver) and "Recommended On-hand Hardware" (Tapcons 1/4"x2" and 3/8"x2"; "Washers" followed by an empty list item). No quantities or part numbers, so nothing exported. Unfinished (empty washer list).

## Hardware Stock (page)

https://app.notion.com/p/26fdcb3d06b280099819fe5f327750dc, last edited 2026-04-13T21:12:00Z. Callout: "Deprecating this document as Hardware Team has handed off all production duties to our contract manufacturer, ByTechs LLC." Four plain tables of on-hand stock per person (Monti 15 rows, Steve 3, Tim 12, Ben 2), columns Item Name / Qty / Notes. These are inventory counts, not BoMs, so not exported. Useful facts: Steve's table names "TRIPWIRE BAR ENCLOSURE V4 ORG/BLK" and "TRIPWIRE BAR BASE V3" ("Pairs with v3 or v4 enclosure"); Tim's table lists Party HAT X2B, Super Watchdog HAT v9, SixFab HATs (no modem / Telit / Quectel), ~180 RPi 5 16GB, "v3.1 compute stack cases", "Antennas???".

## Engineering Change Notices (page)

https://app.notion.com/p/31edcb3d06b280b1b6b9f074d6c84b0d, last edited 2026-09-10T21:46:13Z. "Living document that will hold all design changes for items that are in production", newest first. Five ECNs, none with a part number or revision letter:

1. 2026-09-10 Dual Camera Bollard Base Mount: slot added to the inner ring to clear the weld bead in ULINE 4.5" bollards; insert diameter reduced. No new part number; PIC-003/004 databases unchanged in name.
2. 2026-08-14 Sensor Bar Mounting Screw: extra screw on the fork mount; base mount screws re-arranged. Likely changes fastener counts in SEN2-001-000; not checked against the database.
3. **2026-08-13 Compute Stack Antenna Wing: switching to the Quectel RG255C-GL modem (5G RedCap) with "one large monolithic flex antenna"; "new plastics, antenna, and modem".** The CS3-001-000 database (page last edited 2026-05-13) still lists the I425-GL / EG25-G modem, two separate antennas (Pulse W3906B0100, Antenova SRFL029-100) and the old wing plastics, so the Notion compute-stack BoM predates this ECN.
4. 2026-04-08 Retroreflector: single-reflector variant discontinued; dual reflector gets break-away tabs for flat and round-bollard mounting. Matches the single "Dual Retro Reflective Rain Cover (Round & Flat)" row in SEN2-002-000.
5. 2026-03-09 Sensor Bar Set Screw: M5x10mm set screw replaced by M5x12mm (McMaster 92095A210); ByTechs stock updated from 2026-03-06. It says "BoM for sensor bars has been updated", linking https://app.notion.com/p/1ebdcb3d06b280c38593d858644168c3 — the **V3.1 "Sensor Bar (Rescue)" database**, not the vπ SEN2-001-000 one. As of March 2026 that older database was treated as the sensor-bar BoM of record. Both databases now show M5x12mm (SEN2-001-009_SetScrew).

## Purchasing Documentation (page)

https://app.notion.com/p/33cdcb3d06b28099b2cbff18af5d7ad9, last edited 2026-04-08T17:49:03Z. Supplier notes, no BoM: SendCutSend (bollard washers, "no suitable OTS part found"), Pololu (JST-PH cables for OLED), Waveshare (OLED displays), ELP (all 4/6/8mm cameras; contact blank), Haig Precision ("Sheet metal sensor enclosures and Wall mount camera body"; two named contacts with emails). Haig matches the supplier on PIC-005-001 Wall Bracket and SEN2-003 enclosure rows.

## Searches (2026-11-13)

Ran Notion searches "BoM", "bill of materials", "kit BoM", "assembly BoM" (page_size 20–25 each). New BoMs found that are not linked from the pages in the brief, or only indirectly: X1 BoM and X2 BoM (V4 LiDAR X1/X2 Documentation), SixFab LTE Kit BOM (Cellular Connectivity & Hardware for Tripwire 3.x), the Meta Menlo Park "BoM Table", and the V3.1 source databases on Camera Glow Up / Sensor Bar (Rescue) / Compute Stack Case. Also an older copy of the vπ SOP ("Tripwire vπ Assembly SoP", no parent page). The "bill of materials" search mostly returns meeting notes; the ones that speak to which BoM is current are summarised in the "Which BoM is current" section below. Search also surfaced "BOMA leads upload" (Sales Ops, unrelated).

## V4 LiDAR X1/X2 Documentation (page), X1 BoM and X2 BoM (databases)

Page https://app.notion.com/p/3a4dcb3d06b280e49706cafb071e3410, last edited 2026-07-31T16:08:01Z. X1 (clamping couplers, ABS Sch 40 pipe on a 60" 4.5" ULINE bollard) deployed at Washington Hill 2026-06-17 (five units); X2 (screwed coupler, countersunk holes) deployed at Gateway, Peachtree and Denver Arts Garage from 2026-07-15. X1's clamp coupler is described as inadequate and replaced in X2, so X1 is superseded. A "Tools required" table (countersink bit, 7/32 drill, T30 bit) is tooling, not exported. Peachtree used a REVODATA PoE splitter (not in any BoM).

- X1 BoM, collection://974dcb3d-06b2-822b-b603-078eaaa72c46, `v4-x1-lidar.csv`, 10 rows. Old template ("Quantity Per Purchase", "Links" as text with Markdown links). No part numbers anywhere except the M12 cable whose Part Name is its MPN (M12A-17BMMM-PL8D05). In-house parts have supplier "AirGarage Inc." and OnShape links. No cost on any row.
- X2 BoM, collection://4aedcb3d-06b2-83e4-879d-8709a7a1aa0a, `v4-x2-lidar.csv`, **3 rows only** (Tube Drill Jig, 18x #10 flathead thread-forming screws McMaster 95893A950, M12 cable). Looks like a delta from X1 rather than a full BoM, and includes a jig (tooling). X3B's Assembly BoM uses 18x #10 tamper-resistant drilling screws 94625A423 instead.

## SixFab LTE Kit BOM (database)

https://app.notion.com/p/233dcb3d06b28044b798e5c47ec86680, collection://233dcb3d-06b2-80b1-907d-000b4870bf52, on "Cellular Connectivity & Hardware for Tripwire 3.x" (search timestamp 2025-07-17). `tripwire-v3-x-sixfab-lte-kit.csv`, 7 rows. A cost comparison of the SixFab kit's contents against alternate vendors, not a build BoM: columns Name, Part Number, SixFab Link, SixFab Cost, Alt Vendor Link, Alt Vendor Cost @ min(100, MOQ), Unit Cost Delta (formula, blank). **No quantity column.** Includes a "LTE Discount Code" row at -$25 and a "40-pin Stacking Header" row with nothing filled in. Shows the origin of the Pulse W3906B0100 / Antenova SRFL029-100 antennas and the Eagle I425-GL modem used in CS3-001-000.

## Materials Inventory (OLD, v2) (database)

https://app.notion.com/p/b191225853dd4b05845b207fa9ae5b43, collection://91655b71-cc5f-46a0-846c-eed4ae4d8ad2, full-page database under Tripwire Home's v2 section ("Tripwire v2 is based on a Raspberry Pi 3B and a 12V battery architecture ... as of Q1 '24"). `tripwire-v2-materials-inventory.csv`, 42 rows. Inventory plus BoM: has "Quantity Req. per Unit" and stock at SF and DC, with formula columns Buildable Units (SF/DC) and Cost per Unit (blank in export). "Date" is empty on every row; "Tags" has no options. Two rows marked "Discontinued" with qty/unit 0 (1000 Ohm resistor, Arducam IR camera); 9V PSU "Purchase link needs update". Retired hardware generation; exported for completeness only.

## Meta: Menlo Park Installation Notes — "BoM Table" (database)

Page https://app.notion.com/p/203dcb3d06b280d39bb1f82db1d7e594 (search timestamp 2025-06-17), states it "will host the high level Bill of Materials (assemblies and fasteners) required for the Meta installation". Database "BoM Table", https://app.notion.com/p/206dcb3d06b2803e9e6afd66efe81c5b, collection://206dcb3d-06b2-8005-a1a1-000bc7e2a7d7, `meta-menlo-park-install-bom.csv`, 11 rows. Columns Name, Quantity, Text (a URL column left with its default name "Text", empty on every row), Notes. Site-specific install BoM (tapcons, washers, enclosure, Cantex box, ULINE bollard, camera and compute assemblies, lag bolts, ground rod and clamp). No part numbers. Not a product BoM; exported because it is a BoM table in Notion.

## Tripwire vπ Assembly SoP (older copy) and V4 X3B Assembly SOP

- https://app.notion.com/p/2cddcb3d06b2800686a9ee2f259aec49, last edited 2026-01-29T17:11:57Z, no parent page in the ancestor path (probably a private or workspace-root page). An earlier copy of "SOP: Tripwire vπ Assembly": same callout dates, generic names ("Modem HAT", "Power Supply HAT" instead of SixFab / Sequent), no SJ1-jumper step. Its Materials block is another linked view of CS3-001-000 (https://app.notion.com/p/2cddcb3d06b28064bcd4de87394bd4a1). Nothing new to export.
- V4 X3B Assembly SOP, https://app.notion.com/p/3c0dcb3d06b280a58518e29d3ee6aac6, last edited 2026-09-11T16:51:44Z: images only, no materials tables; "Coupler Assembly" section empty. Mentions a "3ft M12 17P extension cable" (X3B Assembly BoM lists a 1m M12 cable).

## Database last-edited times from search

`fetch` does not return a last-edited time for databases, but search results carry a `timestamp`. Collected on 2026-11-13: CS3-001-000 2026-05-27T15:19Z; Compute Stack Kit 2026-04-09T20:37Z; SEN2-001-000 2026-04-22T16:00Z; SEN2-002-000 2026-04-09T19:45Z; SEN2-002-000 (1) 2026-05-28T20:21Z; SEN2-003-000 2026-06-29T13:16Z; TB kit 2026-04-23T00:40Z; RR kit 2026-04-23T00:37Z; camera kits 2026-04-09T21:13Z–21:30Z; V3.1 camera "BoM" 2026-07-21T18:50Z; V3.1 sensor-bar "BoM" 2026-04-07T20:02Z; V3.1 Compute Stack BoM 2025-10-30T15:15Z; V4 X3B Manufacturing 2026-08-21T18:10Z, Powder Coating 2026-08-21T18:44Z, Assembly 2026-08-21T19:57Z; V4A Machining 2026-10-06T15:25Z; V4A LiDAR Assembly 2026-10-28T15:51Z; V4 Sensor Kit 2026-11-04T20:12Z; X1 2026-07-31T16:09Z; X2 2026-07-21T18:58Z; SixFab LTE Kit 2025-07-17T13:37Z. Not returned for PIC-001…005, X4A Sensor Interposer PCB, Materials Inventory (OLD, v2) or the Menlo Park BoM Table. Most vπ module and kit databases were created on 2026-04-09 (row IDs 33ddcb3d…), two days after the Procurement Handoff meeting below.

## Which BoM is current, what is retired, numbering and templates

Status statements found (quotes are short, cited):

- **Procurement Handoff, 2026-04-07** (https://app.notion.com/p/33bdcb3d06b280a68278f9e9aaf5ede1, AI meeting summary): "Compute stack BOM exists but needs updates for recent changes (new plastics version transitioned last week)"; "Sensor bar BOM exists within sensor bar assembly"; "Install kits have detailed BOM already (managed by Anthony)"; the **Party HAT BoM "exists as spreadsheet from ECAD software on Josiah's hard drive (not in Notion or Google Drive)"**; "Camera module BOM location unknown"; "All BOMs need updates to reflect current manufacturing versions (mostly fasteners and plastics changes)"; action "Ben and Monty to update bills of materials for current manufacturing versions this week". It also lists the product categories that became the kit BoMs: Packaged Compute Stack (barrel-jack extension separate from the core stack BoM), Packaged Sensor Bars split into retroreflective and through-beam SKUs, Packaged Camera Modules "six variants", Enclosures, Install Kits, Bollard Covers, Bollards and Delineators, packaging, filament (ASA, TPE), acrylic. The vπ kit and module databases were created two days later (2026-04-09), which matches that action item. **No install-kit BoM managed by Anthony was found in Notion**, and no Party HAT BoM.
- **ECN page** (https://app.notion.com/p/31edcb3d06b280b1b6b9f074d6c84b0d): the 2026-03-09 set-screw ECN treats the V3.1 "Sensor Bar (Rescue)" database as the sensor-bar BoM; the 2026-08-13 ECN (RG255C-GL 5G modem, single flex antenna, new wing plastics) post-dates the CS3-001-000 database (last edited 2026-05-27), so **the Notion compute-stack BoM is behind the current build**. The 2026-04-08 ECN retires the single retroreflector variant.
- **V4 LiDAR X1/X2 Documentation**: X1 clamp coupler replaced by X2 screwed coupler (X1 retired). Then X3B (V4 X3B BoM, 2026-08) and X4B/V4A (V4 X4B Assembly SOP and BoM, 2026-09 to 2026-10) follow; the X4B page is the newest V4 assembly. Which V4 revision is in production is not stated.
- **Hardware Stock** (deprecated; production handed to ByTechs LLC). **Materials Inventory (OLD, v2)**, v1/v2 build instructions: retired generations per Tripwire Home.
- **Tripwire V3.1 BoM** page (2025-12-31) still collects the v3.1 camera, sensor bar and compute stack; vπ superseded v3.1 for compute and camera, but the sensor-bar parts and numbers carried over unchanged into vπ SEN2-001-000.
- **Meetings on the migration**: 2026-03-09 "Team to create detailed bill of materials for every package in Notion" (https://app.notion.com/p/31edcb3d06b280288145e96ba5b82b90); 2026-04-10 Aligni evaluation with ByTechs, wanting multi-level BoMs with sub-assemblies (https://app.notion.com/p/33edcb3d06b2800c86e3fe9ab37e509e); 2026-05-06 "Nested bill of materials created : Kit SKUs map to Shopify" (https://app.notion.com/p/358dcb3d06b2801098bee1938ab38e4c, presumably in Aligni); a "Tripwire Leadership Weekly Standup - Template" has a "Shopify → Aligni sync status" line; 2026-10-27 Katana call: "Phase 1: Import items, ingredients, and bill of materials (BOM) into Katana", with Ben to export BoM data from the existing MRP using Katana's CSV templates (https://app.notion.com/p/406dcb3d06b2816da8fed8d0b74e4fb0). Hardware Ops - Team Syncs (2026-11-12) has an agenda line "BOM (multi levels)" next to "Katana". Taken together: Notion BoMs fed Aligni in April–May 2026, and Aligni (not Notion) is the system being migrated to Katana.

Part-numbering schemes seen in Notion (none is written down as a standard except the PIC legend):

- vπ camera: PIC-00N-000 assemblies, PIC-00N-0NN_<ShortName> parts; legend on the vπ Camera page (PIC = vPi Camera; 001 Dual body, 002 Single body, 003 Round bollard mount, 004 Square bollard mount, 005 Wall mount).
- vπ compute: CS3-001-000, parts CS3-001-001…007_<ShortName>.
- Sensor bar (v3.1 and vπ): SEN2-001-000 / -002-000 / -003-000, parts SEN2-00N-0NN_<ShortName>; kits SEN2-TB-Kit, SEN2-RR-Kit.
- v3.1: CAM4-001-0NN (camera) and COM4-001-0NN (compute). The "4" in CAM4/COM4 versus "3" in CS3 is unexplained.
- Bought parts: `EXT-<MPN or distributor PN>` in vπ compute/sensor databases (not used in the camera databases, V3.1 camera/compute, or any V4 database).
- V4/V4A/X1–X4: no internal numbers; vendor PNs or blanks.
- Aligni (from `boms/index.csv`) prefixes all of these with `AG-` and splits camera assemblies and kits by lens option (e.g. AG-PIC-001-000_Dual46, AG-Dual46-WallMount-Kit); Notion has no lens-specific SKUs.

BoM template: no page states a template, but the vπ, V4 X3B and V4A databases share one column set (Part Name, Part Number - Internal, Part Number, Quantity Per Unit, Supplier, Links, Cost, Min Quantity Per Purchase, Cost Per Unit, Notes, Part Number - Mfg), and the X1/X2 databases have a "New page" page template. Older databases (V3.1 camera, X1/X2) use "Name"/"Quantity Per Purchase" instead. The CS3-001-000 database diverges ("Manufacturer Part Number", "Internal Part Number", "Alternate Link"). `docs/boms/plan.md` assumed the Notion column set is the standard; this is consistent with what Notion shows but nothing in Notion says so.

## Export check

The CSVs were written by hand-transcribing rows-mode output into `notion_to_csv.py`, so four of the largest tables were checked against Notion SQL aggregates on 2026-11-13 (row count, sum of quantity, sum of cost, total character length of a text column). All matched: CS3-001-000 (27 rows, qty 38, cost 9.32, internal-PN length 442), X4A Sensor Interposer PCB (18, 18, 68.56, Notes length 4177, Part Number length 226), Materials Inventory (OLD, v2) (42, 85, SF 240, DC 516, cost 469, link length 3453), V3.1 camera (14, 37, 2322.45, Notes 356). The one difference is V3.1 camera internal-PN length 351 vs 353: the ELP cell has a trailing space before each line break that the clean-up strips. All 34 CSVs are rectangular and free of `<p>`, `<b>`, `<u>`, backslash escapes and formula references.

## Not exported, and why

- Plain tables on SOP pages (vπ Camera ×3, vπ Sensor Bar ×4): every assembly they describe has a database (PIC-001/003/004/005, SEN2-001). Differences worth comparing are noted in those sections.
- Hardware Stock tables (×4): stock counts, not BoMs. X1/X2 "Tools required" table: tooling. Standard Deployment Kit: lists without quantities. Bollard Mount Dual Camera Manufacturing Package: numbered lists of printed parts. Contract Manufacturing (ByTechs LLC): assembly labour quotes ("Quantity: 5 units ... $24/unit"), no BoM.
- Formula columns (every "Cost Per Unit", SixFab "Unit Cost Delta", v2 "Buildable Units"/"Cost per Unit"): values not readable through the MCP; columns kept, blank.
- Attachments, not downloaded per the brief: `bollard-hybrid-cable.bom.tsv` (a cable BoM generated by WireViz) plus `.yml`/`.svg`/`.png` on the V4 X4B page; SendCutSend invoice PDF; Bambu `.zip` on the Bollard Mount package page. The cable BoM TSV is the only BoM-like attachment seen.
- Blocks the API could not render: "Part Manufacturing Docs" alias on vπ Camera; an "ai_block" on Tripwire V3.1 BoM.
- Outside Notion: "V3 Materials Inventory" Google Sheet linked from Tripwire Home (v3.0); Party HAT BoM on Josiah's drive (per 2026-04-07 meeting); install-kit BoM "managed by Anthony" (not found in Notion).
- Not opened in full: the v3.1 source pages Camera Glow Up (Cam Housing), Sensor Bar (Rescue) and Compute Stack Case (only their databases), Cellular Connectivity & Hardware for Tripwire 3.x (only its database), V4 Installation SOP (search shows a to-do "Create high level assembly BoM for installers"), Manufacturing Batches, and meeting notes beyond the search highlights quoted above.

## Scope check against Tripwire Home (2026-11-13)

Ben set the scope after the export: every hardware BoM lives under Tripwire Home (https://app.notion.com/p/0afdeb167ec24c0a82661e860449cfa0), so stay inside that subtree. Each of the 34 exported databases has Tripwire Home in its ancestor path, either directly or through a child page; the v2 inventory was confirmed by a row page whose path is "Engineering Home / Tripwire Home / Materials Inventory (OLD, v2)", last edited 2024-02-14T15:47:03Z. No CSV or manifest change is needed.

These sources from the earlier notes are **outside** that subtree. They are context only, not BoMs, and should be weighed as such:

- "Tripwire vπ Assembly SoP" (older copy, https://app.notion.com/p/2cddcb3d06b2800686a9ee2f259aec49): no parent in its ancestor path. Nothing was exported from it.
- Meeting Notes database pages: Procurement Handoff 2026-04-07; Inventory Check-In 2026-05-06; Ben / Britney 2026-10-27; AirGarage / ByTechs / Aligni 2026-04-10; Benjamin / Britney 2026-03-09.
- Hardware Ops - Team Syncs (Operations Home).

The "Which BoM is current" section relies on those meeting notes for the 2026-04-07 BoM status (compute stack needs updates, Party HAT BoM off-Notion, install-kit BoM with Anthony, camera BoM location unknown) and for the Aligni and Katana migration history. Inside the subtree, the status evidence is the ECN page, the X1/X2 page, the "deprecating" callout on Hardware Stock, and the database edit times. I did not search further outside the subtree after the scope note.

