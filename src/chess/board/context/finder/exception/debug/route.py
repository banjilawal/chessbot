# src/chess/board/context/finder/exception/debug/route.py

"""
Module: chess.board.context.finder.exception.debug.route.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_BOARD_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
    "BoardSearchRouteException",
]

from chess.system import NoSearchRouteException
from chess.board import BoardException


# ======================# UNHANDLED_BOARD_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
class BoardSearchRouteException(BoardException, NoSearchRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the Board search failed because there was no search method for the Board attribute that was
        supported in the BoardContext.

    # PARENT:
        *   BoardException
        *   oSearchRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_BOARD_SEARCH_ROUTE_ROUTE_ERROR"
    DEFAULT_MESSAGE = "Board search failed: No search method was provided for the Board attribute."