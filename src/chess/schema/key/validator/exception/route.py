from chess.schema import InvalidSchemaException
from chess.schema.key.validator.exception.wrapper import InvalidSchemaSuperKeyException
from chess.system import UnhandledRouteException

__all__ = [
    # ======================# UNHANDLED_SCHEMA_VALIDATION_ROUTE EXCEPTION #======================#
    "SchemSuperKeyValidationRouteException",
]


# ======================# UNHANDLED_SCHEMA_VALIDATION_ROUTE EXCEPTION #======================#
class SchemSuperKeyValidationRouteException(InvalidSchemaSuperKeyException, UnhandledRouteException):
    """
    # ROLE: Fallback Result

    # RESPONSIBILITIES:
    1. Indicate that Raised when SchemaSuperKeyBuilder encounters unhandled execution flow during a build

    # PARENT:
        *   InvalidSchemaSuperKeyException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_SCHEMA_VALIDATION_ROUTE"
    DEFAULT_MESSAGE = (
        "The SchemaSuperKeyValidator did not handle a parameter or condition that needs it own execution route. "
        "The validation process was not exhaustive. Ensure all possible branches are covered in the "
        "verification process."
    )