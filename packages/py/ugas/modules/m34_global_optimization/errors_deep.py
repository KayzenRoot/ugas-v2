# GENERATED-DEEP-PREPROGRAMMED
class M34Error(Exception):
    retryable: bool = False

class ValidationFailure(M34Error): pass
class PolicyFailure(M34Error): pass
class CapabilityFailure(M34Error): retryable = True
class QualityFailure(M34Error): pass
class InvariantFailure(M34Error): pass
