from __future__ import annotations

"""Concrete cross-module foundation contracts for S01.

These are PREPROGRAMMED contracts. Codex may complete bounded validation/serialization details,
but must not redesign ownership or replace these with provider-specific objects.
"""
from dataclasses import dataclass, field
from enum import StrEnum
import json
from typing import Any, Mapping

from .fingerprinting import FINGERPRINT_FIELD, content_fingerprint, content_payload


class NodeState(StrEnum):
    PLANNED = "planned"
    READY = "ready"
    RUNNING = "running"
    CANDIDATE = "candidate"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    BLOCKED = "blocked"
    INVALIDATED = "invalidated"


class QualificationState(StrEnum):
    DISCOVERED = "discovered"
    CANDIDATE = "candidate"
    QUALIFIED = "qualified"
    PROMOTED = "promoted"
    REJECTED = "rejected"
    SUSPENDED = "suspended"


class KnowledgeState(StrEnum):
    KNOWN = "known"
    DEGRADED = "degraded"
    UNKNOWN = "unknown"


@dataclass(frozen=True, slots=True)
class Fingerprinted:
    id: str
    version: int
    fingerprint: str

    def __post_init__(self) -> None:
        if not self.id.strip():
            raise ValueError("id must be non-empty")
        if self.version < 1:
            raise ValueError("version must be >= 1")
        if not self.fingerprint.strip():
            raise ValueError("fingerprint must be explicit")


@dataclass(frozen=True, slots=True)
class IRDocument(Fingerprinted):
    project_id: str
    modality: str
    intent: Mapping[str, Any] = field(default_factory=dict)
    locked_paths: tuple[str, ...] = ()
    references: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class GraphNode(Fingerprinted):
    project_id: str
    state: NodeState
    ir_ref: str
    artifact_refs: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class GraphEdge:
    source: str
    target: str
    relation: str

    def __post_init__(self) -> None:
        if self.source == self.target:
            raise ValueError("self edge is forbidden")
        if not self.relation.strip():
            raise ValueError("relation must be explicit")


@dataclass(frozen=True, slots=True)
class ProductionGraph(Fingerprinted):
    project_id: str
    nodes: tuple[GraphNode, ...] = ()
    edges: tuple[GraphEdge, ...] = ()


@dataclass(frozen=True, slots=True)
class AssetDNA(Fingerprinted):
    project_id: str
    canonical_asset_id: str
    locked_traits: Mapping[str, Any] = field(default_factory=dict)
    variable_traits: Mapping[str, Any] = field(default_factory=dict)
    parent_fingerprint: str | None = None


@dataclass(frozen=True, slots=True)
class ResourceEnvelope(Fingerprinted):
    knowledge: KnowledgeState
    gpu_name: str | None
    vram_total_mb: int | None
    vram_available_mb: int | None
    ram_total_mb: int | None
    concurrency_limit: int = 1

    def __post_init__(self) -> None:
        Fingerprinted.__post_init__(self)
        for value in (self.vram_total_mb, self.vram_available_mb, self.ram_total_mb):
            if value is not None and value < 0:
                raise ValueError("resource values cannot be negative")
        if self.vram_total_mb is not None and self.vram_available_mb is not None and self.vram_available_mb > self.vram_total_mb:
            raise ValueError("available VRAM cannot exceed total VRAM")
        if self.concurrency_limit < 1:
            raise ValueError("concurrency_limit must be >= 1")


@dataclass(frozen=True, slots=True)
class ModelProfile(Fingerprinted):
    model_key: str
    qualification: QualificationState
    capabilities: Mapping[str, float] = field(default_factory=dict)
    min_vram_mb: int | None = None


@dataclass(frozen=True, slots=True)
class RouteDecision(Fingerprinted):
    model_key: str
    score: float
    reason_codes: tuple[str, ...]
    hardware_fingerprint: str
    requirements_fingerprint: str


def canonical_dict(contract: Any) -> Any:
    """Stable JSON-compatible representation of a foundation contract.

    Enum values are normalized through canonical_value, mapping keys are sorted and sequences keep their
    declared order, so mapping key order cannot affect the result. Unsupported and non-finite values raise
    CanonicalizationError instead of producing a partially serialized object.
    """
    return content_payload(contract)


def canonical_json(contract: Any) -> str:
    """Canonical JSON text for a contract, excluding declared fingerprint fields."""
    return json.dumps(canonical_dict(contract), ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def content_fingerprint_of(contract: Any) -> str:
    """Fingerprint a contract should declare for its current semantic content."""
    return content_fingerprint(contract)


def fingerprint_matches(contract: Any) -> bool:
    """True when the contract's declared fingerprint matches its semantic content."""
    return getattr(contract, FINGERPRINT_FIELD, None) == content_fingerprint_of(contract)


def assert_fingerprint(contract: Any) -> None:
    """Reject a contract whose declared fingerprint does not match its content.

    A stale declared fingerprint is a correctness defect, not a formatting detail: every downstream cache,
    proof carry-forward and invalidation decision keys off it.
    """
    declared = getattr(contract, FINGERPRINT_FIELD, None)
    actual = content_fingerprint_of(contract)
    if declared != actual:
        raise ValueError(f"declared fingerprint does not match content: declared={declared!r} actual={actual!r}")


# CODEX-TASK[S01-CONTRACT-SERIALIZATION]
# DONE: canonical_dict/canonical_json delegate to the shared canonicalizer so enum normalization, key sorting
#       and unsupported-value rejection live in exactly one place; assert_fingerprint ties a contract's
#       declared fingerprint to its semantic content.
