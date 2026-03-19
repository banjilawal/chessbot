# src/logic/board/database/core/exception/insertion/worker.py

"""
Module: logic.board.database.core.exception.insertion.work
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# UNIQUE_BOARD_INSERTION_FAILURE #======================#
    "UniqueBoardInsertionException",
]

from logic.board import BoardException
from logic.system import InsertionException


# ======================# UNIQUE_BOARD_INSERTION_FAILURE #======================#
class UniqueBoardInsertionException(BoardException, InsertionException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Wrap debug exceptions indicating why inserting a unique board failed. The encapsulated exceptions create 
        chain for tracing the source of the failure.

    Super Class:
        *   BoardException
        *   InsertionException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "UNIQUE_BOARD_INSERTION_FAILURE"
    MSG = "Unique board insertion failed."