# src/chess/board/token/exception/catchall.py

"""
Module: chess.board.token.exception.catchall
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.board import BoardException

__all__ = [
    # ======================# BOARD_TOKEN_SERVICE EXCEPTION #======================#
    "BoardTokenServiceException",
]


# ======================# BOARD_TOKEN_SERVICE EXCEPTION #======================#
class BoardTokenServiceException(BoardException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for BoardTokenService errors.

    # PARENT:
        *   BoardTokenException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_TOKEN_SERVICE_ERROR"
    DEFAULT_MESSAGE = "BoardTokenService raised an exception."