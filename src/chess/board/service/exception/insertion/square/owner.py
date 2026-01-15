# src/chess/board/service/exception/insertion/square/owner.py

"""
Module: chess.board.service.exception.insertion.square.owner
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

___all__ = [
    # ======================# SQUARE_ON_DIFFERENT_BOARD EXCEPTION #======================#
    "SquareBelongsToDifferentBoardException",
]

from chess.square import SquareException
from chess.board import BoardException



# ======================# SQUARE_ON_DIFFERENT_BOARD EXCEPTION #======================#
class SquareOnDifferentBoardException(BoardException, SquareException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that inserting a BoardSquare failed because the square belonged to a  different board.

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
    ERROR_CODE = "SQUARE_ON_DIFFERENT_BOARD"
    DEFAULT_MESSAGE = "BoardService insertion operation failed: Square belongs to a different board."