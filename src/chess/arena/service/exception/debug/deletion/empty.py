# src/chess/arena/service/exception/debug/deletion/empty.py

"""
Module: chess.arena.service.exception.debug.deletion.empty
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

__all__ = [
    # ======================# POPPING_EMPTY_ARENA EXCEPTION #======================#
    "PoppingEmptyArenaException",
]

from chess.arena import ArenaException
from chess.system import DebugException


# ======================# POPPING_EMPTY_ARENA EXCEPTION #======================#
class PoppingEmptyArenaException(ArenaException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the arena is empty so no teams can be removed

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
    ERROR_CODE = "POPPING_EMPTY_ARENA_ERROR"
    DEFAULT_MESSAGE = "The arena is empty. There are no teams to remove."