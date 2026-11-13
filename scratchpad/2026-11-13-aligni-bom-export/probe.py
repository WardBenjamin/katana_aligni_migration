# /// script
# requires-python = ">=3.15"
# ///
"""One request: counts, part types, rate-limit budget."""
import json
from aligni import gql
Q = """query {
 rateLimit { cost limit remaining resetAt used }
 metadata { queryCost totalComplexity totalQueries totalRecords }
 parts(first: 1) { totalCount }
 partRevisions(first: 1) { totalCount }
 partTypes(first: 100) { totalCount nodes { id name partnumberKey isNonMaterial parentOnly parent { name } } }
 units(first: 100) { nodes { id name } }
}"""
out = gql(Q)
json.dump(out, open("data/probe.json", "w"), indent=1)
d = out["data"]
print(d["rateLimit"], d["metadata"], d["parts"], d["partRevisions"], d["partTypes"]["totalCount"])
for t in d["partTypes"]["nodes"]:
    print(" ", t["partnumberKey"], "|", t["name"], "|", (t["parent"] or {}).get("name"), "| nonmat" if t["isNonMaterial"] else "")
