# ELP, Haig and MakerBright documents from Ben

Written 2026-11-13T17:00Z. Ben put four more PDFs in `scratchpad/` on 2026-11-13. They are now under `scratchpad/2026-11-13-vpi-assembly-price/data/invoices/`. All have a text layer and were read with `pdftotext -layout`. A second copy of `OrdAck1426189.pdf` arrived with them; it was byte-identical to the one already filed (`cmp`) and was removed.

## ELP cameras: `elp/Ailipu PI NO.ELPFP2026012704C-1.pdf`

Proforma invoice ELPFP2026012704C from Shenzhen Ailipu Technology Co., Ltd, dated 2026.1.27, to AirGarage (attn. Bryan Monti). Payment in full before shipment; lead time 35 to 45 working days after payment. A proforma invoice is an offer to sell; the document does not show that it was paid.

| Model | Description | Qty | Unit | Total |
|---|---|---|---|---|
| ELP-USBGS5MP01-KV100IR | 5MP global shutter USB camera, V100 lens, IR LED, 5 m USB cable | 50 | $123.60 | $6,180.00 |
| ELP-USBGS5MP01-KL60IR | same, 6 mm lens | 400 | $123.60 | $49,440.00 |
| ELP-USBGS5MP01-KL80IR | same, 8 mm lens | 150 | $123.60 | $18,540.00 |

Total EXW $74,160.00; delivery by air express, tax included, $2,095.00; bank charge $20.00; total $76,275.00. Landed per camera: $123.60 x 76,275 / 74,160 = $127.125.

- Each line reads "with ... IR LED & 5m usb cable", so the cable `AG-PIC-001-006_ELPCamUSB` is priced at $0.00 as included.
- Each line also says the camera is customized to control the IR LED and IR cut filter independently through I/O.
- KV100IR is taken as the 4 mm camera `AG-PIC-001-007_ELPCam4`, following the V3.1 camera note in `boms/index.csv` ("KV100IR (4mm)"). The proforma does not state a focal length for the V100 lens.
- The proforma names the 6 mm and 8 mm cameras KL60IR and KL80IR; the same `boms/index.csv` note calls them KV60IR and KV80IR.
- The date is before 2026-05-14, so the roll-up marks the cameras stale.

## ELP lenses: `elp/Ailipu PI NO.ELPFP2026011501C-1.pdf`

Proforma invoice ELPFP2026011501C, dated 2026.1.15: 75 x 8 mm M12 lens at $4.00, 50 x 6 mm M12 lens at $4.00, one 8 mm and one 12 mm C-mount lens at $31.00 each. Total EXW $562.00; UPS delivery $108.00; bank charge $20.00; total $690.00. Loose lenses are in no BOM, so nothing in the roll-up uses them. Typed into `invoice_lines.csv` for the record.

## Wall-mount camera bracket: `haig/Inv.98995.pdf`

Haig Precision Mfg. Corp. invoice 98995, dated 06-Oct-26, ship to ByTechs, will call.

- 56 x "Wall Mount Dual Camera(5) Brkt", powdercoat black Cardinal P004-BK02, 5052 aluminium, part "CAMERA MOUNT (5)", job 42402: $45.11 each, $2,526.16.
- Santa Clara Co. sales tax $252.62. Invoice total $2,778.78. Landed each: $49.62.
- This is `AG-PIC-005-001_WallBracket` in `AG-PIC-005-000` (vπ Wall Mount). It is not in the round-bollard configuration, so the current total does not change. A rule is in `price_rules.csv` for when a wall-mount configuration is priced.
- This is not the sensor enclosure. No Haig document for the enclosure base and top has been supplied.

## Raspberry Pi and cooler: `makerbright/Invoice_1381.pdf`

MakerBright invoice 1381, dated 06/Nov/2026, bill to AirGarage c/o ByTechs, balance due $58,725.00.

| Item | Description | Unit | Qty | Total |
|---|---|---|---|---|
| SC1113 | Raspberry Pi 5 (16GB) | $385.00 | 150 | $57,750.00 |
| SC1148 | Raspberry Pi Active Cooler | $6.50 | 150 | $975.00 |

No tax or shipping line. The invoice terms say sales tax is collected only in Florida and North Carolina and that use tax elsewhere is the buyer's responsibility.

- The $385.00 matches the price Ben gave earlier the same day, so the manual quote was removed from `manual_prices.csv` in favour of this invoice.
- The cooler moves from a stale $5.62 (Digi-Key, 2025-04-23) to $6.50.

## Effect on the roll-up

Query: `uv run --python 3.15 price_config.py configs/rr-bollard-dual46.csv --as-of 2026-11-13`. Result: `out/rr-bollard-dual46_price_lines.csv`.

- Priced: $1,706.57 (was $1,451.45). $1,007.45 on prices inside six months, $699.12 on older ones.
- 71 of 124 leaf parts priced; 54 part rows and 12 labour rows unpriced.
- Reflectors stay at the Digi-Key price of $26.11 on Ben's instruction (2026-11-13: "our most recent source"), not Powermatic's $20.94.
