# src/chess/game/context/builder/exception/route.py

"""
Module: chess.game.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_GAME_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "GameContextBuildRouteException",
]

from chess.game import GameContextException
from chess.system import NoBuildRouteException


# ======================# UNHANDLED_GAME_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class GameContextBuildRouteException(GameContextException, NoBuildRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the GameContext build failed because there was no build route for the Game key.

    # PARENT:
        *   GameContextException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_GAME_CONTEXT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = "GameContext build failed: No build path existed for the Game key."