# src/chess/board/service/data/exception/search/wrapper.py

"""
Module: chess.board.service.data.exception.search.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# UNIQUE_BOARD_SEARCH_FAILURE EXCEPTION #======================#
    "UniqueBoardSearchFailedException",
]

from chess.board import BoardException
from chess.system import SearchFailedException


# ======================# UNIQUE_BOARD_SEARCH_FAILURE EXCEPTION #======================#
class UniqueBoardSearchFailedException(BoardException, SearchFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why inserting a unique board failed. The encapsulated exceptions create 
        chain for tracing the source of the failure.

    # PARENT:
        *   BoardException
        *   SearchFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_BOARD_SEARCH_FAILURE"
    DEFAULT_MESSAGE = "Unique board search failed."