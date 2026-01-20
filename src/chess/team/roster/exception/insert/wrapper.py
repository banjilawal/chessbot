# src/chess/team/roster/exception/insertion/wrapper.py

"""
Module: chess.team.roster.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.team import TeamRosterException

__all__ = [
    # ======================# ADDING_TOKEN_TO_ROSTER_FAILURE #======================#
    "AddingTeamRosterMemberFailedException",
]


# ======================# ADDING_TOKEN_TO_ROSTER_FAILURE #======================#
class AddingTeamRosterMemberFailedException(TeamRosterException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that add a token to the roster failed.

    # PARENT:
        *   UniqueTeamDataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_TOKEN_TO_ROSTER_FAILURE_ERROR"
    DEFAULT_MESSAGE = "Adding roster member failed."