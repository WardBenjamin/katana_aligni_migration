# Camera import duty estimate (ELP order, PI ELPFP2026012704C)

Started 2026-11-13T17:10Z. All sources read 2026-11-13. Times UTC.

## Answer

No actual duty payment was found (Ramp local pull, Ramp connector, Slack). This is an estimate.

| | Duty, 600 cameras | Per camera | Effective rate on $74,160 |
|---|---|---|---|
| Low | $12,978 | $21.63 | 17.5% |
| Likely | $25,956 | $43.26 | 35.0% |
| High | $26,689 | $44.48 | 35% (applied to $76,255 incl. freight) |

Add about $257 merchandise processing fee (formal entry) and an unknown UPS brokerage/disbursement fee. Arithmetic: `scratchpad/2026-11-13-vpi-assembly-price/camera_duty_estimate.py`.

Note on "High": same 35% stack applied to $76,255 (goods + $2,095 freight; only if freight were wrongly or legitimately included in customs value). Duty $26,689; +MPF $264. Per camera $44.48. A bigger high is only possible if the classification or stack is wrong in a way I could not find.

## 1. Entry date

Likely entry 2026-04-16 to 2026-04-17 (US entry via Alaska/UPS), window 2026-04-15 to 2026-04-20. Confidence: moderate-high for April; the exact day is not known.

Evidence:
- PI dated 2026-01-27, lead time 35-45 working days after full payment (proforma). Payment date unknown. Paid early Feb would give about early-to-mid April, consistent with what happened. Chinese New Year 2026 was 2026-02-17, so a factory pause of about 1-2 weeks is likely inside that window.
- #airgarage-bytechs, 2026-04-10T16:04Z, Bryan Monti relays ELP: "We already shipped out the order", 12 cartons, two UPS tracking numbers. Carton counts sum to 600 (50 + 96 + 54 + 336 + 64), so this is the PI order. https://airgarage.slack.com/archives/C09FF4GLH9R/p1775837057811809
- Same thread, 2026-04-15T23:50Z: "These are still in China according to UPS". https://airgarage.slack.com/archives/C09FF4GLH9R/p1776297001894089
- Same thread, 2026-04-17T12:59Z, Chris (Bytechs): "Looks like cameras made it thru Alaska. Says Monday delivery." (Monday = 2026-04-20.) Thread read via slack_read_thread, parent ts 1775836387.012279.
- Same thread, 2026-04-23T16:02Z onward: delivered to Monti, 10 of 12 boxes forwarded to Bytechs, 2 boxes delayed or returned.
- Group DM, 2026-02-20T19:33Z, Josiah: "Did we already pay the huge tariffs on our ELP order?"; Ben: "We have not on our most recent camera order". So the PI order had not entered by 2026-02-20. https://airgarage.slack.com/archives/C08EUD1T2US/p1771615984347319
- Carrier is UPS Express (air), so UPS likely acted as customs broker and billed duty to AirGarage after clearance. Not confirmed.

Not found: payment date, any Ramp transaction or bill to Ailipu/ELP/UPS/DHL for this order. Ramp vendor search found no Ailipu/ELP/DHL Express vendor; FedEx and UPS vendors exist but no UPS transactions 2026-03-25 to 2026-06-01 and no card transactions over $20,000 2026-01-20 to 2026-04-15 in the connector. Local pull only has two DHL "duties" charges of $176.59 (2026-03-31, Wondfo; 2026-06-11, Waveshare LCD), unrelated. The order was probably paid by wire from outside these three people's cards.

Slack context that matters: Josiah, 2026-04-15T23:26Z, "wasn't our last tariff bill on the cameras like $35K?" and 2026-02-20 "$30K". That refers to the earlier ~350-camera order, entered under the 2025 IEEPA stack, not this one. https://airgarage.slack.com/archives/C08EUD1T2US/p1776295590373499 This may be what Ben remembers as "giant tariffs on cameras".

