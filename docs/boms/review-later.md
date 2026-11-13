# BOM items for later review

As of 2026-11-13 (UTC). Things Ben chose to defer: each is built into `boms/` as described, so the Katana import can go ahead, and should be revisited. Placeholder part numbers (`EXT-TBD-*`) are listed separately in [part-numbers.md](part-numbers.md#placeholders-to-fill-ext-tbd).

| # | Item | As built now | Why review | Who |
|---|---|---|---|---|
| 1 | V4 install packs | `AG-IP-V4BM-DC-Kit` = 1x `AG-IP-RRBM-DC-Kit`; `AG-IP-V4WM-DCR-Kit` = 1x `AG-IP-RRWM-DCR-Kit` | The RR bollard pack carries reflector-bollard Tapcons and washers that a V4 lane may not need. Ben 2026-11-13: "Not sure, work with this for now". Slack 2026-11-06 left the V4 pack contents disputed. | Ben, ByTechs |
| 2 | V4 sensor X5 BOM | `AG-SEN4-001-000` (rev X5) joins the Notion V4A LiDAR Assembly, V4A Machining and V4 X3B Assembly BoMs | Ben 2026-11-13: largely the same as X5, but X5 has design revisions that should have been released to `tripwire-mcad`. The repo's `V4-release/X5 Release/` has an internal coupler, Vamp Clamp, main housing and top hood; none is in a BoM. Release the X5 CAD, then update the BOM. | Monti |
| 3 | V4 interposer design files | `AG-SEN4-002-000_Interposer` (X4A) from the Notion BoM | Notion's X4A values (R1 6.8k, R3 1M, D2 SMAJ28A, C1 10nF 1kV, R6 10k) are in no `tripwire-ecad` branch; main and PR #27 have the older values ([research/ecad-open-prs.md](research/ecad-open-prs.md)). Same pattern as item 2: released hardware not in the repo. | Monti |
| 4 | Modem Bridge X3 design files | `AG-CS3-004-000_ModemBridge` (X3) from the X2 schematic | X3 (flex) is in production but not in `tripwire-ecad`. | Ben |
| 5 | Nylocks per enclosure | 2 per enclosure in the sensor bar kits (Ben 2026-11-13) | Both install-pack sheets listed M6 nylocks at 4 per RR and 8 per TB pack ("secure sensor bar to enclosure base"). ByTechs may still pack 4. | ByTechs |
