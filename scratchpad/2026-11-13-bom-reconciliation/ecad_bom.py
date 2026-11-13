# /// script
# requires-python = ">=3.15"
# dependencies = []
# ///
"""BOMs from the KiCad schematics in repos/tripwire-ecad (stdlib only, no kicad-cli).

`uv run --python 3.15 ecad_bom.py` writes, under data/ecad/ next to this script:
  <project>.csv              grouped BOM per project, from schematic symbols
  manifest.csv               one row per project: title block, last commit, counts
  committed_bom_diff.csv     committed sensor-board BOM CSVs vs the schematic, per designator
  history/<file>@<sha>.csv   BOM exports that were committed and later deleted (xlsx -> csv)

Rules: power symbols (#PWR, #FLG, lib power:) are skipped. A symbol is a BOM line if
(in_bom yes) or (dnp yes); DNP lines stay in, flagged, with their InBOM/OnBoard flags so a
reader can drop them. Multi-unit symbols count once per reference. Hierarchical sheets are
followed per instance, so a sheet placed twice counts twice. A project with no schematic of
its own (modem-bridge) uses the sibling schematic that holds every symbol its PCB places,
filtered to those symbols.
"""

import csv
import io
import re
import subprocess
import zipfile
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path
from xml.etree import ElementTree

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ECAD = ROOT / "repos" / "tripwire-ecad"
OUT = HERE / "data" / "ecad"

# project -> (.kicad_pro path, regex for the board name used in commit subjects)
PROJECTS = {
    "party-hat": ("party-hat/party-hat.kicad_pro", r"Party HAT"),
    "sensor-bar-io-breakout": ("sensor-bar-io-breakout/sensor-bar-io-breakout.kicad_pro", r"Sensor Bar I/O Breakout(?: \([^)]*\))?"),
    "bollard-interposer-board": ("bollard-interposer-board/bollard-interposer-board.kicad_pro", r"Bollard Interposer(?: Board)?"),
    "party-hat-usb-bridges": ("party-hat-usb-bridges/party-hat-usb-bridges.kicad_pro", r"(?:USB[^,:]*?|Modem) Bridge"),
    "hat-usb-bridge": ("party-hat-usb-bridges/hat-usb-bridge.kicad_pro", r"USB[^,:]*? Bridge"),
    "modem-bridge": ("party-hat-usb-bridges/modem-bridge.kicad_pro", r"Modem Bridge"),
    "tripwire-v3": ("sensor-board/rev1/src/tripwire-v3.kicad_pro", None),  # named rev1/rev2.1, not Xn
    "combined-sensor-board": ("sensor-board/rev2/src/combined-sensor-board.kicad_pro", None),
}
COMMITTED = {  # committed BOM exports to check against the schematic BOM
    "tripwire-v3": "sensor-board/rev1/outputs/tripwire-BOM.csv",
    "combined-sensor-board": "sensor-board/rev2/outputs/tripwire-rev2-bom.csv",
}

TOKEN = re.compile(r'\(|\)|"(?:[^"\\]|\\.)*"|[^\s()"]+')
NOT_KEY = re.compile(r"^(Reference|Datasheet|Description|Sim\..*)$")  # not part identity
SUPPLIER = re.compile(r"digi|dpn|lcsc|mouser|supplier|alt", re.I)


def parse(text):
    """S-expression text -> nested lists of str. Quoted strings lose their quotes."""
    stack = [[]]
    for tok in TOKEN.findall(text):
        if tok == "(":
            stack.append([])
        elif tok == ")":
            done = stack.pop()
            stack[-1].append(done)
        elif tok.startswith('"'):
            stack[-1].append(re.sub(r"\\(.)", r"\1", tok[1:-1]))
        else:
            stack[-1].append(tok)
    return stack[0][0]


def kids(node, name):
    return [c for c in node[1:] if isinstance(c, list) and c and c[0] == name]


def first(node, name, default=None):
    found = kids(node, name)
    return found[0] if found else default


def flag(node, name, default):
    f = first(node, name)
    return f[1] if f and len(f) > 1 else default


def props(node):
    return {p[1]: p[2] for p in kids(node, "property")}


def natural(s):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", s)]


def git(*args):
    return subprocess.run(["git", "-C", str(ECAD), *args], capture_output=True, text=True, check=True).stdout


