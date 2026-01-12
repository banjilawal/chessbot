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

from chess.system import ChessException


# ======================# SQUARE EXCEPTION #======================#
class SquareException(ChessException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for Square errors not covered by SquareException subclasses.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_ERROR"
    DEFAULT_MESSAGE = "Square raised an exception."