# src/logic/arena/service/exception/debug/deletion/empty.py

"""
Module: logic.arena.service.exception.debug.deletion.empty
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

__all__ = [
    # ======================# POPPING_EMPTY_ARENA EXCEPTION #======================#
    "PoppingEmptyArenaException",
]

from logic.arena import ArenaException
from system import DebugException


# ======================# POPPING_EMPTY_ARENA EXCEPTION #======================#
class PoppingEmptyArenaException(ArenaException, DebugException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that the arena is empty so no teams can be removed

    Super Class:
        *   ArenaException
        *   DebugException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "POPPING_EMPTY_ARENA_EXCEPTION"
    MSG = "The arena is empty. There are no teams to remove."