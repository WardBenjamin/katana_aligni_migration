# BOM reconciliation: Aligni vs every other source

As of 2026-11-13 (UTC). Aligni snapshot 2026-11-13T03:25Z (`boms/`, commit e13d88b). Sources and how each was read: [data-sources.md](data-sources.md). Evidence: `research/` notes, each finding cited there.

## Summary

- Aligni holds 30 active vπ BOMs (12 assemblies, 18 kits). Line by line they match Notion on 140 of 154 lines (`scratchpad/2026-11-13-bom-reconciliation/out/aligni_vs_notion_*.csv`). Where the two disagree, Slack says Aligni is right except for the compute stack, the reflector part and the RJ-12 cable.
- Aligni is behind the build on the compute stack: no Party HAT, USB bridge, modem bridge, Pi cooler, 18650 batteries, GPIO spacer or Party HAT to watchdog wire. Notion is behind in the same way.
- Not in Aligni at all: every PCB assembly (Party HAT, bridges, sensor bar I/O breakout, bollard interposer, compute-stack bollard interface), all V4 / Obelisk hardware, the 6 install packs and the V4 install kit, the aerial camera bundle. Their BOMs live in KiCad, Notion and the "Install Packs" Google Sheet.
- Aligni's last bill was paid 2026-11-10 (Slack, #tripwire-leadership). The snapshot in `scratchpad/2026-11-13-aligni-bom-export/data/20261113T0325Z/` may be the last full pull.

## Per assembly (Aligni active revisions)

Status: **OK** = matches the build as far as the sources show; **Fix** = Aligni needs a change; **Decide** = sources conflict and a person must choose.

