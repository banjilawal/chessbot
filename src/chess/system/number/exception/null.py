# src/chess/system/number/exception/null.py

"""
Module: chess.system.number.exception.null
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import InvalidNumberException, NullException

__all__ = [
    # ======================# NULL NUMBER EXCEPTION #======================#
    "NullNumberException",
]




# ======================# NULL NUMBER EXCEPTION #======================#
class NullNumberException(InvalidNumberException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates a method, object or operation that required a number received null instead.

    # PARENT:
        *   InvalidNumberException
        *   NullNumberException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_NUMBER_ERROR"
    DEFAULT_MESSAGE = "Number cannot be null."