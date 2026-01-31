# src/chess/team/database/core/exception/pop/unfound.py

"""
Module: chess.team.database.core.exception.pop.unfound
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""


__all__ = [
    # ======================# TEAM_DOES_NOT_EXIST_FOR_REMOVAL EXCEPTION #======================#
    "TeamDoesNotExistForRemovalException",
]

from chess.system import NullException
from chess.team import TeamStackException


# ======================# TEAM_DOES_NOT_EXIST_FOR_REMOVAL EXCEPTION #======================#
class TeamDoesNotExistForRemovalException(TeamStackException, NullException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove instances of a team by a unique attribute failed because no bag
        matching the property were found in the dataset.

    # PARENT:
        *   TeamDaaServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_DOES_NOT_EXIST_FOR_REMOVAL_ERROR"
    DEFAULT_MESSAGE = "Team pop failed: The team was not found in the dataset. Nothing to remove."