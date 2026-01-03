# src/chess/team/service/data/exception/pop.py

"""
Module: chess.team.service.data.exception.pop
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.team import TeamDataServiceException

__all__ = [
    # ======================# POPPING_EMPTY_TEAM_DATA_SERVICE EXCEPTION #======================#
    "PoppingEmtpyTeamDataServiceException",
]


# ======================# POPPING_EMPTY_TEAM_DATA_SERVICE EXCEPTION #======================#
class PoppingEmtpyTeamDataServiceException(TeamDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove a team failed because the TeamDataService was not managing any teams.

    # PARENT:
        *   TeamDaaServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "POPPING_EMPTY_TEAM_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "Team deletion failed: TeamDataService does not own any teams."