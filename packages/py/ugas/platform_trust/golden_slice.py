from __future__ import annotations
from dataclasses import dataclass
from .contracts import *
from .memory import plan_context
from .provenance import validate_provenance_graph
from .security_storage import assert_capability,validate_cache_entry,verify_object

@dataclass(frozen=True,slots=True)
class PlatformTrustSlice:
    request:ContextRequest
    memories:tuple[MemoryRecord,...]
    provenance:tuple[ProvenanceNode,...]
    grants:tuple[CapabilityGrant,...]
    principal_id:str
    capability:str
    resource_scope:str
    now_epoch:int
    stored_object:StoredObject
    object_bytes:bytes
    cache_entry:CacheEntry|None=None

@dataclass(frozen=True,slots=True)
class PlatformTrustResult:
    context_refs:tuple[str,...]
    provenance_node_ids:tuple[str,...]
    content_hash:str

def evaluate_platform_trust_slice(v:PlatformTrustSlice)->PlatformTrustResult:
    context=plan_context(v.request,v.memories)
    validate_provenance_graph(v.provenance)
    assert_capability(v.grants,principal_id=v.principal_id,capability=v.capability,resource_scope=v.resource_scope,now_epoch=v.now_epoch)
    verify_object(v.stored_object,v.object_bytes)
    if v.cache_entry is not None: validate_cache_entry(v.cache_entry,v.stored_object)
    return PlatformTrustResult(tuple(r.content_ref for r in context),tuple(sorted(n.id for n in v.provenance)),v.stored_object.content_hash)

# CODEX-TASK[S06-GOLDEN-WIRING]
# Add fake repositories/audit sink and prove the full chain request scope -> retrieval -> provenance ->
# authorization -> immutable object -> optional cache. Cache must remain outside correctness boundary.
