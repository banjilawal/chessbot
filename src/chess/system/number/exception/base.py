# src/chess/system/number/exception/base.py

"""
Module: chess.system.number.exception.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# NUMBER EXCEPTION #======================#
    "NumberException",
]


# ======================# NUMBER EXCEPTION #======================#
class NumberException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by Numbers.
    2.  Catchall for conditions which are not covered by lower level Number exceptions.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NUMBER_ERROR"
    DEFAULT_MESSAGE = "Number raised an exception."