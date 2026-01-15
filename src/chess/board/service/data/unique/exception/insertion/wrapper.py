# src/chess/board/service/data/exception/insertion/wrapper.py

"""
Module: chess.board.service.data.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# UNIQUE_BOARD_INSERTION_FAILURE EXCEPTION #======================#
    "UniqueBoardInsertionFailedException",
]

from chess.board import BoardException
from chess.system import InsertionFailedException


# ======================# UNIQUE_BOARD_INSERTION_FAILURE EXCEPTION #======================#
class UniqueBoardInsertionFailedException(BoardException, InsertionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why inserting a unique board failed. The encapsulated exceptions create 
        chain for tracing the source of the failure.

    # PARENT:
        *   BoardException
        *   InsertionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_BOARD_INSERTION_FAILURE"
    DEFAULT_MESSAGE = "Unique board insertion failed."