# /// script
# requires-python = ">=3.15"
# ///
"""Build the corrected BOM set in <workspace>/boms/ from the Aligni export plus the other sources. No network.

    uv run --python 3.15 build_boms.py

Inputs: boms/aligni-20261113T0325Z/ (untouched export), the Aligni snapshot's parts.json (item master),
data/ecad/ (KiCad BOMs), data/notion/ (V4, X4A interposer, V3.1), data/sheets/bytechs-install-packs_SKUs.csv.
Outputs, each one CSV per assembly in the export's column layout:
  boms/<PN>.csv            in scope for Katana (vπ, PCBAs, install packs, V4 sensor)
  boms/legacy-v3.1/<PN>.csv  cleaned up, not migrated
  boms/obelisk/<PN>.csv    draft, not migrated
  boms/index.csv, boms/items.csv (item master: every part used, with where it came from)
Decisions applied are Ben's of 2026-11-13 (docs/boms/reconciliation.md). Unknown part numbers are EXT-TBD-*.
"""
import csv, json, re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
WS = HERE.parents[1]
ALIGNI = WS / "boms/aligni-20261113T0325Z"
SNAP = WS / "scratchpad/2026-11-13-aligni-bom-export/data/20261113T0325Z"
ECAD, NOTION, SHEETS = HERE / "data/ecad", HERE / "data/notion", HERE / "data/sheets"
OUT = WS / "boms"
COLS = ["Line", "Part Name", "Part Number", "Part Number - Mfg", "Manufacturer", "Supplier",
        "Supplier Part Number", "Quantity Per Unit", "Unit", "Min Quantity Per Purchase", "Cost",
        "Cost Per Unit", "Links", "Notes", "Designator", "No Load", "Part Type", "Child Revision"]
ITEM_COLS = ["Part Number", "Part Name", "Part Type", "Unit", "Manufacturer", "Part Number - Mfg", "Supplier",
             "Supplier Part Number", "Cost Per Unit", "Source", "Notes"]

# Renumbering (proposed in docs/boms/part-numbers.md): fixes the PIC-001-005 collision and gives the
# sensor breakout PCBA an assembly number so its bare board can be an item of it.
RENAME = {
    "AG-PIC-001-005_ELPCam4": "AG-PIC-001-007_ELPCam4",
    "AG-PIC-001-005_ELPCam6": "AG-PIC-001-008_ELPCam6",
    "AG-PIC-001-005_ELPCam8": "AG-PIC-001-009_ELPCam8",
    "AG-SEN2-001-001_Breakout": "AG-SEN2-004-000_Breakout",
}

items = {}  # Part Number -> item row


def item(pn, name, ptype, mfr="", mpn="", supplier="", spn="", cost="", source="", notes="", unit="each"):
    if pn in items:
        return pn
    items[pn] = {"Part Number": pn, "Part Name": name, "Part Type": ptype, "Unit": unit, "Manufacturer": mfr,
                 "Part Number - Mfg": mpn, "Supplier": supplier, "Supplier Part Number": spn,
                 "Cost Per Unit": cost, "Source": source, "Notes": notes}
    return pn


def line(pn, qty, notes="", designator="", noload=False, rev=""):
    i = items[pn]
    return {"Part Name": i["Part Name"], "Part Number": pn, "Part Number - Mfg": i["Part Number - Mfg"],
            "Manufacturer": i["Manufacturer"], "Supplier": i["Supplier"], "Supplier Part Number": i["Supplier Part Number"],
            "Quantity Per Unit": qty, "Unit": i["Unit"], "Min Quantity Per Purchase": "", "Cost": "",
            "Cost Per Unit": i["Cost Per Unit"], "Links": "", "Notes": notes, "Designator": designator,
            "No Load": "Y" if noload else "", "Part Type": i["Part Type"], "Child Revision": rev}


def rows(path):
    return list(csv.DictReader(open(path)))


def num(s):
    try:
        f = float(str(s).replace("$", "").replace(",", ""))
        return int(f) if f.is_integer() else f
    except ValueError:
        return None


# ---------------------------------------------------------------- item master from Aligni
revs = json.load(open(SNAP / "part_revisions.json"))
aname = {r["part"]["id"]: r["description"] for r in revs if r["active"]}
for p in json.load(open(SNAP / "parts.json")):
    if p["partNumber"] == "TEST-Kit":
        continue
    vpn = p["vendorPartNumbers"]["nodes"]
    sup = (p["preferredVendor"] or {}).get("name") or (vpn[0]["vendorName"] if vpn else "")
    item(RENAME.get(p["partNumber"], p["partNumber"]), aname[p["id"]], p["partType"]["name"], p["manufacturer"]["name"],
         p["manufacturerPn"], sup, next((v["partNumber"] for v in vpn if v["vendorName"] == sup), ""),
         num(p["standardCost"]) or "", "Aligni", unit=p["unit"]["name"])
items["AG-SEN2-004-000_Breakout"]["Part Type"] = "Assembly"
items["AG-SEN2-002-000"]["Part Type"] = "Assembly"

