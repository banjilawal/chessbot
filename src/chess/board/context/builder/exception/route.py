# src/chess/board/context/builder/exception/route.py

"""
Module: chess.board.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_BOARD_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "BoardContextBuildRouteException",
]

from chess.board import BoardContextException
from chess.system import NoBuildRouteException


# ======================# UNHANDLED_BOARD_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class BoardContextBuildRouteException(BoardContextException, NoBuildRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the BoardContext build failed because there was no build route for the Board key.

    # PARENT:
        *   BoardContextException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_BOARD_CONTEXT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = "BoardContext build failed: No build path existed for the Board key."