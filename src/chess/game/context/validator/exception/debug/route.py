# src/chess/game/context/validator/exception/debug/route.py

"""
Module: chess.game.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NO_PERSONA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "GameContextValidationRouteException",
]

from chess.game import GameContextException
from chess.system import NoExecutionRouteException


# ======================# NO_GAME_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class GameContextValidationRouteException(GameContextException, NoExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the GameContext validation failed because there was no build route for the GameContext key.

    # PARENT:
        *   GameContextException
        *   NoExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_GAME_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "GameContext validation failed: No validation route was provided for the Game attribute."