boms = {}  # PN -> {"name", "rev", "scope", "lines", "source", "change"}


def bom(pn, name, rev, scope, lines, source, change=""):
    item(pn, name, "Assembly", "AirGarage", "", "", "", "", source)
    items[pn]["Part Name"] = name
    boms[pn] = {"name": name, "rev": rev, "scope": scope, "lines": lines, "source": source, "change": change}


# ---------------------------------------------------------------- vπ from Aligni, with the decisions applied
idx = {r["Assembly"]: r for r in rows(ALIGNI / "index.csv") if r["Active"]}
for pn, r in idx.items():
    ls = [dict(x, **{"Part Number": RENAME.get(x["Part Number"], x["Part Number"])}) for x in rows(ALIGNI / r["File"])]
    boms[pn] = {"name": r["Name"], "rev": r["Revision"], "scope": "katana", "lines": ls, "source": "Aligni", "change": ""}

# New items used by the fixes
item("EXT-E39-R1S", "Omron E39-R1S Retroreflector", "Mechanical", "Omron", "E39-R1S", "DigiKey", "", "", "Slack 2026-10-15; Ben 2026-11-13")
item("EXT-TBD-RJ12-15FT", "RJ-12 Cable (15ft)", "Cable", "", "", "", "", "", "Slack 2026-11-12",
     "Replaces EXT-CS-44050-08 (8ft). Part number to confirm.")
item("EXT-B0C52TVDGW", "M6 x 1.0 Nylock, stainless", "Mechanical", "", "B0C52TVDGW", "Amazon", "B0C52TVDGW", "", "Install-pack sheet")
item("EXT-27PIF0089", "Enclosure Peg (nylon pin)", "Mechanical", "Essentra", "27PIF0089", "Mouser", "", "", "Notion SEN2-002-000 BoM (1); Slack 2026-05-28")
item("EXT-OLKOS75-100", "3/4in Snap-in Knockout Seal, zinc-plated steel (enclosure cap)", "Mechanical", "OHLECTRIC", "OLKOS75-100",
     "Amazon", "B0GNN6HDVH", "", "ByTechs install-pack sheet; Notion SEN2-002-000 BoM (1) links the same item",
     "Sold in packs of 100 (Amazon title: 3/4-Inch Snap-in Knockout Seals (100 Pack) Zinc-Plated Steel).")
item("EXT-SC1148", "Raspberry Pi 5 Active Cooler", "Mechanical", "Raspberry Pi", "SC1148", "MakerBright", "", "", "Notion V3.1 Compute Stack BoM; Slack 2026-04-02")
item("EXT-INR-18650-P30B", "Molicel P30B 18650 Battery", "Power", "Molicel", "INR-18650-P30B", "18650BatteryStore", "", 4.49,
     "Notion V3.1 Compute Stack BoM", "2 per compute stack (Ben 2026-11-13).")
item("AG-CS3-001-008_GPIOSpacer", "GPIO Spacer (3D printed)", "Mechanical", "ByTechs LLC", "CS3-001-008_GPIOSpacer", "ByTechs LLC", "", "",
     "Slack 2026-04-02", "One per unit.")
item("AG-CS3-001-009_SWDWire", "Party HAT to Watchdog HAT Wire", "Cable", "", "", "ByTechs LLC", "", "", "Slack 2026-04-02",
     "Construction not documented; confirm with ByTechs.")
item("EXT-95893A198", "M3x30mm Thread Forming Screw", "Mechanical", "McMaster-Carr", "95893A198", "McMaster-Carr", "95893A198", "",
     "McMaster purchases 2026-03-20 and 2026-04-10; Ben 2026-11-13", "Aligni listed 95893A197. Sold in packs of 25.")
item("EXT-H-2118F", "Uline Standard Safety Bollard, 4.5 x 36in, fixed", "Mechanical", "Uline", "H-2118F", "Uline", "H-2118F", "",
     "Notion PIC-003 BoM (listed at quantity 0); Ben 2026-11-13", "In no BOM. One per round-bollard-mount unit.")


def patch(pn, rev, change, drop=(), swap=None, add=()):
    b = boms[pn]
    ls = [x for x in b["lines"] if x["Part Number"] not in drop]
    for x in ls:
        if swap and x["Part Number"] in swap:
            new, q = swap[x["Part Number"]]
            x.update(line(new, q, x["Notes"]), Line=x["Line"])
    ls += add
    b.update(lines=ls, rev=rev, change=change)


