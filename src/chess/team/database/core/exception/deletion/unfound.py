# src/chess/tea/database/core/exception/deletion/unfound.py

"""
Module: chess.team.database.core.exception.deletion.unfound
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.team import TeamDataServiceException

__all__ = [
    # ======================# TEAM_DOES_NOT_EXIST_FOR_REMOVAL EXCEPTION #======================#
    "TeamDoesNotExistForRemovalException",
]


# ======================# TEAM_DOES_NOT_EXIST_FOR_REMOVAL EXCEPTION #======================#
class TeamDoesNotExistForRemovalException(TeamDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove instances of a team by a unique attribute failed because no items
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
    DEFAULT_MESSAGE = "Team deletion failed: The team was not found in the dataset. Nothing to remove."