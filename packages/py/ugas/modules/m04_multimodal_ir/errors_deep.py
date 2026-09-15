# GENERATED-DEEP-PREPROGRAMMED
class M04Error(Exception):
    retryable: bool = False

class ValidationFailure(M04Error): pass
class PolicyFailure(M04Error): pass
class CapabilityFailure(M04Error): retryable = True
class QualityFailure(M04Error): pass
class InvariantFailure(M04Error): pass
