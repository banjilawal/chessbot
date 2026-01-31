# src/chess/team/database/core/exception/pop/empty

"""
Module: chess.team.database.core.exception.pop.empty
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""



__all__ = [
    # ======================# POPPING_EMPTY_TEAM_STACK EXCEPTION #======================#
    "PoppingEmptyTeamStackException",
]

from chess.system import NullException
from chess.team import TeamStackException


# ======================# POPPING_EMPTY_TEAM_STACK EXCEPTION #======================#
class PoppingEmptyTeamStackException(TeamStackException, NullException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove a team failed because the TeamStack was not managing any teams.

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
    DEFAULT_MESSAGE = "Team pop failed: The stack is empty. Nothing to delete"