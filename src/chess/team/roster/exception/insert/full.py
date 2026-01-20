# src/chess/team/roster/exception/insertion/full.py

"""
Module: chess.team.roster.exception.insertion.full
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# ROSTER_IS_FULL EXCEPTION #======================#
    "TeamRosterIsFullException",
]

from chess.team import TeamRosterException


# ======================# ROSTER_IS_FULL EXCEPTION #======================#
class TeamRosterIsFullException(TeamRosterException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that adding a square to the team failed because the roster has all sixteen tokens.

    # PARENT:
        *   RosterException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ROSTER_IS_FULL_ERROR"
    DEFAULT_MESSAGE = "Adding roster member failed: The roster has all sixteen chess pieces."