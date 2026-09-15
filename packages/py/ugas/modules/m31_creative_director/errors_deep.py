# GENERATED-DEEP-PREPROGRAMMED
class M31Error(Exception):
    retryable: bool = False

class ValidationFailure(M31Error): pass
class PolicyFailure(M31Error): pass
class CapabilityFailure(M31Error): retryable = True
class QualityFailure(M31Error): pass
class InvariantFailure(M31Error): pass