## 2. Classification

Most likely HTSUS 8525.89.30 (heading 8525, "Television cameras ... Other: Television cameras: Other"), column 1 general rate Free. Source: USITC HTS search, saved `data/tariffs/hts_8525.89.json` (HTS Revision 23 (2026), `data/tariffs/ch99.txt` from the same release).
- HQ H332743 (2024-06-21): a digital security camera that streams to external devices and does not record to internal media goes in 8525.89.30, not 8525.89.40. The ELP USB module streams to a host and has no storage, which fits. https://rulings.cbp.gov/ruling/H332743 (API copy `data/tariffs/r_H332743.json`)
- HQ H331315 (2025-12-05): thermal network cameras go in 8525.89.50 ("Other, Other"). Fits as the second option; same Section 301 treatment as .30. https://rulings.cbp.gov/ruling/H331315
- NY N018295 (2007): USB webcam in 8525.80.30 (old numbering for what is now 8525.89.30). Pointer only; not read in full.
- Alternate, less likely: 8525.89.40 "Digital still image video cameras", general Free. It is the only camera line on the lower Section 301 list (List 4A, 7.5%). Used for the low case.
- Other headings (8471.90 machine vision, 8543) not researched; 8525 is the usual home. No CBP ruling on a bare USB camera module with IR LED was found. A broker should confirm.

## 3. Duty stack for entry 2026-04-16 to 2026-04-20

| Measure | Rate | Applies? | Legal basis, dates | Source |
|---|---|---|---|---|
| MFN column 1 | 0% | yes | 8525.89.30 general "Free" | HTS API, `hts_8525.89.json` |
| Section 301 China, List 3 (9903.88.03) | +25% | yes | 8525.89.30 and 8525.89.50 are in the 9903.88.03 list (U.S. note 20(f)). In force through the window. | `ch99.txt` lines 18052, 19560; `hts_9903.88.03.json` ("+25%") |
| Section 301 China, List 4A (9903.88.15) | +7.5% | only if 8525.89.40 | 8525.89.40 is in the 9903.88.15 list (note 20(s)). | `ch99.txt` lines 22188, 22891, 22149 |
| Section 301 exclusions | none | no | No exclusion covers 8525.89.30/.40/.50 in HTS ch. 99 (only old microscope-camera exclusions under 8525.80.3010). | `ch99.txt` ~25503; grep of 8525.89 found only list entries |
| IEEPA fentanyl (China) and reciprocal | 0% | no | EO 14389 (2026-02-20) ended them; CBP stopped collecting 2026-02-24 after the Supreme Court ruling. | https://www.federalregister.gov/documents/2026/02/25/2026-03832/ending-certain-tariff-actions ; `fr_2026-03832.xml` |
| Section 122 import surcharge (9903.03.01) | +10% | yes | Proclamation 2026-02-20, effective 2026-02-24 00:01 EST, expired 2026-07-24 00:01 EDT. 10%, not the 15% statutory maximum. Stacks on Section 301 (note 2(aa)(i)). 8525.89 is not in the exempt lists (exemption list (aa)(ii) has 1,099 codes; none are 8525; the (aa)(iii) list has no 8525). | https://www.whitehouse.gov/presidential-actions/2026/02/imposing-a-temporary-import-surcharge-to-address-fundamental-international-payments-problems/ ; https://www.federalregister.gov/documents/2026/02/25/2026-03824/imposing-a-temporary-import-surcharge-to-address-fundamental-international-payments-problems ; `ch99.txt` lines 15279-15564 |
| Section 232 | 0% | no | No 8525.89 entry in any 232 annex found in HTS ch. 99. Does not stack with Section 122 where it applies, so it matters only if the USB cable were classed as a copper derivative (cable is part of the camera set; unlikely). The 57.5% charged on RJ-12 cables in Slack (2026-06-05) fits 50% copper 232 + 7.5% List 4A; my inference, not verified. | `ch99.txt`; Slack https://airgarage.slack.com (DM Ben Ward / Chris Williamson, 2026-06-05T15:43Z) |
| Later 12.5% layer from 2026-07-24 | n/a | no | After the entry date. Seen in a secondary summary only; not checked. | web search, not opened |

