# src/chess/board/context/finder/exception/wrapper.py

"""
Module: chess.board.context.finder.exception.wrapper
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.board import BoardException
from chess.system import SearchException

__all__ = [
    # ======================# BOARD_SEARCH_FAILURE EXCEPTION #======================#
    "BoardSearchException",
]


# ======================# BOARD_SEARCH_FAILURE EXCEPTION #======================#
class BoardSearchException(BoardException, SearchException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any condition that prevents a search from completing creates a debug exception that explains why the query
        failed. That debug exception is wrapped in the BoardSearchException which is the middle layer of the
        3-part exception chain.

    # PARENT:
        *   BoardException
        *   SearchException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_SEARCH_FAILURE"
    DEFAULT_MESSAGE = "Board search failed."