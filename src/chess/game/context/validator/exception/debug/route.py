__all__ = [
    # ======================# UNHANDLED_GAME_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "GameContextValidationRouteException",
]

from chess.game import GameException
from chess.system import UnhandledRouteException


# ======================# UNHANDLED_GAME_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class GameContextValidationRouteException(GameException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the GameContext validation failed because there was no build route for the GameContext key.

    # PARENT:
        *   GameException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_GAME_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "GameContext validation failed: No validation route was provided for the Game attribute."