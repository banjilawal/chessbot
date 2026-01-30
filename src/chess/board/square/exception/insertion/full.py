# src/chess/board/item/exception/insertion/full.py

"""
Module: chess.board.item.exception.insertion.full
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_REACHED_LIMIT_FOR_SQUARES EXCEPTION #======================#
    "BoardSquareListIsFullException",
]

from chess.board import BoardSquareMemberException


# ======================# BOARD_REACHED_LIMIT_FOR_SQUARES EXCEPTION #======================#
class BoardSquareListIsFullException(BoardSquareMemberException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that adding a item to the board failed because the board has its maximum number of squares.

    # PARENT:
        *   BoardSquareMemberException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_REACHED_LIMIT_FOR_SQUARES_ERROR"
    DEFAULT_MESSAGE = "Adding board item failed: The has reached its maximum number of squares."