from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Mapping

from .contracts import CanonState


class CanonChangeKind(StrEnum):
    ADD = "add"
    UPDATE = "update"
    RETCON = "retcon"


@dataclass(frozen=True, slots=True)
class CanonChange:
    key: str
    value: str
    kind: CanonChangeKind
    reason: str
    approval_ref: str | None = None


@dataclass(frozen=True, slots=True)
class CanonDelta:
    base_fingerprint: str
    changes: tuple[CanonChange,...]


def apply_canon_delta(canon: CanonState, delta: CanonDelta, *, new_fingerprint: str) -> CanonState:
    if delta.base_fingerprint != canon.fingerprint:
        raise ValueError("canon delta based on stale state")
    facts=dict(canon.facts)
    for change in delta.changes:
        exists=change.key in facts
        if change.kind is CanonChangeKind.ADD and exists:
            raise ValueError(f"canon fact already exists: {change.key}")
        if change.kind is CanonChangeKind.UPDATE and not exists:
            raise ValueError(f"cannot update missing canon fact: {change.key}")
        if exists and facts[change.key] != change.value and change.kind is not CanonChangeKind.RETCON:
            raise ValueError(f"contradictory canon change requires RETCON: {change.key}")
        if change.kind is CanonChangeKind.RETCON and (not change.reason or not change.approval_ref):
            raise ValueError(f"retcon requires reason and approval: {change.key}")
        facts[change.key]=change.value
    return CanonState(canon.project_id,canon.version+1,new_fingerprint,facts)


# CODEX-TASK[M14-CONTINUITY-DEPENDENCY]
# Record which scenes/character states/world facts depend on changed canon keys. A retcon must emit
# deterministic invalidation scope so only affected narrative/audio/media proofs are re-evaluated.
