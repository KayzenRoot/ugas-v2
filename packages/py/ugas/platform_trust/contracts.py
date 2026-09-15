from __future__ import annotations
from dataclasses import dataclass
from enum import StrEnum

class TrustState(StrEnum):
    VERIFIED="verified"; DEGRADED="degraded"; UNKNOWN="unknown"

@dataclass(frozen=True,slots=True)
class ProjectScope:
    project_id:str
    tenant_id:str

@dataclass(frozen=True,slots=True)
class MemoryRecord:
    id:str
    scope:ProjectScope
    fingerprint:str
    content_ref:str
    provenance_ref:str
    token_estimate:int

@dataclass(frozen=True,slots=True)
class ContextRequest:
    scope:ProjectScope
    query_fingerprint:str
    token_budget:int
    required_tags:frozenset[str]=frozenset()

@dataclass(frozen=True,slots=True)
class ProvenanceNode:
    id:str
    fingerprint:str
    source_ref:str
    rights_ref:str
    parent_refs:tuple[str,...]=()

@dataclass(frozen=True,slots=True)
class CapabilityGrant:
    principal_id:str
    capability:str
    resource_scope:str
    expires_at_epoch:int|None=None

@dataclass(frozen=True,slots=True)
class SecretRef:
    provider:str
    key_ref:str

@dataclass(frozen=True,slots=True)
class StoredObject:
    content_hash:str
    size_bytes:int
    media_type:str
    storage_ref:str

@dataclass(frozen=True,slots=True)
class CacheEntry:
    key:str
    source_content_hash:str
    value_ref:str
    expires_at_epoch:int|None=None

# CODEX-TASK[S06-CONTRACT-EXPANSION]
# Materialize module-owned M22 retrieval/context contracts, M23 transformation/credential graph,
# M24 policy/audit contracts and M25 integrity/cache contracts from deep specs. No secret values.
