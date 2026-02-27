# src/chess/board/context/finder/exception/debug/route.py

"""
Module: chess.board.context.finder.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NO_BOARD_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
    "BoardSearchRouteException",
]

from chess.system import NoExecutionRouteException
from chess.board import BoardException


# ======================# NO_BOARD_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
class BoardSearchRouteException(BoardException, NoExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the Board search failed because there was no search method for the Board attribute that was
        supported in the BoardContext.

    # PARENT:
        *   BoardException
        *   SearchRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_BOARD_SEARCH_ROUTE_ROUTE_EXCEPTION"
    MSG = "Board search failed: No search method was provided for the Board attribute."