# ---------------------------------------------------------------- PCBAs from KiCad and Notion
def ecad_bom(project, pcb_pn, pcb_name, fab):
    item(pcb_pn, pcb_name, "Mechanical", "AirGarage", pcb_pn.removeprefix("AG-"), fab, "", "", f"KiCad {project}")
    out, dnp = {pcb_pn: line(pcb_pn, 1)}, []
    for r in rows(ECAD / f"{project}.csv"):
        if "MountingHole" in r["Value"] + r["Footprint"] or r["Value"] == "TestPoint":
            continue  # not a part
        if r.get("InBOM") == "no" or r["DNP"]:
            dnp.append(r["Designators"])  # KiCad's own BOM export leaves these out too
            continue
        mpn_field = (r.get("MPN") or "").strip()
        mfr, mpn = (mpn_field.rsplit(" ", 1) if " " in mpn_field else ("", mpn_field))
        mfr = mfr or r.get("Manufacturer", "")
        refs = r["Designators"]
        pn = "EXT-" + re.sub(r"[^A-Za-z0-9.\-+/#]", "-", mpn) if mpn else f"EXT-TBD-{project}-{refs.split(',')[0]}"
        dpn = next((r[k] for k in r if re.match(r"(Digi-?key|DPN)", k, re.I) and r[k]), "")
        fp = r["Footprint"].split(":")[-1]
        desc = " ".join(x for x in (r["Value"], r.get("Description", "").split(" | ")[0], f"({fp})") if x)
        item(pn, desc, "Electronic", mfr, mpn, "DigiKey" if dpn else "", dpn, "", f"KiCad {project}",
             "" if mpn else "No MPN in the schematic.")
        if pn in out:  # same part split over two KiCad rows (fields differ): one line
            out[pn]["Quantity Per Unit"] += int(r["Quantity"])
            out[pn]["Designator"] += "," + refs
        else:
            out[pn] = line(pn, int(r["Quantity"]), designator=refs)
    if dnp:
        out[pcb_pn]["Notes"] = "Not fitted (DNP): " + ",".join(dnp)
    return list(out.values())


bom("AG-CS3-002-000_PartyHAT", "Party HAT PCBA", "X5C", "katana",
    ecad_bom("party-hat", "AG-CS3-002-001_PCB", "Party HAT bare PCB", "JLCPCB"), "KiCad party-hat @ tripwire-ecad 81160fe",
    "C10 (68p) carries DigiKey 1276-1135-2-ND, the same as C11, C12, C16 (22u); one is wrong. ByTechs' pick-and-place list is the working copy.")
bom("AG-CS3-003-000_USBBridge", "USB-A (HAT) Bridge PCBA", "X3", "katana",
    ecad_bom("hat-usb-bridge", "AG-CS3-003-001_PCB", "USB-A Bridge bare PCB", "JLCPCB"), "KiCad hat-usb-bridge",
    "Schematic title block says X2; X3 was a PCB-only change.")
bom("AG-CS3-004-000_ModemBridge", "Modem Bridge PCBA", "X3", "katana",
    ecad_bom("modem-bridge", "AG-CS3-004-001_PCB", "Modem Bridge bare PCB (flex)", "JLCPCB"), "KiCad modem-bridge (shared schematic, X1/X2)",
    "X3 (flex) is in production but its design files are not in tripwire-ecad; BOM is from the X2 board.")
bom("AG-SEN2-004-000_Breakout", "Sensor Bar I/O Breakout PCBA", "X2", "katana",
    ecad_bom("sensor-bar-io-breakout", "AG-SEN2-004-001_PCB", "Sensor Bar I/O Breakout bare PCB", ""), "KiCad sensor-bar-io-breakout",
    "Was AG-SEN2-001-001_Breakout in Aligni (a Module with no BOM).")

patch("AG-CS3-001-000", "C", "Adds the PCBAs, cooler, batteries, GPIO spacer and watchdog wire the build uses (Slack 2026-04-02, 2026-05-26). "
      "Keeps the I425-GL modem and the cell+GPS combo and diversity antennas (Ben 2026-11-13). Watchdog HAT ships as V11, same SKU.",
      add=[line("AG-CS3-002-000_PartyHAT", 1, rev="X5C"), line("AG-CS3-003-000_USBBridge", 1, rev="X3"),
           line("AG-CS3-004-000_ModemBridge", 1, rev="X3"), line("EXT-SC1148", 1),
           line("EXT-INR-18650-P30B", 2), line("AG-CS3-001-008_GPIOSpacer", 1),
           line("AG-CS3-001-009_SWDWire", 1)])
patch("AG-SEN2-002-000", "D", "2x E39-R1S per retroreflector, so 4 per RR kit (Ben 2026-11-13). Was 4x E39-R1.",
      swap={"EXT-E39-R1": ("EXT-E39-R1S", 2)})
for kit, n, rev in (("AG-SEN2-RR-Kit", 1, "D"), ("AG-SEN2-TB-Kit", 2, "B")):
    patch(kit, rev, "RJ-12 8ft to 15ft (Slack 2026-11-12). Adds the nylocks, enclosure pegs and 3/4in caps ByTechs now packs "
          "with sensor bar kits (ByTechs install-pack sheet), one set per enclosure: 2 nylocks, 4 pegs (Ben 2026-11-13), "
          "2 caps (Monti, Slack 2026-05-28).",
          swap={"EXT-CS-44050-08": ("EXT-TBD-RJ12-15FT", 1)},
          add=[line("EXT-B0C52TVDGW", 2 * n), line("EXT-27PIF0089", 4 * n), line("EXT-OLKOS75-100", 2 * n)])

