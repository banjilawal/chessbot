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
    "InvalidBoardException",
]


# ======================# BOARD_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidBoardException(BoardException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a Board candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an InvalidBoardException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The InvalidBoardException chain is useful for tracing a  failure to its source.

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