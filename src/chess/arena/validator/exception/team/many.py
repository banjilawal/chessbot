# src/chess/arena/validator/exception/team/many.py

"""
Module: chess.arena.validator.exception.team.many
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.system import BoundsException
from chess.arena import InvalidArenaException

__all__ = [
    # ======================# NULL ARENA EXCEPTION #======================#
    "ToManyTeamsInArenaException",
]


# ======================# NULL ARENA EXCEPTION #======================#
class ToManyTeamsInArenaException(InvalidArenaException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an Arena's UniqueDataService instance contains more than two teams.

    # PARENT:
        *   InvalidArenaException
        *   ToManyTeamsInArenaException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TO_MANY_TEAMS_IN_ARENA_ERROR"
    DEFAULT_MESSAGE = (
        "Arena's UniqueTeamDataService contains more than two teams. Only two teams are "
        "allowed in an arena. A game cannot be played with more than two teams."
    )