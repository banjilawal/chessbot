# src/chess/board/token/exception/insertion/full.py

"""
Module: chess.board.token.exception.insertion.full
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_REACHED_LIMIT_FOR_TOKENS EXCEPTION #======================#
    "BoardTokenServiceIsFullException",
]

from chess.board import BoardTokenServiceException


# ======================# BOARD_REACHED_LIMIT_FOR_TOKENS EXCEPTION #======================#
class BoardTokenServiceIsFullException(BoardTokenServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that adding a token to the board failed because the board has its maximum number of tokens.

    # PARENT:
        *   BoardTokenServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_ALREADY_ON_TOKEN_ERROR"
    DEFAULT_MESSAGE = "Adding board token failed: The has reached its maximum number of tokens."