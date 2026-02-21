# src/chess/board/service/exception/insertion/occupant/owner.py

"""
Module: chess.board.service.exception.insertion.occupant.owner
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

___all__ = [
    # ======================# TOKEN_ON_DIFFERENT_BOARD EXCEPTION #======================#
    "TokenBelongsToDifferentBoardException",
]

from chess.token import TokenException
from chess.board import BoardException


# ======================# TOKEN_ON_DIFFERENT_BOARD EXCEPTION #======================#
class TokenOnDifferentBoardException(BoardException, TokenException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that inserting a BoardToken failed because the occupant belonged to a  different board.

    # PARENT:
        *   BoardException
        *   TokenException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_ON_DIFFERENT_BOARD"
    DEFAULT_MESSAGE = "BoardService insertion operation failed: Token belongs to a different board."