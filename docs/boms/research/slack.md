# Slack: BOM changes, current versions and decisions

Started 2026-11-13 (UTC). Read-only via the Slack MCP (search, read channel, read thread). Window 2025-10-01 to 2026-11-13, weighted to 2026-07 onward. Times are UTC. Quotes are at most ~25 words. Attachments not downloaded; names and permalinks noted. Machine-readable list: `scratchpad/2026-11-13-bom-reconciliation/data/slack/events.csv`.

Channel IDs (found with `slack_search_channels`, 2026-11-13):

- #airgarage-bytechs C09FF4GLH9R (private)
- #airgarage-bytechs-hardware-chat C0C1WC7D468 (private, created 2026-09-14)
- #airgarage-bytechs-tripleb-v4-hardware C0C1C27RFP1 (public, created 2026-09-14)
- #pt-tripwire C04PDLL3GAF (public)
- #pt-obelisk C0C7J22K5PT (public, created 2026-10-07)
- #pt-v4-sensors C0ARYAA2FNF (public, created 2026-04-10)

## #airgarage-bytechs-hardware-chat (C0C1WC7D468)

Read the whole channel, 2026-09-14 (creation) to 2026-11-12T20:49Z, about 330 messages, plus threads below. Slack Connect channel with ByTechs (Chris Williamson); Ben, Monti. Base URL for permalinks: `https://airgarage.slack.com/archives/C0C1WC7D468/p<ts>`.

