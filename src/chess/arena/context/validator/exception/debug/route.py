__all__ = [
    # ======================# UNHANDLED_ARENA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "ArenaContextValidationRouteException",
]

from chess.arena import ArenaException
from chess.system import UnhandledRouteException


# ======================# UNHANDLED_ARENA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class ArenaContextValidationRouteException(ArenaException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the ArenaContext validation failed because there was no build route for the ArenaContext key.

    # PARENT:
        *   ArenaException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_ARENA_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "ArenaContext validation failed: No validation route was provided for the Arena attribute."