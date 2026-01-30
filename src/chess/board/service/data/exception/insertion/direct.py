# src/chess/board/service/data/exception/insertion/direct.py

"""
Module: chess.board.service.data.exception.insertion.direct
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# APPENDING_BOARD_DIRECTLY_INTO_ITEMS EXCEPTION #======================#
    "AppendingBoardDirectlyIntoItemsFailedException",
]

from chess.board import BoardDataServiceException


# ======================# APPENDING_BOARD_DIRECTLY_INTO_ITEMS EXCEPTION #======================#
class AppendingBoardDirectlyIntoItemsFailedException(BoardDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that appending the board directly into self.bag was not in the list after running bag.append.

    # PARENT:
        *   BoardDataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "APPENDING_BOARD_DIRECTLY_INTO_ITEMS_ERROR"
    DEFAULT_MESSAGE = "Board insertion failed: The board was not found in self.bag after running self.bag.append."