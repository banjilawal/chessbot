__all__ = [
    # ======================# ENTITY_SERVICE_VALIDATION_FAILURE EXCEPTION #======================#
    "EntityServiceValidationFailedException",
]

from chess.system import ServiceException, ValidationFailedException


# ======================# ENTITY_SERVICE_VALIDATION_FAILURE EXCEPTION #======================#
class EntityServiceValidationFailedException(ServiceException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a Service candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an EntityServiceValidationFailedException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The EntityServiceValidationFailedException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   ServiceException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ENTITY_SERVICE_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "EntityService validation failed."