# src/chess/arena/service/exception/debug/deletion/blocked.py

"""
Module: chess.arena.service.exception.debug.deletion.blocked
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

__all__ = [
    # ======================# BLOCKED_ARENA_TEAM_REMOVAL EXCEPTION #======================#
    "ArenaTeamDeletionBlockedException",
]

from chess.arena import ArenaException
from chess.system import DebugException


# ======================# BLOCKED_ARENA_TEAM_REMOVAL EXCEPTION #======================#
class ArenaTeamDeletionBlockedException(ArenaException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a team cannot be deleted once it's in the arena
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
    ERROR_CODE = "BLOCKED_ARENA_TEAM_REMOVAL_ERROR"
    DEFAULT_MESSAGE = "Once a game has started a team cannot be removed from the arena."