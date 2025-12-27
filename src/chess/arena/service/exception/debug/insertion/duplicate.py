# src/chess/arena/service/exception/debug/insertion/duplicate.py

"""
Module: chess.arena.service.exception.debug.insertion.duplicate
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

__all__ = [
    # ======================# ARENA_ALREADY_CONTAINS_TEAM EXCEPTION #======================#
    "ArenaAlreadyContainsTemException",
]

from chess.arena import ArenaException
from chess.system import DebugException


# ======================# ARENA_ALREADY_CONTAINS_TEAM EXCEPTION #======================#
class ArenaAlreadyContainsTemException(ArenaException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the team is already in the arena. It cannot be added again.

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
    ERROR_CODE = "ARENA_ALREADY_CONTAINS_TEAM_ERROR"
    DEFAULT_MESSAGE = "The team is already in the arena it cannot be added again."