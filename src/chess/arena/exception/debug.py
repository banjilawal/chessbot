# src/chess/arena/exception/debug.py

"""
Module: chess.arena.exception.debug
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""


__all__ = [
    # ======================# ARENA_DEBUG EXCEPTION #======================#
    "ArenaDebugException",
]

from chess.arena import ArenaException
from chess.system import DebugException


# ======================# ARENA_DEBUG EXCEPTION #======================#
class ArenaDebugException(ArenaException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Arena operation failure.

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
    ERROR_CODE = "ARENA_DEBUG_ERROR"
    DEFAULT_MESSAGE = "A ArenaDebugException was raised."