# ---------------------------------------------------------------- install packs: base set + add-on kits
IP_ITEMS = {  # sheet part name -> part number (vendor IDs from data/sheets/install-pack-links.csv)
    "Alcohol Wipes": ("EXT-GOJ902712", "Alcohol Wipes (Purell, 120 ct)", "Purell", "GOJ902712", "Home Depot", "301078769"),
    "Enclosure padlocks": ("EXT-4680DBLKHC", "Enclosure Padlock (Master Lock TSA combo)", "Master Lock", "4680DBLKHC", "Home Depot", "100205856"),
    "Super 33+ Electrical Tape": ("EXT-6132-BA-10", "Super 33+ Electrical Tape", "3M Scotch", "6132-BA-10", "Home Depot", "304653556"),
    "Lexel Glue": ("EXT-B00IQCHZS4", "Lexel Adhesive, clear", "Sashco", "B00IQCHZS4", "Amazon", "B00IQCHZS4"),
    "IPEX Junction Boxes 12”x12”x6”": ("EXT-277009", "IPEX Junction Box 12x12x6in", "IPEX", "277009", "Gordon Electric Supply", "6458751"),
    "IPEX Junction Boxes 8”x8”x4”": ("EXT-277006", "IPEX Junction Box 8x8x4in", "IPEX", "277006", "Gordon Electric Supply", "6458748"),
    "3/4\" one hole straps - flat": ("EXT-B000W38PHU", "3/4in One-Hole Conduit Strap", "", "B000W38PHU", "Amazon", "B000W38PHU"),
    "1/2\" one hole straps - flat": ("EXT-26151", "1/2in One-Hole EMT Strap", "Halex", "26151", "Home Depot", "100172548"),
    "Tapcon 1/4” x 1.25”": ("EXT-TBD-TAPCON-025X125-SS", "Tapcon 1/4 x 1-1/4in, 410 stainless, hex", "", "", "Fasteners Plus", ""),
    "Tapcon 5/8” x 3”": ("EXT-THD50300H", "Strong-Tie Titen HD Screw Anchor 1/2 x 3in, zinc", "Simpson Strong-Tie", "THD50300H", "Fasteners Plus", ""),
    "Topaz 3/4” Rain Tight Connector": ("EXT-652SRT", "Topaz 3/4in Raintight Compression Connector", "Topaz", "652SRT", "Gordon Electric Supply", "6162894"),
    "Topaz 1/2” Rain Tight Connector": ("EXT-651SRT", "Topaz 1/2in Raintight Compression Connector", "Topaz", "651SRT", "Gordon Electric Supply", "6162893"),
    "Washers": ("AG-IP-001-001_Washer", "Bollard Washer (custom)", "SendCutSend", "IP-001-001_Washer", "SendCutSend", ""),
    "13 Gal Trashbag": ("EXT-B07NWC11T6", "13 gal Trash Bag", "", "B07NWC11T6", "Amazon", "B07NWC11T6"),
    "Microfiber Cloth": ("EXT-B0FSRN2719", "Microfiber Cloth", "", "B0FSRN2719", "Amazon", "B0FSRN2719"),
}
for pn, name, mfr, mpn, sup, spn in IP_ITEMS.values():
    item(pn, name, "Mechanical", mfr, mpn, sup, spn, "", "ByTechs install-pack sheet",
         "Vendor page has no maker part number." if pn.startswith("EXT-TBD") else
         ("CAD: tripwire-mcad Installer Kits/Bollard Washers." if pn.startswith("AG-") else ""))

items["EXT-THD50300H"]["Notes"] = ("The sheet calls this Tapcon 5/8 x 3in; the anchor bought and packed is the Titen HD "
                                   "1/2 x 3in, sold in packs of 25 (Ben 2026-11-13).")
items["EXT-GOJ902712"]["Notes"] = "Quantity is single wipes, from a box of 120 (Ben 2026-11-13)."

