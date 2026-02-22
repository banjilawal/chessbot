# src/chess/board/context/validator/exception/wrapper.py

"""
Module: chess.board.context.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import ValidationException
from chess.board import BoardContextException

__all__ = [
    # ======================# BOARD_CONTEXT_VALIDATION_FAILURE #======================#
    "BoardContextValidationException",
]


# ======================# BOARD_CONTEXT_VALIDATION_FAILURE #======================#
class BoardContextValidationException(BoardContextException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a BoardContext. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   BoardContextException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "BoardContext validation failed."