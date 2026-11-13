# /// script
# requires-python = ">=3.15"
# ///
"""Flatten the raw Ramp pulls in data/ramp/raw/ into CSVs in data/ramp/.

Run: uv run --python 3.15 flatten_ramp.py
"""

import csv
import glob
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "data", "ramp", "raw")
OUT = os.path.join(HERE, "data", "ramp")
USERS = {
    "01954cee-c726-7b10-b069-c9c9b450ee6c": "Benjamin Ward",
    "01954cee-c717-707b-a6d2-fd8f365f01ac": "Bryan Monti",
    "019c9064-3541-72df-bab0-c9322d9fe100": "Chris Williamson",
}


def load(pattern):
    return [json.load(open(p)) for p in sorted(glob.glob(os.path.join(RAW, pattern)))]


def write(name, rows):
    path = os.path.join(OUT, name)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"{name}: {len(rows)} rows")


def cell(row, key):
    c = next(c for c in row["cells"] if c["column_key"] == key)["cell_data"]
    if c is None:
        return ""
    if "search_tag_info" in c and c["search_tag_info"] and key in ("USER", "PAYEE"):
        return c["search_tag_info"]["label"]
    if "amount" in c:
        return c["amount"]
    return c.get("value") or ""


# spend report: every card transaction, reimbursement and bill for the three users
spend = []
for page in load("spend_report/page_*.json"):
    for r in page["response"]["table"]["data"]:
        spend.append({
            "spend_type": cell(r, "SPEND_TYPE"),
            "card_transaction_id": cell(r, "TRANSACTION_CANONICAL_UUID"),
            "user": cell(r, "USER"),
            "payee": cell(r, "PAYEE"),
            "spend_time_utc": cell(r, "SPEND_TIME"),
            "amount_usd": cell(r, "AMOUNT"),
            "original_currency": cell(r, "ORIGINAL_CURRENCY"),
            "memo": cell(r, "MEMO"),
            "invoice_number": cell(r, "INVOICE_NUMBER"),
            "receipt_availability": cell(r, "RECEIPT_AVAILABILITY"),
            "fund": cell(r, "SPEND_ALLOCATION"),
            "paid_status": cell(r, "SPEND_OLAP__QUALIFIED_PAID_STATUS"),
            "reimbursement_type": cell(r, "REIMBURSEMENT_TYPE"),
            "category": cell(r, "CATEGORY"),
        })
memo_by_txn = {s["card_transaction_id"]: s["memo"] for s in spend if s["card_transaction_id"]}

# card transactions (team scope also returned Lorenzo Allas; out of scope, dropped here)
txns = [t for p in load("transactions/page_*.json") for t in p["transactions"]
        if t["spent_by_user_uuid"] in USERS]
transactions = [{
    "transaction_uuid": t["transaction_uuid"],
    "user": t["spent_by_user"],
    "transaction_time_utc": t["transaction_time"],
    "state": t["state"],
    "amount": t["amount_value"],
    "currency": t["amount_currency"],
    "merchant": t["merchant_name"],
    "merchant_category": t["merchant_category"],
    "fund": t["spend_allocation_name"],
    "accounting": "; ".join(f'{a["tracking_category_name"]}={a["tracking_category_option_name"]}'
                            for a in t["accounting_categories"] or []),
    "memo": memo_by_txn.get(t["transaction_uuid"], ""),
    "n_receipts": len(t["receipt_uuids"] or []),
    "receipt_uuids": ";".join(t["receipt_uuids"] or []),
    "link": t["transaction_link"],
} for t in txns]

# receipt line items, joined to their card transaction
txn_by_receipt = {r: t for t in txns for r in t["receipt_uuids"] or []}
receipts = {r["receipt_uuid"]: r for b in load("receipt_details/batch_*.json") for r in b["receipts"]}
lines = []
for rid, t in sorted(txn_by_receipt.items(), key=lambda kv: (kv[1]["transaction_time"], kv[0])):
    sd = (receipts.get(rid) or {}).get("structured_data") or {}
    base = {
        "user": t["spent_by_user"],
        "transaction_uuid": t["transaction_uuid"],
        "transaction_time_utc": t["transaction_time"],
        "txn_amount": t["amount_value"],
        "txn_merchant": t["merchant_name"],
        "memo": memo_by_txn.get(t["transaction_uuid"], ""),
        "fund": t["spend_allocation_name"],
        "n_receipts_on_txn": len(t["receipt_uuids"]),
        "receipt_uuid": rid,
        "receipt_found": rid in receipts,
        "receipt_merchant": sd.get("merchant_name"),
        "receipt_date": sd.get("transaction_date"),
        "receipt_total": sd.get("total_amount"),
        "receipt_subtotal": sd.get("subtotal"),
        "receipt_tax": sum(x["tax_amount"] or 0 for x in sd.get("taxes") or []),
        "receipt_fees": sum(x["fee_amount"] or 0 for x in sd.get("fees") or []),
        "receipt_discounts": sum(x.get("discount_amount") or 0 for x in sd.get("discounts") or []),
        "receipt_currency": sd.get("currency_code"),
        "is_itemized": sd.get("is_itemized"),
    }
    items = sd.get("line_items") or [{}]
    for i, li in enumerate(items, 1):
        lines.append(base | {
            "line_no": i if li else "",
            "item_name": li.get("item_name"),
            "item_quantity": li.get("item_quantity"),
            "item_unit_price": li.get("item_unit_price"),
            "item_total_price": li.get("item_total_price"),
        })

# reimbursements (drafts included; the spend report only has submitted ones)
reimb_receipts = {}
rr_path = os.path.join(RAW, "reimbursement_receipts.jsonl")
if os.path.exists(rr_path):
    for line in open(rr_path):
        rec = json.loads(line)
        reimb_receipts[rec["reimbursement_uuid"]] = rec["response"].get("receipts") or []
reimbursements = [{
    "reimbursement_uuid": r["uuid"],
    "user": USERS[r["user_id"]],
    "status": r["status"],
    "merchant": r["merchant_name"],
    "amount": r["amount"],
    "currency": r["currency"],
    "memo": r["memo"],
    "transaction_date": (r["transaction_date"] or "")[:10],
    "submitted_at_utc": r["submitted_at"],
    "fund": (r["fund"] or {}).get("fund_name"),
    "accounting": "; ".join(f'{s["category_name"]}={(s["option_selection"] or {}).get("option_name")}'
                            for s in r["tracking_category_selections"] or []),
    "n_receipts": len(reimb_receipts.get(r["uuid"], [])),
    "receipt_uuids": ";".join(x["receipt_uuid"] for x in reimb_receipts.get(r["uuid"], [])),
    "link": r["reimbursement_link"],
} for p in load("reimbursements/*_page_*.json") for r in p["reimbursements"]]

# completeness checks against the pull counts recorded in the research note
assert len(spend) == 1573, len(spend)
assert len(transactions) == 1437 == sum(s["spend_type"] == "Transaction" for s in spend)
assert {t["transaction_uuid"] for t in transactions} == {s["card_transaction_id"] for s in spend if s["card_transaction_id"]}
assert len(txn_by_receipt) == 1346, len(txn_by_receipt)
assert len(reimbursements) == 160, len(reimbursements)
missing = [r for r in txn_by_receipt if r not in receipts]
print(f"receipts with no extraction pulled: {len(missing)}")

write("spend.csv", spend)
write("transactions.csv", transactions)
write("receipt_lines.csv", lines)
write("reimbursements.csv", reimbursements)
