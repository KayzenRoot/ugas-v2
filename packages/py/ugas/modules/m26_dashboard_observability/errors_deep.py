# GENERATED-DEEP-PREPROGRAMMED
class M26Error(Exception):
    retryable: bool = False

class ValidationFailure(M26Error): pass
class PolicyFailure(M26Error): pass
class CapabilityFailure(M26Error): retryable = True
class QualityFailure(M26Error): pass
class InvariantFailure(M26Error): pass