sheet = list(csv.reader(open(SHEETS / "bytechs-install-packs_SKUs.csv")))
hdr, body = sheet[0], [r for r in sheet[1:] if r[1] and r[1] != "Totals" and not r[1].startswith("Nylocks")]
total = next(r for r in sheet if r[1] == "Totals")
PACKS = [  # (sheet column, name-col, assembly PN, name, kit PN, kit name)
    (5, 1, "AG-IP-001-000", "Install Pack Base Set", "AG-IP-RRWM-DC-Kit", "Install Pack: Retro Reflective - Wall Mount - Dual Camera"),
    (4, 1, "AG-IP-002-000", "Install Pack Add-on: RR Bollard Mount", "AG-IP-RRBM-DC-Kit", "Install Pack: Retro Reflective - Bollard Mount - Dual Camera"),
    (6, 1, "AG-IP-003-000", "Install Pack Add-on: Through Beam", "AG-IP-TB-DC-Kit", "Install Pack: Through Beam - Dual Camera"),
    (10, 7, "AG-IP-004-000", "Install Pack Add-on: RR Bollard Mount, Reverse Camera", "AG-IP-RRBM-DCR-Kit", "Install Pack: Retro Reflective - Bollard Mount - Dual Camera - Reverse Camera"),
    (11, 7, "AG-IP-005-000", "Install Pack Add-on: RR Wall Mount, Reverse Camera", "AG-IP-RRWM-DCR-Kit", "Install Pack: Retro Reflective - Wall Mount - Dual Camera - Reverse Camera"),
    (12, 7, "AG-IP-006-000", "Install Pack Add-on: Through Beam, Reverse Camera", "AG-IP-TB-DCR-Kit", "Install Pack: Through Beam - Dual Camera - Reverse Camera"),
]
for col, ncol, pn, name, kit, kitname in PACKS:
    ls = [line(IP_ITEMS[r[ncol]][0], int(r[col])) for r in body if r[col].strip().isdigit() and int(r[col])]
    assert sum(x["Quantity Per Unit"] for x in ls) == int(total[col]), pn  # self-check against the sheet's own total
    bom(pn, name, "A", "katana", ls, f"ByTechs install-pack sheet, column '{hdr[col]}'")
    kids = [line("AG-IP-001-000", 1)] + ([] if pn == "AG-IP-001-000" else [line(pn, 1)])
    bom(kit, kitname, "A", "katana", kids, "ByTechs install-pack sheet", "Full pack = base set + add-on (Ben 2026-11-13).")
for kit, name, inner in (("AG-IP-V4BM-DC-Kit", "Install Pack: v4 - Bollard Mount - Dual Camera", "AG-IP-RRBM-DC-Kit"),
                         ("AG-IP-V4WM-DCR-Kit", "Install Pack: v4 - Wall Mount - Dual Camera - Reverse Camera", "AG-IP-RRWM-DCR-Kit")):
    bom(kit, name, "A", "katana", [line(inner, 1)], "Ben 2026-11-13",
        f"One vπ pack as a part ({inner}); V4 sensor hardware ships in the V4 box. Confirm the mapping.")

# ---------------------------------------------------------------- V4 sensor (X5), from Notion V4A/X4B and X3B
V4 = [  # (pn, name, type, mfr, mpn, supplier, spn, cost, source, notes)
    ("EXT-D1R", "Seyond Hummingbird D1R LiDAR", "Module", "Seyond", "D1R", "Seyond", "", 800, "Notion V4 X3B Assembly BoM", ""),
    ("AG-SEN4-001-001_Housing", "LiDAR Housing (plastic)", "Mechanical", "", "", "", "", "", "Notion V4A LiDAR Assembly BoM", "CAD: tripwire-mcad V4-release/X5 Release."),
    ("AG-SEN4-001-002_TopCover", "LiDAR Top Cover (plastic)", "Mechanical", "", "", "", "", "", "Notion V4A LiDAR Assembly BoM", ""),
    ("AG-SEN4-001-003_PCBMount", "Coupler PCB Mount (plastic)", "Mechanical", "", "", "", "", "", "Notion V4A LiDAR Assembly BoM", ""),
    ("AG-SEN4-001-004_Heatsink", "LiDAR Heatsink X2", "Mechanical", "SendCutSend", "", "SendCutSend", "", 14.5, "Notion V4A LiDAR Assembly BoM", ""),
    ("AG-SEN4-001-005_Coupler", "Bollard Coupler (machined, powder coated)", "Mechanical", "Triple B", "", "Triple B", "", "", "Notion V4A Machining BoM; Slack 2026-10-06",
     "Machined from 5.5in OD 6061 round stock (Nox Metals). Powder coat changing to an exterior-rated grey (Slack 2026-11-10)."),
    ("AG-SEN4-001-006_LiDARCoupler", "LiDAR Coupler / Housing Adapter (machined)", "Mechanical", "Triple B", "", "Triple B", "", "", "Notion V4A Machining BoM; Slack 2026-10-06",
     "Machined from 4in OD 6061 tube (McMaster 9056K42)."),
    ("AG-SEN4-001-007_ExtTube", "Extension Tube (machined, powder coated)", "Mechanical", "Triple B", "", "Triple B", "", "", "Notion V4A Machining BoM; Slack 2026-10-06",
     "Cut 23.5 to 23.75in from 4in schedule 40 6061 pipe."),
    ("EXT-MSAS17ML-SASFL-SB001", "M12 17-pin M-F Cable (1m)", "Cable", "Amphenol", "MSAS17ML-SASFL-SB001", "Mouser", "", 61.17, "Notion V4 X3B Assembly BoM",
     "V4A note: replacement wanted (availability; 2.5ft requested)."),
    ("EXT-91292A112", "M3x8mm Socket Head Screw", "Mechanical", "McMaster-Carr", "91292A112", "McMaster-Carr", "91292A112", "", "Notion V4A LiDAR Assembly BoM", ""),
    ("EXT-96817A322", "T10 M3x10mm Thread-Forming Screw for Plastic", "Mechanical", "McMaster-Carr", "96817A322", "McMaster-Carr", "96817A322", "", "Notion V4A LiDAR Assembly BoM", ""),
    ("EXT-94625A131", "T27 Security Torx Self-Tapping Screw", "Mechanical", "McMaster-Carr", "94625A131", "McMaster-Carr", "94625A131", "", "Notion V4A LiDAR Assembly BoM",
     "Coupler screws: Slack 2026-10-30 commits to 1in self-tapping stainless (Tanner Bolts); the V4 kit note names 95015A314. Confirm."),
    ("EXT-TBD-T27-14-20", "T27 Security Torx 1/4-20 Screw", "Mechanical", "", "", "", "", "", "Notion V4A LiDAR Assembly BoM", "No part number in Notion."),
    ("EXT-TBD-V4-THERMALPAD", "Thermal Pad (LiDAR)", "Mechanical", "", "", "", "", "", "Notion V4A LiDAR Assembly BoM", "No part number in Notion."),
    ("EXT-MB-835", "MaxiBond MB-835 Epoxy", "Other", "MaxiBond", "MB-835", "", "", "", "Notion V4A LiDAR Assembly BoM", "Glues the 4in OD tube."),
    ("EXT-95893A198", "Plastic Thread-Forming Screw 30mm", "Mechanical", "McMaster-Carr", "95893A198", "McMaster-Carr", "95893A198", "", "Notion V4A LiDAR Assembly BoM", "Quantity blank in Notion."),
]
for t in V4:
    item(*t)
