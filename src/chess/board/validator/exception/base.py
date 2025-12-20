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
    # ======================# BOARD VALIDATION EXCEPTION #======================#
    "InvalidBoardException",
]


# ======================# INVALID_BOARD EXCEPTION #======================#
class InvalidBoardException(BoardException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised Board validation.
    2.  Wraps unhandled exceptions that hit the finally-block in BoardValidator methods.

    # PARENT:
        *   BoardException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD__VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Board validation failed."