- 2026-09-17T19:28Z, Ben, compute stack: "Modem Bridge X4 changes" thread. Planned: "remove unused traces, shrink the paste apertures on the 5-pin THT USB header", update version marking; Chris says micro-USB wicks solder. https://airgarage.slack.com/archives/C0C1WC7D468/p1789673299388479
- 2026-09-21T16:45Z, Ben, all assemblies (MCAD release naming): "All of these should ideally be the same part number as we use in Aligni/BOMs tagged with a revision _X<n>". Context: Chris printed 24 compute-stack faces and 2 wall mounts "the wrong rev". https://airgarage.slack.com/archives/C0C1WC7D468/p1790009100556319
- 2026-09-21T23:01Z, Ben, V4 sensor kit: "for v4 sensors, can we include an RJ-12 and RJ-45 cable in each box?" Chris then sources 8 to 10 ft Cable Matters Ethernet; Ben: "step up to 10ft". https://airgarage.slack.com/archives/C0C1WC7D468/p1790031709845179
- 2026-09-21T23:41Z, Ben, compute stack: "considering having us fix up the form factor and reduce the BOM on the compute stack" (FFC, Sequent HAT changes), for Q4. https://airgarage.slack.com/archives/C0C1WC7D468/p1790034110675289
- 2026-09-22T13:47Z, Chris, compute stack stock: "15x seq hat old version 40x seq hat new version 52x partyhat 75x sixfab hats ... ~50 of each antenna". As of this date stacks still use the SixFab HAT and two antennas. https://airgarage.slack.com/archives/C0C1WC7D468/p1790084845779609
- 2026-09-24T00:55Z, Chris, Party HAT: next-rev idea, "Attach the USB bridge via flex, all in one." Attachment `Screenshot_20260923_205422_Chrome.jpg` (F0C448K59SM). https://airgarage.slack.com/archives/C0C1WC7D468/p1790211321868949
- 2026-10-07T00:13Z, Monti, wall mount (PIC-005-001): "Camera wall mount brackets finished up at Haig ... total of 56 brackets". 2026-10-09: Monti says old brackets can still be used for Meta. https://airgarage.slack.com/archives/C0C1WC7D468/p1791332020915919
- 2026-10-08T13:24Z, Ben, compute stack: "I ordered more of the same rev of modem bridges (160x) and USB bridges (120x); haven't had time to prioritize a new rev". So Modem Bridge X4 was not built as of then. https://airgarage.slack.com/archives/C0C1WC7D468/p1791465840018219
- 2026-10-21T17:04Z, Ben forwards a TripleB-channel post (LiDAR housing printing) here, "sans TripleB": machining topics stay in the TripleB channel until an NDA is signed. Chris asks to "list all hardware needed for V4 install kits here". https://airgarage.slack.com/archives/C0C1WC7D468/p1792602276361989
- 2026-10-24 to 2026-10-30, V4 LiDAR housing build: adhesive moves from Maxibond panel bond to 3M Scotch-Weld (DP8425NS suggested, 8810NS/8407 discussed; McMaster 7467A88), weatherstripping on the support bracket, NinjaTek TPE for gaskets, textured vs gloss powder coat (Ben: maybe switch to gray). Not in any BOM yet.
- 2026-10-30T14:15Z, Ben, V4 sensor kit and Obelisk: "we're committed to those screws for all v4 sensor couplers and for all Obelisk couplers" (1 in self-tapping stainless screws, Tanner Bolts, matching McMaster; T27 bits). https://airgarage.slack.com/archives/C0C1WC7D468/p1793369724787719
- 2026-11-03, Ben: "transition immediately to a vamp clamp extension tube and bollard coupler" for V4. Not yet a BOM.
- 2026-11-04T20:09Z, Chris/Monti, V4 Sensor Install Kit: the kit BoM is the Notion page "V4 Sensor Install Kit BoM" (https://app.notion.com/p/airgarage/V4-Sensor-Install-Kit-BoM-3f0dcb3d06b28127ac28ce13354bea62). Chris added 4x tapcons, washers, 7/32 in HSS stub drill bit and Tanner screw links that day; ByTechs prints it to pack kits. Monti's RJ-12 wire: Amazon B0D224XJ1Z. https://airgarage.slack.com/archives/C0C1WC7D468/p1793822988408399
- 2026-11-04, Chris orders 50x Amphenol MSAS-17PMMP-SF8001 (M12 17-pin) from Mouser for V4; Ben wants to talk about cutting M12 off and repinning to JST-PUD.
- 2026-11-09T20:52Z, Monti, camera module (next rev): "Current camera cables are JST-PH. For camera module we're planning to make JST-PH to JST-PH", plus a JST-PH/XA to USB-A cable. https://airgarage.slack.com/archives/C0C1WC7D468/p1794257553517599
- 2026-11-11, Chris: "knock out ~50x party hats with old pcbs i have" (rev not named).
- 2026-11-12T20:49Z, Ben, sensor bar kits: Chris asks whether to keep 8ft RJ-12 or move "all to 15ft"; Ben: "All 15 is good". The 8ft cable `EXT-CS-44050-08` in both Aligni sensor-bar kits is being replaced by a 15ft cable. https://airgarage.slack.com/archives/C0C1WC7D468/p1794516579631739

## #temp-katana-onboarding (C0CGR5LKQ95), not on Ben's list

Created 2026-11-12 by Britney ("onboarding plan, project milestones, + working space for Katana onboarding between HOps, Eng, and CM"). Only join and topic messages so far; nothing about BOMs. Read whole channel.

## #airgarage-bytechs-tripleb-v4-hardware (C0C1C27RFP1)

Read the whole channel, 2026-09-14 (creation; renamed from "v4-hardware" 2026-09-28) to 2026-11-12T02:44Z, about 470 messages; threads not opened except where noted. Slack Connect with ByTechs (Chris) and TripleB Machine (Ben Courlas). Mostly V4 machining and Obelisk design; no BOM documents are posted here. Machining files stay here until the TripleB NDA (signed 2026-10-21).

- 2026-09-23T18:44Z, Ben, Obelisk: "proceed with a scrappy version of "Obelisk" (working name) - fully integrating our current hardware, including the LiDAR sensor, into one monolithic tube", on a 3 ft or 42 in bollard, Q4. https://airgarage.slack.com/archives/C0C1C27RFP1/p1790189073618949
- 2026-09-30T20:30Z, Monti, V4 sensor kit: "I made a bunch of 12ft RJ45 and RJ12's ... until we get that custom cable". https://airgarage.slack.com/archives/C0C1C27RFP1/p1790800250228159
- 2026-10-06T16:42Z, Monti, V4 X5: "An update on V4 X5 production": TripleB machines Coupler, LiDAR coupler and Extension Tube from final CAD; extension tube cut 23.5 to 23.75 in from 72 in 4 in sch 40 pipe. So X5 is the production V4 build from this batch. https://airgarage.slack.com/archives/C0C1C27RFP1/p1791304976184289
- 2026-10-16T20:09Z, Monti, V4 materials: SpeedyMetals 4 in sch 40 6061 pipe (72 in), McMaster 9056K42 (LiDAR coupler), Nox Metals 6061-T6511 5.5 x 3 in round bar (bollard coupler). Materials quoted 2026-09-15 by TripleB: "11.51 for lidar coupler and 60.12 for the 24" tube". https://airgarage.slack.com/archives/C0C1C27RFP1/p1792181396951119
- 2026-10-21T19:04Z, Monti, Obelisk: two joint designs (internal vamp clamp; set-screw internal coupler), attachments `Internal Vamp Clamp.step` (F0CAWUZNFHR), `Internal Coupler.step` (F0CB30YTC2W) and five images. Later (2026-10-30) the set-screw design is scrapped for the vamp clamp. Design work, not a BOM. https://airgarage.slack.com/archives/C0C1C27RFP1/p1792609457596849
- 2026-10-29, Ben posts a McMaster order (O-rings 8785N556 / 9396K126 / 1182N42, M2.5x6 SHCS 91292A010, spacers 92825A032, several 4-40 shoulder screws) for the Obelisk prototype; 2026-10-30: machined parts use only 1/4-20 and #4-40, PCB "pillow blocks" use M2.5.
- 2026-11-04T03:35Z, Ben, Obelisk/V4 pipe mounts: shoulder screws snap; current McMaster 94035A522, "My pick is 90292A076 (#8, 17-4)". Not final. https://airgarage.slack.com/archives/C0C1C27RFP1/p1793763334384569
- 2026-11-06T14:59Z, Ben, V4 and Obelisk: "8x 20' tubes @ $308 apiece ... around 100x more v4 sensors ($34 materials price each) ... 200x Obelisks by end of Q2 ... $68 each in housing materials". 2026-11-10: finance approved ~40 tubes; 2026-11-11: Nox order of ~40 to 50 pieces expected 2026-11-13. https://airgarage.slack.com/archives/C0C1C27RFP1/p1793977189612909

## #pt-obelisk (C0C7J22K5PT)

Read the whole channel, 2026-10-07 (creation) to 2026-11-12T18:54Z, about 40 messages. R&D for Obelisk (all-in-one bollard LPR). No BOM, kit or part-number decisions; everything is prototype design. Relevant points:

- 2026-10-16T19:53Z, Monti, Obelisk: interlock design, "schedule 40 pipe segments that connect via three Vamp Clamps ... M10 countersunk fastener", 7075 laser-cut snap rings, magnet plus TMR/Hall sensor glued with 3M DP460NS. Onshape link in the message. https://airgarage.slack.com/archives/C0C7J22K5PT/p1792180395459809
- 2026-10-29, Ben: O-ring material table (EPDM best fit, AS568-045 at 1.32 mm gap); asks whether to drop M3/M2.5 for #4-40 on electronics.
- 2026-10-31, Ben: microcontroller shortlist for Obelisk modules (STM32C5 lean, SAM E53J fallback).
- 2026-11-05, Monti: cables through 3/4 in conduit for Obelisk/V4: "RJ12 cable (power for LiDAR) ... RJ45 cable (data for LiDAR) ... 2x Camera USB Cables".
- 2026-11-10T18:38Z, Ben, V4 and Obelisk tubes: "the current one is rated for interior use only"; leaning to lighter grey satin from Prismatic Powders. Powder coat spec for V4 tubes will change for future batches. https://airgarage.slack.com/archives/C0C7J22K5PT/p1794335881867329
- 2026-11-12, Monti: new Obelisk camera module with individually pivoting cameras; future IR LED band outside the cameras.

## #pt-tripwire (C04PDLL3GAF)

Read: full history 2026-07-06 to 2026-11-11 (about 90 messages); before that, keyword searches only (BOM, modem, antenna, reflector, ECN, compute stack, Party HAT) back to 2025-10-01, with the threads behind hits. Mostly software and fleet operations; hardware BOM content is sparse.

- 2026-04-08T16:29Z, Monti, retroreflector (SEN2-002-000): "only using dual reflectors going forward in an attempt to reduce SKU's". Ben "This seems like a good option to me"; Lorenzo, Josiah agree. Monti adds a "round-flat combo dual reflector mount. The rear tabs can be broken away". This is the 2026-04-08 ECN. https://airgarage.slack.com/archives/C04PDLL3GAF/p1775665798971899
- 2026-04-02/03: VHB tape on the printed hood does not hold; Monti prints the mounting face with fuzzy skin. 2025-11-05: Monti looks at Omron E39-R1K (non-fogging).
- 2026-05-21, Ben: "Modem Bridge X3 assembly and testing notes" thread; X3 flex bridge works but "should still be ever so slightly longer (maybe 0.5mm)".
- 2026-06-29T13:31Z, Ben, sensor enclosure: "Sensor bar BOM in Notion updated to add enclosure/base/assembly SKUs (SEN2-003-00x)", linking the SEN2-003-000 database (the one the Notion notes call half-edited). https://airgarage.slack.com/archives/C04PDLL3GAF/p1782739911176109
- 2026-07-21, Ben: modems salvaged from old v3.1/vπ units swallow packets at provisioning; CM disconnects the USB bridge to provision. Confirms stacks were being built from salvaged modems.
- 2026-08-13T15:54Z, Monti, compute stack: RG255C-GL vs I425-GLGD evaluation; RG255C ~30% more bandwidth (LTE only; 5G blocked by firmware); best antenna "Quectel YFCO002AA". https://airgarage.slack.com/archives/C04PDLL3GAF/p1786636484236489
- 2026-08-13T20:36Z, Monti, compute stack: "We have not rolled out the antenna wing updates (or modems) from above but I put a placeholder ECN". In the thread: new wing CAD "still compatible with the old antennas and modem setup, so we will switch our antenna plastics to this rev"; Ben: "We should also go ahead and switch antennas"; Monti: "since we don't plan to utilize the GPS. One less SKU!" So the 2026-08-13 ECN in Notion is a placeholder, not a released change. https://airgarage.slack.com/archives/C04PDLL3GAF/p1786653413315709
- 2026-09-10, Tory/Monti, bollard camera mount (PIC-003/004): camera base gets a notch for a 12 mm weld seam; ECN filed. https://airgarage.slack.com/archives/C04PDLL3GAF/p1789054152553969
- 2026-09-24, Monti: "Entire stack up of v4 is 89" ... 7ft to top of extension".
- 2026-10-30, Ben: ordered Siraya Tech 85A TPU to trial for camera lens gaskets, "1/4th of the cost of the NinjaFlex 75A we are currently using". 2026-10-15, Faiber: lens gaskets splitting at Hager exits.

## #pt-v4-sensors (C0ARYAA2FNF)

Read the whole channel, 2026-04-10 (creation) to 2026-11-11, about 230 messages. Mostly LiDAR software. BOM-relevant:

- 2026-06-02T00:35Z, Ben, V4 sensor: "We'll be moving forward with the Hummingbird D1R!" (Seyond), scoring in Notion "v4 Sensor Decision Matrix"; PO for 8 units. https://airgarage.slack.com/archives/C0ARYAA2FNF/p1780446915458149
- 2026-06-02, Ben: PCB-mount 17-pin M12 connector Amphenol M12A-17PFFP-SF8001.
- 2026-06-12T00:30Z, Monti, V4 sensor: M12 17-pin breakout to "an RJ45 (ethernet), RJ12 (power), and DuPont", so standard M12-17P cables can be bought; to become a PCB (the sensor interposer). Attachment `IMG_8985.HEIC` (F0B9YD6P8BF). https://airgarage.slack.com/archives/C0ARYAA2FNF/p1781224228948409
- 2026-07-29, Monti: self-drilling screw McMaster 94625A423 for the bollard coupler, T20 bit shears; wants a jig.
- 2026-07-31T20:37Z, Ben, V4 revisions: X1 (Washington Hill, 5 lanes), X2 (Peachtree, Gateway, Denver Arts), X3 "mechanical design complete, waiting on fabrication". https://airgarage.slack.com/archives/C0ARYAA2FNF/p1785530229517279
- 2026-08-10 to 08-13, Monti: X3 couplers machined by TripleB; "X3 sensor interposer board" built, ethernet pinout mirrored ("crimp one side backwards for this rev").
- 2026-08-13T00:00Z, Ben, V4 X4: first X4 articles from the CM targeted 2026-09-15; mechanical handoff to ByTechs/TripleB by 2026-09-01. https://airgarage.slack.com/archives/C0ARYAA2FNF/p1786579224745209
- 2026-08-17, Ben: Notion design doc "Bollard Interposer Board X2 Power Stage Design"; battery backup out of scope for that rev.
- 2026-08-20T20:18Z, Ben, camera modules: "We use ELP-USBGS5MP01-KL60IR (6mm lens) ELP-USBGS5MP01-KL80IR (8mm lens) ELP-USBGS5MP01-KL100IR ("4mm" lens)". The 2026-04-10 ELP packing list in #airgarage-bytechs names the 4mm part `ELP-USBGS5MP01-KV100IR` (and Josiah's 2025-05 handoff note uses KV100IR), so KL100IR is likely a slip. https://airgarage.slack.com/archives/C0ARYAA2FNF/p1787257099819929 and https://airgarage.slack.com/archives/C09FF4GLH9R/p1775837057811809
- 2026-09-25, Ben: cable for 3/4 in EMT, "JST-PUD for Ethernet and JST-XA for power"; not yet built.

## #airgarage-bytechs (C09FF4GLH9R)

Read: top-level history 2025-10-01 to 2026-02-20 (about 200 messages) and 2026-08-15 to 2026-11-12 (about 70 top-level messages); 2026-02-20 to 2026-08-15 through keyword searches (BOM, Aligni, SKU, modem, RG255C, antenna, reflector, E39, hood, wall, power supply, Katana) with the threads behind hits, about 30 threads in all. Private channel, Slack Connect with ByTechs (Chris Williamson) since 2025-12-15. The main channel for what ByTechs builds and ships.

### Compute stack (AG-CS3-001-000, AG-CS3-Kit)

- 2025-11-15T03:49Z, Ben: first CM PCB order "10x each Party HAT X5, Modem Bridge X1, and HAT USB-A Bridge X2 ... I'll supply all of the BOMs Monday". https://airgarage.slack.com/archives/C09FF4GLH9R/p1763178551392789?thread_ts=1761665877.615859&cid=C09FF4GLH9R
- 2025-12-27T19:39Z, Ben: "40x Party HAT X5B, 120x USB Bridge X3, 140x Modem Bridge X2 have finished fabrication". https://airgarage.slack.com/archives/C09FF4GLH9R/p1766864355224829
- 2026-01-26, Ben asks for "10x L6R36-120 power supply" (the 12V/36W in Aligni `AG-CS3-Kit`); 2026-02-20: "140x ... each of power supplies and cables for compute stacks ordered" (attachment image.png F0AH37LJDS4). https://airgarage.slack.com/archives/C09FF4GLH9R/p1769467512655039 , https://airgarage.slack.com/archives/C09FF4GLH9R/p1771618014345619
- 2026-02-11, Ben: "200x ea antennas" (two antenna types). 2026-02-27: "50x SixFab LTE HATs ordered ... let me make sure the BOM is fully updated". https://airgarage.slack.com/archives/C09FF4GLH9R/p1770853873852149 , https://airgarage.slack.com/archives/C09FF4GLH9R/p1772206367907649
- 2026-03-17T02:45Z, Ben: "30x (2x2) panels of Party HAT X5C ... No BOM changes, only copper". https://airgarage.slack.com/archives/C09FF4GLH9R/p1773715518658449
- 2026-04-02T00:16Z, Ben: compute stack parts inventory, a de facto parts list: "57 RPi 5 16GB / 70 coolers / 136 I425-GL modems / 34 SixFab Cellular HATs / 156 Sequent SWD HATs / 25 microSD / USB bridges / modem bridges / 69 ribbon cables / Party HAT to SWD HAT wires / Party HATs / 72 thermal pads / 50 GPIO spacers / 132 batteries / standoffs / ~265x of each antenna / 163 power supplies / 160 extension cables". Thread: GPIO spacer is 3D printed, one per unit; Pis and coolers bought from MakerBright. Items here that Aligni `AG-CS3-001-000` lacks: Party HAT, USB bridge, modem bridge, Pi cooler, batteries, GPIO spacer, Party HAT to SWD wire. https://airgarage.slack.com/archives/C09FF4GLH9R/p1775088983421139
- 2026-04-06, Chris: "new style antenna wings for the new cases" being printed (the new plastics the 2026-04-07 meeting mentions). https://airgarage.slack.com/archives/C09FF4GLH9R/p1775488584933189
- 2026-05-22T00:01Z, Ben: "Modem Bridge X3 checks out"; thread: "we'll need to use the new plastics revision for the antenna wing and outer case". https://airgarage.slack.com/archives/C09FF4GLH9R/p1779399706930059
- 2026-05-26T22:05Z, Monti: front panel gets "a slot for an M2x18mm screw (and nut) that pushes the SWDv9 reset button"; use up ~20 old fronts first. Monti: parts added "EXT-90593A024 EXT-91290A049"; Ben: "Aligni has been updated!" Chris in the thread: "We also need to add partyhat, modem bridge, and usb bridge to Aligni" (still missing from Aligni today). Note Aligni names EXT-91290A049 "M2 ... 20 mm Long" while Monti wrote M2x18. https://airgarage.slack.com/archives/C09FF4GLH9R/p1779833114513549
- 2026-05-28, Ben: 18x USB-C to micro-USB cables (Amazon B0CMLS2MB1) as a stopgap for modem bridge production problems. https://airgarage.slack.com/archives/C09FF4GLH9R/p1779926277762709
- 2026-07-09T01:51Z (2026-07-08 local), Ben: "the new RG255C modems have finished production ... ship samples to Monti so he can test with some new antennas and modify the antenna wing + case". 2026-07-17: 250x RG255C shipped. https://airgarage.slack.com/archives/C09FF4GLH9R/p1783537211043519 , https://airgarage.slack.com/archives/C09FF4GLH9R/p1784253075869459
- 2026-07-08, #tripwire-leadership (not on the list), Ben: Chris salvaging EG25-GL from returned units; outstanding EG25-GL PO with Quectel cancelled. https://airgarage.slack.com/archives/C0AA64RJ6BV/p1783516669795349
- 2026-08-11T15:51Z, Ben: "150x I425-GL are stuck in customs ... ~248x RG255C are with you ... but will require a plastics + antenna change". Eagle (I425-GL) modems arrived 2026-08-17. https://airgarage.slack.com/archives/C09FF4GLH9R/p1786463481304349
- 2026-08-17T13:48Z, Ben: "I'll have you a new power supply SKU for compute stacks by EOD Wednesday; starting a thermal burn-in". The new SKU is never named in Slack; ByTechs later reorders "more of the same ones" (DM 2026-09-18). Open question. https://airgarage.slack.com/archives/C09FF4GLH9R/p1786974507426269
- 2026-09-19T20:44Z, Chris: Sequent watchdog HAT "Same SKU number, but now V11 instead of V9", with a DIP switch that hits the Party HAT USB jack; Sequent says no functional change; ByTechs reworks. Aligni `EXT-SM-I-003` is named "v9". https://airgarage.slack.com/archives/C09FF4GLH9R/p1789850668237949
- 2026-09-28/29, Chris: low on compute-stack LCDs (Waveshare 0.91 in OLED, SKU 14657 per Ben 2026-06-02), 18650 batteries, SIM cards; units 690 to 708 shipped without LCDs (2026-10-15).
- 2026-10-14 to 10-19: USB bridges and modem bridges shipped from JLCPCB and received (the 2026-10-08 same-rev reorder).
- 2026-11-04, Chris: "36x modem hats and 10x seq power hats" in stock, reordering. The SixFab HAT build is still current.
- 2026-11-12T15:47Z, Chris: "wrapping up 50x partyhats today on PNP ... 36 v3.1 ... im going to rebuild into vpi". https://airgarage.slack.com/archives/C09FF4GLH9R/p1794498475240559

### Sensor bar, retroreflector, enclosure (SEN2-*)

- 2026-01-16 and 2026-02-16: reflector housings short; new "big" reflector hoods, a prototype from Josiah, "we will probably order them from you next week" (2026-02-14T00:52Z). Josiah: order them for LA "since they should slightly improve RR reliability". https://airgarage.slack.com/archives/C09FF4GLH9R/p1771026776647419
- 2026-02-19 and 2026-04-08, Ben asks for counts of "E3Z-T61, E3Z-R61, and E39-R1S reflectors"; Chris: "114x E39-R1S Reflectors 100x E3Z-R61 ... 7x E3Z-T61 Pairs". The reflector in stock is named E39-R1S. https://airgarage.slack.com/archives/C09FF4GLH9R/p1775655256457339?thread_ts=1775655069.285139&cid=C09FF4GLH9R
- 2026-03-09T18:39Z, Ben (thread on 8ft RJ-12 cables, 2026-03-06): RJ-12 cables go in the sensor bar package; "Only the receiver side of the T61 bars needs one. The emitter side should just get the small 12V power supply". Chris: "I haven't added any power supplies to those units." Ben then sends the L6R06H-120 DigiKey link (DMs 2026-03-09/10). So the TB kit carries the 12V/6W PSU and the RR kit does not, which matches Aligni `AG-SEN2-RR-Kit` rev C. https://airgarage.slack.com/archives/C09FF4GLH9R/p1773081547139139?thread_ts=1772809746991309&cid=C09FF4GLH9R
- 2026-04-10, Chris: ordering fasteners for 200 sensor bars and "the BOM for the PCB" (sensor bar I/O breakout) from Mouser; 2026-04-06: next PCBs may move to JST-XA.
- 2026-04-23T00:46Z, Ben: Aligni "parts, BOMs, manufacturers, and vendors are set up correctly now (for sensor bars ONLY)". https://airgarage.slack.com/archives/C09FF4GLH9R/p1776905164941089
- 2026-05-28T20:29Z, Monti: two enclosure parts "slipped through the cracks. We'll need to add these to aligni": Essentra 27PIF0089 pins, 4 per enclosure; 3/4 in knock-out seals, 2 per enclosure; "I don't think we ever made an enclosure BoM". Neither part is in Aligni `AG-SEN2-003-000` today. ByTechs packs them in the installer packs (Chris 2026-06-30: "3/4 caps and pins for the enclosures. I normally have those in the installer packs"). https://airgarage.slack.com/archives/C09FF4GLH9R/p1780000141544559
- 2026-06-26T19:13Z, Chris: "Aligni should have been removing 4x reflectors per build, but it is only removing 1x per build. The part number in Aligni is for the dual reflector (E39-R2), where as I only have the E39-R1 units." Britney: replacements shipping are "R1". https://airgarage.slack.com/archives/C09FF4GLH9R/p1782501184337819?thread_ts=1782499574.359229&cid=C09FF4GLH9R
- 2026-06-29T13:15Z, Ben: "Replace E39-R2 dual-reflector (was 1x but should have been 2x qty) with 4x E39-R1 single-reflector" in SEN2-002-000; enclosures now in Aligni: `AG-SEN2-003-001_EnclosureBase` "SENSOR ENCLOSURE BASE V5", `AG-SEN2-003-002_EnclosureTop` "SENSOR ENCLOSURE ASSY V5 CARDINAL ORANGE T009-OG26", `AG-SEN2-003-000` "vπ Sensor Enclosure X5". https://airgarage.slack.com/archives/C09FF4GLH9R/p1782738921179649?thread_ts=1782499574.359229&cid=C09FF4GLH9R
- 2026-07-14T19:01Z, Ben: "The current version "V5" enclosure top and base are now separate items in Shopify ... (Britney will archive the previous V4 enclosure listing". https://airgarage.slack.com/archives/C09FF4GLH9R/p1784055708547169
- 2026-10-15T15:53Z, Ben: "Can you order 100 from DigiKey?" linking DigiKey 761204, which is E39-R1S. So the part bought in October is E39-R1S, while Aligni carries `EXT-E39-R1` (DigiKey 105142, the link Chris used in June). https://airgarage.slack.com/archives/C09FF4GLH9R/p1792079580850449?thread_ts=1792079280.260459&cid=C09FF4GLH9R
- 2026-10-23T00:31Z (thread from 2026-10-22), RJ-12: Monti plans to move away from 8ft cables; Ben: "15ft is fine, let's order 100pc". Obelisk drops RJ-12, V4 sensors keep it. https://airgarage.slack.com/archives/C09FF4GLH9R/p1792709057777179
- 2026-11-04T20:13Z, Chris: "since we are moving away from the enclosures", when planning cartons for V4 shipments (V4 replaces the sensor bar plus enclosure). https://airgarage.slack.com/archives/C09FF4GLH9R/p1793823203744379
- 2026-11-12, Britney asks for "reflector hoods ... that can be drilled in" (no answer yet).

### Cameras (PIC-*)

- 2026-01-07T17:27Z, Chris: "Ben mentioned dual cameras should use the 8mm lens". https://airgarage.slack.com/archives/C09FF4GLH9R/p1767806869610249
- 2026-04-10T16:04Z, Monti: ELP order packing list: `ELP-USBGS5MP01-KV100IR` 50 pcs, `ELP-USBGS5MP01-KL80IR`, `ELP-USBGS5MP01-KL60IR`. https://airgarage.slack.com/archives/C09FF4GLH9R/p1775837057811809?thread_ts=1775836387.012279&cid=C09FF4GLH9R
- 2026-09-22T14:08Z, Chris: "these 4mm have the extended lens so we have to modify the camera housing to use them". 2026-10-27: "Ive been trying to save the 4mm new lens style for wall mount cameras ... 18x 6/4 and say 100x 8/6". https://airgarage.slack.com/archives/C09FF4GLH9R/p1790086121163469 , https://airgarage.slack.com/archives/C09FF4GLH9R/p1793119408161369
- 2026-10-08/09, Britney's orders list "wall mount camera 6mm/8mm", i.e. a dual-lens camera on the wall mount. https://airgarage.slack.com/archives/C09FF4GLH9R/p1791492209933539?thread_ts=1791482413.079469&cid=C09FF4GLH9R

### Install packs and kits outside Aligni

- 2026-01-14T03:48Z, Anthony: plan to move "LPR Install packs" to ByTechs; thread lists contents being bought: IPEX 277009 12x12x6 PVC junction box, EZ-RJ12 connectors, 1/2 in EMT one-hole straps, tape, hex lock nuts, enclosure locks, TSA locks for large J-boxes, glue, SendCutSend washers, fasteners (FastenersPlus). Chris: base kit is RR-WM-IP-DC, "the bare minimum of all 6 kits". https://airgarage.slack.com/archives/C09FF4GLH9R/p1768362482449579
- 2026-01-16T00:31Z, Anthony: "I've got the BOM for install packs ready to go", Google Sheet https://docs.google.com/spreadsheets/d/1Qsc5gxIf8g-M4u9SausMnXMgNn1OOJiesQ50L1Hw7uI (not opened), "6 SKUs". Chris (2026-01-16): "We can use your SKUs on shopify, and then I can carry an itemized list for each SKU on my end". https://airgarage.slack.com/archives/C09FF4GLH9R/p1768523478893699
- Install pack SKUs (Anthony, DM 2026-01-26): RR-BM-IP-DC, RR-WM-IP-DC, TB-IP-DC, RR-BM-IP-DC-R, RR-WM-IP-DC-R, TB-IP-DC-R. In use: RRBMIPDC, RRWMIPDC, RRWMIPDCR. "BM"/"WM" name how the reflectors are mounted, not the camera (Anthony 2026-11-04; Britney 2026-09-02).
- 2026-02-17T22:43Z, Anthony: Aerial Camera bundle handed to ByTechs: Yellowstone Y2 solar camera with panel, WingHome mount, 2 hose clamps per camera (or screws), Loctite threadlocker. No Aligni part. https://airgarage.slack.com/archives/C09FF4GLH9R/p1771281801028279
- 2026-06-24, Chris "updating the BOM for installer packs" (microfiber towels). 2026-09-02: 3/4 in conduit straps to conduit hangers at installer request. https://airgarage.slack.com/archives/C09FF4GLH9R/p1788362640494089
- 2026-11-03T20:55Z, Ben, V4 sensor kit: last old-batch V4 sensors shipped "with 8ft RJ-12 and no TS30 driver or 7/32" drill bit ... per Monti's BoM" (the Notion V4 Sensor Install Kit BoM). https://airgarage.slack.com/archives/C09FF4GLH9R/p1793739353454379
- 2026-11-04T21:53Z, Anthony/Chris/Ben, V4 and install packs: "V4 units come with their own tapcons and cables packed with the units"; installer packs stay the same, one per V4 lane; Ben: V4 kit must stay "fully self-contained"; Anthony adds a new SKU column to the sheet; locks: Forge 6-pack. 2026-11-06 Chris: Britney's new "v4-BM-IP-DC" is not what was agreed; installer kits are "for camera equipment only". Unresolved at read time. https://airgarage.slack.com/archives/C09FF4GLH9R/p1793829197128999 , https://airgarage.slack.com/archives/C09FF4GLH9R/p1793991552509009

### ERP, Shopify, Katana

- 2025-10-24, Ben: Shopify store "just for tracking inventory and fulfilling internal orders". https://airgarage.slack.com/archives/C09FF4GLH9R/p1761338840058449
- 2026-04-15T15:27Z, Ben: ByTechs to load "Parts and Partslists (their term for BOMs) into Aligni"; "fill in all of the missing metadata and load it in the correct spreadsheet format". https://airgarage.slack.com/archives/C09FF4GLH9R/p1776266877839939
- 2026-06-05T18:50Z, Ben: "Aligni->Shopify sync is now working ... products need to have identical SKUs set up in Shopify." https://airgarage.slack.com/archives/C09FF4GLH9R/p1780685412641359
- 2026-07-08, Ben: Aligni counts updated "for kits only" against a physical count and synced to Shopify; 2026-07-13: Aligni cannot hold negative stock, so Shopify drifts. https://airgarage.slack.com/archives/C09FF4GLH9R/p1783538477973049 , https://airgarage.slack.com/archives/C09FF4GLH9R/p1783968184532729
- 2026-10-05T14:04Z, Britney: "finding an erp that is a better fit ... So far, katana seems to be the best option"; Chris wants a demo account. 2026-10-15: Chris plans an inventory audit "in Aligni or whatever other software". https://airgarage.slack.com/archives/C09FF4GLH9R/p1791209087494529

## Outside the six channels

Found through workspace-wide searches (BOM, Aligni, Katana, RG255C, E39, wall mount, partyhat). Only the hits below were opened.

- #tripwire-leadership (C0AA64RJ6BV): 2026-04-09T16:31Z Ben: "consider switching to 1x E39-R2 instead of 2x E39-R1S reflector" (not adopted). https://airgarage.slack.com/archives/C0AA64RJ6BV/p1775752294639369 . 2026-07-09T16:49Z Ben: Shopify install-pack listings, "SKUs are only set for the last two, and the handle and SKU match but not the title" (RRBMIPDC sits on the RR-WM-IP-DC title, RRWMIPDC on TB-IP-DC; same mismatch as the Shopify notes). https://airgarage.slack.com/archives/C0AA64RJ6BV/p1783615784954409 . 2026-07-23: "Install kits - should we be tracking these in Aligni?" 2026-09-21T19:30Z Britney: "can you drop v4 hardware and install packs into aligni+shopify?" https://airgarage.slack.com/archives/C0AA64RJ6BV/p1790019035394979 . 2026-09-17: Katana and Odoo are the two options. 2026-11-03T16:25Z Britney: Katana contract, annual only; 2026-11-06 agreed bi-annual payments. https://airgarage.slack.com/archives/C0AA64RJ6BV/p1793723119748629 . 2026-11-10T19:15Z Ben: "Just paid our last Aligni bill". https://airgarage.slack.com/archives/C0AA64RJ6BV/p1794338140143389
- DM Ben/Monti (D08EQLEPAKX), 2026-04-30T13:12Z: "Wall Mount Dual Cam Kit looks like a typo. The CSV lists Single Camera Module (PIC-002-000) ... Should I substitute PIC-001-000". Monti: "Ah yes"; Ben: "already went ahead and did it in Aligni". https://airgarage.slack.com/archives/D08EQLEPAKX/p1777554733392829 . Same DM, 2026-04-09: Ben numbered the camera parts PIC-001 to PIC-005.
- DM Ben/Chris (D09P9DCN5M2), Party HAT: 2026-10-12T14:49Z Chris: "Partyhat pnp parts needed 22U_35V 330nf cap Bss138ps 22u Acs37041 Tps54202hddcr Ads1015idgs L78l33abutr Tcmt4100"; C2012X5R1V226M125AC needs a substitute; Chris suggests another "partyhat x5c order" at JLC. 2026-10-29T17:42Z: "the entire partyhat bom of parts is here" (loaded for ByTechs' pick-and-place). https://airgarage.slack.com/archives/D09P9DCN5M2/p1791816540695779 , https://airgarage.slack.com/archives/D09P9DCN5M2/p1793295722829179
- #eng-hardware-team-internal (C0A4URQGP33), 2026-11-03: Ben asks Monti for the RG255C VID/PID or "a live device that has one installed"; #peridio-airgarage 2026-10-22: "When the RG255C arrives". Neither suggests RG255C is in fielded units.
- Q2 2026 retro draft (DM, 2026-07-14): "ERP (Aligni) ... build scheduling live mid-May; reflector BOM bug (E39-R2 vs 4x E39-R1)"; "modem chipset EOL -> hedged 750-unit PO -> RG255C 5G RedCap migration".

## Answers to the brief (as of 2026-11-13)

(a) Current vπ compute stack. Production is still the SixFab LTE HAT build with an I425-GL (Eagle) modem or a salvaged Quectel EG25 modem, two antennas, Party HAT X5C (copper-only change from X5B, "No BOM changes"), USB-A Bridge X3, Modem Bridge X3 (X4 planned 2026-09-17, not built; 2026-10-08 reorder was "the same rev"), Sequent Super Watchdog HAT now V11 (same SKU as v9), and the new antenna-wing and outer-case plastics (from about 2026-04 to 05) plus the 2026-05-26 front panel with M2 screw and nut. RG255C plus one large antenna is not rolled out: Monti 2026-08-13 "We have not rolled out the antenna wing updates (or modems)"; the Notion ECN is a placeholder; Chris still stocks "~50 of each antenna" and SixFab HATs on 2026-09-22 and 2026-11-04. Decided 2026-08-13: switch wing plastics to the new rev (fits old antennas and modem) and also switch antennas to drop the GPS one; whether that happened is not in Slack. Aligni `AG-CS3-001-000` lists both I425-GL and EG25-G at qty 1 (alternates), has the "LTE + GPS" W3906 antenna, and lacks Party HAT, USB bridge, modem bridge, cooler, batteries and GPIO spacer.

(b) Wall Mount Dual Cam Kit uses the dual camera module (PIC-001-000). The Notion single-module entry was a typo; Ben fixed Aligni on 2026-04-30 and Monti agreed. Orders call wall mount cameras "6mm/8mm".

(c) Reflector and enclosure. 2026-04-08: dual reflector only, round/flat hood with break-away tabs; big hoods from 2026-02. 2026-06-29: Aligni SEN2-002-000 changed from 1x E39-R2 to 4x E39-R1. Stock and purchases are named E39-R1S (Chris's counts; Ben's 2026-10-15 DigiKey 761204 order), while Aligni and Chris's June link use E39-R1: needs a call. Quantity also needs checking: 4 per SEN2-002-000 and 2 SEN2-002-000 per RR kit gives 8 per kit, while Chris said 4 per build. Enclosure V5 (base plus "ASSY V5 CARDINAL ORANGE T009-OG26" top, Haig) entered Aligni 2026-06-29; pins (Essentra 27PIF0089, 4) and 3/4 in knock-out seals (2) are still missing from Aligni and ByTechs packs them in the installer packs.

(d) Sensor bar kits. RR kit: no power supply (Ben 2026-03-09; matches Aligni rev C). TB kit: one 12V/6W L6R06H-120 for the emitter bar, RJ-12 on the receiver side only. RJ-12 length moves from 8ft (`EXT-CS-44050-08`) to 15ft: Ben "let's order 100pc" in a 2026-10-22 thread, "All 15 is good" 2026-11-12.

(e) Outside Aligni: install packs (Google Sheet, 6 SKUs plus a V4 column added 2026-11-04), V4 Sensor Install Kit BoM (Notion, updated 2026-11-04), V4 X5 machined parts (TripleB: coupler, LiDAR coupler, extension tube; Nox and SpeedyMetals stock), Seyond D1R, M12 cables and interposer PCB, Aerial Camera bundle, Obelisk (design only, no BOM). The V4 install-pack question (is "v4-BM-IP-DC" a real SKU, or does a V4 lane get a normal camera pack) was still open on 2026-11-06.

(f) Migration. Katana chosen over Odoo (options 2026-09-17; Britney 2026-10-05 "katana seems to be the best option"); contract 2026-11-03; last Aligni bill paid 2026-11-10; #temp-katana-onboarding opened 2026-11-12 with no content yet. No Slack decision on how BOMs move to Katana. SKU rules found: Aligni and Shopify need identical SKUs for the sync (2026-06-05); install packs use AirGarage's Shopify SKUs with ByTechs keeping an itemized list per SKU (2026-01-16); CAD release files should use the Aligni/BOM part number with an `_X<n>` revision tag (2026-09-21).

(g) Party HAT and install-kit BoMs. Install kits: Anthony's Google Sheet `1Qsc5gxIf8g-M4u9SausMnXMgNn1OOJiesQ50L1Hw7uI` (tabs gid 871000132 and 480757198), maintained by Anthony, plus Chris's own per-SKU version ("Ive changed this spreadsheet. I will share my version", 2026-11-04). Party HAT: no Slack message mentions the spreadsheet on Josiah's drive; ByTechs holds the working Party HAT parts list for its pick-and-place (DM 2026-10-12, 2026-10-29) and Ben orders the PCBs at JLC. The KiCad repo (`party-hat` X5C) is the nearest source of record.
