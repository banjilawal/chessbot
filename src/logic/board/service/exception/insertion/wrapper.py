# src/logic/item/database/core/exception/insertion/wrapper.py

"""
Module: logic.item.database.core.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_SERVICE_INSERTION_OPERATION_FAILURE #======================#
    "BoardServiceInsertionOpFailedException",
]

from logic.board import BoardServiceException
from logic.system import InsertionException


# ======================# BOARD_SERVICE_INSERTION_OPERATION_FAILURE #======================#
class BoardServiceInsertionOpFailedException(BoardServiceException, InsertionException):
    """
    Role:Exception Wrapper

    Responsibilities:
    1.  Wrap debug exceptions indicating why inserting either a BoardSquare or BoardToken failed. The encapsulated
        exceptions create chain for tracing the source of the failure.

    Super Class:
        *   BoardServiceException
        *   InsertionException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "BOARD_SERVICE_INSERTION_OPERATION_FAILURE"
    MSG = "BoardService insertion operation failed."