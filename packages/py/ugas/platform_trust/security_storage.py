from __future__ import annotations
import hashlib
from typing import Sequence
from .contracts import CapabilityGrant,CacheEntry,StoredObject

def assert_capability(grants:Sequence[CapabilityGrant],*,principal_id:str,capability:str,resource_scope:str,now_epoch:int)->None:
    valid=[g for g in grants if g.principal_id==principal_id and g.capability==capability and g.resource_scope==resource_scope and (g.expires_at_epoch is None or g.expires_at_epoch>now_epoch)]
    if not valid: raise PermissionError("least-privilege capability denied")

def content_hash(data:bytes)->str:
    return hashlib.sha256(data).hexdigest()

def verify_object(obj:StoredObject,data:bytes)->None:
    if obj.size_bytes!=len(data): raise ValueError("stored object size mismatch")
    if obj.content_hash!=content_hash(data): raise ValueError("stored object integrity mismatch")

def validate_cache_entry(entry:CacheEntry,source:StoredObject)->None:
    if entry.source_content_hash!=source.content_hash: raise ValueError("stale cache source fingerprint")
    if not entry.value_ref: raise ValueError("cache value reference required")

# CODEX-TASK[M24-M25-ADAPTERS]
# Resolve SecretRef only inside authorized provider adapters and redact values from logs/evidence.
# Implement S3-compatible immutable object store and disposable cache adapters. Cache loss must affect
# performance only, never canonical correctness or provenance.
