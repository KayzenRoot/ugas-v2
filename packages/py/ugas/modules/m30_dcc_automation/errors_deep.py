# GENERATED-DEEP-PREPROGRAMMED
class M30Error(Exception):
    retryable: bool = False

class ValidationFailure(M30Error): pass
class PolicyFailure(M30Error): pass
class CapabilityFailure(M30Error): retryable = True
class QualityFailure(M30Error): pass
class InvariantFailure(M30Error): pass
