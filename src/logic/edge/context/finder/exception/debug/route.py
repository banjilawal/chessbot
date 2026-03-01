# src/logic/edge/context/finder/exception/debug/route.py

"""
Module: logic.edge.context.finder.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NO_EDGE_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
    "EdgeSearchRouteException",
]

from logic.system import ExecutionRouteException
from logic.edge import EdgeException


# ======================# NO_EDGE_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
class EdgeSearchRouteException(EdgeException, ExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the Edge search failed because there was no search method for the Edge attribute that was
        supported in the EdgeContext.

    # PARENT:
        *   EdgeException
        *   oSearchRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_EDGE_SEARCH_ROUTE_ROUTE_EXCEPTION"
    MSG = "Edge search failed: No search method was provided for the Edge attribute."