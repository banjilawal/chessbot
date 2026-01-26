# src/chess/board/occupant/exception/catchall.py

"""
Module: chess.board.occupant.exception.catchall
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_TOKEN_SERVICE EXCEPTION #======================#
    "BoardTokenServiceException",
]

from chess.board import BoardException
from chess.token import TokenException
from chess.system import ServiceException


# ======================# BOARD_TOKEN_SERVICE EXCEPTION #======================#
class BoardTokenServiceException(BoardException, TokenException, ServiceException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for BoardTokenService errors.

    # PARENT:
        *   BoardTokenException
        *   TokenException
        *   ServiceException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_TOKEN_SERVICE_ERROR"
    DEFAULT_MESSAGE = "BoardTokenService raised an exception."