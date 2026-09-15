# GENERATED-PREPROGRAMMED: architecture scaffold, not implemented production logic.
# Do not redesign ownership here. Follow planning canon + Context Pack.
class ModuleError(Exception):
    retryable: bool = False

class ValidationError(ModuleError): pass
class CapabilityUnavailable(ModuleError): retryable = True
class PolicyBlocked(ModuleError): pass
