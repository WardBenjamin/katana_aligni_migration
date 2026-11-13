# /// script
# requires-python = ">=3.15"
# ///
"""Build data/slack/events.csv from data/slack/events_src.tsv. No network.

    uv run slack_events.py

events_src.tsv is hand-curated while reading Slack: channel_id, ts, thread_ts (blank for
top-level), author, assembly, parts, event_type, summary, quote. This adds the UTC date,
the channel name and the permalink, checks the fields, and sorts by time.
"""

import csv
import sys
from datetime import UTC, datetime
from pathlib import Path

HERE = Path(__file__).parent / "data" / "slack"
CHANNELS = {
    "C09FF4GLH9R": "#airgarage-bytechs",
    "C0C1WC7D468": "#airgarage-bytechs-hardware-chat",
    "C0C1C27RFP1": "#airgarage-bytechs-tripleb-v4-hardware",
    "C04PDLL3GAF": "#pt-tripwire",
    "C0C7J22K5PT": "#pt-obelisk",
    "C0ARYAA2FNF": "#pt-v4-sensors",
    "C0AA64RJ6BV": "#tripwire-leadership",
    "D08EQLEPAKX": "DM Ben/Monti",
    "D09P9DCN5M2": "DM Ben/Chris",
}
TYPES = {"bom-change", "decision", "current-version", "retired", "issue", "question", "build-or-po", "migration"}
OUT = ["date_utc", "channel", "author", "permalink", "assembly", "parts", "event_type", "summary", "quote"]


def permalink(cid: str, ts: str, thread_ts: str) -> str:
    url = f"https://airgarage.slack.com/archives/{cid}/p{ts.replace('.', '')}"
    return f"{url}?thread_ts={thread_ts}&cid={cid}" if thread_ts else url


def row(r: dict) -> dict:
    assert r["channel_id"] in CHANNELS, r
    assert r["event_type"] in TYPES, r
    assert len(r["quote"].split()) <= 25, r["quote"]
    when = datetime.fromtimestamp(float(r["ts"]), UTC).strftime("%Y-%m-%dT%H:%MZ")
    return {
        "date_utc": when,
        "channel": CHANNELS[r["channel_id"]],
        "author": r["author"],
        "permalink": permalink(r["channel_id"], r["ts"], r["thread_ts"]),
        **{k: r[k] for k in ("assembly", "parts", "event_type", "summary", "quote")},
    }


def main() -> None:
    with open(HERE / "events_src.tsv", newline="") as f:
        rows = [row(r) for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)]
    rows.sort(key=lambda r: r["date_utc"])
    links = [r["permalink"] for r in rows]
    assert len(links) == len(set(links)), "duplicate event"
    with open(HERE / "events.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=OUT)
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} events -> {HERE / 'events.csv'}", file=sys.stderr)


if __name__ == "__main__":
    main()
