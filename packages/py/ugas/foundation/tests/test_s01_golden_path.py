"""A2 Golden Foundation slice: IRDocument -> ProductionGraph -> AssetDNA -> ResourceEnvelope -> RouteDecision.

This is the only S01 suite that spans packages: it composes the M04/M01/M05/M02/M03 services through injected
ports to prove the acceptance path end to end. Every port here is fake or in-memory, so no provider, network,
GPU or model call is reachable. The production dependency direction is unchanged - foundation never imports the
modules; only this test wires them together.
"""
import asyncio

from ugas.foundation.contracts import (
    AssetDNA, GraphEdge, GraphNode, IRDocument, KnowledgeState, ModelProfile, NodeState,
    ProductionGraph, QualificationState, ResourceEnvelope, assert_fingerprint, content_fingerprint_of,
)
from ugas.foundation.golden_slice import FoundationSliceInput, evaluate_foundation_slice_evidenced
from ugas.foundation.routing import TaskRequirements
from ugas.modules.m01_product_production_os.contracts import PlanningRequest
from ugas.modules.m01_product_production_os.services_deep import ProductionGraphService
from ugas.modules.m02_hardware_intelligence.services_deep import ResourceEnvelopeService
from ugas.modules.m03_model_intelligence.services_deep import RouteSelector
from ugas.modules.m04_multimodal_ir.services_deep import IRCompiler
from ugas.modules.m05_asset_dna.services_deep import AssetDNAService
import pytest


def run(coro):
    return asyncio.run(coro)


class FakeEvidenceSink:
    def __init__(self):
        self.events = []

    async def emit(self, event):
        self.events.append(event)


def _input(project="p", ir_ref="ir-1", node_state=NodeState.READY):
    ir = IRDocument("ir-1", 1, "pending", project, "image",
                    {"subject": {"wardrobe": "blue"}, "shot": "wide"}, ("subject.wardrobe",), ("ref-a",))
    nodes = (
        GraphNode("a", 1, "fa", project, node_state, ir_ref, ()),
        GraphNode("b", 1, "fb", project, NodeState.READY, "ir-b", ()),
    )
    graph = ProductionGraph("g", 1, "fg", project, nodes, (GraphEdge("a", "b", "depends"),))
    dna = AssetDNA("dna", 1, "pending", project, "hero", {"face": "A"}, {"hair": "black"}, None)
    hardware = ResourceEnvelope("hw", 1, "fh", KnowledgeState.KNOWN, "gpu", 8192, 7000, 24000, 2)
    requirements = TaskRequirements("rq", {"image": 1.0}, {"image": 0.7})
    models = (
        ModelProfile("model-a", 1, "fma", "model-a", QualificationState.QUALIFIED, {"image": 0.9}, 6000),
        ModelProfile("model-b", 1, "fmb", "model-b", QualificationState.QUALIFIED, {"image": 0.8}, 6000),
    )
    return FoundationSliceInput(ir=ir, graph=graph, dna=dna, hardware=hardware, requirements=requirements, models=models)


def _services(sink=None):
    return {
        "compiler": IRCompiler(known_refs={"ref-a"}),
        "graph_service": ProductionGraphService(),
        "dna_service": AssetDNAService(),
        "hardware_service": ResourceEnvelopeService(),
        "route_selector": RouteSelector(),
        "evidence_sink": sink,
    }


def test_golden_path_produces_an_evidenced_deterministic_decision():
    sink = FakeEvidenceSink()
    result = run(evaluate_foundation_slice_evidenced(_input(), **_services(sink)))
    assert result.decision.model_key == "model-a"
    assert_fingerprint(result.decision)
    assert len(result.lineage) == 5 and len(result.evidence_refs) == 5
    assert sink.events and sink.events[0]["lineage"] == result.lineage


def test_golden_path_is_reproducible_for_identical_canonical_inputs():
    first = run(evaluate_foundation_slice_evidenced(_input(), **_services()))
    second = run(evaluate_foundation_slice_evidenced(_input(), **_services()))
    assert first.lineage == second.lineage
    assert first.decision.fingerprint == second.decision.fingerprint


def test_lineage_is_evidence_addressable_and_unique():
    result = run(evaluate_foundation_slice_evidenced(_input(), **_services()))
    assert len(set(result.lineage)) == len(result.lineage), "each stage must contribute a distinct digest"
    assert all(ref == f"evidence:{digest}" for ref, digest in zip(result.evidence_refs, result.lineage))


def test_decision_binds_requirements_and_hardware_fingerprints():
    value = _input()
    result = run(evaluate_foundation_slice_evidenced(value, **_services()))
    assert result.decision.hardware_fingerprint == value.hardware.fingerprint
    assert result.decision.requirements_fingerprint == value.requirements.fingerprint


def test_cross_project_slice_is_rejected():
    value = _input()
    foreign = ProductionGraph("g", 1, "fg", "other", value.graph.nodes, value.graph.edges)
    with pytest.raises(ValueError):
        run(evaluate_foundation_slice_evidenced(
            FoundationSliceInput(ir=value.ir, graph=foreign, dna=value.dna, hardware=value.hardware,
                                 requirements=value.requirements, models=value.models), **_services()))


def test_graph_that_does_not_reference_the_supplied_ir_is_rejected():
    """The slice must bind the graph to the IR it compiles, not accept two unrelated canonical inputs."""
    value = _input(ir_ref="ir-something-else")
    with pytest.raises(ValueError):
        run(evaluate_foundation_slice_evidenced(value, **_services()))


def test_unknown_hardware_envelope_blocks_the_slice():
    value = _input()
    unknown = ResourceEnvelope("hw", 1, "fh", KnowledgeState.UNKNOWN, None, None, None, None)
    with pytest.raises(ValueError):
        run(evaluate_foundation_slice_evidenced(
            FoundationSliceInput(ir=value.ir, graph=value.graph, dna=value.dna, hardware=unknown,
                                 requirements=value.requirements, models=value.models), **_services()))


def test_unqualified_only_candidates_fail_the_slice_closed():
    value = _input()
    unqualified = (
        ModelProfile("candidate", 1, "fc", "candidate", QualificationState.CANDIDATE, {"image": 1.0}, 1000),
    )
    with pytest.raises(Exception) as excinfo:
        run(evaluate_foundation_slice_evidenced(
            FoundationSliceInput(ir=value.ir, graph=value.graph, dna=value.dna, hardware=value.hardware,
                                 requirements=value.requirements, models=unqualified), **_services()))
    assert "no qualified model route" in str(excinfo.value)


def test_slice_runs_without_an_evidence_sink():
    result = run(evaluate_foundation_slice_evidenced(_input(), **{**_services(), "evidence_sink": None}))
    assert result.decision.model_key == "model-a"
