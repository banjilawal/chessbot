# src/chess/board/validator/base.py

"""
Module: chess.board.validator.exception
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD BUILD EXCEPTIONS #======================#
    "InvalidBoardException",
    "NullBoardException",
]

from chess.board import BoardException
from chess.system import NullException, ValidationException


# ======================# INVALID BOARD EXCEPTIONS #======================#
class InvalidBoardException(BoardException, ValidationException):
    """Catchall Exception for BoardValidator when a candidate fails a sanity check."""
    ERROR_CODE = "BOARD_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Board validation failed."


class NullBoardException(BoardException, NullException):
    """Raised if an entity, method, or operation requires Board but gets null instead."""
    ERROR_CODE = "NULL_BOARD_ERROR"
    DEFAULT_MESSAGE = "Board cannot be validation"