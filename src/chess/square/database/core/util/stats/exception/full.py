# src/chess/square/database/core/util/stats/exception/full.py

"""
Module: chess.square.database.core.util.stats.exception.full
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_STACK_FULL EXCEPTION #======================#
    "SquareStackFullException",
]

from chess.system import DebugException
from chess.square import SquareStackException


# ======================# SQUARE_STACK_FULL EXCEPTION #======================#
class SquareStackFullException(SquareStackException, DebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that pushing square on to the stack failed there was no space left for
        adding another square.

    # PARENT:
        *   DebugException
        *   SquareStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_STACK_FULL_ERROR"
    DEFAULT_MESSAGE = "Pushing square failed: The is no space left for adding another square."