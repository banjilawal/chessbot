# src/chess/board/context/finder/exception/wrapper.py

"""
Module: chess.board.context.finder.exception.wrapper
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.board import BoardException
from chess.system import SearchFailedException

__all__ = [
    # ======================# BOARD_SEARCH_FAILURE EXCEPTION #======================#
    "BoardSearchFailedException",
]


# ======================# BOARD_SEARCH_FAILURE EXCEPTION #======================#
class BoardSearchFailedException(BoardException, SearchFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Any condition that prevents a search from completing creates a debug exception that explains why the query
        failed. That debug exception is wrapped in the BoardSearchFailedException which is the middle layer of the
        3-part exception chain.

    # PARENT:
        *   BoardException
        *   SearchFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_SEARCH_FAILURE"
    DEFAULT_MESSAGE = "Board search failed."