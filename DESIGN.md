# BoundaryBeacon

Locks an operational boundary only when two public policy records describe the same permitted limit. Lifecycle: DRAFT -> REVIEWED -> CONFIRMED or CONFLICT -> WITHDRAWN. The named policy owner alone can amend a conflicted draft; anyone can review or withdraw after expiry.

This is not an event trigger or provenance chain: it compares an explicitly bounded operating rule and stores the agreed boundary plus retrieved-content digests.
