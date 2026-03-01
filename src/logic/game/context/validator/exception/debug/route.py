# src/logic/game/context/validator/exception/debug/route.py

"""
Module: logic.game.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NO_PERSONA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "GameContextValidationRouteException",
]

from logic.game import GameContextException
from logic.system import ExecutionRouteException


# ======================# NO_GAME_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class GameContextValidationRouteException(GameContextException, ExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the GameContext validation failed because there was no build route for the GameContext key.

    # PARENT:
        *   GameContextException
        *   ExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_GAME_CONTEXT_VALIDATION_ROUTE_EXCEPTION"
    MSG = "GameContext validation failed: No validation route was provided for the Game attribute."