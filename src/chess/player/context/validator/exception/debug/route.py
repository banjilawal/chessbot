__all__ = [
    # ======================# UNHANDLED_PLAYER_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "PlayerContextValidationRouteException",
]

from chess.player import PlayerException
from chess.system import UnhandledRouteException


# ======================# UNHANDLED_PLAYER_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class PlayerContextValidationRouteException(PlayerException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the PlayerContext validation failed because there was no build route for the PlayerContext key.

    # PARENT:
        *   PlayerException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_PLAYER_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "PlayerContext validation failed: No validation route was provided for the Player attribute."