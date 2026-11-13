# /// script
# requires-python = ">=3.15"
# ///
"""Price one unit of a configuration from the Ramp cost record.

    uv run price_config.py configs/rr-bollard-dual46.csv [--as-of 2026-11-13]

Each leaf part gets one row per configuration line; each assembly gets a labour row.
A part listed in price_adders.csv also gets an adder row for a cost that is on no invoice line
(import duty, for example).
A price comes from, in order of preference: the latest purchase at production quantity
(enough for MIN_BUILDS units), a price in manual_prices.csv, the latest small-lot purchase.
Anything dated within STALE_DAYS of the as-of date beats anything older; older prices are
marked stale. Purchases are found by part number, and by the patterns in price_rules.csv.
Writes out/<config>_price_lines.csv and prints totals by status.
"""

import argparse
import csv
import re
from collections import defaultdict
from datetime import UTC, date, datetime, timedelta
from pathlib import Path

from explode_config import BOMS, COST_LINES, ROOT, explode, read

HERE = Path(__file__).parent
MIN_BUILDS = 10   # a purchase is production quantity if it covers this many units
STALE_DAYS = 183  # six months
MIN_TOKEN = 6     # shorter part-number fragments match unrelated receipt text
# Digi-Key numbers for one part differ only by packaging: -1-ND cut tape, -2-ND reel, -6-ND Digi-Reel
DK_PACKAGING = re.compile(r"(-[126]-ND|(?:TR|CT|DKR)-ND|-ND)$", re.I)
PACK = re.compile(r"packs? of (\d+)")
RANK = {"purchase": 0, "manual": 1, "small-lot purchase": 2}
FIELDS = ["Config Line", "Kind", "Part Number", "Part Name", "Extended Quantity", "Each Cost", "Extended Cost",
          "Status", "Price Date UTC", "Vendor", "Purchased Quantity", "Units Per Pack", "Purchase Lines",
          "Flag", "Source"]


def invoice_lines():
    """Lines typed from invoices outside the Ramp pull, landed pro rata by line total like the cost record."""
    typed = read(HERE / "invoice_lines.csv")
    goods = defaultdict(float)
    for r in typed:
        goods[r["source_file"], r["invoice_goods_total"]] += float(r["line_total"])
    for (source, total), summed in goods.items():
        assert abs(summed - float(total)) < 0.005, f"lines do not add up to the goods total: {source}"
    return [{"date_utc": r["date_utc"], "vendor": r["vendor"], "vendor_pn": "", "mpn": "", "item_code": "",
             "item_name": r["item_name"], "item_name_full": "", "quantity": r["quantity"], "unit_price": r["unit_price"],
             "landed_unit_cost": float(r["line_total"]) * float(r["invoice_total"]) / float(r["invoice_goods_total"]) / float(r["quantity"]),
             "needs_review": "False", "link": f"{r['source_file']} ({r['invoice_no']})", "flag": r["flag"]} for r in typed]


def tokens(part, item):
    raw = {part.removeprefix("EXT-").removeprefix("AG-"), item.get("Part Number - Mfg", ""),
           item.get("Supplier Part Number", "")}
    raw |= {DK_PACKAGING.sub("", t) for t in raw}
    return {t.lower() for t in raw if len(t) >= MIN_TOKEN}


def observations(part, item, need, rules, manual, cost_lines):
    """Every price seen for a part, as dicts with kind, date, each, and where it came from."""
    toks = tokens(part, item)
    obs = []
    for c in cost_lines:
        if not c["landed_unit_cost"] or c["vendor_pn"].upper() == "FREIGHT":
            continue
        rule = next((r for r in rules.get(part, ())
                     if re.search(r["Vendor Pattern"], c["vendor"], re.I) and re.search(r["Item Pattern"], c["_text"])), None)
        if rule is None and not any(t in c["_text"] for t in toks):
            continue
        pack = float(rule["Units Per Pack"]) if rule and rule["Units Per Pack"] else None
        if pack is None:
            m = PACK.search(c["_text"])
            pack = float(m.group(1)) if m else 1.0
        flags = [f for f in (rule and rule["Flag"], c.get("flag")) if f]
        # A record under review has a landed cost spread by estimate, so its receipt unit price is used.
        review = c["needs_review"] == "True"
        if review:
            flags.append("record under review: receipt unit price, no tax or freight")
        qty = float(c["quantity"])
        obs.append({"kind": "purchase" if qty * pack >= MIN_BUILDS * need else "small-lot purchase",
                    "date": c["date_utc"][:10], "each": float(c["unit_price"] if review else c["landed_unit_cost"]) / pack,
                    "vendor": c["vendor"], "qty": qty, "pack": pack, "flag": "; ".join(flags), "source": c["link"]})
    lines = len(obs)
    for m in manual.get(part, ()):
        obs.append({"kind": "manual", "label": m["Basis"], "date": m["Date UTC"], "each": float(m["Each Cost"]),
                    "vendor": "", "qty": "", "pack": "", "flag": m["Note"], "source": m["Source"]})
    return obs, lines


def choose(obs, cutoff):
    """(observation, status). Fresh beats stale; within each, RANK then latest date."""
    if not obs:
        return None, "none"
    fresh = [o for o in obs if o["date"] >= cutoff]
    pick = min(fresh or obs, key=lambda o: (RANK[o["kind"]], -date.fromisoformat(o["date"]).toordinal()))
    return pick, ("" if fresh else "stale ") + pick.get("label", pick["kind"])


