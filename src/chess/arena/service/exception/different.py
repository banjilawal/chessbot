# src/chess/arena/service/exception/different.py

"""
Module: chess.arena.service.exception.different
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

___all__ = [
    # ======================# TEAM_INSIDE_DIFFERENT_ARENA EXCEPTION #======================#
    "TeamInsideDifferentArenaException",
]

from chess.arena import ArenaException
from chess.team import TeamException


# ======================# TEAM_INSIDE_DIFFERENT_ARENA EXCEPTION #======================#
class TeamInsideDifferentArenaException(TeamException, ArenaException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that a team inside a different arena.

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
    ERROR_CODE = "TEAM_INSIDE_DIFFERENT_ARENA_OWNER"
    DEFAULT_MESSAGE = "Team inside a different arena."