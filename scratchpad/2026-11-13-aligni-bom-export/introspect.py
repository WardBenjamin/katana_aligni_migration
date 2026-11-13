# /// script
# requires-python = ">=3.15"
# ///
"""Pull the full GraphQL schema once (1 request) to data/schema.json."""
import json
from aligni import gql

Q = """query { __schema { queryType { name } types { kind name
  fields(includeDeprecated: false) { name args { name type { kind name ofType { kind name ofType { kind name } } } }
    type { kind name ofType { kind name ofType { kind name ofType { kind name } } } } }
  inputFields { name type { kind name ofType { kind name ofType { kind name } } } }
  enumValues { name } } } }"""
out = gql(Q)
json.dump(out, open("data/schema.json", "w"), indent=1)
print(len(out["data"]["__schema"]["types"]), "types; extensions:", out.get("extensions"))
