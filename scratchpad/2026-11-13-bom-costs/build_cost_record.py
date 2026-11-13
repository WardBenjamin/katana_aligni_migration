# /// script
# requires-python = ">=3.15"
# ///
"""Build a per-line-item cost record from the Ramp pull.

One row per purchased line item for every card transaction, reimbursement and
bill dated on or after --since (UTC). Each record's charged amount is spread
over its lines, so landed line totals always sum to what was paid.

Run: uv run --python 3.15 build_cost_record.py [--since 2026-05-13]
Writes out/cost_lines_<since>.csv and out/cost_records_<since>.csv.
"""

import argparse
import collections
import csv
import glob
import json
import os
from email.utils import parsedate_to_datetime

HERE = os.path.dirname(os.path.abspath(__file__))
RAMP = os.path.join(HERE, "data", "ramp")
RAW = os.path.join(RAMP, "raw")
USERS = {
    "01954cee-c726-7b10-b069-c9c9b450ee6c": "Benjamin Ward",
    "01954cee-c717-707b-a6d2-fd8f365f01ac": "Bryan Monti",
    "019c9064-3541-72df-bab0-c9322d9fe100": "Chris Williamson",
}
CENT = 0.02  # totals within 2 cents are the same amount
REVIEW_SHARE = 0.10  # residual not explained by receipt tax/fees above this share of the amount


def jload(pattern):
    return [json.load(open(p)) for p in sorted(glob.glob(os.path.join(RAW, pattern)))]


def num(x):
    return None if x in (None, "") else float(x)


def receipt_lines(sd):
    """Normalized (code, name, qty, unit, total) lines from Ramp's receipt extraction.

    Extraction faults are corrected when doing so moves the line sum closer to the
    receipt's goods total (subtotal, else total less tax, fees and tip):
    - "4 of: ..." lines where item_total_price is really the unit price (Amazon);
    - the whole line list repeated twice;
    - lines with no quantity that are section headers or adders also listed as fees
      (FixturFab "Materials", Digi-Key and Mouser "Tariff").
    Excluded lines stay in the output with a note and no cost.
    """
    rows = [{"item_code": "", "item_name": li["item_name"], "quantity": num(li["item_quantity"]),
             "unit_price": num(li["item_unit_price"]), "line_total": num(li["item_total_price"]), "line_note": ""}
            for li in sd.get("line_items") or []]
    a = adders(sd)
    target = sd.get("subtotal") or ((sd.get("total_amount") or 0) - a["tax"] - a["fees"] - a["tip"])
    gap = lambda rs: abs(sum(r["line_total"] or 0 for r in rs if not r["line_note"]) - target)

    def exclude(rs, test, note):
        trial = [r | {"line_note": r["line_note"] or (note(i) if test(r) else "")} for i, r in enumerate(rs)]
        kept = [r for r in trial if not r["line_note"]]
        return trial if kept and gap(trial) < gap(rs) else rs

    half = len(rows) // 2
    key = lambda r: (r["item_name"], r["quantity"], r["unit_price"], r["line_total"])
    if rows and len(rows) % 2 == 0 and list(map(key, rows[:half])) == list(map(key, rows[half:])):
        trial = rows[:half] + [r | {"line_note": f"excluded: repeat of line {i + 1}"} for i, r in enumerate(rows[half:])]
        rows = trial if gap(trial) < gap(rows) else rows
    as_unit = [r | {"unit_price": r["line_total"], "line_total": r["line_total"] * r["quantity"]}
               if r["unit_price"] is None and r["quantity"] and r["quantity"] != 1 and r["line_total"] is not None else r
               for r in rows]
    if gap(as_unit) < gap(rows):
        rows = as_unit
    if any(r["quantity"] for r in rows):
        rows = exclude(rows, lambda r: r["quantity"] is None and (r["line_total"] or 0) > 0,
                       lambda i: "excluded: no quantity, header or adder listed as a fee")
    for r in rows:
        if r["line_note"]:
            r["line_note"] += f' (line total {r["line_total"]})'
            r["excluded_total"], r["line_total"] = r["line_total"], None
            continue
        if r["line_total"] is None and r["quantity"] is not None and r["unit_price"] is not None:
            r["line_total"] = r["quantity"] * r["unit_price"]
        if r["unit_price"] is None and r["line_total"] is not None and r["quantity"]:
            r["unit_price"] = r["line_total"] / r["quantity"]
    return rows


