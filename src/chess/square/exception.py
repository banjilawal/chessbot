# src/chess/square/exception.py

"""
Module: chess.square.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


__all__ = [
    # ======================# SQUARE EXCEPTION #======================#
    "SquareException",
]

from chess.system.err import ChessException


# ======================# SQUARE EXCEPTION #======================#
class SquareException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by Square objects.
    2.  Catchall for conditions which are not covered by lower level Square exception.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_ERROR"
    DEFAULT_ERROR_CODE = "Square raised an exception."