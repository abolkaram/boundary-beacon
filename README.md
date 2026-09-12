# BoundaryBeacon

> **Decision Card** · Do not act on a boundary until the boundary says the same thing everywhere it matters.

BoundaryBeacon is a consensus gate for an operating limit that must be the same across two public records: a safety threshold, service boundary, eligibility cap, or controlled limit. It stores one extracted boundary only after validators independently fetch both records and agree on the exact text and retrieved-content digests.

## Decision path

`DRAFT → REVIEWED → CONFIRMED`, with owner withdrawal from either active state.

1. `file_beacon` freezes the operational rule and two normalized HTTPS records from different hosts.
2. `review_beacon` asks validators to find the single shared explicit boundary.
3. `confirm_beacon` lets the owner make the reviewed boundary final.
4. `get_beacon` exposes the boundary, URLs, and SHA-256 evidence digests.

## What this card refuses

The contract rejects duplicate IDs, malformed URLs, same-host evidence, unsupported boundaries, and confirmation before review. Every validator recomputes the boundary and ordered digest list; a leader cannot substitute a different limit or evidence snapshot. Web pages are treated as untrusted data, not instructions.

Different hostnames are a technical diversity guard, not evidence of independent institutional control. Use genuinely separate authorities for non-demo records.

## Open the decision

```bash
PYTHONUTF8=1 genvm-lint contracts/contract.py
python -m pytest -q
```

Deployment evidence will be added only after this fresh repository revision is deployed and the new receipt is finalized.
