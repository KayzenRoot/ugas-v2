# GENERATED-DEEP-PREPROGRAMMED
class M08Error(Exception):
    retryable: bool = False

class ValidationFailure(M08Error): pass
class PolicyFailure(M08Error): pass
class CapabilityFailure(M08Error): retryable = True
class QualityFailure(M08Error): pass
class InvariantFailure(M08Error): pass
