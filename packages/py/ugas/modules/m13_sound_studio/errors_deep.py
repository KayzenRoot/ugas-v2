# GENERATED-DEEP-PREPROGRAMMED
class M13Error(Exception):
    retryable: bool = False

class ValidationFailure(M13Error): pass
class PolicyFailure(M13Error): pass
class CapabilityFailure(M13Error): retryable = True
class QualityFailure(M13Error): pass
class InvariantFailure(M13Error): pass
