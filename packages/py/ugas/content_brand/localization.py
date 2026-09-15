from __future__ import annotations

"""M18 localization hard gates for semantic fidelity and subtitle timing."""
from dataclasses import dataclass

from .contracts import LocaleProfile,LocalizedText


@dataclass(frozen=True, slots=True)
class LocalizationObservation:
    semantic_similarity:float
    cultural_violations:tuple[str,...]
    evidence_ref:str


@dataclass(frozen=True, slots=True)
class SubtitleSegment:
    text:str
    start_ms:int
    end_ms:int


def validate_localization(value:LocalizedText,profile:LocaleProfile,observation:LocalizationObservation,*,minimum_semantic_similarity:float)->tuple[str,...]:
    if value.locale!=profile.locale: raise ValueError("locale profile mismatch")
    if not observation.evidence_ref: raise ValueError("localization evaluation requires evidence")
    failures=[]
    if observation.semantic_similarity<minimum_semantic_similarity: failures.append("SEMANTIC_DRIFT")
    failures.extend(f"CULTURAL_CONSTRAINT:{item}" for item in observation.cultural_violations)
    return tuple(failures)


def validate_subtitle(segment:SubtitleSegment,profile:LocaleProfile)->tuple[str,...]:
    if segment.start_ms<0 or segment.end_ms<=segment.start_ms: return ("INVALID_SUBTITLE_TIMING",)
    seconds=(segment.end_ms-segment.start_ms)/1000
    cps=len(segment.text)/seconds
    return (f"SUBTITLE_READING_RATE:{cps:.2f}",) if cps>profile.max_subtitle_chars_per_second else ()


# CODEX-TASK[M18-DUB-SYNC]
# Add DubPlan timing/prosody checks through M11 voice port while preserving meaning and approved
# character identity. Prefer local timing/text repair before redoing unaffected localized media.
