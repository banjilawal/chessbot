# src/chess/board/validator/exception/base.py

"""
Module: chess.board.validator.exception.base
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.board import BoardException
from chess.system import ValidationException

__all__ = [
    # ======================# BOARD_VALIDATION_FAILURE EXCEPTION #======================#
    "BoardValidationException",
]


# ======================# BOARD_VALIDATION_FAILURE EXCEPTION #======================#
class BoardValidationException(BoardException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a Board. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   BoardException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Board validation failed."