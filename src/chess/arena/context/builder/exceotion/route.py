# src/chess/arena/context/builder/exception/route.py

"""
Module: chess.arena.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NO_ARENA_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "ArenaContextBuildRouteException",
]

from chess.arena import ArenaContextException
from chess.system import NoExecutionRouteException


# ======================# NO_ARENA_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class ArenaContextBuildRouteException(ArenaContextException, NoExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the ArenaContext build failed because there was no build route for the Arena key.

    # PARENT:
        *   ArenaContextException
        *   NoExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_ARENA_CONTEXT_BUILD_ROUTE_ERROR"
    MSG = "ArenaContext build failed: No build path existed for the Arena key."