def last_commit(*paths):
    """(sha, UTC ISO time, subject) of the last commit on HEAD touching any of paths."""
    out = git("log", "-1", "--format=%h%x00%cI%x00%s", "--", *paths).strip()
    if not out:
        return "", "", ""
    sha, when, subject = out.split("\0")
    return sha, datetime.fromisoformat(when).astimezone(UTC).strftime("%Y-%m-%dT%H:%MZ"), subject


def symbols(sch, project, path=None, seen=None):
    """BOM-relevant symbols of a schematic and its sub-sheets: list of (ref, uuid, fields, flags)."""
    root = parse(sch.read_text())
    path = path or "/" + first(root, "uuid")[1]
    seen = set() if seen is None else seen
    found = []
    for s in kids(root, "symbol"):
        fields = props(s)
        lib = first(s, "lib_id")[1]
        ref = fields.get("Reference", "")
        inst = first(s, "instances")
        if inst:  # per-instance reference, preferring this project's entry
            refs = [(p[1], first(pa, "reference")[1]) for p in kids(inst, "project") for pa in kids(p, "path") if pa[1] == path]
            refs.sort(key=lambda pr: pr[0] != project)
            ref = refs[0][1] if refs else ref
        flags = {"DNP": flag(s, "dnp", "no"), "InBOM": flag(s, "in_bom", "yes"), "OnBoard": flag(s, "on_board", "yes")}
        if lib.startswith("power:") or ref.startswith("#") or (path, ref) in seen:
            continue  # power symbol, or another unit of a multi-unit symbol already counted
        if flags["InBOM"] == "no" and flags["DNP"] != "yes":
            continue
        assert not ref.endswith("?"), f"{sch}: unannotated symbol {ref}"
        seen.add((path, ref))
        fields["Reference"] = ref
        found.append((ref, first(s, "uuid")[1], fields, flags))
    for sheet in kids(root, "sheet"):  # each placement is its own (sheet ...), so instances multiply
        f = props(sheet)
        sub = sch.parent / (f.get("Sheetfile") or f["Sheet file"])
        found += symbols(sub, project, f"{path}/{first(sheet, 'uuid')[1]}", seen)
    return found


def schematic_for(pro):
    """(schematic, uuids or None). No own schematic: the sibling one holding all the PCB's symbols."""
    own = pro.with_suffix(".kicad_sch")
    if own.exists():
        return own, None
    pcb = parse(pro.with_suffix(".kicad_pcb").read_text())
    uuids = {first(fp, "path")[1].split("/")[-1] for fp in kids(pcb, "footprint") if first(fp, "path")}
    for sch in sorted(pro.parent.glob("*.kicad_sch")):
        have = {first(s, "uuid")[1] for s in kids(parse(sch.read_text()), "symbol")}
        if uuids <= have:
            return sch, uuids
    raise SystemExit(f"{pro}: no schematic holds all {len(uuids)} PCB symbols")


def group(syms):
    """KiCad-style grouped rows: one per unique part identity + flags."""
    groups = defaultdict(list)
    for ref, _, fields, flags in syms:
        key = tuple(sorted((k, v) for k, v in fields.items() if not NOT_KEY.match(k) and v)) + tuple(flags.items())
        groups[key].append((ref, fields, flags))
    rows = []
    for members in groups.values():
        refs = sorted((m[0] for m in members), key=natural)
        row = {"Designators": ",".join(refs), "Quantity": len(refs), **members[0][2]}
        row["DNP"] = "DNP" if row["DNP"] == "yes" else ""
        for k in {k for m in members for k in m[1]} - {"Reference"}:
            row[k] = " | ".join(dict.fromkeys(m[1].get(k, "") for m in members if m[1].get(k)))
        rows.append(row)
    return sorted(rows, key=lambda r: natural(r["Designators"]))


def columns(rows):
    have = {k for r in rows for k in r}
    lead = ["Designators", "Quantity", "Value", "Footprint", "MPN", "Manufacturer"]
    supplier = sorted(k for k in have if SUPPLIER.search(k) and k not in lead)
    flags = ["DNP", "InBOM", "OnBoard"]
    return lead + supplier + flags + sorted(have - set(lead) - set(supplier) - set(flags))


def write_csv(path, rows, cols=None):
    path.parent.mkdir(parents=True, exist_ok=True)
    cols = cols or list(rows[0])
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, cols, extrasaction="raise")
        w.writeheader()
        w.writerows({c: r.get(c, "") for c in cols} for r in rows)


