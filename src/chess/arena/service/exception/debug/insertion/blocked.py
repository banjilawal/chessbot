# src/chess/arena/service/exception/debug/insertion/blocked.py

"""
Module: chess.arena.service.exception.debug.insertion.blocked
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

__all__ = [
    # ======================# BLOCKED_ARENA_TEAM_CHANGE EXCEPTION #======================#
    "ChangingArenaTeamBlockedException",
]

from chess.arena import ArenaException
from chess.system import DebugException


# ======================# BLOCKED_ARENA_TEAM_CHANGE EXCEPTION #======================#
class ChangingArenaTeamBlockedException(ArenaException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a team cannot be replaced once a game has started.
.
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
    ERROR_CODE = "BLOCKED_ARENA_TEAM_CHANGE_ERROR"
    DEFAULT_MESSAGE = "Once a game has started a team in the arena cannot be changed for another."