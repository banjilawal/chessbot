# src/chess/board/validator/exception/base.py

"""
Module: chess.board.validator.exception.base
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.board import BoardException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# BOARD_VALIDATION_FAILURE EXCEPTION #======================#
    "BoardValidationFailedException",
]


# ======================# BOARD_VALIDATION_FAILURE EXCEPTION #======================#
class BoardValidationFailedException(BoardException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why a candidate failed its validation as a Board. The encapsulated
        exceptions create a chain for tracing the source of the failure.

    # PARENT:
        *   BoardException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Board validation failed."