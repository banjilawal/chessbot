# src/chess/arena/context/finder/exception/route.py

"""
Module: chess.arena.context.finder.exception.route.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_ARENA_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
    "ArenaSearchRouteException",
]

from chess.system import UnhandledRouteException
from chess.arena import ArenaException


# ======================# UNHANDLED_ARENA_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
class ArenaSearchRouteException(ArenaException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the Arena search failed because there was no search method for the Arena attribute that was
        supported in the ArenaContext.

    # PARENT:
        *   ArenaContext
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_ARENA_SEARCH_ROUTE_ROUTE_ERROR"
    DEFAULT_MESSAGE = "Arena search failed: No search method was provided for the Arena attribute."