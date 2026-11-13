# /// script
# requires-python = ">=3.15"
# ///
"""Find purchase lines for high-value parts by vendor and item name.

    uv run probe_names.py

These lines carry no part number, so explode_config.py misses them.
Writes out/name_probe_lines.csv. A planning lookup: matches are unreviewed.
"""

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COST_LINES = ROOT / "scratchpad/2026-11-13-bom-costs/out/cost_lines_20250101.csv"

# probe: (vendor pattern, item-name pattern); an empty pattern matches anything
PROBES = {
    "Uline bollard": (r"^ULINE$", r"bollard"),
    "Uline boxes": (r"^ULINE$", r"corrugated"),
    "Bollard washer": (r"^SendCutSend$", r"bollard"),
    "Raspberry Pi 5 16GB": (r"", r"raspberry pi 5 \(16gb\)|sc1113"),
    "Watchdog HAT": (r"^Sequent", r"watchdog"),
    "Sixfab base HAT": (r"^Sixfab$", r"base hat"),
    "I425-GL modem": (r"", r"i425|cat 4 minipcie"),
    "Samsung PRO Endurance 256GB": (r"", r"pro endurance 256"),
    "Molicel P30B": (r"", r"p30b"),
    "ELP camera": (r"", r"\belp\b"),
    "Haig Precision": (r"haig", r""),
    "ByTechs": (r"^Bytechs$", r""),
    "Concrete anchors": (r"^Fasteners Plus$", r""),
    "JLCPCB bare PCB": (r"^JLCPCB$", r"printed circuit board"),
}
FIELDS = ["date_utc", "vendor", "quantity", "unit_price", "landed_unit_cost", "needs_review",
          "line_source", "item_name", "item_name_full", "record_id", "line_no"]


def main():
    with open(COST_LINES, newline="", encoding="utf-8-sig") as f:
        lines = list(csv.DictReader(f))
    out = Path(__file__).parent / "out" / "name_probe_lines.csv"
    out.parent.mkdir(exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["probe"] + FIELDS, extrasaction="ignore")
        w.writeheader()
        for probe, (vendor, name) in PROBES.items():
            hits = [l for l in lines
                    if re.search(vendor, l["vendor"], re.I)
                    and re.search(name, l["item_name"] + " " + l["item_name_full"], re.I)]
            for l in sorted(hits, key=lambda l: l["date_utc"], reverse=True):
                w.writerow({"probe": probe, **l})
            costed = sum(1 for l in hits if l["landed_unit_cost"])
            print(f"{len(hits):>3} lines, {costed:>3} with a cost  {probe}")
    print(f"-> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
