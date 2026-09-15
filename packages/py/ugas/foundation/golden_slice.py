from __future__ import annotations

"""Pure S01 Golden Foundation integration slice.

This intentionally performs no persistence, network or provider execution. It proves the
contract path Codex must preserve when wiring production adapters.
"""
from dataclasses import dataclass
from typing import Sequence

from .contracts import AssetDNA, IRDocument, ModelProfile, ProductionGraph, ResourceEnvelope
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


# CODEX-TASK[S01-GOLDEN-PERSISTENCE]
# WHAT: wire this pure slice through M04/M01/M05/M02/M03 service ports and EvidenceSink.
# INPUT: same canonical contracts plus fake repositories/probes for A2.
# OUTPUT: persisted/evidenced RouteDecision and lineage references.
# INVARIANTS: pure result semantics unchanged; no circular imports; retries idempotent.
# ERRORS: domain errors remain typed at owning module boundary.
# TEST: one A2 fixture follows IR -> graph -> DNA -> hardware -> route and emits evidence.
# DONE: S01 WO acceptance can be reviewed without any real model/provider call.
