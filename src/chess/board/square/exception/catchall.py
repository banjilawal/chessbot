# src/chess/board/square/exception/catchall.py

"""
Module: chess.board.square.exception.catchall
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.board import BoardException

__all__ = [
    # ======================# BOARD_SQUARE_SERVICE EXCEPTION #======================#
    "BoardSquareServiceException",
]


# ======================# BOARD_SQUARE_SERVICE EXCEPTION #======================#
class BoardSquareServiceException(BoardException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for BoardSquareService errors.

    # PARENT:
        *   BoardSquareException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_SQUARE_SERVICE_ERROR"
    DEFAULT_MESSAGE = "BoardSquareService raised an exception."