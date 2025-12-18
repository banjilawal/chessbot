# src/chess/arena/validator/exception/team/single.py

"""
Module: chess.game.arena.validator.exception.team.single
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.system import BoundsException
from chess.arena import InvalidArenaException

__all__ = [
    # ======================# NULL ARENA EXCEPTION #======================#
    "SingleTeamInArenaException",
]


# ======================# NULL ARENA EXCEPTION #======================#
class SingleTeamInArenaException(InvalidArenaException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an Arena's UniqueDataService instance contains only one team.

    # PARENT:
        *   InvalidArenaException
        *   SingleTeamInArenaException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SINGLE_TEAM_IN_ARENA_ERROR"
    DEFAULT_MESSAGE = (
        "Arena's UniqueTeamDataService contains only one team. A game cannot be played without only "
        "one team in the arena."
    )