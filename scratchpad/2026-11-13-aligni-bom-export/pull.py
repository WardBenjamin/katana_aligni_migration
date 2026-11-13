# /// script
# requires-python = ">=3.15"
# ///
"""Snapshot every Aligni part and part revision (with BOM lines) to data/<UTC stamp>/.

Paced by aligni.gql (one request at a time, >= 7 s apart). The account has ~105 parts,
so this is a handful of requests.
"""
import json, sys, time
from pathlib import Path
from aligni import gql

PAGE = 50
PART = """id partNumber manufacturerPn description: valueText value hidden manufacturedHere
  createdAt updatedAt standardCost standardCostCurrency standardLeadTime attrition reorderQuantity
  partType { name partnumberKey } unit { name } manufacturer { name shortName }
  preferredVendor { name }
  vendorPartNumbers(first: 20) { nodes { partNumber vendorName comment } }
  customParameters(first: 50) { nodes { name value } }
  activeRevision { id revisionName }"""
REV = """id revisionName active status description comment revisionReason releasedAt createdAt updatedAt
  part { id partNumber } bomItems(first: 1) { totalCount }"""
BOM_ITEM = """id position buildSequence quantity designator comment noLoad
  childPart { id partNumber manufacturerPn } childPartRevision { id revisionName }"""
ITEM_COST = 16  # observed complexity per nested BOM line, with margin; cap is 10,000 per request


def page_all(root, fields):
    out, after = [], None
    while True:
        q = f"query($after: String) {{ rateLimit {{ cost remaining }} {root}(first: {PAGE}, after: $after) {{ totalCount pageInfo {{ endCursor hasNextPage }} nodes {{ {fields} }} }} }}"
        d = gql(q, {"after": after})["data"]
        c = d[root]
        out += c["nodes"]
        print(f"  {root}: {len(out)}/{c['totalCount']} (cost {d['rateLimit']['cost']}, remaining {d['rateLimit']['remaining']})", flush=True)
        if not c["pageInfo"]["hasNextPage"]:
            return out
        after = c["pageInfo"]["endCursor"]


stamp = time.strftime("%Y%m%dT%H%MZ", time.gmtime())
dest = Path("data") / stamp
dest.mkdir(parents=True)
parts = page_all("parts", PART)
json.dump(parts, open(dest / "parts.json", "w"), indent=1)
revs = page_all("partRevisions", REV)

# Phase 2: fetch BOM lines only for revisions that have them, several per request via aliases.
todo = [r for r in revs if r["bomItems"]["totalCount"]]
assert max((r["bomItems"]["totalCount"] for r in todo), default=0) * ITEM_COST < 9000, "one BOM too big for a request; add paging"
batch = []
def flush():
    q = "query { " + " ".join(
        f'r{i}: partRevision(id: "{r["id"]}") {{ bomItems(first: {r["bomItems"]["totalCount"]}) {{ totalCount nodes {{ {BOM_ITEM} }} }} }}'
        for i, r in enumerate(batch)) + " }"
    d = gql(q)["data"]
    for i, r in enumerate(batch):
        r["bomItems"] = d[f"r{i}"]["bomItems"]
        assert len(r["bomItems"]["nodes"]) == r["bomItems"]["totalCount"], r["id"]
    print(f"  bom lines for {len(batch)} revisions", flush=True)
    batch.clear()
for r in todo:
    if batch and (sum(b["bomItems"]["totalCount"] for b in batch) + r["bomItems"]["totalCount"]) * ITEM_COST >= 9000:
        flush()
    batch.append(r)
if batch:
    flush()
json.dump(revs, open(dest / "part_revisions.json", "w"), indent=1)
print(dest, len(parts), "parts", len(revs), "revisions")
