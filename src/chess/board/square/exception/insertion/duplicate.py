# src/chess/board/square/exception/insertion/duplicate.py

"""
Module: chess.board.square.exception.insertion.duplicate
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_ALREADY_ON_BOARD EXCEPTION #======================#
    "SquareAlreadyOnBoardException",
]

from chess.board import BoardSquareServiceException


# ======================# SQUARE_ALREADY_ON_BOARD EXCEPTION #======================#
class SquareAlreadyOnBoardException(BoardSquareServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that adding a square to the board failed because the square was already present.

    # PARENT:
        *   BoardSquareServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_ALREADY_ON_SQUARE_ERROR"
    DEFAULT_MESSAGE = "Adding board square failed: The square was is already in the board."