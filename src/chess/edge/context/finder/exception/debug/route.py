# src/chess/edge/context/finder/exception/debug/route.py

"""
Module: chess.edge.context.finder.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NO_EDGE_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
    "EdgeSearchRouteException",
]

from chess.system import NoExecutionRouteException
from chess.edge import EdgeException


# ======================# NO_EDGE_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
class EdgeSearchRouteException(EdgeException, NoExecutionRouteException):
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
    ERR_CODE = "NO_EDGE_SEARCH_ROUTE_ROUTE_ERROR"
    MSG = "Edge search failed: No search method was provided for the Edge attribute."