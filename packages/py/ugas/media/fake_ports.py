from __future__ import annotations

"""Deterministic in-memory S02 ports for A1/A2 proof without GPU/network/providers."""
from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class FakeArtifactStore:
    values: dict[str, Any] = field(default_factory=dict)

    async def put(self, artifact: Any) -> None:
        key = getattr(artifact, "id", None)
        if not key:
            raise ValueError("artifact id required")
        self.values[key] = artifact

    async def get(self, artifact_id: str) -> Any | None:
        return self.values.get(artifact_id)


@dataclass(slots=True)
class FakeEvidenceSink:
    events: list[dict[str, Any]] = field(default_factory=list)

    async def write(self, event_type: str, payload: dict[str, Any]) -> str:
        ref = f"evidence:{len(self.events)+1:04d}"
        self.events.append({"ref": ref, "type": event_type, "payload": payload})
        return ref


@dataclass(slots=True)
class FakeConsentRegistry:
    verified_refs: set[str] = field(default_factory=set)

    async def is_verified(self, consent_ref: str) -> bool:
        return consent_ref in self.verified_refs


@dataclass(slots=True)
class FakeEvaluator:
    responses: dict[str, Any] = field(default_factory=dict)

    async def evaluate(self, artifact_id: str) -> Any:
        if artifact_id not in self.responses:
            raise ValueError(f"no fake evaluation registered for {artifact_id}")
        return self.responses[artifact_id]


# CODEX-TASK[S02-FAKE-PROVIDER-PORTS]
# Add narrow fake ImageProvider, VideoProvider, MotionProvider and DccPort implementing the exact
# module ports after materialization. Fixtures must be deterministic and must not hide provider
# contract violations. These fakes are the default S02 A2 path; real GPU/provider tests are separate.
