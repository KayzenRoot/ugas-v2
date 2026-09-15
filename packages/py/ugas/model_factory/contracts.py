from __future__ import annotations
from dataclasses import dataclass
from enum import StrEnum

class SplitKind(StrEnum): TRAIN="train"; VALIDATION="validation"; TEST="test"; GOLDEN="golden"
@dataclass(frozen=True,slots=True)
class DatasetItem:
    id:str; content_fingerprint:str; provenance_ref:str; rights_ref:str; annotation_ref:str|None=None
@dataclass(frozen=True,slots=True)
class DatasetVersion:
    id:str; parent_ref:str|None; item_ids:tuple[str,...]; manifest_fingerprint:str
@dataclass(frozen=True,slots=True)
class DatasetSplit:
    id:str; dataset_ref:str; kind:SplitKind; item_ids:tuple[str,...]; sealed:bool=False
@dataclass(frozen=True,slots=True)
class EvalSuite:
    id:str; golden_split_ref:str; metric_refs:tuple[str,...]; evaluator_versions:tuple[str,...]
@dataclass(frozen=True,slots=True)
class TrainingRecipe:
    id:str; base_model_ref:str; train_split_ref:str; validation_split_ref:str; hyperparameter_ref:str; hardware_envelope_ref:str
@dataclass(frozen=True,slots=True)
class ModelArtifact:
    id:str; recipe_ref:str; artifact_fingerprint:str; provenance_ref:str; benchmark_evidence_ref:str
@dataclass(frozen=True,slots=True)
class PromotionDecision:
    model_ref:str; baseline_ref:str; promoted:bool; evidence_refs:tuple[str,...]; reason_codes:tuple[str,...]

# CODEX-TASK[M38-CONTRACT-EXPANSION]
# Add annotation schemas, dedup/near-dup records, contamination reports, evaluator calibration, training
# checkpoints, model cards and rollback metadata. Dataset/model lineage must remain immutable and auditable.