| Assembly | Rev | Status | What differs | Fix for Katana |
|---|---|---|---|---|
| AG-CS3-001-000 vπ Compute Stack | B | Fix | Matches Notion (I425-GL and EG25-G listed as alternates; Notion leaves the power cable qty blank). Both lack Party HAT X5C, USB-A Bridge X3, Modem Bridge X3, Pi cooler, batteries, GPIO spacer, Party HAT to watchdog wire (Slack 2026-04-02 parts list; Chris 2026-05-26 "add partyhat, modem bridge, and usb bridge to Aligni"). Draft rev C "Adding electronics" is identical to B. The 2026-08-13 RG255C modem and single-antenna change is a placeholder and not built (Monti, #pt-tripwire). Watchdog HAT `EXT-SM-I-003` is now V11, same SKU. Wing plastics: switched to the new rev 2026-08 (fits old antennas); dropping the GPS antenna was agreed but not confirmed. | New revision: add the PCBAs as sub-assemblies (BOMs from `data/ecad/`), cooler, batteries, spacer, wire; confirm antennas. Do not import RG255C as released. |
| AG-CS3-Kit | A | OK | Matches Notion. A "new power supply SKU" promised 2026-08-17 is never named. | Confirm PSU `EXT-L6R36-120` is still current. |
| AG-PIC-001-000_Dual46, _Dual68 | A | OK | Notion has one generic "ELP Camera (4/6/8mm)" line at qty 2; Aligni splits by lens. | None. |
| AG-PIC-002-000_Single4/6/8 | A | OK | Matches. | None. |
| AG-PIC-003-000, AG-PIC-004-000 bollard mounts | A | OK | Notion also lists the ULINE bollard at qty 0 (reference). ECN 2026-09-10 changed the base mount (weld-bead slot) with no new part number or revision. | Bump the base-mount revision in Katana, or record that rev A includes the slot. |
| AG-PIC-005-000 wall mount | A | OK | Matches Notion. MCAD has two "Camera Yaw Pitch Mount" files with no part in either BOM. | Check with Monti. |
| 6 dual-camera kits | A | OK | Wall-mount dual kits: Notion lists the single module (typo); Aligni has the dual module, fixed 2026-04-30 (Ben/Monti DM). | None in Aligni; fix the Notion typo. |
| 9 single-camera kits | A | OK | Matches. Shopify titles them "Single Camera - Reverse (Assembled)". | None. |
| AG-SEN2-001-000 sensor bar | A | OK | Matches Notion line for line. ECN 2026-08-14 added a screw on the fork mount; counts not checked. | Recount fasteners against the build. |
| AG-SEN2-002-000 retroreflector | C | Decide | Aligni 4x `EXT-E39-R1` (changed from 1x E39-R2 on 2026-06-29); Notion 1x E39-R2; stock, the October order and the Shopify title are E39-R1S. Chris said 4 reflectors per build; Aligni gives 8 per RR kit (2 retroreflectors x 4). | Pick E39-R1 or E39-R1S and the per-kit count. |
| AG-SEN2-003-000 sensor enclosure | A | Fix | Part numbers match Notion (Notion's names are half-edited). Pins (Essentra 27PIF0089, 4) and 3/4 in knock-out seals (2) are in neither; ByTechs packs them in install packs (Monti 2026-05-28). | Add pins and seals to the enclosure or to the install packs. |
| AG-SEN2-RR-Kit | C | Fix | No power supply, as decided 2026-03-09; Notion still lists one. RJ-12 8 ft `EXT-CS-44050-08` is being replaced by 15 ft ("All 15 is good", 2026-11-12). | Swap to the 15 ft cable. |
| AG-SEN2-TB-Kit | A | Fix | Matches Notion (2 bars, 1 PSU for the emitter). Same RJ-12 change. | Swap to the 15 ft cable. |

## Missing from Aligni

| Item | BOM lives in | State |
|---|---|---|
| Party HAT X5C | `data/ecad/party-hat.csv` (KiCad, 37 lines); ByTechs holds a pick-and-place list (Chris 2026-10-29) | C10 shares DigiKey PN 1276-1135-2-ND with C11, C12, C16 although the MPNs differ. |
| USB-A Bridge X3, Modem Bridge X2/X3 | `data/ecad/hat-usb-bridge.csv`, `modem-bridge.csv` | Title blocks say X2/X1; commits say X3/X2; Slack says Modem Bridge X3 in production. Modem bridge has no schematic of its own. |
| Sensor bar I/O breakout X2 | `data/ecad/sensor-bar-io-breakout.csv` | Aligni has the part `AG-SEN2-001-001_Breakout` but no BOM. |
| Bollard interposer (V4) | KiCad main and PR #27; Notion "X4A Sensor Interposer PCB" | Notion is newer (R1, R3, D2, C1, R6 changed); those values are in no branch. PR #27 changes layout only. |
| Compute-stack bollard interface (V4) | KiCad PR #28 only | New board, no BOM anywhere. |
| V4 / Obelisk: X3B, X4B/V4A machining and LiDAR assembly, V4 sensor install kit | Notion (`data/notion/v4-*.csv`, `v4a-*.csv`) | No internal part numbers; install kit has no part numbers, suppliers or costs. Shopify sells "v4 Sensor Bar Assembly". Obelisk is design-only. |
| Install packs RR-BM, RR-WM, TB, each with and without reverse camera (6) | Google Sheet "Install Packs", tab SKUs (`data/sheets/`) | 13 items each, no part numbers. Shopify SKUs sit on the wrong products (`RRWMIPDC` on TB-IP-DC, `RRBMIPDC` on RR-WM-IP-DC); four packs have no SKU. A V4 column was reported added 2026-11-04 but was not in the sheet on 2026-11-13. |
| V4 install packs v4-BM-IP-DC, v4-WM-IP-DCR | Shopify only | Disputed 2026-11-06: V4 units ship with their own hardware. |
| Aerial camera bundle and its two install packs | Slack 2026-02-17 description only | No BOM. |
| V3.1 camera, sensor bar, compute stack | Notion `tripwire-v3-1-*.csv` | Legacy; Shopify archived. |

## Data quality to fix before import

- Item code `PIC-001-005` names four parts (`_DualWinMount`, `_ELPCam4/6/8`); `SEN2-001-002` unused.
- `EXT-` parts use DigiKey numbers (`732-10422-ND`, `952-3964-ND`, ...) and Amazon ASINs as manufacturer part numbers; `EXT-SC1113` (Raspberry Pi 5) lists the reseller as manufacturer.
- Only 12 of 105 Aligni parts have a cost; none have lead time or reorder quantity.
- Shopify: install-pack SKUs on the wrong titles; `AG-SEN2-002-000` titled E39-R1S; sensor bar kits under "V3.1 Sensor Bar Assembly".

## Part numbers and revisions

Aligni part numbers are the standard: `AG-<family>-<assembly>-<item>_<suffix>` for our parts, `EXT-<vendor PN>` for bought parts, `-Kit` for shippable kits that are also Shopify SKUs. CAD release files should carry the same part number with an `_X<n>` revision tag (Ben, #airgarage-bytechs-hardware-chat, 2026-09-21). V4, install packs and PCBAs have no part numbers yet.

## Decisions needed

1. Reflector: E39-R1 or E39-R1S, and how many per RR kit.
2. Compute stack: confirm antennas (drop GPS?), and that the PCBAs go in as sub-assemblies with their own BOMs.
3. Pins and knock-out seals: enclosure BOM or install pack.
4. V4 install packs: real SKUs or not.
5. Part numbers for PCBAs, install packs and V4 parts before they enter Katana.
6. Whether V3.1 and Obelisk go into Katana at all.
