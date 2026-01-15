# src/chess/square/context/finder/exception/debug/route.py

"""
Module: chess.square.context.finder.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_SQUARE_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
    "SquareSearchRouteException",
]

from chess.system import NoSearchRouteException
from chess.square import SquareException


# ======================# UNHANDLED_SQUARE_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
class SquareSearchRouteException(SquareException, NoSearchRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the Square search failed because there was no search method for the Square attribute that was
        supported in the SquareContext.

    # PARENT:
        *   SquareException
        *   oSearchRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_SQUARE_SEARCH_ROUTE_ROUTE_ERROR"
    DEFAULT_MESSAGE = "Square search failed: No search method was provided for the Square attribute."