# X4A interposer, from the Notion BoM (newer than KiCad; see research/ecad-open-prs.md)
item("AG-SEN4-002-001_PCB", "Sensor Interposer bare PCB", "Mechanical", "AirGarage", "SEN4-002-001_PCB", "OSHPark", "", 43, "Notion X4A Sensor Interposer PCB")
ip_lines = [line("AG-SEN4-002-001_PCB", 1)]
for r in rows(NOTION / "x4a-sensor-interposer-pcb.csv"):
    q = num(r["Quantity Per Unit"])
    if not r["Part Number"] or not q:
        continue  # the bare PCB (above) and the 0603 LED kept at qty 0 "for reference"
    refs = re.match(r"^([A-Z]+\d+(?:,\s*[A-Z]+\d+)*)\s*[—-]", r["Notes"])
    pn = "EXT-" + r["Part Number"]
    item(pn, r["Part Name"], "Electronic", "", r["Part Number"], "DigiKey", "", num(r["Cost"]) or "", "Notion X4A Sensor Interposer PCB")
    ip_lines.append(line(pn, q, designator=refs[1].replace(" ", "") if refs else ""))
bom("AG-SEN4-002-000_Interposer", "Sensor Interposer PCBA", "X4A", "katana", ip_lines, "Notion X4A Sensor Interposer PCB",
    "Notion values (R1 6.8k, R3 1M, D2 SMAJ28A, C1 10nF 1kV, R6) are in no tripwire-ecad branch; KiCad main and PR #27 still have the older values.")
bom("AG-SEN4-001-000", "V4 LiDAR Sensor", "X5", "katana", [
    line("EXT-D1R", 1), line("AG-SEN4-002-000_Interposer", 1, rev="X4A"), line("AG-SEN4-001-001_Housing", 1),
    line("AG-SEN4-001-002_TopCover", 1), line("AG-SEN4-001-003_PCBMount", 1), line("AG-SEN4-001-004_Heatsink", 1),
    line("AG-SEN4-001-005_Coupler", 1), line("AG-SEN4-001-006_LiDARCoupler", 1), line("AG-SEN4-001-007_ExtTube", 1),
    line("EXT-MSAS17ML-SASFL-SB001", 1), line("EXT-91292A112", 7), line("EXT-96817A322", 8), line("EXT-94625A131", 6),
    line("EXT-TBD-T27-14-20", 3), line("EXT-TBD-V4-THERMALPAD", 1), line("EXT-MB-835", 1),
    line("EXT-95893A198", "TBD", "Quantity blank in Notion.")],
    "Notion V4A LiDAR Assembly + V4A Machining + V4 X3B Assembly",
    "X5 is the production build (Slack 2026-10-06); no X5 BoM exists, so this joins the newest Notion BoMs. MCAD X5 Release also has "
    "Internal Coupler ASM and Vamp Clamp ASM, in no BoM. Confirm with Monti.")
V4KIT = [("EXT-TBD-T27-SELFDRILL", "T27 Security Torx Self-Drilling Screw", 6, "P/N not finalized in Notion."),
         ("EXT-TBD-T27-BIT", "T27 Security Torx Impact Bit", 2, ""), ("EXT-GOJ902712", None, 1, ""),
         ("EXT-TBD-DRILL-7-32", "7/32in Drill Bit", 1, ""), ("EXT-TBD-RJ45-15FT", "RJ-45 Cable (15ft)", 1, ""),
         ("EXT-TBD-RJ12-15FT", None, 1, ""), ("EXT-TBD-TAPCON-050", "1/2in Tapcon", 4, ""), ("EXT-TBD-WASHER-050", "1/2in Washer", 4, "")]
