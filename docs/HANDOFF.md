# Handoff

As of 2026-11-13 (UTC).

## Goal

Migrate MRP/ERP to [Katana](https://katanamrp.com/). That Aligni is the system being replaced is inferred from the workspace name and `repos/aligni-mcp-server`; not yet confirmed.

## Status

Workspace scaffolded. No migration work started and no topics yet (see [README.md](README.md)).

## Open items

- `repos/aligni-mcp-server` is a plain copy with no git history, so it is gitignored instead of being a submodule. It needs a remote to become one.
- `boms/` at the root is empty and outside the layout in `CLAUDE.md`. BOM exports would normally go in a scratchpad task's `data/`.
- The `aligni` MCP server connects and reads live data (checked 2026-11-13T03:18Z). It is registered at local scope in `~/.claude.json` and runs `repos/aligni-mcp-server/dist/index.js` with the workspace `.env` (`ALIGNI_ORG`, `ALIGNI_API_TOKEN`).
- `mcp__aligni__run_graphql` can run mutations against live Aligni and has no `ask` rule in `.claude/settings.json`.
