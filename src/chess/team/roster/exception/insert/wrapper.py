# src/chess/team/roster/exception/insertion/wrapper.py

"""
Module: chess.team.roster.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.team import TeamRosterException

__all__ = [
    # ======================# FILLING_TEAM_ROSTER_FAILURE #======================#
    "FillingTeamRosterFailedException",
]


# ======================# FILLING_TEAM_ROSTER_FAILURE #======================#
class FillingTeamRosterFailedException(TeamRosterException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Carry the DebugException that explains why initializing the team's roster failed.

    # PARENT:
        *   TeamDatabaseException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FILLING_TEAM_ROSTER_FAILURE_ERROR"
    DEFAULT_MESSAGE = "Filling the team's roster failed."