for pn, name, _, note in V4KIT:
    if name:
        item(pn, name, "Mechanical", "", "", "", "", "", "Notion V4 Sensor Kit BoM", note)
bom("AG-SEN4-003-000", "V4 Sensor Install Kit", "A", "katana", [line(pn, q) for pn, _, q, _ in V4KIT],
    "Notion V4 Sensor Kit BoM (2026-11-04)", "Every line lacks a part number in Notion.")
bom("AG-SEN4-Kit", "V4 Sensor Kit", "A", "katana", [line("AG-SEN4-001-000", 1, rev="X5"), line("AG-SEN4-003-000", 1)],
    "Shopify 'v4 Sensor Bar Assembly'; Slack 2026-11-04", "Install hardware ships in the V4 box (Slack 2026-11-04).")

# ---------------------------------------------------------------- V3.1 (cleaned, not migrated)
ALIAS = {"SC1113": "EXT-SC1113", "MB-MJ256KA": "EXT-MB-MJ256KA/AM", "G3 (Global-3)": "EXT-G3-F", "952-3964-ND": "EXT-952-3964-ND",
         "732-12917-ND": "EXT-732-12917-ND", "SC1148": "EXT-SC1148", "INR-18650-P30B": "EXT-INR-18650-P30B"}


def v31(slug, name_col):
    out = []
    for r in rows(NOTION / f"{slug}.csv"):
        mpn = (r.get("Part Number - Mfg") or "").strip()
        internal = (r.get("Part Number - Internal") or r.get("Part Number") or "").strip()
        if mpn and mpn != "N/A":
            pn = ALIAS.get(mpn) or "EXT-" + re.sub(r"[^A-Za-z0-9.\-+/#]", "-", mpn.split(",")[0])
        elif internal.startswith("ELP-"):
            pn, mpn = "EXT-ELP-USBGS5MP01", internal
        else:
            pn = "AG-" + internal
        item(pn, r[name_col], "Mechanical", "", mpn if mpn != "N/A" else "", r.get("Supplier", ""), "",
             "", f"Notion {slug}", f"V3.1 internal number {internal}" if internal and pn.startswith("EXT-") else "")
        out.append(line(pn, num(r["Quantity Per Unit"]) or "", r.get("Notes", "").replace("\n", " ")[:200]))
    return out


bom("AG-CAM4-001-000", "Tripwire V3.1 Camera Assembly", "A", "legacy", v31("tripwire-v3-1-camera-assembly", "Name"),
    "Notion Tripwire V3.1 Camera Assembly BoM", "Not migrated. ELP camera is one of KV100IR (4mm), KV60IR (6mm), KV80IR (8mm).")
bom("AG-COM4-001-000", "Tripwire V3.1 Compute Stack", "A", "legacy", v31("tripwire-v3-1-compute-stack", "Part Name"),
    "Notion Tripwire V3.1 Compute Stack BoM", "Not migrated. V3.1 sensor bar = AG-SEN2-001-000 (same parts and numbers).")

# ---------------------------------------------------------------- Obelisk (draft, not migrated)
csbi = []
item("AG-OBL-002-001_PCB", "Compute Stack Bollard Interface bare PCB", "Mechanical", "AirGarage", "OBL-002-001_PCB", "", "", "", "tripwire-ecad PR #28")
csbi.append(line("AG-OBL-002-001_PCB", 1))
for r in rows(ECAD / "compute-stack-bollard-interface@88d20a6.csv"):
    if r["Value"] == "MountingHole":
        continue
    mfr, mpn = r["MPN"].rsplit(" ", 1)
    pn = "EXT-" + mpn
    item(pn, f"{r['Value']} ({r['Footprint'].split(':')[-1]})", "Electronic", mfr, mpn, "", "", "", "tripwire-ecad PR #28")
    csbi.append(line(pn, int(r["Quantity"]), designator=r["Designators"]))
bom("AG-OBL-002-000_CSInterface", "Compute Stack Bollard Interface PCBA", "X1", "draft", csbi,
    "tripwire-ecad PR #28 (HW-975) @ 88d20a6", "Open PR; product assignment assumed (Obelisk). Confirm.")
