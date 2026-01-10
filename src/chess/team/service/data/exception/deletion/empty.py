# src/chess/team/service/data/exception/deletion/empty

"""
Module: chess.team.service.data.exception.deletion.empty
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.team import TeamDataServiceException

__all__ = [
    # ======================# POPPING_EMPTY_TEAM_STACK EXCEPTION #======================#
    "PoppingEmtpyTeamDataStackException",
]


# ======================# POPPING_EMPTY_TEAM_STACK EXCEPTION #======================#
class PoppingEmtpyTeamDataStackException(TeamDataServiceException):
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
    ERROR_CODE = "POPPING_EMPTY_TEAM_STACK_ERROR"
    DEFAULT_MESSAGE = "Team deletion failed: The stack is empty. Nothing to delete"