# src/chess/board/context.validator/exception/wrapper.py

"""
Module: chess.board.context.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import ValidationFailedException
from chess.board import BoardContextException

__all__ = [
    # ======================# BOARD_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
    "BoardContextValidationFailedException",
]


# ======================# BOARD_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
class BoardContextValidationFailedException(BoardContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why a candidate failed its validation as a BoardContext. The encapsulated
        exceptions create a chain for tracing the source of the failure.

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