OBL = [("AG-OBL-001-001_Tube", "Schedule 40 Pipe Segment", "Slack #pt-obelisk 2026-10-16", "TBD"),
       ("AG-OBL-001-002_VampClamp", "Vamp Clamp (module interlock)", "Slack #pt-obelisk 2026-10-16; MCAD X5 Release Vamp Clamp ASM", "TBD"),
       ("AG-OBL-001-003_SnapRing", "Snap Ring, 7075 laser cut", "Slack #pt-obelisk 2026-10-16", "TBD"),
       ("EXT-TBD-M10-CS", "M10 Countersunk Fastener", "Slack #pt-obelisk 2026-10-16", "TBD"),
       ("EXT-TBD-OBL-MAGNET", "Magnet (module presence)", "Slack #pt-obelisk 2026-10-16", "TBD"),
       ("EXT-TBD-OBL-TMR", "TMR/Hall Sensor", "Slack #pt-obelisk 2026-10-16", "TBD"),
       ("EXT-DP460NS", "3M DP460NS Epoxy", "Slack #pt-obelisk 2026-10-16", "TBD"),
       ("EXT-TBD-AS568-045-EPDM", "O-ring AS568-045, EPDM", "Slack #pt-obelisk 2026-10-29", "TBD"),
       ("EXT-TBD-OBL-MCU", "Module MCU (STM32C5 shortlisted)", "Slack #pt-obelisk 2026-10-31", "TBD"),
       ("EXT-90292A076", "#8-32 Shoulder Screw, 17-4PH (proposed)", "Slack 2026-11-04", "TBD"),
       ("EXT-TBD-RJ45-15FT", None, "Slack #pt-obelisk 2026-11-05", 1),
       ("EXT-TBD-OBL-CAMUSB", "Camera USB Cable", "Slack #pt-obelisk 2026-11-05", 2),
       ("AG-OBL-003-000_CameraModule", "Obelisk Camera Module (pivoting cameras)", "Slack #pt-obelisk 2026-11-12", 1)]
for pn, name, src, _ in OBL:
    if name:
        item(pn, name, "Mechanical", "", "", "", "", "", src, "Prototype; in flux.")
bom("AG-OBL-001-000", "Obelisk (draft)", "draft", "draft",
    [line("EXT-D1R", 1), line("AG-OBL-002-000_CSInterface", 1, rev="X1"),
     line("AG-CS3-001-000", 1, "Assumed; Obelisk compute is not defined.")] + [line(pn, q, src) for pn, _, src, q in OBL],
    "Slack #pt-obelisk, #airgarage-bytechs-tripleb-v4-hardware; tripwire-ecad PR #28",
    "Design in flux (Ben 2026-11-13). Skeleton of known modules and parts with sources; not a buildable BOM.")

# ---------------------------------------------------------------- part-number corrections (Ben 2026-11-13)
CORRECT = {"EXT-95893A197": ("EXT-95893A198", "M3 x 30 mm screw is McMaster 95893A198, not 95893A197 (Ben 2026-11-13).")}
for b in boms.values():
    for x in b["lines"]:
        if x["Part Number"] in CORRECT:
            new, why = CORRECT[x["Part Number"]]
            x.update(line(new, x["Quantity Per Unit"], x.get("Notes", "")))
            if why not in b["change"]:
                b["change"] = f"{b['change']} {why}".strip()
for old in CORRECT:
    del items[old]

# ---------------------------------------------------------------- write
for d in ("", "legacy-v3.1", "obelisk"):
    (OUT / d).mkdir(exist_ok=True)
    for old in (OUT / d).glob("*.csv"):
        old.unlink()  # generated files only; the Aligni export lives in its own folder
DIRS = {"katana": "", "legacy": "legacy-v3.1", "draft": "obelisk"}
used = Counter()
index = []
for pn, b in sorted(boms.items()):
    ls = b["lines"]
    for i, x in enumerate(ls, 1):
        x["Line"] = i
        assert x["Part Number"] in items, (pn, x["Part Number"])  # self-check: every child is a known item
        used[x["Part Number"]] += 1
    path = OUT / DIRS[b["scope"]] / f"{pn.replace('/', '-')}.csv"
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, COLS)
        w.writeheader()
        w.writerows({c: x.get(c, "") for c in COLS} for x in ls)
    index.append({"Assembly": pn, "Name": b["name"], "Revision": b["rev"],
                  "Scope": {"katana": "Katana", "legacy": "Legacy (not migrated)", "draft": "Draft (not migrated)"}[b["scope"]],
                  "Lines": len(ls), "Open": sum(1 for x in ls if "TBD" in x["Part Number"] or x["Quantity Per Unit"] in ("", "TBD")),
                  "File": str(path.relative_to(OUT)), "Source": b["source"], "Change": b["change"]})
with open(OUT / "index.csv", "w", newline="") as f:
    w = csv.DictWriter(f, list(index[0]))
    w.writeheader()
    w.writerows(index)
with open(OUT / "items.csv", "w", newline="") as f:
    w = csv.DictWriter(f, ITEM_COLS + ["Used In BOMs", "Renamed From"])
    w.writeheader()
    old = {v: k for k, v in RENAME.items()}
    w.writerows(dict(i, **{"Used In BOMs": used[p], "Renamed From": old.get(p, "")}) for p, i in sorted(items.items()))
dup = [k for k, v in Counter((i["Part Name"], i["Part Number - Mfg"]) for i in items.values() if i["Part Number - Mfg"]).items() if v > 1]
print(f"{len(index)} BOMs ({Counter(i['Scope'] for i in index)}), {len(items)} items, {sum(i['Open'] for i in index)} open lines")
print("items sharing a name and MPN under different part numbers:", dup or "none")
