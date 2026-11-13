"""Minimal Aligni GraphQL client: one request at a time, paced under the 10 req/min limit."""
import json, os, time, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MIN_GAP_S = 7.0  # 10 req/min plan limit -> 6 s; margin for clock skew
_last = 0.0


def _env():
    env = {}
    for line in (ROOT / ".env").read_text().splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    return env


ENV = _env()
ORG = ENV["ALIGNI_ORG"]
HOST = ORG if "." in ORG else f"{ORG}.aligni.com"
URL = f"https://{HOST}/api/v3/graphql"


def gql(query, variables=None, retries=5):
    global _last
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    for attempt in range(retries):
        wait = _last + MIN_GAP_S - time.monotonic()
        if wait > 0:
            time.sleep(wait)
        req = urllib.request.Request(URL, data=body, headers={
            "Content-Type": "application/json",
            "User-Agent": "aligni-export/0.1",
            "Authorization": f"Token {ENV['ALIGNI_API_TOKEN']}",
        })
        _last = time.monotonic()
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                out = json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 429 or e.code >= 500:
                back = int(e.headers.get("Retry-After") or 30 * (attempt + 1))
                print(f"  HTTP {e.code}, sleeping {back}s", flush=True)
                time.sleep(back)
                continue
            raise RuntimeError(f"HTTP {e.code}: {e.read()[:500]!r}") from None
        if out.get("errors"):
            msgs = "; ".join(x.get("message", "") for x in out["errors"])
            if "rate" in msgs.lower() or "throttl" in msgs.lower():
                print(f"  throttled: {msgs[:200]}; sleeping 60s", flush=True)
                time.sleep(60)
                continue
            raise RuntimeError(f"GraphQL errors: {msgs[:1000]}")
        return out
    raise RuntimeError("gave up after retries")
