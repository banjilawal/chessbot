# src/chess/square/context/exception/debug.py

"""
Module: chess.square.context.exception.debug
Author: Banji Lawal
Created: 2026-02-23
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_CONTEXT_DEBUG EXCEPTION #======================#
    "SquareContextDebugException",
]

from chess.square.context import SquareContextException
from chess.system import DebugException


# ======================# SQUARE_CONTEXT_DEBUG EXCEPTION #======================#
class SquareContextDebugException(SquareContextException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a SquareContext operation failure.

    # PARENT:
        *   SquareContextException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERR_CODE = "SQUARE_CONTEXT_DEBUG_ERROR"
    MSG = "A SquareContextDebugException was raised."