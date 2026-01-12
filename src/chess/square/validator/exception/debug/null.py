# src/chess/square/validator/exception/null.py

"""
Module: chess.square.validator.exception.null
Author: Banji Lawal
Created: 2025-11-19
"""

__all__ = [
    # ======================# NULL_SQUARE EXCEPTION #======================#
    "NullSquareException",
]


from chess.system import NullException
from chess.square import SquareException

# ======================# NULL_SQUARE EXCEPTION #======================#
class NullSquareException(SquareException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that an entity, method, or operation that required a Square but got null instead.

    # PARENT:
        *   NullSquareException
        *   SquareValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_SQUARE_ERROR"
    DEFAULT_MESSAGE = "Square cannot be null."