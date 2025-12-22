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
from chess.square import InvalidSquareException

# ======================# NULL_SQUARE EXCEPTION #======================#
class NullSquareException(InvalidSquareException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates an entity, method, or operation that required a Square but got null instead.

    # PARENT:
        *   NullSquareException
        *   InvalidSquareException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_SQUARE_ERROR"
    DEFAULT_MESSAGE = "Square cannot be null."