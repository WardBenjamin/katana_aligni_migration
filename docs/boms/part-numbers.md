# Part numbers

As of 2026-11-13 (UTC). Status: **proposed**, for Ben to confirm. Every number below is already used in the corrected BOM set (`boms/`), so changing one means editing `RENAME`, `IP_ITEMS`, `V4` or the `bom(...)` calls in `scratchpad/2026-11-13-bom-reconciliation/build_boms.py` and rebuilding.

## Rules (unchanged from Aligni)

- Our parts: `AG-<FAM>-<NNN>-<III>[_<Suffix>]`. `FAM` is the subsystem and its generation (CS3 compute stack, PIC vπ camera, SEN2 vπ sensor bar). `NNN` numbers an assembly in the family; `III = 000` is the assembly itself and `001` up are its items. The suffix is a short readable name.
- Bought parts: `EXT-<maker part number>`, or the vendor's number when there is no maker number (Amazon ASIN, McMaster number). Unknown ones are `EXT-TBD-<what>` until someone finds the number.
- Shippable kits, which are also the Shopify SKUs: `AG-<name>-Kit`.
- Revisions are not in the part number. BOM revisions are letters (A, B, C); PCBAs and machined assemblies keep their design revision (X5C, X4A, X5), and CAD files carry `_X<n>` (Ben, Slack 2026-09-21).

## New numbers

### PCBAs (sub-assemblies with their own BOMs)

| Part number | What | Design rev | Bare board |
|---|---|---|---|
| AG-CS3-002-000_PartyHAT | Party HAT PCBA | X5C | AG-CS3-002-001_PCB |
| AG-CS3-003-000_USBBridge | USB-A (HAT) Bridge PCBA | X3 | AG-CS3-003-001_PCB |
| AG-CS3-004-000_ModemBridge | Modem Bridge PCBA (flex) | X3 | AG-CS3-004-001_PCB |
| AG-SEN2-004-000_Breakout | Sensor Bar I/O Breakout PCBA | X2 | AG-SEN2-004-001_PCB |
| AG-SEN4-002-000_Interposer | V4 Sensor Interposer PCBA | X4A | AG-SEN4-002-001_PCB |

Components on these boards are `EXT-<MPN>` from the KiCad symbol fields (Notion for the interposer). PCBAs sit in the family of the product they go in, so the Party HAT is the compute stack's assembly 002.

### Compute stack items added to AG-CS3-001-000

`AG-CS3-001-008_GPIOSpacer` (3D printed), `AG-CS3-001-009_SWDWire` (Party HAT to watchdog HAT wire), `EXT-SC1148` (Pi 5 active cooler), `EXT-INR-18650-P30B` (Molicel 18650, qty 2 from the V3.1 BoM).

### V4 sensor: family SEN4

Named for the V4 product. `SEN3` would continue SEN2's count instead; either works, SEN4 is easier to read next to "V4".

| Part number | What |
|---|---|
| AG-SEN4-Kit | V4 Sensor Kit (shippable; the Shopify product "v4 Sensor Bar Assembly" gets this SKU) |
| AG-SEN4-001-000 | V4 LiDAR Sensor, X5 |
| AG-SEN4-001-001_Housing, -002_TopCover, -003_PCBMount | Printed LiDAR housing, top cover, coupler PCB mount |
| AG-SEN4-001-004_Heatsink | LiDAR heatsink (SendCutSend) |
| AG-SEN4-001-005_Coupler, -006_LiDARCoupler, -007_ExtTube | Machined parts (Triple B) |
| AG-SEN4-002-000_Interposer | Sensor interposer PCBA (above) |
| AG-SEN4-003-000 | V4 Sensor Install Kit (ships in the V4 box) |

### Install packs: family IP

A full pack is the base set plus its add-on (Ben 2026-11-13), so each pack kit has two lines: `AG-IP-001-000` and its add-on. The wall-mount RR pack is the base set alone.

