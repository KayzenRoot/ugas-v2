from __future__ import annotations

"""Evidence-oriented M10 spatial dossier. No confidence-only acceptance."""
from dataclasses import dataclass
from typing import Mapping

from .acceptance import SpatialAcceptanceDecision, SpatialGate


@dataclass(frozen=True, slots=True)
class ProbeEvidence:
    probe_id: str
    artifact_fingerprint: str
    camera_fingerprint: str
    metrics: Mapping[str, float]
    evidence_ref: str


@dataclass(frozen=True, slots=True)
class SpatialQualityDossier:
    master_fingerprint: str
    derivative_fingerprint: str
    decision: SpatialAcceptanceDecision
    probes: tuple[ProbeEvidence, ...]
    lineage_refs: tuple[str, ...]
    repair_scope_refs: tuple[str, ...] = ()


def compile_dossier(*, master_fingerprint: str, derivative_fingerprint: str, decision: SpatialAcceptanceDecision, probes: tuple[ProbeEvidence, ...], lineage_refs: tuple[str, ...], repair_scope_refs: tuple[str, ...] = ()) -> SpatialQualityDossier:
    if not master_fingerprint or not derivative_fingerprint:
        raise ValueError("master and derivative fingerprints required")
    if not probes:
        raise ValueError("spatial acceptance requires probe evidence")
    if any(not probe.evidence_ref for probe in probes):
        raise ValueError("every spatial probe requires evidence reference")
    if not lineage_refs:
        raise ValueError("spatial dossier requires lineage")
    return SpatialQualityDossier(master_fingerprint, derivative_fingerprint, decision, probes, lineage_refs, repair_scope_refs)


def failed_gate_names(dossier: SpatialQualityDossier) -> tuple[str, ...]:
    return tuple(gate.value for gate in dossier.decision.failed_gates)


# CODEX-TASK[M10-M19-M20-DOSSIER-BRIDGE]
# Map failed SpatialGate values to M19 Defect records and then M20 minimal RepairRegion scopes.
# Revalidation must reuse unaffected probes/proofs and rerun only probes intersecting repaired scope.
