# /// script
# requires-python = ">=3.15"
# ///
"""Explode a configuration into purchased leaf parts and probe the Ramp cost record for each.

    uv run explode_config.py configs/rr-bollard-dual46.csv

Reads boms/ (Katana-scope BOMs and items.csv) and the all-history cost lines.
Writes out/<config>_leaf_parts.csv, one row per leaf part with its extended quantity.
"""

import csv
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BOMS = ROOT / "boms"
COST_LINES = ROOT / "scratchpad/2026-11-13-bom-costs/out/cost_lines_20250101.csv"
MIN_TOKEN = 5  # shorter part-number fragments match unrelated receipt text


def read(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def explode(part, qty, boms, path=()):
    """Yield (part number, extended quantity, parent assembly, is_assembly) for the part and all below it."""
    if part in path:
        raise ValueError(f"BOM cycle: {' > '.join(path + (part,))}")
    lines = boms.get(part)
    yield part, qty, path[-1] if path else "", lines is not None
    for line in lines or ():
        if line["No Load"].strip().upper() == "Y":
            continue
        yield from explode(line["Part Number"], qty * float(line["Quantity Per Unit"]), boms, path + (part,))


def probe(tokens, cost_lines):
    """Costed purchase lines whose part-number or name text contains one of the tokens, oldest first."""
    # ponytail: substring match on part numbers, good for a coverage count only;
    # the price itself needs a reviewed part-to-line match table.
    tokens = {t.lower() for t in tokens if len(t) >= MIN_TOKEN}
    hits = [c for c in cost_lines if c["landed_unit_cost"] and any(t in c["_text"] for t in tokens)]
    return sorted(hits, key=lambda c: c["date_utc"])


def selftest():
    boms = {
        "KIT": [{"Part Number": "ASM", "Quantity Per Unit": "2", "No Load": ""},
                {"Part Number": "X", "Quantity Per Unit": "1", "No Load": ""}],
        "ASM": [{"Part Number": "X", "Quantity Per Unit": "3", "No Load": ""},
                {"Part Number": "ALT", "Quantity Per Unit": "1", "No Load": "Y"}],
    }
    leaves, assemblies = defaultdict(float), defaultdict(float)
    for part, qty, _, is_assembly in explode("KIT", 1, boms):
        (assemblies if is_assembly else leaves)[part] += qty
    assert dict(leaves) == {"X": 7.0}, leaves
    assert dict(assemblies) == {"KIT": 1.0, "ASM": 2.0}, assemblies


def main(config_path):
    selftest()
    index = [r for r in read(BOMS / "index.csv") if r["Scope"] == "Katana"]
    boms = {r["Assembly"]: read(BOMS / r["File"]) for r in index}
    items = {r["Part Number"]: r for r in read(BOMS / "items.csv")}
    cost_lines = read(COST_LINES)
    for c in cost_lines:
        c["_text"] = " ".join(c[k] for k in ("vendor_pn", "mpn", "item_code", "item_name", "item_name_full")).lower()

    qty, parents = defaultdict(float), defaultdict(set)
    for line in read(config_path):
        for part, q, parent, is_assembly in explode(line["Part Number"], float(line["Quantity"]), boms):
            if is_assembly:
                continue
            qty[part] += q
            parents[part].add(parent or "(config)")

    out = Path(__file__).parent / "out" / f"{Path(config_path).stem}_leaf_parts.csv"
    out.parent.mkdir(exist_ok=True)
    fields = ["Part Number", "Part Name", "Part Type", "Manufacturer", "Part Number - Mfg", "Supplier",
              "Supplier Part Number", "Extended Quantity", "Parents", "In items.csv", "Listed Cost Per Unit",
              "Ramp Lines", "Ramp Last Date UTC", "Ramp Last Vendor", "Ramp Last Landed Unit Cost",
              "Ramp Last Needs Review"]
    matched = 0
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for part in sorted(qty):
            item = items.get(part, {})
            stem = part.removeprefix("EXT-").removeprefix("AG-")
            hits = probe({stem, item.get("Part Number - Mfg", ""), item.get("Supplier Part Number", "")}, cost_lines)
            last = hits[-1] if hits else {}
            matched += bool(hits)
            w.writerow({
                **{k: item.get(k, "") for k in fields[1:7]},
                "Part Number": part,
                "Extended Quantity": f"{qty[part]:g}",
                "Parents": "; ".join(sorted(parents[part])),
                "In items.csv": "Y" if item else "N",
                "Listed Cost Per Unit": item.get("Cost Per Unit", ""),
                "Ramp Lines": len(hits),
                "Ramp Last Date UTC": last.get("date_utc", "")[:10],
                "Ramp Last Vendor": last.get("vendor", ""),
                "Ramp Last Landed Unit Cost": last.get("landed_unit_cost", ""),
                "Ramp Last Needs Review": last.get("needs_review", ""),
            })
    print(f"{len(qty)} leaf parts, {matched} with a part-number match in the Ramp cost lines -> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1])
