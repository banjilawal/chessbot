# src/chess/square/exception/debug.py

"""
Module: chess.square.exception.debug
Author: Banji Lawal
Created: 2026-01-26
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_DEBUG EXCEPTION #======================#
    "SquareDebugException",
]

from chess.square import SquareException
from chess.system import DebugException


# ======================# SQUARE_DEBUG EXCEPTION #======================#
class SquareDebugException(SquareException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Square operation failure.

    # PARENT:
        *   SquareException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "SQUARE_DEBUG_ERROR"
    DEFAULT_MESSAGE = "A item debug error occurred."