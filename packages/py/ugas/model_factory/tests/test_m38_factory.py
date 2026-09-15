from ugas.model_factory.contracts import *
from ugas.model_factory.datasets import assert_split_isolation,validate_dataset
from ugas.model_factory.promotion import decide_promotion

def test_duplicate_content_is_rejected():
    items=(DatasetItem("a","same","p","r"),DatasetItem("b","same","p","r"))
    try: validate_dataset(DatasetVersion("v",None,("a","b"),"manifest"),items)
    except ValueError as exc: assert "duplicate" in str(exc)
    else: raise AssertionError("must fail")

def test_golden_split_must_be_sealed():
    try: assert_split_isolation((DatasetSplit("g","v",SplitKind.GOLDEN,("a",),False),))
    except ValueError as exc: assert "sealed" in str(exc)
    else: raise AssertionError("must fail")

def test_training_item_cannot_leak_into_golden():
    splits=(DatasetSplit("t","v",SplitKind.TRAIN,("a",)),DatasetSplit("g","v",SplitKind.GOLDEN,("a",),True))
    try: assert_split_isolation(splits)
    except ValueError as exc: assert "leakage" in str(exc)
    else: raise AssertionError("must fail")

def test_candidate_regression_blocks_promotion():
    d=decide_promotion(model_ref="new",baseline_ref="old",candidate_scores={"quality":.9,"identity":.7},baseline_scores={"quality":.8,"identity":.8},required_metrics=frozenset({"quality","identity"}),minimum_delta={"quality":0,"identity":0},evidence_refs=("eval:1",))
    assert not d.promoted; assert "metric_regression:identity" in d.reason_codes

# CODEX-TASK[M38-A2]
# Add near-duplicate contamination, rights failure, repeated-seed statistical comparison, evaluator drift,
# checkpoint resume and model rollback fixtures. Tests remain deterministic and do not train a real model.
