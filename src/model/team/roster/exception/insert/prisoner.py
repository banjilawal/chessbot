# src/model/team/roster/exception/insertion/captured.py

"""
Module: model.team.roster.exception.insertion.captured
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# ADDING_PRISONER_TO_ROSTER EXCEPTION #======================#
    "AddingPrisonerToTeamRosterException",
]

from model.team import TeamRosterException


# ======================# ADDING_PRISONER_TO_ROSTER EXCEPTION #======================#
class AddingPrisonerToTeamRosterException (TeamRosterException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a occupant cannot be added to the roster because it was not free.

    Super Class:
        *   TeamRosterException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ADDING_PRISONER_TO_ROSTER_EXCEPTION"
    MSG = "Roster addition failed: A captured occupant cannot be added to the roster of active pieces."