def pcb_check(pcb, syms):
    """'ok', or how the populated schematic BOM differs from the PCB's BOM footprints."""
    placed = {}
    for fp in kids(parse(pcb.read_text()), "footprint"):
        attr = (first(fp, "attr") or [])[1:]
        if {"board_only", "exclude_from_bom", "dnp"} & set(attr):
            continue
        f = props(fp)  # KiCad 8+; KiCad 7 boards keep reference/value in fp_text
        f.update({t[1]: t[2] for t in kids(fp, "fp_text") if t[1] in ("reference", "value")})
        ref = f.get("Reference") or f["reference"]
        placed[ref] = (f.get("Value") or f["value"], fp[1], f.get("MPN") if "Reference" in f else None)
    ours = {r: (f.get("Value", ""), f.get("Footprint", ""), f.get("MPN", "")) for r, _, f, fl in syms
            if fl["DNP"] != "yes" and fl["InBOM"] == "yes" and fl["OnBoard"] == "yes"}
    issues = [f"{r} only on PCB" for r in placed.keys() - ours.keys()] + [f"{r} not on PCB" for r in ours.keys() - placed.keys()]
    for r in placed.keys() & ours.keys():
        p, s = placed[r], ours[r]
        issues += [f"{r} {n}: sch '{b}' pcb '{a}'" for n, a, b in zip(("value", "footprint", "MPN"), p, s) if a is not None and a != b]
    return "; ".join(sorted(issues, key=natural)) or "ok"


def committed_rows(text):
    """Per-designator rows of a committed BOM CSV (PCBWay quote or KiCad-style export)."""
    table = list(csv.reader(io.StringIO(text)))
    head_i = next(i for i, r in enumerate(table) if any("Designator" in c for c in r))
    head = table[head_i]
    col = lambda *names: next((i for i, h in enumerate(head) if any(n in h for n in names)), None)
    ref_i, val_i, fp_i = col("Designator"), col("Value", "Designation"), col("Footprint")
    pn_i = [i for i, h in enumerate(head) if re.search(r"part #|supplier", h, re.I)]
    out = {}
    for r in table[head_i + 1 :]:
        if len(r) <= ref_i or not r[ref_i].strip():
            continue
        pn = " ".join(r[i].strip() for i in pn_i if r[i].strip())
        for ref in r[ref_i].split(","):
            out[ref.strip()] = {"value": " ".join(r[val_i].split()), "footprint": r[fp_i].strip(), "pn": " ".join(pn.split())}
    return out


def compare(project, rel, syms):
    sha = last_commit(rel)[0]
    theirs = committed_rows((ECAD / rel).read_text())
    ours = {ref: f for ref, _, f, flags in syms}
    rows = []
    for ref in sorted(set(theirs) | set(ours), key=natural):
        t, o = theirs.get(ref), ours.get(ref)
        diffs = []
        if not t:
            diffs.append("not in committed CSV")
        elif not o:
            diffs.append("not in schematic")
        else:
            if t["value"].split()[0].lower() != o.get("Value", "").lower():
                diffs.append("value")
            if t["footprint"].split(":")[-1] != o.get("Footprint", "").split(":")[-1]:
                diffs.append("footprint")
            if t["pn"] and not o.get("MPN"):
                diffs.append("part number only in committed CSV")
        rows.append({
            "project": project, "committed_file": f"{rel}@{sha}", "designator": ref,
            "committed_value": t and t["value"], "schematic_value": o and o.get("Value"),
            "committed_footprint": t and t["footprint"], "schematic_footprint": o and o.get("Footprint"),
            "committed_part_number": t and t["pn"], "schematic_mpn": o and o.get("MPN", ""),
            "differences": "; ".join(diffs),
        })
    return rows


def xlsx_rows(data):
    """First worksheet of an .xlsx as a list of rows (stdlib only)."""
    z = zipfile.ZipFile(io.BytesIO(data))
    ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        for si in ElementTree.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", ns):
            shared.append("".join(t.text or "" for t in si.iter(f"{{{ns['m']}}}t")))
    sheet = sorted(n for n in z.namelist() if n.startswith("xl/worksheets/sheet"))[0]
    rows = []
    for row in ElementTree.fromstring(z.read(sheet)).iter(f"{{{ns['m']}}}row"):
        cells = {}
        for c in row.findall("m:c", ns):
            v = c.find("m:v", ns)
            text = c.findtext("m:is/m:t", "", ns) if v is None else v.text
            col = re.match(r"[A-Z]+", c.get("r")).group()
            cells[sum((ord(ch) - 64) * 26**i for i, ch in enumerate(reversed(col))) - 1] = (
                shared[int(text)] if c.get("t") == "s" else text
            )
        rows.append([cells.get(i, "") for i in range(max(cells, default=-1) + 1)])
    return rows


