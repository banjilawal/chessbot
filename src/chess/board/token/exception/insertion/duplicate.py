# src/chess/board/token/exception/insertion/duplicate.py

"""
Module: chess.board.token.exception.insertion.duplicate
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_ALREADY_ON_BOARD EXCEPTION #======================#
    "TokenAlreadyOnBoardException",
]

from chess.board import BoardTokenServiceException


# ======================# TOKEN_ALREADY_ON_BOARD EXCEPTION #======================#
class TokenAlreadyOnBoardException(BoardTokenServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that adding a token to the board failed because the token was already present.

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
    DEFAULT_MESSAGE = "Adding board token failed: The token was is already in the board."