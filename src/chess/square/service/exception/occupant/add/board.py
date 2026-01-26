# src/chess/square/service/exception/occupant/add/board.py

"""
Module: chess.square.service.exception.occupant.add.board
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

___all__ = [
    # ======================# TOKEN_CANNOT_ENTER_SQUARE_FROM_DIFFERENT_BOARD EXCEPTION #======================#
    "TokenEnteringSquareOnWrongBoardException",
]

from chess.square import SquareDebugException

# ======================# TOKEN_CANNOT_ENTER_SQUARE_FROM_DIFFERENT_BOARD EXCEPTION #======================#
class TokenEnteringSquareOnWrongBoardException(SquareDebugException):
      
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that a square occupation failed because the token belongs to a different
        board.

    # PARENT:
        *   SquareDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_CANNOT_ENTER_SQUARE_FROM_DIFFERENT_BOARD_ERROR"
    DEFAULT_MESSAGE = "Token entering a square failed: The token belongs to a different board."