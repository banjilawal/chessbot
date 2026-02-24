# src/chess/square/context/finder/exception/debug/route.py

"""
Module: chess.square.context.finder.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NO_SQUARE_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
    "SquareSearchRouteException",
]

from chess.square.context import SquareContextDebugException
from chess.system import NoExecutionRouteException


# ======================# NO_SQUARE_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
class SquareSearchRouteException(SquareContextDebugException, NoExecutionRouteException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing SearchResult was returned because there was no search route was provided for the
        SquareContext attribute.

    # PARENT:
        *   SquareContextDebugException
        *   NoExecutionRouteException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_SQUARE_SEARCH_ROUTE_ROUTE_ERROR"
    DEFAULT_MESSAGE = "Square search failed: No search route was provided for the Square attribute."