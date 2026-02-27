# src/chess/board/context/builder/exception/route.py

"""
Module: chess.board.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NO_BOARD_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "BoardContextBuildRouteException",
]

from chess.board import BoardContextException
from chess.system import NoExecutionRouteException


# ======================# NO_BOARD_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class BoardContextBuildRouteException(BoardContextException, NoExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the BoardContext build failed because there was no build route for the Board key.

    # PARENT:
        *   BoardContextException
        *   NoExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_BOARD_CONTEXT_BUILD_ROUTE_EXCEPTION"
    MSG = "BoardContext build failed: No build path existed for the Board key."