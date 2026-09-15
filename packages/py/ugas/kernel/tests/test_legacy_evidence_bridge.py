"""A2 compatibility proof for the legacy evidence bridge.

This suite intentionally imports the real module bundles (media, audio_narrative, content_brand) to prove the
bridge works against the actual legacy contracts, not a mock. It is therefore kept out of
test_kernel_readiness.py, which stays dependency-light.
"""
from ugas.kernel.evidence_graph import ProofState as CanonicalProofState
from ugas.kernel.evidence_graph import validate_graph
from ugas.kernel.legacy_evidence_bridge import (
    canonical_proof_state,
    evidence_graph_from_legacy_bundle,
    evidence_nodes_from_legacy_proof,
)
import pytest

from ugas.media.evidence import MediaEvidenceBundle, ProofRecord as MediaProof
from ugas.media.evidence import ProofState as MediaProofState
from ugas.audio_narrative.evidence import AudioNarrativeEvidenceBundle, AudioNarrativeProof
from ugas.audio_narrative.evidence import ProofState as AudioProofState
from ugas.content_brand.evidence import ContentEvidenceBundle, ContentProof
from ugas.content_brand.evidence import ProofState as ContentProofState

LEGACY_STATES=[("media",MediaProofState),("audio_narrative",AudioProofState),("content_brand",ContentProofState)]

def test_legacy_modules_declare_parallel_proof_state_definitions():
    """The mismatch this bridge exists to resolve: three packages redefine the canonical taxonomy."""
    for name,legacy in LEGACY_STATES:
        assert legacy is not CanonicalProofState, f"{name} must not be the canonical object"
        assert str(legacy.PROVEN.value)==CanonicalProofState.PROVEN.value, f"{name} values must map by value"

def test_legacy_definitions_are_incomplete_relative_to_canonical():
    """media mirrors all five canonical members; audio_narrative and content_brand omit NOT_REQUIRED."""
    assert {s.value for s in MediaProofState}=={s.value for s in CanonicalProofState}
    for name,legacy in LEGACY_STATES[1:]:
        missing={s.value for s in CanonicalProofState}-{s.value for s in legacy}
        assert missing=={"not_required"}, f"{name} is expected to omit only NOT_REQUIRED, got {missing}"

def test_every_canonical_value_maps_back_from_each_legacy_definition():
    for name,legacy in LEGACY_STATES:
        for member in legacy:
            assert canonical_proof_state(member) is CanonicalProofState(member.value), name

def test_unknown_legacy_state_fails_closed():
    class Rogue: value="locally_invented_state"
    try: canonical_proof_state(Rogue())
    except ValueError as exc: assert "unknown legacy proof state" in str(exc)
    else: raise AssertionError("an unknown legacy state must not be coerced into canonical proof")

def test_media_bundle_adapts_and_validates():
    bundle=MediaEvidenceBundle("p","id-fp",("art-fp",),(
        MediaProof("m1","asset:v1",MediaProofState.PROVEN,"proof:m1",frozenset({"identity","continuity"})),
        MediaProof("m2","video:v1",MediaProofState.INVALIDATED,None,frozenset({"temporal"}),("m1",)),),"cmd",(5,))
    graph=evidence_graph_from_legacy_bundle(bundle,producer_ref="m07")
    validate_graph(graph)
    ids=sorted(n.id for n in graph.nodes)
    assert ids==["m1::continuity","m1::identity","m2::temporal"]
    by_id={n.id:n for n in graph.nodes}
    assert by_id["m1::identity"].dimension=="identity" and by_id["m1::identity"].state is CanonicalProofState.PROVEN
    assert by_id["m2::temporal"].state is CanonicalProofState.INVALIDATED

def test_multi_dimension_proof_stays_independently_invalidatable():
    """A repair in one dimension must not invalidate an unrelated dimension of the same proof."""
    bundle=MediaEvidenceBundle("p","id-fp",(),(
        MediaProof("m1","asset:v1",MediaProofState.PROVEN,"proof:m1",frozenset({"identity","continuity"})),),"cmd",(5,))
    graph=evidence_graph_from_legacy_bundle(bundle,producer_ref="m07")
    from ugas.kernel.evidence_graph import invalidate
    out={n.dimension:n.state for n in invalidate(graph,{"asset:v1"}).nodes}
    assert set(out)=={"identity","continuity"}, "both dimensions survive as separate nodes"

def test_legacy_causal_lineage_becomes_dependency_edges():
    bundle=MediaEvidenceBundle("p","id-fp",(),(
        MediaProof("m1","asset:v1",MediaProofState.PROVEN,"proof:m1",frozenset({"identity"})),
        MediaProof("m2","video:v1",MediaProofState.PROVEN,"proof:m2",frozenset({"temporal"}),("m1",)),),"cmd",(5,))
    graph=evidence_graph_from_legacy_bundle(bundle,producer_ref="m07")
    validate_graph(graph)
    by_id={n.id:n for n in graph.nodes}
    assert by_id["m2::temporal"].dependency_refs==("m1::identity",), "resolvable causal ref must become a real dependency"

def test_unresolvable_causal_refs_are_dropped_not_fabricated():
    bundle=MediaEvidenceBundle("p","id-fp",(),(
        MediaProof("m1","asset:v1",MediaProofState.PROVEN,"proof:m1",frozenset({"identity"}),("does-not-exist",)),),"cmd",(5,))
    graph=evidence_graph_from_legacy_bundle(bundle,producer_ref="m07")
    validate_graph(graph)
    assert graph.nodes[0].dependency_refs==(), "unresolvable lineage must be dropped rather than dangle"

def test_audio_narrative_and_content_brand_bundles_adapt():
    audio=AudioNarrativeEvidenceBundle("p","canon-fp","scene",(
        AudioNarrativeProof("a1","voice:v1",frozenset({"voice"}),AudioProofState.PROVEN,"proof:a1"),),"cmd",(3,))
    content=ContentEvidenceBundle("p","brand-fp","campaign",("v1",),(
        ContentProof("c1","brand:v1",frozenset({"claim","localization"}),ContentProofState.CARRY_FORWARD,"proof:c1"),),"cmd",(4,))
    ag=evidence_graph_from_legacy_bundle(audio,producer_ref="m11")
    cg=evidence_graph_from_legacy_bundle(content,producer_ref="m17")
    validate_graph(ag); validate_graph(cg)
    assert [n.id for n in ag.nodes]==["a1::voice"]
    assert sorted(n.id for n in cg.nodes)==["c1::claim","c1::localization"]

def test_single_proof_expansion_is_deterministic():
    proof=MediaProof("m1","asset:v1",MediaProofState.PROVEN,"proof:m1",frozenset({"b","a","c"}))
    first=evidence_nodes_from_legacy_proof(proof,project_id="p",producer_ref="m07")
    second=evidence_nodes_from_legacy_proof(proof,project_id="p",producer_ref="m07")
    assert [n.id for n in first]==["m1::a","m1::b","m1::c"]
    assert first==second
