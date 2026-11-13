# /// script
# requires-python = ">=3.15"
# ///
"""Write one CSV per Aligni assembly to <workspace>/boms/ from a pull.py snapshot. No network.

    uv run export.py data/20261113T0325Z

Columns follow the Notion BoM databases (Part Name ... Notes), then the Aligni fields
Katana needs. Active revision -> boms/<PN>.csv; other revisions -> boms/revisions/<PN>_Rev<X>.csv.
"""
import csv, json, sys
from pathlib import Path

SNAP = Path(sys.argv[1])
OUT = Path(__file__).resolve().parents[2] / "boms"
EXCLUDE = {"TEST-Kit"}  # Aligni test object, not a product
COLS = ["Line", "Part Name", "Part Number", "Part Number - Mfg", "Manufacturer", "Supplier",
        "Supplier Part Number", "Quantity Per Unit", "Unit", "Min Quantity Per Purchase", "Cost",
        "Cost Per Unit", "Links", "Notes", "Designator", "No Load", "Part Type", "Child Revision"]

parts = {p["id"]: p for p in json.load(open(SNAP / "parts.json"))}
revs = json.load(open(SNAP / "part_revisions.json"))
name = {r["part"]["id"]: r["description"] for r in revs if r["active"]}


def num(x):
    return "" if x is None else (int(x) if float(x).is_integer() else x)


def row(b):
    c = parts[b["childPart"]["id"]]
    vpn = c["vendorPartNumbers"]["nodes"]
    supplier = (c["preferredVendor"] or {}).get("name") or (vpn[0]["vendorName"] if vpn else "")
    spn = next((v["partNumber"] for v in vpn if v["vendorName"] == supplier), "")
    return {"Line": b["position"], "Part Name": name.get(c["id"], ""), "Part Number": c["partNumber"],
            "Part Number - Mfg": c["manufacturerPn"], "Manufacturer": c["manufacturer"]["name"],
            "Supplier": supplier, "Supplier Part Number": spn, "Quantity Per Unit": num(b["quantity"]),
            "Unit": c["unit"]["name"], "Min Quantity Per Purchase": "", "Cost": "",
            "Cost Per Unit": num(c["standardCost"]), "Links": "", "Notes": b["comment"] or "",
            "Designator": b["designator"] or "", "No Load": "Y" if b["noLoad"] else "",
            "Part Type": c["partType"]["name"], "Child Revision": b["childPartRevision"]["revisionName"]}


(OUT / "revisions").mkdir(parents=True, exist_ok=True)
index = []
for r in sorted(revs, key=lambda r: (r["part"]["partNumber"], r["revisionName"])):
    pn, items = r["part"]["partNumber"], r["bomItems"].get("nodes", [])
    if not items or pn in EXCLUDE:
        continue
    path = OUT / (f"{pn}.csv" if r["active"] else f"revisions/{pn}_Rev{r['revisionName']}.csv")
    rows = [row(b) for b in sorted(items, key=lambda b: (b["position"] or 0, b["childPart"]["partNumber"]))]
    assert len(rows) == r["bomItems"]["totalCount"], pn
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, COLS)
        w.writeheader()
        w.writerows(rows)
    index.append({"Assembly": pn, "Name": r["description"], "Revision": r["revisionName"],
                  "Status": r["status"], "Active": "Y" if r["active"] else "", "Lines": len(rows),
                  "Released At": r["releasedAt"] or "", "Revision Reason": r["revisionReason"] or "",
                  "File": str(path.relative_to(OUT)), "Aligni Revision ID": r["id"]})

with open(OUT / "index.csv", "w", newline="") as f:
    w = csv.DictWriter(f, list(index[0]))
    w.writeheader()
    w.writerows(index)
print(len(index), "BOM files;", sum(1 for i in index if i["Active"]), "active")
