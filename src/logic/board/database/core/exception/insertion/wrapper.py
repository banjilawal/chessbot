# src/logic/board/database/core/exception/insertion/wrapper.py

"""
Module: logic.board.database.core.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_INSERTION_FAILURE #======================#
    "BoardInsertionException",
]

from logic.board import BoardException
from logic.system import InsertionException


# ======================# BOARD_INSERTION_FAILURE #======================#
class BoardInsertionException(BoardException, InsertionException):
    """
    Role:Exception Wrapper

    Responsibilities:
    1.  Indicate that add a occupant to the roster failed.

    Super Class:
        *   BoardException
        *   InsertionException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "BOARD_INSERTION_FAILURE"
    MSG = "Board insertion failed."