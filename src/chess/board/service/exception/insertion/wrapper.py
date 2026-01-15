# src/chess/square/service/data/exception/insertion/wrapper.py

"""
Module: chess.square.service.data.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_SERVICE_INSERTION_OPERATION_FAILURE EXCEPTION #======================#
    "BoardServiceInsertionOpFailedException",
]

from chess.board import BoardServiceException
from chess.system import InsertionFailedException


# ======================# BOARD_SERVICE_INSERTION_OPERATION_FAILURE EXCEPTION #======================#
class BoardServiceInsertionOpFailedException(BoardServiceException, InsertionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why inserting either a BoardSquare or BoardToken failed. The encapsulated
        exceptions create chain for tracing the source of the failure.

    # PARENT:
        *   BoardServiceException
        *   InsertionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_SERVICE_INSERTION_OPERATION_FAILURE"
    DEFAULT_MESSAGE = "BoardService insertion operation failed."