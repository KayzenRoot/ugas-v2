# GENERATED-DEEP-PREPROGRAMMED
class M28Error(Exception):
    retryable: bool = False

class ValidationFailure(M28Error): pass
class PolicyFailure(M28Error): pass
class CapabilityFailure(M28Error): retryable = True
class QualityFailure(M28Error): pass
class InvariantFailure(M28Error): pass
