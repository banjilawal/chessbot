# src/chess/rank/exception/debug.py

"""
Module: chess.rank.exception.debug
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""


__all__ = [
    # ======================# RANK_DEBUG EXCEPTION #======================#
    "RankDebugException",
]

from chess.rank import RankException
from chess.system import DebugException


# ======================# RANK_DEBUG EXCEPTION #======================#
class RankDebugException(RankException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Rank operation failure.

    # PARENT:
        *   RankException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "RANK_DEBUG_ERROR"
    DEFAULT_MESSAGE = "A RankDebugException was raised."