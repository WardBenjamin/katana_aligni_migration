# /// script
# requires-python = ">=3.15"
# ///
"""Write one Notion BoM to data/notion/<slug>.csv from rows pasted on stdin. No network.

    uv run notion_to_csv.py <slug> < rows.json

stdin: {"columns": [...Notion column names in display order...], "rows": [{...}, ...]}
`rows` is the `results` list from the Notion MCP query (rows mode), or a plain table
transcribed as dicts. Columns keep Notion's names; "Notion URL" (row page) is appended
when rows carry a `url`. Cell clean-up, so values compare as text:
  - <p>...</p> wrappers, inline <u>/<b>/<i>/<s>/<code> tags and surrounding whitespace dropped
  - <br /> becomes a newline (Notion's in-cell line break)
  - Markdown backslash escapes removed (CS3-001-006\\_PDisp -> CS3-001-006_PDisp)
  - formula cells: the API returns only a formulaResult:// reference, so they are left blank
  - numbers written without a trailing .0
"""
import csv, json, re, sys
from pathlib import Path

OUT = Path(__file__).resolve().parent / "data" / "notion"


def clean(v):
    if v is None:
        return ""
    if isinstance(v, bool):
        return "Yes" if v else "No"
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    if not isinstance(v, str):
        return str(v)
    if v.startswith("formulaResult://"):
        return ""
    if v in ("__YES__", "__NO__"):  # checkbox values from rows mode
        return "Yes" if v == "__YES__" else "No"
    v = re.sub(r"</?(?:p|u|b|i|s|em|strong|code)>", "", v)
    v = re.sub(r"<br\s*/?>", "\n", v)
    v = re.sub(r"\\([\\`*_{}\[\]()#+\-.!|~<>$])", r"\1", v)
    return "\n".join(line.strip() for line in v.strip().splitlines())


def main(slug, data):
    cols = list(data["columns"])
    rows = data["rows"]
    if any("url" in r for r in rows):
        cols.append("Notion URL")
    with open(OUT / f"{slug}.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in rows:
            r = dict(r, **({"Notion URL": r["url"]} if "url" in r else {}))
            extra = set(r) - set(cols) - {"url"}
            assert not extra, f"row has columns not in schema: {extra}"
            w.writerow([clean(r.get(c)) for c in cols])
    print(f"{slug}.csv: {len(rows)} rows, {len(cols)} columns")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        assert clean("<p>\nM2 Hex Nut \n</p>") == "M2 Hex Nut"
        assert clean("<u>ByTechs</u> LLC") == "ByTechs LLC"
        assert clean("CS3-001-006\\_PDisp") == "CS3-001-006_PDisp"
        assert clean("I425-GL<br />EG25-G") == "I425-GL\nEG25-G"
        assert clean(2.0) == "2" and clean(6.99) == "6.99" and clean(None) == ""
        assert clean("formulaResult://a/b/c") == ""
        assert clean("__YES__") == "Yes" and clean("__NO__") == "No"
        print("ok")
    else:
        main(sys.argv[1], json.load(sys.stdin))
