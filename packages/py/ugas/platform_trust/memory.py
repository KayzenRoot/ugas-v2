from __future__ import annotations
from typing import Sequence
from .contracts import ContextRequest,MemoryRecord

def plan_context(request:ContextRequest,candidates:Sequence[MemoryRecord])->tuple[MemoryRecord,...]:
    if request.token_budget<=0: raise ValueError("context token budget must be positive")
    scoped=[r for r in candidates if r.scope==request.scope and r.token_estimate>0]
    scoped.sort(key=lambda r:(r.token_estimate,r.fingerprint,r.id))
    selected=[]; used=0
    for record in scoped:
        if used+record.token_estimate>request.token_budget: continue
        if not record.provenance_ref: continue
        selected.append(record); used+=record.token_estimate
    return tuple(selected)

# CODEX-TASK[M22-HYBRID-RETRIEVAL]
# Add lexical/vector/hierarchical retrieval behind ports, deterministic reranking and explicit source
# provenance. Retrieval MUST enforce ProjectScope before ranking so cross-project memory cannot leak.
