# src/logic/square/context/finder/exception/debug/route.py

"""
Module: logic.square.context.finder.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NO_SQUARE_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
    "SquareSearchRouteException",
]

from logic.square.context import SquareContextDebugException
from logic.system import ExecutionRouteException


# ======================# NO_SQUARE_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
class SquareSearchRouteException(SquareContextDebugException, ExecutionRouteException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing SearchResult was returned because there was no search route was provided for the
        SquareContext attribute.

    # PARENT:
        *   SquareContextDebugException
        *   ExecutionRouteException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_SQUARE_SEARCH_ROUTE_ROUTE_EXCEPTION"
    MSG = "Square search failed: No search route was provided for the Square attribute."