Court activity near the window (secondary sources, not opened): the Supreme Court ruling on IEEPA was 2026-02-20; a secondary summary says the CIT ruled Section 122 unlawful on 2026-05-07 and the Federal Circuit stayed relief 2026-06-11. Unverified. If Section 122 duty were later refunded, the bill would fall to 25%. Importers paid Section 122 at entry; any refund would come later. A 2026-04-15 WSJ headline shared in Slack says an IEEPA refund process begins the following week; IEEPA is not part of this entry, so no refund expected on it.

## 4. Estimate

Dutiable value: $74,160.00, the EXW goods price, which is the transaction value. Excluded: $2,095 air freight (international freight is not dutiable if separately stated) and $20 bank charge. Not known whether the declared value matched the proforma.

- Likely: 8525.89.30, 25% + 10% = 35%. $74,160 x 0.35 = $25,956.00. Per camera $25,956 / 600 = $43.26. Effective rate 35% of goods, 34.0% of the $76,275 invoice total.
- Low: 8525.89.40, 7.5% + 10% = 17.5%. $74,160 x 0.175 = $12,978.00, $21.63 per camera. A second low, if Section 122 were refunded: 25% = $18,540, $30.90 per camera.
- High: 35% on $76,255 (goods + freight) = $26,689.25, $44.48 per camera. The statutory stack cannot go much higher.
- Merchandise processing fee: 0.3464% of value, min $33.58 and max $651.50 for FY2026 (to 2026-09-30). $74,160 x 0.003464 = $256.89. https://www.federalregister.gov/documents/2025/07/23/2025-13869/customs-user-fees-to-be-adjusted-for-inflation-in-fiscal-year-2026-cbp-dec-25-10 . Air freight, so no harbor maintenance fee. UPS brokerage and duty-advance fees: amount unknown, not guessed. A shipment this size needs a formal entry (informal entry limit is $2,500; Ben noted in Slack 2026-06-04 that AirGarage had imported under informal rules, which would not hold at $74K).

Why the bounds: date (April is solid; any day 2026-04-15 to 04-21 gives the same stack, since nothing changed in that window), classification (25% vs 7.5% list), and whether Section 122 was later refunded.

"(Tax Included)" on the $2,095 delivery line: could mean Chinese VAT or export taxes are in the freight price (normal), or that the seller quoted DDP (US duty included). The $2,095 for about 177 kg by air express (12 cartons, 13+12.8x2+14.3+12.7x7+17 kg) is about $12/kg, which looks like freight alone; US duty of $13-26K cannot be in it. Ben says duty was paid separately, so treated as not included.

## 5. What would settle it

CBP Form 7501 entry summary for the UPS entry of the two tracking numbers 1Z64W3460494806172 and 1Z64W3460428084853 (entry date, HTS, value, duty lines). Or the UPS Customs Brokerage invoice/duty bill for April 2026. Holders: Bryan Monti (received the shipment and signed up for UPS and DHL updates) and whoever pays UPS bills; also UPS Customs Brokerage online account, or the ACE portal if AirGarage has a broker bond. Ben can also check the AirGarage bank statement for a UPS debit around 2026-04-17 to 2026-04-30.

## Unverified

- Section 122 15% rumour: whitehouse.gov proclamation and the HTS 9903.03.01 text both say 10%. Secondary sources disagree; not used.
- CIT / Federal Circuit rulings on Section 122 (secondary only).
- Whether UPS used the HTS code I assumed.
- Slack search was keyword-limited; the user's other channels or UPS emails may hold the duty bill.
