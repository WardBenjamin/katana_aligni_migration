# /// script
# requires-python = ">=3.15"
# ///
"""Read ByTechs' itemized invoice PDFs into one line table.

    uv run parse_bytechs_invoices.py data/invoices/bytechs/ByTechs-AG-2026

Needs pdftotext. Writes invoice_lines_bytechs.csv beside this script, in the column layout of
invoice_lines.csv, so price_config.py can read it. Every invoice's lines must add up to its total.
"""

import csv
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).parent
MONEY = r"-?\$[\d,]+\.\d\d"
# "12. Manufacturing    Compute Stack Units    41    $75.00    $3,075.00"; the description may be empty
ITEM = re.compile(rf"^\s*(\d+)\.\s+(\S.*?)(?:\s{{2,}}(\S.*?))?\s+(-?[\d,]*\.?\d+)\s+({MONEY})\s+({MONEY})\s*$")
TOTAL = re.compile(rf"^\s*Total\s+({MONEY})\s*$")
FIELDS = ["date_utc", "vendor", "item_name", "quantity", "unit_price", "line_total", "invoice_goods_total",
          "invoice_total", "invoice_no", "source_file", "flag", "note"]


def money(s):
    return float(s.replace("$", "").replace(",", ""))


def parse(text):
    """(invoice number, ISO date, total, [line dicts]) from one invoice's layout text."""
    text = text.replace("−", "-")  # credits are printed with a typographic minus sign
    number = re.search(r"Invoice no\.:\s*(\S+)", text).group(1)
    date = datetime.strptime(re.search(r"Invoice date:\s*(\S+)", text).group(1), "%m/%d/%Y").date().isoformat()
    lines, total, open_item, pending = [], None, None, ""
    for raw in text.splitlines():
        if re.fullmatch(r"\s*\d+\.\s*", raw):
            pending = raw.strip() + " "  # a page break can leave the line number on a line of its own
            continue
        if pending and raw.strip():
            raw, pending = pending + raw.strip(), ""
        if m := ITEM.match(raw):
            no, product, desc, qty, rate, amount = m.groups()
            open_item = {"no": int(no), "product": product.strip(), "desc": (desc or "").strip(),
                         "qty": float(qty.replace(",", "")), "rate": money(rate), "amount": money(amount)}
            lines.append(open_item)
        elif m := TOTAL.match(raw):
            total, open_item = money(m.group(1)), None
        elif open_item and raw.startswith(" " * 20) and raw.strip() and not re.search(MONEY, raw):
            open_item["desc"] = f"{open_item['desc']} {raw.strip()}".strip()  # wrapped description
        elif raw.strip() and not raw.startswith(" " * 20):
            open_item = None
    return number, date, total, lines


def selftest():
    text = """    Invoice no.: 9
    Invoice date: 09/30/2026
#       Product or service              Description                                      Qty           Rate   Amount
1.      Consulting                      October Rent                                          1     $250.00    $250.00
12. Consulting                          Troubleshooting and Fixing returned                   0      $80.00      $0.00
                                        Compute Stacks
29. Manufacturing                       Lenses - 4x Polycarb, 4x                           0.5   $150.00         $75.00
                                        Acrylic Hourly
30.
    Laser Cutting                       Laser Cutting for Monti                            1   $10.00        $10.00
                                        6x Vertical Dual Lens
                                                                                   Total                      $335.00
"""
    number, date, total, lines = parse(text)
    assert (number, date, total) == ("9", "2026-09-30", 335.0)
    assert [(l["no"], l["qty"], l["rate"], l["amount"]) for l in lines] == [(1, 1, 250, 250), (12, 0, 80, 0), (29, .5, 150, 75), (30, 1, 10, 10)]
    assert lines[3]["desc"] == "Laser Cutting for Monti 6x Vertical Dual Lens"
    assert lines[1]["desc"] == "Troubleshooting and Fixing returned Compute Stacks"
    assert lines[2]["desc"] == "Lenses - 4x Polycarb, 4x Acrylic Hourly"


def main(folder):
    selftest()
    rows = []
    for pdf in sorted(Path(folder).glob("*.pdf")):
        text = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True, check=True).stdout
        number, date, total, lines = parse(text)
        summed = round(sum(l["amount"] for l in lines), 2)
        assert total is not None and abs(summed - total) < 0.005, f"{pdf.name}: lines add to {summed}, total is {total}"
        assert [l["no"] for l in lines] == list(range(1, len(lines) + 1)), f"{pdf.name}: line numbers skip"
        for l in lines:
            assert abs(l["qty"] * l["rate"] - l["amount"]) < 0.011, f"{pdf.name} line {l['no']}: qty x rate is not the amount"
            rows.append({"date_utc": date, "vendor": "Bytechs", "item_name": f"{l['product']}: {l['desc']}".rstrip(": "),
                         "quantity": f"{l['qty']:g}", "unit_price": f"{l['rate']:.2f}", "line_total": f"{l['amount']:.2f}",
                         "invoice_goods_total": f"{total:.2f}", "invoice_total": f"{total:.2f}", "invoice_no": number,
                         "source_file": str(pdf.resolve().relative_to(HERE)), "flag": "", "note": f"line {l['no']}"})
    out = HERE / "invoice_lines_bytechs.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    invoices = {r["invoice_no"] for r in rows}
    print(f"{len(invoices)} invoices, {len(rows)} lines, ${sum(float(r['line_total']) for r in rows):,.2f} -> {out.name}")


if __name__ == "__main__":
    main(sys.argv[1])
