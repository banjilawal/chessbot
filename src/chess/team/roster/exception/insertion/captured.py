# src/chess/team/roster/exception/insertion/captured.py

"""
Module: chess.team.roster.exception.insertion.captured
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# ADDING_CAPTURED_MEMBER_TO_ROSTER EXCEPTION #======================#
    "AddingCapturedTeamMemberException",
]

# ======================# ADDING_CAPTURED_MEMBER_TO_ROSTER EXCEPTION #======================#
class AddingCapturedTeamMemberException(TeamRosterException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a token cannot be added to roster because berths are full.

    # PARENT:
        *   TeamException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_CAPTURED_MEMBER_TO_ROSTER_ERROR"
    DEFAULT_MESSAGE = "Adding roster member failed: A captured team member cannot join the roster again."