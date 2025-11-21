# src/chess/system/identity/id/collision.py

"""
Module: chess.system.identity.id.exception
Author: Banji Lawal
Created: 2025-09-17
version: 1.0.0
"""

from chess.system import ValidationException, NullException

__all__ = [
    "InvalidIdException",
    "IdNullException",
    "NegativeIdException"
]


class InvalidIdException(ValidationException):
    """Catchall Exception for IdValidator when a candidate fails a sanity check."""
    ERROR_CODE = "ID_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Id Validation failed."


class IdNullException(NullException):
    """Raised if an entity, method, or operation requires ID but gets validation instead."""
    ERROR_CODE = "NULL_ID_ERROR"
    DEFAULT_MESSAGE = "Id cannot be validation."


class NegativeIdException(InvalidIdException):
    """Raised if ID is zero or negative."""
    ERROR_CODE = "ID_IS_NEGATIVE"
    DEFAULT_MESSAGE = "Id cannot be less than one."
