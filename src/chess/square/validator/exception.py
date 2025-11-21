# src/chess/square/validator/collision.py

"""
Module: chess.square.validator.exception
Author: Banji Lawal
Created: 2025-09-11
"""

from chess.square import SquareException
from chess.system import ValidationException

__all__ = [
    "InvalidSquareException",
]


class InvalidSquareException(SquareException, ValidationException):
    """Catchall Exception for SquareValidator when a validation candidate fails a sanity check."""
    ERROR_CODE = "SQUARE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Square validation failed."