# src/chess/square/exception/exception.py

"""
Module: chess.square.exception.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE EXCEPTION #======================#
    "SquareException",
]

from chess.system import SuperClassException


# ======================# SQUARE EXCEPTION #======================#
class SquareException(SuperClassException):
    """
    # ROLE: DebugException Parent, Exception Chain Layer 0

    # RESPONSIBILITIES:
    2.  Parent of SquareDebugException

    # PARENT:
        *   SuperClassException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_ERROR"
    DEFAULT_MESSAGE = "Square raised an exception."