def adders(sd):
    s = lambda key, f: sum(x[f] or 0 for x in sd.get(key) or [])
    return {"tax": s("taxes", "tax_amount"), "fees": s("fees", "fee_amount"),
            "discounts": s("discounts", "discount_amount"), "tip": sd.get("tip") or 0}


def allocate(amount, lines):
    """Spread amount over lines pro rata by line_total. Returns (lines, flags).

    Lines whose totals sum to the opposite sign of amount are flipped (Pirate Ship
    lists label purchases as negative debits). With no priced lines, a single
    unallocated line carries the whole amount so nothing drops out of the record.
    """
    flags = []
    priced = [l for l in lines if l["line_total"]]
    base = sum(l["line_total"] for l in priced)
    if base and amount and (base > 0) != (amount > 0):
        for l in priced:
            l["line_total"] = -l["line_total"]
            l["unit_price"] = -l["unit_price"] if l["unit_price"] is not None else None
        base, flags = -base, ["line_signs_flipped"]
    if any(l["line_total"] is None and not l.get("line_note") for l in lines):
        flags.append("unpriced_lines")
    if not base:
        lines.append({"item_code": "", "item_name": "[unallocated: no priced lines]", "quantity": None,
                      "unit_price": None, "line_total": None, "line_source": "unallocated"})
        for l in lines:
            l["adders_allocated"] = 0.0
            l["landed_total"] = amount if l["line_source"] == "unallocated" else None
        return lines, flags + ["no_priced_lines"]
    residual = amount - base
    for l in lines:
        share = (l["line_total"] or 0) / base
        l["adders_allocated"] = residual * share
        l["landed_total"] = (l["line_total"] + residual * share) if l["line_total"] else None
    return lines, flags


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", default="2026-05-13", help="UTC date, inclusive")
    since = ap.parse_args().since

    spend = list(csv.DictReader(open(os.path.join(RAMP, "spend.csv"))))
    memo_by_txn = {s["card_transaction_id"]: s["memo"] for s in spend if s["card_transaction_id"]}
    manual = collections.defaultdict(list)
    for m in csv.DictReader(open(os.path.join(RAMP, "manual_lines.csv"))):
        manual[m["record_id"]].append({"item_code": m["item_code"], "item_name": m["item_name"],
                                       "quantity": num(m["quantity"]), "unit_price": num(m["unit_price"]),
                                       "line_total": num(m["line_total"]), "line_source": "manual:" + m["source_file"]})
    receipts = {r["receipt_uuid"]: r["structured_data"] or {}
                for d in jload("receipt_details/batch_*.json") + jload("reimbursement_receipt_details/*.json")
                for r in d["receipts"]}

    records = []

    # card transactions, grouped into orders when several charges share one receipt
    txns = [t for p in jload("transactions/page_*.json") for t in p["transactions"] if t["spent_by_user_uuid"] in USERS]
    fp = lambda rid: (receipts[rid].get("merchant_name"), receipts[rid].get("total_amount"),
                      tuple((l["item_name"], l["item_total_price"]) for l in receipts[rid].get("line_items") or []))
    itemized = lambda t: [r for r in t["receipt_uuids"] or [] if receipts.get(r, {}).get("line_items")]
    charges_by_fp = collections.defaultdict(list)
    for t in txns:
        for f in {fp(r) for r in itemized(t)}:
            charges_by_fp[f].append(t)
    order_of = {}
    for t in txns:
        rids = itemized(t)
        if not rids or any(abs((receipts[r].get("total_amount") or 0) - float(t["amount_value"])) < CENT for r in rids):
            continue
        for r in rids:  # a receipt split across charges that add up to its total
            group = {c["transaction_uuid"]: c for c in charges_by_fp[fp(r)]}
            total = sum(float(c["amount_value"]) for c in group.values())
            if len(group) > 1 and abs(total - (receipts[r].get("total_amount") or 0)) < CENT:
                for uid in group:
                    order_of[uid] = (tuple(sorted(group)), r)
                break

    done = set()
    for t in sorted(txns, key=lambda t: t["transaction_time"]):
        if t["transaction_uuid"] in done:
            continue
        uids, chosen = order_of.get(t["transaction_uuid"], ((t["transaction_uuid"],), None))
        group = [x for x in txns if x["transaction_uuid"] in uids]
        done.update(uids)
        if max(g["transaction_time"][:10] for g in group) < since:
            continue
        amount = round(sum(float(g["amount_value"]) for g in group), 2)
        rids = [r for g in group for r in itemized(g)]
        flags = ["split_across_charges"] if len(group) > 1 else []
        if chosen is None and rids:
            match = [r for r in rids if abs((receipts[r].get("total_amount") or 0) - amount) < CENT]
            pool = match or rids
            def fit(r):  # prefer the copy whose lines add up to its own goods total, then the fullest
                sd, ls = receipts[r], receipt_lines(receipts[r])
                a = adders(sd)
                goal = sd.get("subtotal") or ((sd.get("total_amount") or 0) - a["tax"] - a["fees"] - a["tip"])
                return (-round(abs(sum(l["line_total"] or 0 for l in ls) - goal), 2),
                        sum(1 for l in ls if l["line_total"]), len(ls))
            chosen = max(pool, key=fit)
            if not match:
                flags.append("receipt_total_mismatch")
        all_rids = [r for g in group for r in g["receipt_uuids"] or []]
        if t["transaction_uuid"] in manual:
            lines, sd = manual[t["transaction_uuid"]], {}
        elif chosen:
            sd = receipts[chosen]
            lines = [l | {"line_source": "receipt_extraction"} for l in receipt_lines(sd)]
        else:
            sd = {}
            flags.append("no_receipt" if not all_rids else "receipt_not_itemized")
            lines = [{"item_code": "", "item_name": memo_by_txn.get(t["transaction_uuid"]) or t["merchant_name"],
                      "quantity": None, "unit_price": None, "line_total": amount, "line_source": "record_only"}]
        records.append({
            "record_type": "card", "record_id": ";".join(g["transaction_uuid"] for g in group),
            "date_utc": t["transaction_time"], "user": t["spent_by_user"], "vendor": t["merchant_name"],
            "vendor_category": t["merchant_category"], "amount": amount, "status": t["state"],
            "memo": " | ".join(filter(None, (memo_by_txn.get(g["transaction_uuid"]) for g in group))),
            "fund": t["spend_allocation_name"],
            "accounting": "; ".join(f'{a["tracking_category_name"]}={a["tracking_category_option_name"]}'
                                    for a in t["accounting_categories"] or []),
            "receipt_uuid": chosen or "", "receipt_total": sd.get("total_amount"), "receipt_date": sd.get("transaction_date"),
            "receipts_on_record": len(all_rids), "adders": adders(sd), "lines": lines, "flags": flags,
            "link": t["transaction_link"],
        })

    # reimbursements (drafts kept and flagged)
    rr = {}
    for line in open(os.path.join(RAW, "reimbursement_receipts.jsonl")):
        rec = json.loads(line)
        rr[rec["reimbursement_uuid"]] = [x["receipt_uuid"] for x in rec["response"]["receipts"]]
    for r in [r for p in jload("reimbursements/*_page_*.json") for r in p["reimbursements"]]:
        date = (r["transaction_date"] or r["submitted_at"] or "")[:10]
        if date < since:
            continue
        amount = float(r["amount"])
        rids = rr.get(r["uuid"], [])
        flags = ["draft"] if r["status"] == "DRAFT" else []
        chosen, sd = None, {}
        for rid in rids:
            if receipts.get(rid, {}).get("line_items"):
                chosen, sd = rid, receipts[rid]
                break
        if r["uuid"] in manual:
            lines, chosen = manual[r["uuid"]], chosen or (rids[0] if rids else None)
        elif chosen:
            lines = [l | {"line_source": "receipt_extraction"} for l in receipt_lines(sd)]
            if abs((sd.get("total_amount") or 0) - amount) >= CENT:
                flags.append("receipt_total_mismatch")
        else:
            flags.append("no_receipt" if not rids else ("receipt_not_extracted" if rids[0] not in receipts else "receipt_not_itemized"))
            lines = [{"item_code": "", "item_name": r["memo"] or r["merchant_name"] or "", "quantity": None,
                      "unit_price": None, "line_total": amount, "line_source": "record_only"}]
        records.append({
            "record_type": "reimbursement", "record_id": r["uuid"], "date_utc": date, "user": USERS[r["user_id"]],
            "vendor": r["merchant_name"] or "", "vendor_category": "", "amount": amount, "status": r["status"],
            "memo": r["memo"] or "", "fund": (r["fund"] or {}).get("fund_name", ""),
            "accounting": "; ".join(f'{s["category_name"]}={(s["option_selection"] or {}).get("option_name")}'
                                    for s in r["tracking_category_selections"] or []),
            "receipt_uuid": chosen or "", "receipt_total": sd.get("total_amount"), "receipt_date": sd.get("transaction_date"),
            "receipts_on_record": len(rids), "adders": adders(sd), "lines": lines, "flags": flags,
            "link": r["reimbursement_link"],
        })

    # bills: lines transcribed from the invoice files into manual_lines.csv
    paid = {(s["invoice_number"], float(s["amount_usd"])): s for s in spend if s["spend_type"] == "Bill"}
    for b in jload("bills/*.details.json"):
        s = paid[(b["invoice_number"], float(b["amount"]))]
        if s["spend_time_utc"][:10] < since:
            continue
        flags = []
        lines = manual.get(b["id"])
        if not lines:
            flags.append("invoice_not_transcribed")
            lines = [{"item_code": "", "item_name": b["memo"] or b["invoice_number"], "quantity": None,
                      "unit_price": None, "line_total": float(b["amount"]), "line_source": "record_only"}]
        records.append({
            "record_type": "bill", "record_id": b["id"], "date_utc": s["spend_time_utc"], "user": s["user"],
            "vendor": b["vendor_name"], "vendor_category": s["category"], "amount": float(b["amount"]),
            "status": b["payment_status"], "memo": b["memo"] or "", "fund": "",
            "accounting": "; ".join(sorted({f'{c["category_name"]}={c["option_name"]}' for c in b["accounting_field_codings"] or []})),
            "receipt_uuid": "", "receipt_total": None,
            "receipt_date": parsedate_to_datetime(b["invoice_date"]).date().isoformat() if b["invoice_date"] else "",
            "receipts_on_record": 0, "adders": {"tax": 0, "fees": 0, "discounts": 0, "tip": 0}, "lines": lines,
            "flags": flags, "link": b["bill_url"],
        })

    # spread each record's amount over its lines; write both files
    line_rows, rec_rows = [], []
    for rec in sorted(records, key=lambda r: (r["date_utc"], r["record_id"])):
        lines, aflags = allocate(rec["amount"], [dict(l) for l in rec["lines"]])
        flags = rec["flags"] + aflags
        base = sum(l["line_total"] or 0 for l in lines)
        a = rec["adders"]
        stated = a["tax"] + a["fees"] + a["tip"]
        # receipts list discounts whether or not line prices already include them; take the reading that fits
        # and excluded adder lines (tariff) may or may not also appear as fees
        ex = sum(l.get("excluded_total") or 0 for l in lines)
        other = min((rec["amount"] - base - stated + d - e for d in (0, a["discounts"]) for e in (0, ex)),
                    key=abs) if base else 0.0
        if abs(other) > max(1.0, REVIEW_SHARE * abs(rec["amount"])):
            flags.append("residual_not_on_receipt")
        review = any(f in flags for f in ("receipt_total_mismatch", "no_priced_lines",
                                           "residual_not_on_receipt", "receipt_not_extracted", "invoice_not_transcribed"))
        landed = sum(l["landed_total"] or 0 for l in lines)
        assert abs(landed - rec["amount"]) < 0.01, (rec["record_id"], landed, rec["amount"])
        common = {k: rec[k] for k in ("record_type", "record_id", "date_utc", "user", "vendor", "vendor_category",
                                      "amount", "status", "memo", "fund", "accounting")}
        for i, l in enumerate(lines, 1):
            q = l["quantity"]
            line_rows.append(common | {
                "line_no": i, "item_code": l["item_code"], "item_name": l["item_name"], "quantity": q,
                "unit_price": l["unit_price"], "line_total": l["line_total"],
                "adders_allocated": round(l["adders_allocated"], 4),
                "landed_total": None if l["landed_total"] is None else round(l["landed_total"], 4),
                "landed_unit_cost": round(l["landed_total"] / q, 6) if q and l["landed_total"] else None,
                "line_source": l["line_source"], "line_note": l.get("line_note", ""), "receipt_uuid": rec["receipt_uuid"], "receipt_date": rec["receipt_date"],
                "flags": ";".join(flags), "needs_review": review, "link": rec["link"],
            })
        rec_rows.append(common | {
            "n_lines": len(lines), "line_sources": ";".join(sorted({l["line_source"].split(":")[0] for l in lines})),
            "sum_line_totals": round(base, 2), "receipt_total": rec["receipt_total"],
            "receipt_tax": round(a["tax"], 2), "receipt_fees": round(a["fees"], 2), "receipt_tip": round(a["tip"], 2),
            "receipt_discounts": round(a["discounts"], 2), "residual_not_on_receipt": round(other, 2),
            "landed_sum": round(landed, 2), "receipt_uuid": rec["receipt_uuid"], "receipt_date": rec["receipt_date"],
            "receipts_on_record": rec["receipts_on_record"], "flags": ";".join(flags), "needs_review": review,
            "link": rec["link"],
        })

    # every spend record in the window is in the output once
    want = {s["card_transaction_id"] for s in spend if s["spend_type"] == "Transaction" and s["spend_time_utc"][:10] >= since}
    have = {u for r in rec_rows if r["record_type"] == "card" for u in r["record_id"].split(";")}
    assert want <= have, want - have
    assert len(have) == sum(len(r["record_id"].split(";")) for r in rec_rows if r["record_type"] == "card")
    n_bills = sum(1 for s in spend if s["spend_type"] == "Bill" and s["spend_time_utc"][:10] >= since)
    assert n_bills == sum(r["record_type"] == "bill" for r in rec_rows)

    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    tag = since.replace("-", "")
    for name, rows in ((f"cost_lines_{tag}.csv", line_rows), (f"cost_records_{tag}.csv", rec_rows)):
        with open(os.path.join(HERE, "out", name), "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(rows)
        print(f"out/{name}: {len(rows)} rows")
    c = collections.Counter(r["record_type"] for r in rec_rows)
    print(f"records: {dict(c)}; total ${sum(r['amount'] for r in rec_rows):,.2f}; "
          f"needs_review {sum(r['needs_review'] for r in rec_rows)}")
    for f, n in collections.Counter(f for r in rec_rows for f in r["flags"].split(";") if f).most_common():
        print(f"  {f}: {n}")


def _check():
    # sign flip, residual spread, unpriced record
    lines, flags = allocate(10.0, [{"item_code": "", "item_name": "a", "quantity": 2, "unit_price": -2.0,
                                   "line_total": -4.0, "line_source": "x"},
                                  {"item_code": "", "item_name": "b", "quantity": 1, "unit_price": -4.0,
                                   "line_total": -4.0, "line_source": "x"}])
    assert flags == ["line_signs_flipped"] and [l["landed_total"] for l in lines] == [5.0, 5.0]
    lines, flags = allocate(7.0, [{"item_code": "", "item_name": "a", "quantity": None, "unit_price": None,
                                  "line_total": None, "line_source": "x"}])
    assert "no_priced_lines" in flags and sum(l["landed_total"] or 0 for l in lines) == 7.0


if __name__ == "__main__":
    _check()
    main()
