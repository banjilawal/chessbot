# src/chess/team/roster/exception/insertion/captured.py

"""
Module: chess.team.roster.exception.insertion.captured
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# ADDING_PRISONER_TO_ROSTER EXCEPTION #======================#
    "AddingPrisonerToTeamRosterException",
]

from chess.team import TeamRosterException


# ======================# ADDING_PRISONER_TO_ROSTER EXCEPTION #======================#
class AddingPrisonerToTeamRosterException (TeamRosterException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a occupant cannot be added to the roster because it was not free.

    # PARENT:
        *   TeamRosterException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_PRISONER_TO_ROSTER_ERROR"
    DEFAULT_MESSAGE = "Roster addition failed: A captured occupant cannot be added to the roster of active pieces."