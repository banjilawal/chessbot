# src/chess/arena/service/exception/debug/full.py

"""
Module: chess.arena.service.exception.debug.full
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.system import DebugException
from chess.arena import ArenaException

__all__ = [
    # ======================# ARENA_IS_FULL EXCEPTION #======================#
    "ArenaIsFullException",
]


# ======================# ARENA_IS_FULL EXCEPTION #======================#
class ArenaIsFullException(ArenaException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the arena is full so no teams can be added
    
    # PARENT:
        *   ArenaException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ARENA_IS_FULL_ERROR"
    DEFAULT_MESSAGE = "The arena is full no more teams can be added."