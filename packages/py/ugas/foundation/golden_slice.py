from __future__ import annotations

"""Pure S01 Golden Foundation integration slice.

This intentionally performs no persistence, network or provider execution. It proves the
contract path Codex must preserve when wiring production adapters.
"""
from dataclasses import dataclass
from typing import Any, Sequence

from .contracts import (
    AssetDNA, IRDocument, ModelProfile, ProductionGraph, ResourceEnvelope, RouteDecision,
    content_fingerprint_of,
)
from .invariants import assert_graph
from .routing import ScoredRoute, TaskRequirements, choose_route


@dataclass(frozen=True, slots=True)
class FoundationSliceInput:
    ir: IRDocument
    graph: ProductionGraph
    dna: AssetDNA
    hardware: ResourceEnvelope
    requirements: TaskRequirements
    models: Sequence[ModelProfile]


@dataclass(frozen=True, slots=True)
class FoundationSliceResult:
    ir_fingerprint: str
    graph_fingerprint: str
    dna_fingerprint: str
    hardware_fingerprint: str
    selected_route: ScoredRoute


def evaluate_foundation_slice(value: FoundationSliceInput) -> FoundationSliceResult:
    if value.ir.project_id != value.graph.project_id or value.ir.project_id != value.dna.project_id:
        raise ValueError("golden foundation slice cannot cross project boundaries")
    assert_graph(value.graph)
    if not any(node.ir_ref == value.ir.id for node in value.graph.nodes):
        raise ValueError("production graph does not reference supplied canonical IR")
    selected = choose_route(value.models, value.requirements, value.hardware)
    return FoundationSliceResult(
        ir_fingerprint=value.ir.fingerprint,
        graph_fingerprint=value.graph.fingerprint,
        dna_fingerprint=value.dna.fingerprint,
        hardware_fingerprint=value.hardware.fingerprint,
        selected_route=selected,
    )


@dataclass(frozen=True, slots=True)
class EvidencedSliceResult:
    decision: RouteDecision
    graph_fingerprint: str
    ir_fingerprint: str
    dna_fingerprint: str
    hardware_fingerprint: str
    lineage: tuple[str, ...]
    evidence_refs: tuple[str, ...]


async def evaluate_foundation_slice_evidenced(
    value: FoundationSliceInput,
    *,
    compiler: Any,
    graph_service: Any,
    dna_service: Any,
    hardware_service: Any,
    route_selector: Any,
    evidence_sink: Any = None,
) -> EvidencedSliceResult:
    """Wire the pure slice through the M04/M01/M05/M02/M03 service ports and an evidence sink.

    Services are injected rather than imported, so the foundation package never depends on the modules that
    depend on it. Every port here is expected to be fake or in-memory: no provider, network or GPU call is
    possible from this function, and the resulting decision carries fingerprints that make its lineage
    evidence-addressable.

    The M04 compile result and M05 DNA are re-validated here rather than trusted, because a service that
    rewrites canonical content must not silently change what the slice was proven against.
    """
    if value.ir.project_id != value.graph.project_id or value.ir.project_id != value.dna.project_id:
        raise ValueError("golden foundation slice cannot cross project boundaries")
    assert_graph(value.graph)
    if not any(node.ir_ref == value.ir.id for node in value.graph.nodes):
        raise ValueError("production graph does not reference supplied canonical IR")

    compiled_ir = await compiler.execute(value.ir)
    if compiled_ir.fingerprint != content_fingerprint_of(compiled_ir):
        raise ValueError("compiled IR does not carry a content-derived fingerprint")

    graph_report = await graph_service.execute(value.graph)
    if graph_report["graph_fingerprint"] != content_fingerprint_of(value.graph):
        raise ValueError("graph service reported a fingerprint inconsistent with the supplied graph")

    sealed_dna = await dna_service.execute(value.dna)
    if sealed_dna.canonical_asset_id != value.dna.canonical_asset_id:
        raise ValueError("DNA service changed canonical asset identity")
    if sealed_dna.locked_traits != value.dna.locked_traits:
        raise ValueError("DNA service changed a locked trait")

    envelope_report = await hardware_service.execute(value.hardware)
    if not envelope_report["usable_for_planning"]:
        raise ValueError("supplied hardware envelope is not usable for planning")

    decision = await route_selector.execute(
        {"requirements": value.requirements, "hardware": value.hardware, "models": tuple(value.models)}
    )
    if decision.hardware_fingerprint != value.hardware.fingerprint:
        raise ValueError("route decision was made against a different hardware envelope")
    if decision.requirements_fingerprint != value.requirements.fingerprint:
        raise ValueError("route decision was made against different requirements")

    lineage = (compiled_ir.fingerprint, content_fingerprint_of(value.graph), sealed_dna.fingerprint,
               value.hardware.fingerprint, decision.fingerprint)
    evidence_refs = tuple(f"evidence:{digest}" for digest in lineage)
    if evidence_sink is not None:
        await evidence_sink.emit({
            "project_id": value.ir.project_id,
            "lineage": lineage,
            "evidence_refs": evidence_refs,
            "model_key": decision.model_key,
            "reason_codes": decision.reason_codes,
        })
    return EvidencedSliceResult(
        decision=decision,
        graph_fingerprint=content_fingerprint_of(value.graph),
        ir_fingerprint=compiled_ir.fingerprint,
        dna_fingerprint=sealed_dna.fingerprint,
        hardware_fingerprint=value.hardware.fingerprint,
        lineage=lineage,
        evidence_refs=evidence_refs,
    )


# CODEX-TASK[S01-GOLDEN-PERSISTENCE]
# DONE: evaluate_foundation_slice_evidenced wires the pure slice through injected M04/M01/M05/M02/M03 service
#       ports plus an optional EvidenceSink. Services are injected so foundation never imports the modules that
#       depend on it. Re-validates compiled IR fingerprint, DNA identity/locks, envelope usability and decision
#       fingerprints; no provider, network or GPU call is reachable.
