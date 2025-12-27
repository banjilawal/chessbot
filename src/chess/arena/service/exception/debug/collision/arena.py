# src/chess/arena/service/exception/debug/collision/arena.py

"""
Module: chess.arena.service.exception.debug.collision.arena
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

___all__ = [
    # ======================# TEAM_DIFFERENT_DIFFERENT_ARENA EXCEPTION #======================#
    "TeamPlayingDifferentArenaException",
]

from chess.arena import ArenaException
from chess.team import TeamException


# ======================# TEAM_DIFFERENT_DIFFERENT_ARENA EXCEPTION #======================#
class TeamPlayingDifferentArenaException(TeamException, ArenaException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that a team different a different arena.

    # PARENT:
        *   ArenaException
        *   TeamException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_DIFFERENT_DIFFERENT_ARENA_OWNER"
    DEFAULT_MESSAGE = "Team is playing in a different arena."