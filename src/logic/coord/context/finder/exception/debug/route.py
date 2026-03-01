# src/logic/coord/context/finder/exception/debug/route.py

"""
Module: logic.coord.context.finder.exception.debug.route.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


__all__ = [
    # ======================# NO_COORD_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
    "CoordSearchRouteException",
]

from logic.system import ExecutionRouteException
from logic.coord import CoordException


# ======================# NO_COORD_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
class CoordSearchRouteException(CoordException, ExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the Coord search failed because there was no search method for the Coord attribute that was
        supported in the CoordContext.

    # PARENT:
        *   CoordException
        *   ExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_COORD_SEARCH_ROUTE_ROUTE_EXCEPTION"
    MSG = "Coord search failed: No search method was provided for the Coord attribute."