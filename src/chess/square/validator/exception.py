# src/chess/square/validator/exception.py

"""
Module: chess.square.validator.exception
Author: Banji Lawal
Created: 2025-09-11
"""

from chess.square import SquareException
from chess.system import ValidationException, NullException

__all__ = [
    "InvalidSquareException",
    "NullSquareException"
]


class InvalidSquareException(SquareException, ValidationException):
    """Catchall Exception for SquareValidator when a candidate fails a sanity check.""""""
    ERROR_CODE = "SQUARE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Square validation failed."


class NullSquareException(SquareException, NullException):
    """Raised if an entity, method, or operation requires Square but gets null instead."""
    ERROR_CODE = "NULL_SQUARE_ERROR"
    DEFAULT_MESSAGE = "Square cannot be null."