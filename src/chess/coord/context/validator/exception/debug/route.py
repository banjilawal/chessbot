__all__ = [
    # ======================# UNHANDLED_PERSONA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "CoordContextValidationRouteException",
]

from chess.coord import CoordException
from chess.system import UnhandledRouteException


# ======================# UNHANDLED_COORD_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class CoordContextValidationRouteException(CoordException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the CoordContext validation failed because there was no build route for the CoordContext key.

    # PARENT:
        *   CoordException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_COORD_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "CoordContext validation failed: No validation route was provided for the Coord attribute."