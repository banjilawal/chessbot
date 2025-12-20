# src/chess/arena/validator/exception/team/none.py

"""
Module: chess.arena.validator.exception.team.none
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.system import NullException
from chess.arena import InvalidArenaException

__all__ = [
    # ======================# NULL ARENA EXCEPTION #======================#
    "NoTeamsInArenaException",
]


# ======================# NULL ARENA EXCEPTION #======================#
class NoTeamsInArenaException(InvalidArenaException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an Arena's UniqueDataService instance contains no teams.

    # PARENT:
        *   InvalidArenaException
        *   NoTeamsInArenaException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_TEAMS_IN_ARENA_ERROR"
    DEFAULT_MESSAGE = (
        "Arena's UniqueTeamDataService contains no teams. A game cannot be played without two "
        "teams in the arena."
    )