# src/chess/board/item/exception/catchall.py

"""
Module: chess.board.item.exception.catchall
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""


__all__ = [
    # ======================# BOARD_SQUARE_SERVICE EXCEPTION #======================#
    "BoardSquareServiceException",
]

from chess.board import BoardException
from chess.square import SquareException
from chess.system import ServiceException


# ======================# BOARD_SQUARE_SERVICE EXCEPTION #======================#
class BoardSquareServiceException(BoardException, SquareException,ServiceException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for BoardSquareService errors.

    # PARENT:
        *   BoardSquareException
        *   SquareException
        *   ServiceException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_SQUARE_SERVICE_ERROR"
    DEFAULT_MESSAGE = "BoardSquareService raised an exception."