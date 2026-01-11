# src/chess/square/validator/exception/null/exception.py

"""
Module: chess.square.validator.exception.null.exception
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""


__all__ = [
    # ======================# NULL_SQUARE_CONTEXT EXCEPTION #======================#
    "NullSquareContextException",
]

from chess.system import NullException
from chess.square import InvalidSquareContextException


# ======================# NULL_SQUARE_CONTEXT EXCEPTION #======================#
class NullSquareContextException(InvalidSquareContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that SquareContext validation failed because the candidate was null.

    # PARENT:
        *   NullSquareContextException
        *   SquareContextValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_SQUARE_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "SquareContext validation failed: The candidate was null."