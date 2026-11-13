# Aligni BOM export

Goal: snapshot every Aligni part and BOM, and write one CSV per assembly to `boms/`.

Status: done 2026-11-13T03:40Z. Snapshot `data/20261113T0325Z/` (105 parts, 112 revisions, 36 with BOM lines).

## Run

```bash
uv run --python 3.15 pull.py                          # ~7 requests, ~1 min; writes data/<UTC stamp>/
uv run --python 3.15 export.py data/20261113T0325Z    # no network; writes boms/aligni-20261113T0325Z/
```

- `aligni.py`: GraphQL client. One request at a time, at least 7 s apart (plan limit 10/min, 1 concurrent, 10,000 complexity per request, 600,000 per hour). Sends a generic User-Agent because Cloudflare blocks urllib's default (error 1010).
- `pull.py`: parts in pages of 50, revisions in pages of 50 with a BOM line count, then BOM lines only for revisions that have them, batched by alias under the complexity cap.
- `export.py`: snapshot to CSV. `TEST-Kit` (Aligni test object) is skipped.
- `introspect.py`, `show.py`, `probe.py`: schema pull (`data/schema.json`) and a type printer.

## Notes

- Aligni's API has no part description; a part's name is its active revision's `description`.
- The `aligni` MCP server's `get_bom` queries `subparts`, which does not exist in the schema; the field is `PartRevision.bomItems`.
