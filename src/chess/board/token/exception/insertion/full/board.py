# src/chess/board/occupant/exception/insertion/full.py

"""
Module: chess.board.occupant.exception.insertion.full
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_REACHED_LIMIT_FOR_TOKENS EXCEPTION #======================#
    "BoardTokenListIsFullException",
]

from chess.board import BoardTokenMemberException


# ======================# BOARD_REACHED_LIMIT_FOR_TOKENS EXCEPTION #======================#
class BoardTokenListIsFullException(BoardTokenMemberException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that adding a occupant to the board failed because the board has its maximum number of tokens.

    # PARENT:
        *   BoardTokenMemberException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_REACHED_LIMIT_FOR_TOKENS_ERROR"
    DEFAULT_MESSAGE = "Adding board occupant failed: The has reached its maximum number of tokens."