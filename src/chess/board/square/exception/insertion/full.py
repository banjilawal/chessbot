# src/chess/board/square/exception/insertion/full.py

"""
Module: chess.board.square.exception.insertion.full
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_REACHED_LIMIT_FOR_SQUARES EXCEPTION #======================#
    "BoardSquareServiceIsFullException",
]


# ======================# BOARD_REACHED_LIMIT_FOR_SQUARES EXCEPTION #======================#
class BoardSquareServiceIsFullException(BoardSquareException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that adding a square to the board failed because the board has its maximum number of squares.

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
    DEFAULT_MESSAGE = "Adding board square failed: The has reached its maximum number of squares."