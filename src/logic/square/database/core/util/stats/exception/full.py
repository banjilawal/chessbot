# src/logic/square/database/core/util/stats/exception/full.py

"""
Module: logic.square.database.core.util.stats.exception.full
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_STACK_FULL EXCEPTION #======================#
    "SquareStackFullException",
]

from logic.system import DebugException
from logic.square import SquareStackServiceException


# ======================# SQUARE_STACK_FULL EXCEPTION #======================#
class SquareStackFullException(SquareStackServiceException, DebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that pushing square on to the stack failed there was no space left for
        adding another square.

    # PARENT:
        *   DebugException
        *   SquareStackServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_STACK_FULL_EXCEPTION"
    MSG = "Pushing square failed: The is no space left for adding another square."