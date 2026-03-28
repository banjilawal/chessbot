# src/logic/team/database/kernel/exception/pop/empty

"""
Module: logic.team.database.kernel.exception.pop.empty
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""



__all__ = [
    # ======================# POPPING_EMPTY_TEAM_STACK EXCEPTION #======================#
    "PoppingEmptyTeamStackException",
]

from logic.system import NullException
from logic.team import TeamStackException


# ======================# POPPING_EMPTY_TEAM_STACK EXCEPTION #======================#
class PoppingEmptyTeamStackException(TeamStackException, NullException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attempt to remove a team failed because the TeamStack was not managing any teams.

    Super Class:
        *   TeamDaaServiceException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "POPPING_EMPTY_TEAM_STACK_EXCEPTION"
    MSG = "Team pop failed: The stack is empty. Nothing to delete"