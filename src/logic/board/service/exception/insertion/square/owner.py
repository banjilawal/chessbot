# src/logic/board/service/exception/insertion/item/owner.py

"""
Module: logic.board.service.exception.insertion.item.owner
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

___all__ = [
    # ======================# SQUARE_ON_DIFFERENT_BOARD EXCEPTION #======================#
    "SquareBelongsToDifferentBoardException",
]

from logic.square import SquareException
from logic.board import BoardException



# ======================# SQUARE_ON_DIFFERENT_BOARD EXCEPTION #======================#
class SquareOnDifferentBoardException(BoardException, SquareException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that inserting a BoardSquare failed because the item belonged to a  different board.

    # PARENT:
        *   BoardException
        *   SquareException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_ON_DIFFERENT_BOARD"
    MSG = "BoardService insertion operation failed: Square belongs to a different board."