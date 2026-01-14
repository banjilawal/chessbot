# src/chess/player/context/builder/exception/route.py

"""
Module: chess.player.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_PLAYER_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "PlayerContextBuildRouteException",
]

from chess.player import PlayerContextException
from chess.system import NoBuildRouteException


# ======================# UNHANDLED_PLAYER_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class PlayerContextBuildRouteException(PlayerContextException, NoBuildRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the PlayerContext build failed because there was no build route for the Player key.

    # PARENT:
        *   PlayerContextException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_PLAYER_CONTEXT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = "PlayerContext build failed: No build path existed for the Player key."