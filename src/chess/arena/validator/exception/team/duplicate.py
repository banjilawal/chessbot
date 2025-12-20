# src/chess/arena/number_bounds_validator/exception/team/duplicate.py

"""
Module: chess.game.arena.number_bounds_validator.exception.team.duplicate
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.arena import InvalidArenaException
from chess.team import AddingDuplicateTeamException


__all__ = [
    # ======================# NULL ARENA EXCEPTION #======================#
    "DuplicateTeamInArenaException",
]


# ======================# NULL ARENA EXCEPTION #======================#
class DuplicateTeamInArenaException(InvalidArenaException, AddingDuplicateTeamException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an Arena's UniqueDataService instance contains two copies of the same team. This should not
        be possible, since the UniqueDataService does not allow duplicates.

    # PARENT:
        *   InvalidArenaException
        *   AddingDuplicateTeamException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "DUPLICATE_TEAM_IN_ARENA_ERROR"
    DEFAULT_MESSAGE = (
        "Arena contains two copies of the same team. UniqueTeamDataService failed to prevent this."
    )