# src/chess/system/identity/id/exception.py

"""
Module: chess.system.identity.id.exception
Author: Banji Lawal
Created: 2025-09-17
version: 1.0.0
"""

from chess.system import InvalidTextException, NullException

__all__ = [
# ======================# ID VALIDATION EXCEPTION SUPER CLASS #======================#
    "InvalidIdException",
# ======================# ID VALIDATION SUB CLASSES #======================#
    "IdNullException",
    "NegativeIdException",
]

# ======================# ID VALIDATION EXCEPTION SUPER CLASS #======================#
class InvalidIdException(InvalidTextException):
    """Catchall Exception for IdValidator when a candidate fails a sanity check."""
    ERROR_CODE = "ID_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Id Validation failed."


# ======================# ID VALIDATION SUB CLASSES #======================#
class IdNullException(InvalidIdException, NullException):
    """Raised if an entity, method, or operation requires ID but gets validation instead."""
    ERROR_CODE = "NULL_ID_ERROR"
    DEFAULT_MESSAGE = "Id cannot be null."


class NegativeIdException(InvalidIdException):
    """Raised if ID is zero or negative."""
    ERROR_CODE = "NEGATIVE_ID_ERROR"
    DEFAULT_MESSAGE = "Id cannot be zero or negative."
