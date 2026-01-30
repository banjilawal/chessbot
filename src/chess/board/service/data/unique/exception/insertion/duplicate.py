# src/chess/board/database/exception/insertion/duplicate.py

"""
Module: chess.board.database.exception.insertion.duplicate
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""



__all__ = [
    # ======================# ADDING_DUPLICATE_BOARD EXCEPTION #======================#
    "AddingDuplicateBoardException",
]

from chess.board import UniqueBoardDataServiceException


# ======================# ADDING_DUPLICATE_BOARD EXCEPTION #======================#
class AddingDuplicateBoardException(UniqueBoardDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to add a board to the UniqueBoardDataService's dataset failed because the board was
        already in the collection

    # PARENT:
        *   UniqueBoardDataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_DUPLICATE_BOARD_ERROR"
    DEFAULT_MESSAGE = "Unique board insertion failed: The board is already in the collection."