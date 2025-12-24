# src/chess/board/validator/exception/exception.py

"""
Module: chess.board.validator.exception.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ValidationFailedException
from chess.board import BoardContextException

__all__ = [
    # ======================# BOARD_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidBoardContextException",
]


# ======================# BOARD_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidBoardContextException(BoardContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a BoardContext candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an InvalidBoardContextException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The InvalidBoardContextException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   BoardContextException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "BoardContext validation failed."