| Part number | What | ByTechs code | Shopify product today |
|---|---|---|---|
| AG-IP-001-000 | Base set | RRWMIPDC column | n/a |
| AG-IP-002-000 | Add-on: RR bollard mount | RRBMIPDC | n/a |
| AG-IP-003-000 | Add-on: through beam | TBIPDC | n/a |
| AG-IP-004-000 | Add-on: RR bollard mount, reverse camera | RRBMIPDCR | n/a |
| AG-IP-005-000 | Add-on: RR wall mount, reverse camera | RRWMIPDCR | n/a |
| AG-IP-006-000 | Add-on: through beam, reverse camera | TBIPDCR | n/a |
| AG-IP-001-001_Washer | Custom bollard washer (SendCutSend; CAD in tripwire-mcad `Installer Kits/`) | | |
| AG-IP-RRWM-DC-Kit | RR-WM-IP-DC pack | RRWMIPDC | SKU today `RRBMIPDC` (wrong) |
| AG-IP-RRBM-DC-Kit | RR-BM-IP-DC pack | RRBMIPDC | no SKU |
| AG-IP-TB-DC-Kit | TB-IP-DC pack | TBIPDC | SKU today `RRWMIPDC` (wrong) |
| AG-IP-RRBM-DCR-Kit | RR-BM-IP-DCR pack | RRBMIPDCR | no SKU |
| AG-IP-RRWM-DCR-Kit | RR-WM-IP-DCR pack | RRWMIPDCR | no SKU |
| AG-IP-TB-DCR-Kit | TB-IP-DCR pack | TBIPDCR | no SKU |
| AG-IP-V4BM-DC-Kit | v4-BM-IP-DC pack = 1x AG-IP-RRBM-DC-Kit | | no SKU |
| AG-IP-V4WM-DCR-Kit | v4-WM-IP-DCR pack = 1x AG-IP-RRWM-DCR-Kit | | no SKU |

The V4 packs use your first option (one vπ pack as a part). The bollard-mount mapping brings the RR pack's reflector-bollard tapcons and washers along; if a V4 lane has no reflector bollard, the V4 pack should point at a different add-on. ByTechs' short codes could stay as the SKUs instead; the `AG-…-Kit` form keeps every shippable item in one pattern.

### Legacy and draft (not migrated)

- V3.1: `AG-CAM4-001-000` (camera assembly) and `AG-COM4-001-000` (compute stack), keeping V3.1's own CAM4/COM4 item numbers. The V3.1 sensor bar is `AG-SEN2-001-000`, the same parts and numbers as vπ.
- Obelisk: family `OBL`. `AG-OBL-001-000` (Obelisk, draft skeleton), `AG-OBL-002-000_CSInterface` (compute-stack bollard interface PCBA from tripwire-ecad PR #28; product assumed), `AG-OBL-003-000_CameraModule`, `AG-OBL-001-001_Tube`, `-002_VampClamp`, `-003_SnapRing`.

## Renumbered

| Aligni | New | Why |
|---|---|---|
| AG-PIC-001-005_ELPCam4 | AG-PIC-001-007_ELPCam4 | `PIC-001-005` named four parts |
| AG-PIC-001-005_ELPCam6 | AG-PIC-001-008_ELPCam6 | same |
| AG-PIC-001-005_ELPCam8 | AG-PIC-001-009_ELPCam8 | same; `AG-PIC-001-005_DualWinMount` keeps 005 |
| AG-SEN2-001-001_Breakout | AG-SEN2-004-000_Breakout | Now an assembly with a BOM and a bare board |

Stock held under the old numbers moves to the new ones at the Katana import. None of them is a Shopify SKU. `boms/items.csv` has a `Renamed From` column.

## Placeholders to fill (`EXT-TBD-*`)

RJ-12 15 ft and RJ-45 15 ft cables; both Tapcons (vendor pages give no maker number); V4 kit T27 self-drilling screw, T27 impact bit, 7/32in drill bit, 1/2in Tapcon and washer; V4 sensor T27 1/4-20 screw and thermal pad; connectors without an MPN in KiCad (USB bridge J2, modem bridge P5 and P6, sensor breakout J1); the Obelisk parts. `grep EXT-TBD boms/items.csv` lists them.
