from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .contracts import SoundEvent


@dataclass(frozen=True, slots=True)
class SoundLayer:
    name: str
    events: tuple[SoundEvent,...]


def compile_sound_layers(layers: Sequence[SoundLayer], *, duration_ms: int) -> tuple[SoundEvent,...]:
    if duration_ms <= 0:
        raise ValueError("duration must be positive")
    seen=set()
    events=[]
    for layer in layers:
        for event in layer.events:
            if event.id in seen:
                raise ValueError(f"duplicate sound event id: {event.id}")
            if event.start_ms < 0 or event.end_ms < event.start_ms or event.end_ms > duration_ms:
                raise ValueError(f"sound event outside timeline: {event.id}")
            if not event.asset_ref:
                raise ValueError(f"sound event missing asset: {event.id}")
            seen.add(event.id); events.append(event)
    return tuple(sorted(events,key=lambda e:(e.start_ms,e.end_ms,e.id)))


# CODEX-TASK[M13-SYNC-EVIDENCE]
# Add event-to-visual/narrative sync references, mix preview evaluation and selective replacement of
# defective layers. Preserve unaffected ambience/foley/SFX proofs instead of rebuilding full scene.
