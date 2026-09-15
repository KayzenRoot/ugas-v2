from ugas.kernel.adapter_qualification import AdapterQualification,AdapterState,assert_usable
from ugas.kernel.evidence_graph import EvidenceGraph,EvidenceNode,ProofState,invalidate,validate_graph
from ugas.kernel.observability import FailureRecord,validate_failure
from ugas.kernel.envelopes import FailureKind

def test_evidence_invalidation_is_causal_not_global():
    g=EvidenceGraph("p",(
        EvidenceNode("a","p","asset:v1","identity",ProofState.PROVEN,"m06",(),"proof:a"),
        EvidenceNode("b","p","video:v1","temporal",ProofState.PROVEN,"m08",("a",),"proof:b"),
        EvidenceNode("c","p","audio:v1","voice",ProofState.PROVEN,"m11",(),"proof:c"),))
    validate_graph(g); out=invalidate(g,{"asset:v1"}); states={n.id:n.state for n in out.nodes}
    assert states["a"] is ProofState.INVALIDATED and states["b"] is ProofState.INVALIDATED
    assert states["c"] is ProofState.PROVEN

def test_adapter_requires_qualification_and_evidence():
    q=AdapterQualification("q","blender","blender","5.x",AdapterState.CANDIDATE,frozenset({"dcc.headless"}),"lic","sec","bench","hw","compat")
    try: assert_usable(q,frozenset({"dcc.headless"}))
    except PermissionError: pass
    else: raise AssertionError("candidate adapter must fail closed")

def test_policy_rejection_cannot_be_retryable():
    r=FailureRecord("f","p","trace","op",FailureKind.POLICY_REJECTION,True,"rights_denied","evidence")
    try: validate_failure(r)
    except ValueError as exc: assert "non-retryable" in str(exc)
    else: raise AssertionError("must fail")

# CODEX-TASK[KERNEL-A1]
# Add cycle detection, carry-forward fingerprint checks, adapter version invalidation, secret-redaction and
# transient/provider retry fixtures. Keep this suite dependency-light and runnable before module shards.
