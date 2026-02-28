# src/chess/game/context/builder/exception/route.py

"""
Module: chess.game.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NO_GAME_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "GameContextBuildRouteException",
]

from chess.game import GameContextException
from chess.system import ExecutionRouteException


# ======================# NO_GAME_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class GameContextBuildRouteException(GameContextException, ExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the GameContext build failed because there was no build route for the Game key.

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
    ERR_CODE = "NO_GAME_CONTEXT_BUILD_ROUTE_EXCEPTION"
    MSG = "GameContext build failed: No build path existed for the Game key."