# src/chess/vector/validator/exception/null/exception.py

"""
Module: chess.vector.validator.exception.null.exception_
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_VECTOR EXCEPTION #======================#
    "NullVectorException",
]

from chess.vector.validator.exception.wrapper import InvalidVectorException


# ======================# NULL_VECTOR EXCEPTION #======================#
class NullVectorException(InvalidVectorException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that Vector validation failed because the candidate was null.

    # PARENT:
        *   NullException
        *   InvalidVectorException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_VECTOR EXCEPTION_ERROR"
    DEFAULT_MESSAGE = "Vector validation failed: The candidate was null."