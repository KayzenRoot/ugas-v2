from __future__ import annotations
from typing import Protocol
from .contracts import DccCheckpoint,DccExecutionResult,DccTransaction

class HeadlessDccPort(Protocol):
    def execute(self,transaction:DccTransaction)->DccExecutionResult: ...
    def restore(self,checkpoint:DccCheckpoint)->None: ...

def execute_checkpointed(port:HeadlessDccPort,transaction:DccTransaction)->DccExecutionResult:
    if not transaction.operation_refs: raise ValueError("DCC transaction requires operations")
    result=port.execute(transaction)
    if not result.success:
        port.restore(transaction.input_checkpoint)
        if not result.error_code: raise RuntimeError("failed DCC execution requires error code")
        return result
    if result.output_checkpoint is None or not result.evidence_refs:
        port.restore(transaction.input_checkpoint)
        raise RuntimeError("successful DCC execution requires checkpoint and evidence")
    if transaction.expected_output_fingerprint and result.output_checkpoint.scene_fingerprint!=transaction.expected_output_fingerprint:
        port.restore(transaction.input_checkpoint)
        raise RuntimeError("DCC output fingerprint mismatch")
    return result

# CODEX-TASK[M30-BLENDER-HEADLESS]
# Implement Blender adapter using supported background Python API, semantic selectors instead of UI
# coordinates, factory-startup isolation where appropriate, structured stdout/stderr and atomic .blend
# checkpoints. No manual GUI dependency. Qualify exact Blender LTS through M29 before defaulting it.
