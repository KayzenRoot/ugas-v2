from __future__ import annotations
from typing import Sequence
from .contracts import DatasetItem,DatasetSplit,DatasetVersion,SplitKind

def validate_dataset(version:DatasetVersion,items:Sequence[DatasetItem])->None:
    by_id={i.id:i for i in items}
    if len(by_id)!=len(items): raise ValueError("duplicate dataset item id")
    if set(version.item_ids)!=set(by_id): raise ValueError("dataset manifest/items mismatch")
    fingerprints=[i.content_fingerprint for i in items]
    if len(set(fingerprints))!=len(fingerprints): raise ValueError("exact duplicate content fingerprint")
    for item in items:
        if not item.provenance_ref or not item.rights_ref: raise ValueError(f"dataset item lacks provenance/rights: {item.id}")

def assert_split_isolation(splits:Sequence[DatasetSplit])->None:
    seen={}
    for split in splits:
        if split.kind in {SplitKind.TEST,SplitKind.GOLDEN} and not split.sealed: raise ValueError(f"evaluation split must be sealed: {split.id}")
        for item in split.item_ids:
            prior=seen.get(item)
            if prior is not None and prior!=split.kind: raise ValueError(f"dataset leakage across splits: {item}")
            seen[item]=split.kind

# CODEX-TASK[M38-NEAR-DUP-CONTAMINATION]
# Add perceptual/embedding near-duplicate detection across train/validation/test/golden and external
# benchmark contamination checks. Exact hash isolation is necessary but not sufficient.
