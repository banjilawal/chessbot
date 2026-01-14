# src/chess/arena/context/builder/exception/route.py

"""
Module: chess.arena.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_ARENA_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "ArenaContextBuildRouteException",
]

from chess.arena import ArenaContextException
from chess.system import NoBuildRouteException


# ======================# UNHANDLED_ARENA_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class ArenaContextBuildRouteException(ArenaContextException, NoBuildRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the ArenaContext build failed because there was no build route for the Arena key.

    # PARENT:
        *   ArenaContextException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_ARENA_CONTEXT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = "ArenaContext build failed: No build path existed for the Arena key."