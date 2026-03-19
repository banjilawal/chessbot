# src/logic/board/database/exception/insertion/duplicate.py

"""
Module: logic.board.database.exception.insertion.duplicate
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""



__all__ = [
    # ======================# ADDING_DUPLICATE_BOARD EXCEPTION #======================#
    "AddingDuplicateBoardException",
]

from logic.board import UniqueBoardDataServiceException


# ======================# ADDING_DUPLICATE_BOARD EXCEPTION #======================#
class AddingDuplicateBoardException(UniqueBoardDataServiceException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attempt to add a board to the BoardDatabase's collider_candidates failed because the board was
        already in the collection

    Super Class:
        *   BoardDatabaseException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ADDING_DUPLICATE_BOARD_EXCEPTION"
    MSG = "Unique board insertion failed: The board is already in the collection."