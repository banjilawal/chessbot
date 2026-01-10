# src/chess/coord/context/finder/exception/route.py

"""
Module: chess.coord.context.finder.exception.route.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


__all__ = [
    # ======================# UNHANDLED_COORD_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
    "CoordSearchRouteException",
]

from chess.system import UnhandledRouteException
from chess.coord import CoordException


# ======================# UNHANDLED_COORD_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
class CoordSearchRouteException(CoordException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the Coord search failed because there was no search method for the Coord attribute that was
        supported in the CoordContext.

    # PARENT:
        *   CoordContext
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_COORD_SEARCH_ROUTE_ROUTE_ERROR"
    DEFAULT_MESSAGE = "Coord search failed: No search method was provided for the Coord attribute."