def selftest():
    def o(kind, day):
        return {"kind": kind, "date": day}
    cut = "2026-05-14"
    assert choose([], cut) == (None, "none")
    assert choose([o("small-lot purchase", "2026-06-01"), o("purchase", "2025-01-01")], cut)[1] == "small-lot purchase"
    assert choose([o("purchase", "2026-06-01"), o("purchase", "2026-07-01"), o("manual", "2026-11-01") | {"label": "quote"}], cut)[0]["date"] == "2026-07-01"
    assert choose([o("small-lot purchase", "2025-07-01"), o("purchase", "2025-04-01")], cut)[1] == "stale purchase"
    assert tokens("EXT-X", {"Supplier Part Number": "490-10784-2-ND"}) == {"490-10784-2-nd", "490-10784"}


def main():
    selftest()
    ap = argparse.ArgumentParser()
    ap.add_argument("config")
    ap.add_argument("--as-of", default=datetime.now(UTC).date().isoformat())
    args = ap.parse_args()
    cutoff = (date.fromisoformat(args.as_of) - timedelta(days=STALE_DAYS)).isoformat()

    index = [r for r in read(BOMS / "index.csv") if r["Scope"] == "Katana"]
    boms = {r["Assembly"]: read(BOMS / r["File"]) for r in index}
    names = {r["Assembly"]: r["Name"] for r in index}
    items = {r["Part Number"]: r for r in read(BOMS / "items.csv")}
    rules, manual = defaultdict(list), defaultdict(list)
    for r in read(HERE / "price_rules.csv"):
        assert None not in r, f"unquoted comma in price_rules.csv: {r['Part Number']}"
        rules[r["Part Number"]].append(r)
    for m in read(HERE / "manual_prices.csv"):
        manual[m["Part Number"]].append(m)
    adders = defaultdict(list)
    for a in read(HERE / "price_adders.csv"):
        adders[a["Part Number"]].append(a)
    cost_lines = read(COST_LINES) + invoice_lines()
    for c in cost_lines:
        c["_text"] = " ".join(c[k] for k in ("vendor_pn", "mpn", "item_code", "item_name", "item_name_full")).lower()

    qty = defaultdict(float)  # (config line, part, is_assembly) -> extended quantity
    for line in read(args.config):
        for part, q, _, is_assembly in explode(line["Part Number"], float(line["Quantity"]), boms):
            qty[line["Part Number"], part, is_assembly] += q
    need = defaultdict(float)  # per unit of the whole configuration
    for (_, part, is_assembly), q in qty.items():
        need[part, is_assembly] += q

    rows, priced = [], {}
    for (root, part, is_assembly), q in sorted(qty.items()):
        if (part, is_assembly) not in priced:
            obs, lines = observations(part, items.get(part, {}), need[part, is_assembly], rules, manual, cost_lines)
            priced[part, is_assembly] = (*choose(obs, cutoff), lines)
        pick, status, lines = priced[part, is_assembly]
        pick = pick or {}
        each = pick.get("each")
        rows.append({
            "Config Line": root, "Kind": "labour" if is_assembly else "part", "Part Number": part,
            "Part Name": ("Labour: " + names[part]) if is_assembly else items.get(part, {}).get("Part Name", ""),
            "Extended Quantity": f"{q:g}",
            "Each Cost": "" if each is None else f"{each:.4f}",
            "Extended Cost": "" if each is None else f"{each * q:.2f}",
            "Status": status, "Price Date UTC": pick.get("date", ""), "Vendor": pick.get("vendor", ""),
            "Purchased Quantity": pick.get("qty", ""), "Units Per Pack": pick.get("pack", ""),
            "Purchase Lines": lines, "Flag": pick.get("flag", ""), "Source": pick.get("source", ""),
        })
        for a in () if is_assembly else adders.get(part, ()):
            rows.append({
                "Config Line": root, "Kind": "adder", "Part Number": part, "Part Name": a["Description"],
                "Extended Quantity": f"{q:g}", "Each Cost": f"{float(a['Each Cost']):.4f}",
                "Extended Cost": f"{float(a['Each Cost']) * q:.2f}",
                "Status": ("" if a["Date UTC"] >= cutoff else "stale ") + a["Basis"], "Price Date UTC": a["Date UTC"],
                "Vendor": "", "Purchased Quantity": "", "Units Per Pack": "", "Purchase Lines": "",
                "Flag": a["Note"], "Source": a["Source"],
            })

    out = HERE / "out" / f"{Path(args.config).stem}_price_lines.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)

    def total(pred):
        sel = [r for r in rows if pred(r)]
        return len(sel), sum(float(r["Extended Cost"] or 0) for r in sel)

    print(f"as of {args.as_of}; prices dated before {cutoff} are stale")
    for kind in ("part", "labour", "adder"):
        print(f"\n{kind} rows")
        for status in sorted({r["Status"] for r in rows if r["Kind"] == kind}):
            n, cost = total(lambda r: r["Kind"] == kind and r["Status"] == status)
            print(f"  {status:30} {n:>3} rows  ${cost:>9,.2f}")
    print("\nby configuration line (current / stale / unpriced rows)")
    for root in dict.fromkeys(r["Config Line"] for r in rows):
        mine = lambda r: r["Config Line"] == root
        n_cur, cur = total(lambda r: mine(r) and r["Each Cost"] and not r["Status"].startswith("stale"))
        n_old, old = total(lambda r: mine(r) and r["Status"].startswith("stale"))
        n_none, _ = total(lambda r: mine(r) and r["Status"] == "none")
        print(f"  {root:32} ${cur:>8,.2f} ({n_cur})  ${old:>8,.2f} ({n_old})  {n_none} unpriced")
    print(f"-> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
