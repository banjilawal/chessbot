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
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by Numbers.
    2.  Super for conditions which are not covered by lower level Number exceptions.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NUMBER_ERROR"
    MSG = "Number raised an exception."