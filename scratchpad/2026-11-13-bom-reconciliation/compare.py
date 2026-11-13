# /// script
# requires-python = ">=3.15"
# ///
"""Compare each Aligni BOM in <workspace>/boms/ with its Notion BoM, line by line. No network.

    uv run compare.py

Writes out/aligni_vs_notion_lines.csv (one row per line, status match|qty|aligni-only|notion-only)
and out/aligni_vs_notion_summary.csv (one row per Aligni assembly).
Lines match on any shared part number (internal, manufacturer or supplier, with AG-/EXT- stripped),
then on the AG- base number (before "_") when the names also agree, then on part name.
"""
import csv, difflib, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
BOMS = HERE.parents[1] / "boms/aligni-20261113T0325Z"
NOTION = HERE / "data/notion"
PN_COLS = ["Part Number", "Internal Part Number", "Part Number - Internal", "Manufacturer Part Number",
           "Part Number - Mfg", "Supplier Part Number"]


def norm(s):
    return re.sub(r"^(AG|EXT)-", "", re.sub(r"\s+", "", s or "").upper())


def keys(r):
    out = set()
    for c in PN_COLS:
        for v in [r.get(c) or ""] + re.split(r"\n| / ", r.get(c) or ""):  # Notion packs alternates as "A\nB" or "A / B"
            if len(norm(v)) >= 3 and norm(v) not in {"N/A", "TBD"}:
                out.add(norm(v))
    return out


def base(k):
    return k.split("_")[0]


def name(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def qty(s):
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def notion_slug(pn, slugs):
    """Map an Aligni assembly part number to its Notion BoM slug."""
    m = re.match(r"AG-(Dual|Single)\d+-(Round|Square|Wall)(Bollard|Mount)-Kit$", pn)
    if m:
        mount = {"Round": "round-bollard", "Square": "square-bollard", "Wall": "wall-mount"}[m[2]]
        return f"vpi-{mount}-{m[1].lower()}-cam-kit"
    if pn == "AG-CS3-Kit":
        return "vpi-compute-stack-kit"
    b = pn.removeprefix("AG-").split("_")[0].lower()
    hits = sorted(s for s in slugs if s.endswith(b) and not s.endswith("-copy"))
    return hits[0] if hits else ""


def compare(a_rows, n_rows):
    out, used = [], set()
    for a in a_rows:
        ak, an = keys(a), name(a["Part Name"])
        cand = [i for i, n in enumerate(n_rows) if i not in used and ak & keys(n)]
        if not cand:
            cand = [i for i, n in enumerate(n_rows) if i not in used
                    and {base(k) for k in ak} & {base(k) for k in keys(n)}
                    and difflib.SequenceMatcher(None, an, name(n["Part Name"])).ratio() > 0.6]
        if not cand:
            cand = [i for i, n in enumerate(n_rows) if i not in used
                    and difflib.SequenceMatcher(None, an, name(n["Part Name"])).ratio() > 0.85]
        if cand:
            i = cand[0]
            used.add(i)
            n = n_rows[i]
            st = "match" if qty(a["Quantity Per Unit"]) == qty(n["Quantity Per Unit"]) else "qty"
            out.append((st, a, n))
        else:
            out.append(("aligni-only", a, None))
    out += [("notion-only", None, n) for i, n in enumerate(n_rows) if i not in used]
    return out


def pn_of(r):
    return next((r[c] for c in PN_COLS if r and r.get(c) and r[c] != "N/A"), "")


slugs = {p.stem for p in NOTION.glob("*.csv") if p.stem != "manifest"}
manifest = {r["slug"]: r for r in csv.DictReader(open(NOTION / "manifest.csv"))}
lines, summary = [], []
for r in csv.DictReader(open(BOMS / "index.csv")):
    if not r["Active"]:
        continue
    asm = r["Assembly"]
    a_rows = list(csv.DictReader(open(BOMS / r["File"])))
    slug = notion_slug(asm, slugs)
    n_rows = list(csv.DictReader(open(NOTION / f"{slug}.csv"))) if slug else []
    res = compare(a_rows, n_rows) if slug else [("aligni-only", a, None) for a in a_rows]
    for st, a, n in res:
        lines.append({"Assembly": asm, "Notion BoM": slug, "Status": st,
                      "Aligni Part Number": a["Part Number"] if a else "", "Aligni Part Name": a["Part Name"] if a else "",
                      "Aligni Qty": a["Quantity Per Unit"] if a else "",
                      "Notion Part Number": pn_of(n).replace("\n", " / "), "Notion Part Name": n["Part Name"] if n else "",
                      "Notion Qty": n["Quantity Per Unit"] if n else "", "Notion Notes": (n or {}).get("Notes", "")})
    c = {s: sum(1 for x in res if x[0] == s) for s in ("match", "qty", "aligni-only", "notion-only")}
    summary.append({"Assembly": asm, "Aligni Rev": r["Revision"], "Aligni Lines": len(a_rows),
                    "Notion BoM": slug, "Notion Last Edited": manifest.get(slug, {}).get("page_last_edited_utc", ""),
                    "Notion Lines": len(n_rows), **c})

for name_, rows in [("aligni_vs_notion_lines", lines), ("aligni_vs_notion_summary", summary)]:
    (HERE / "out").mkdir(exist_ok=True)
    with open(HERE / f"out/{name_}.csv", "w", newline="") as f:
        w = csv.DictWriter(f, list(rows[0]))
        w.writeheader()
        w.writerows(rows)

# self-check: every Aligni and Notion line is accounted for exactly once per assembly
for s in summary:
    assert s["match"] + s["qty"] + s["aligni-only"] == s["Aligni Lines"], s
    assert s["match"] + s["qty"] + s["notion-only"] == s["Notion Lines"], s
print(f"{len(summary)} assemblies, {len(lines)} line rows")