def deleted_bom_exports():
    """Every BOM-like file ever deleted from any branch: (path, added sha, deleted sha)."""
    log = git("log", "--all", "--format=@%h", "--name-status", "--diff-filter=AD")
    found, sha = {}, None
    for line in log.splitlines():
        if line.startswith("@"):
            sha = line[1:]
        elif line and re.search(r"bom|\.csv$|\.xlsx?$", line.split("\t")[-1], re.I):
            status, path = line.split("\t")[0], line.split("\t")[-1]
            found.setdefault(path, {})[status] = sha  # log is newest first: keep the latest
    return [(p, s.get("A", ""), s["D"]) for p, s in found.items() if "D" in s]


def main():
    manifest, diffs = [], []
    for name, (rel, board_re) in PROJECTS.items():
        pro = ECAD / rel
        sch, only = schematic_for(pro)
        syms = [s for s in symbols(sch, name) if only is None or s[1] in only]
        rows = group(syms)
        assert sum(r["Quantity"] for r in rows) == len(syms), name  # self-check: no symbol lost or doubled
        write_csv(OUT / f"{name}.csv", rows, columns(rows))

        tb = first(parse(sch.read_text()), "title_block") or ["title_block"]
        sch_rel = str(sch.relative_to(ECAD))
        sha, when, subject = last_commit(sch_rel)
        proj_files = [str(pro.relative_to(ECAD).with_suffix(s)) for s in (".kicad_sch", ".kicad_pcb", ".kicad_pro")]
        psha, pwhen, psubject = last_commit(*proj_files)
        # --full-history: squash-merge commits (e.g. "Bollard Interposer Board X1") are otherwise pruned
        subjects = git("log", "--full-history", "--format=%s", "--", *proj_files).splitlines() if board_re else []
        hits = (re.findall(rf"{board_re}\s+X\d+[A-Z]?", s, re.I) for s in subjects)
        board = "; ".join(next((h for h in hits if h), []))
        populated = [r for r in rows if not r["DNP"]]
        manifest.append({
            "project": name,
            "schematic_path": sch_rel + ("" if only is None else f" (shared; filtered to {pro.with_suffix('.kicad_pcb').name})"),
            "title": flag(tb, "title", ""), "rev": flag(tb, "rev", ""), "schematic_date": flag(tb, "date", ""),
            "last_commit_sha": sha, "last_commit_utc": when, "last_commit_subject": subject,
            "bom_rows": len(rows), "bom_qty": sum(r["Quantity"] for r in populated),
            "parts_missing_mpn": sum(1 for r in populated if not r.get("MPN")),
            "dnp_count": sum(r["Quantity"] for r in rows if r["DNP"]),
            "project_last_commit_sha": psha, "project_last_commit_utc": pwhen, "project_last_commit_subject": psubject,
            "board_name_in_commits": board,
            "pcb_check": pcb_check(pro.with_suffix(".kicad_pcb"), syms),
        })
        if name in COMMITTED:
            diffs += compare(name, COMMITTED[name], syms)
    write_csv(OUT / "manifest.csv", manifest)
    write_csv(OUT / "committed_bom_diff.csv", diffs)

    for path, added, deleted in deleted_bom_exports():
        data = subprocess.run(["git", "-C", str(ECAD), "show", f"{added}:{path}"], capture_output=True, check=True).stdout
        rows = xlsx_rows(data) if path.endswith((".xlsx", ".xls")) else list(csv.reader(io.StringIO(data.decode())))
        dest = OUT / "history" / f"{Path(path).stem}@{added}.csv"
        dest.parent.mkdir(parents=True, exist_ok=True)
        with dest.open("w", newline="") as f:
            csv.writer(f).writerows(rows)
        print(f"deleted export: {path} added {added} deleted {deleted} -> {dest.relative_to(HERE)}")

    for m in manifest:
        print(m)


if __name__ == "__main__":
    main()
