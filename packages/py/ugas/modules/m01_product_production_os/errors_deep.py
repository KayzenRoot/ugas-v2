# GENERATED-DEEP-PREPROGRAMMED
class M01Error(Exception):
    retryable: bool = False

class ValidationFailure(M01Error): pass
class PolicyFailure(M01Error): pass
class CapabilityFailure(M01Error): retryable = True
class QualityFailure(M01Error): pass
class InvariantFailure(M01Error): pass
