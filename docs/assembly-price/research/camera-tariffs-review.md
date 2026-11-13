# Review of the camera duty estimate

Written 2026-11-13T17:30Z. [camera-tariffs.md](camera-tariffs.md) was written by a Sonnet research agent. This note records what was checked afterwards, by Claude in the main session, and how the estimate was used. Files named below are in `scratchpad/2026-11-13-vpi-assembly-price/`.

## Checked against the saved documents

- `data/tariffs/hts_8525.89.json`: 8525.89.30.00, 8525.89.40.00 and 8525.89.50 all show a general rate of "Free".
- `data/tariffs/hts_9903.88.03.json`: general rate "The duty provided in the applicable subheading + 25%".
- `data/tariffs/ch99.txt` (HTS Revision 23 (2026)): line 18052 opens U.S. note 20(f), "Heading 9903.88.03 applies to all products of China that are classified in the following 8-digit subheadings"; line 19560 in that list reads "8525.82.00 8525.83.00 8525.89.30 8525.89.50". Line 22891 lists 8525.89.40 under the note for heading 9903.88.15.
- `data/tariffs/hts_9903.03.json`: heading 9903.03.01, general rate "+ 10%", "articles the product of any country". `ch99.txt` line 15280: headings 9903.03.01 to 9903.03.11 "expired at the close of July 23, 2026". Lines 15279 to 15900 (the note for these headings) contain no "8525" and no "15 percent".
- `data/tariffs/s122_proclamation.txt`: "I impose, for a period of 150 days, a temporary import surcharge of 10 percent ad valorem ... effective February 24, 2026".
- A fourth list in `ch99.txt` (line 37469) names all of 8525.89.20 to .50. It belongs to headings 9903.03.12 to 9903.03.16, which are products of Canada, so it does not apply.
- Slack thread C09FF4GLH9R, parent ts 1775836387.012279, re-read with `slack_read_thread`: ELP's packing list is 50 KV100IR, 150 KL80IR and 400 KL60IR in 12 cartons on two UPS tracking numbers, the same quantities as the proforma; later replies say the cameras were "still in China", then "made it thru Alaska", then delivered.
- Arithmetic: `uv run --python 3.15 camera_duty_estimate.py` reproduces $12,978.00, $18,540.00, $25,956.00 and $26,689.25, and a processing fee of $256.89.

## Not checked

- The Ramp connector searches and the other Slack messages the agent cites.
- The two CBP rulings (saved as `data/tariffs/r_H332743.json` and `r_H331315.json`, not re-read).
- The merchandise processing fee minimum and maximum, which the agent took from a search snippet. The 0.3464% rate gives $256.89, between the two, so they do not affect the figure.
- Everything the agent itself lists as unverified: the code UPS actually declared, the declared value, and the later court rulings on Section 122.

## How it is used

- `price_adders.csv` adds $43.69 per camera: $43.26 duty (35% of $123.60) plus $0.43 processing fee ($256.89 / 600). It is dated 2026-04-17, the likely entry date, so the roll-up marks it "stale estimate".
- With it, one camera lands at $127.13 + $43.69 = $170.81.
- The estimate describes the April 2026 order. Section 122 expired at the close of 2026-07-23, so an order placed now would face a different stack. What replaced it was not researched.
