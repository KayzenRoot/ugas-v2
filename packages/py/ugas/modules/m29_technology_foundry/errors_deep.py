# GENERATED-DEEP-PREPROGRAMMED
class M29Error(Exception):
    retryable: bool = False

class ValidationFailure(M29Error): pass
class PolicyFailure(M29Error): pass
class CapabilityFailure(M29Error): retryable = True
class QualityFailure(M29Error): pass
class InvariantFailure(M29Error): pass
