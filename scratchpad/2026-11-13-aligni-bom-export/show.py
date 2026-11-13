import json, sys
T = {t["name"]: t for t in json.load(open("data/schema.json"))["data"]["__schema"]["types"]}
def tn(t):
    return tn(t["ofType"]) + ("!" if t["kind"] == "NON_NULL" else "") if t["kind"] == "NON_NULL" else ("[" + tn(t["ofType"]) + "]" if t["kind"] == "LIST" else t["name"])
for name in sys.argv[1:]:
    t = T[name]; print(f"== {name} ({t['kind']})")
    for f in t.get("fields") or t.get("inputFields") or []:
        args = ",".join(a["name"] for a in f.get("args") or [])
        print(f"  {f['name']}({args}): {tn(f['type'])}")
    for e in t.get("enumValues") or []: print("  ", e["name"])
