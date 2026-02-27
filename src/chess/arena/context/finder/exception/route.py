# src/chess/arena/context/finder/exception/route.py

"""
Module: chess.arena.context.finder.exception.route.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NO_ARENA_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
    "ArenaSearchRouteException",
]

from chess.system import NoExecutionRouteException
from chess.arena import ArenaException


# ======================# NO_ARENA_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
class ArenaSearchRouteException(ArenaException, NoExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the Arena search failed because there was no search method for the Arena attribute that was
        supported in the ArenaContext.

    # PARENT:
        *   ArenaContext
        *   NoExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_ARENA_SEARCH_ROUTE_ROUTE_EXCEPTION"
    MSG = "Arena search failed: No search method was provided for the Arena attribute."