# src/chess/square/service/visitation/exception/start/board.py

"""
Module: chess.square.service.visitation.exception.start.board
Author: Banji Lawal
Created: 2026-02-22
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
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that a item occupation failed because the occupant belongs to a different
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
    DEFAULT_MESSAGE = "Token entering a item failed: The occupant belongs to a different board."