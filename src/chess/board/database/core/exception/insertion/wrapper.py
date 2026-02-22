# src/chess/board/database/core/exception/insertion/wrapper.py

"""
Module: chess.board.database.core.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_INSERTION_FAILURE #======================#
    "BoardInsertionException",
]

from chess.board import BoardException
from chess.system import InsertionException


# ======================# BOARD_INSERTION_FAILURE #======================#
class BoardInsertionException(BoardException, InsertionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that add a occupant to the roster failed.

    # PARENT:
        *   BoardException
        *   InsertionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_INSERTION_FAILURE"
    DEFAULT_MESSAGE = "Board insertion failed."