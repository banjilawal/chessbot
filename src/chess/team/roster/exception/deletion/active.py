# src/chess/team/roster/exception/insertion/captured.py

"""
Module: chess.team.roster.exception.insertion.captured
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""


__all__ = [
    # ======================# REMOVING_ACTIVE_MEMBER_FROM_ROSTER EXCEPTION #======================#
    "RemovingActiveTeamMemberException",
]


# ======================# REMOVING_ACTIVE_MEMBER_FROM_ROSTER EXCEPTION #======================#
class RemovingActiveTeamMemberException(TeamRosterException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a token cannot be removed from the roster because it has not been captured.

    # PARENT:
        *   TeamException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "REMOVING_ACTIVE_MEMBER_FROM_ROSTER_ERROR"
    DEFAULT_MESSAGE = "Roster member deletion failed: An active team member cannot be removed from roster."