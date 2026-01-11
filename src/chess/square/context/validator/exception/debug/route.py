__all__ = [
    # ======================# UNHANDLED_PERSONA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "SquareContextValidationRouteException",
]

from chess.square import SquareException
from chess.system import UnhandledRouteException


# ======================# UNHANDLED_SQUARE_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class SquareContextValidationRouteException(SquareException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the SquareContext validation failed because there was no build route for the SquareContext key.

    # PARENT:
        *   ResultException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_SQUARE_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "SquareContext validation failed: No validation route was provided for the Square attribute."