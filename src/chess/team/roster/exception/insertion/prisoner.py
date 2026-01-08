# src/chess/team/roster/exception/insertion/captured.py

"""
Module: chess.team.roster.exception.insertion.captured
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# ADDING_PRISONER_TO_ROSTER EXCEPTION #======================#
    "AddingPrisonerToRosterException",
]

from chess.team import RosterServiceException


# ======================# ADDING_PRISONER_TO_ROSTER EXCEPTION #======================#
class AddingPrisonerToRosterException (RosterServiceException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a token cannot be added to the roster because it was not free.

    # PARENT:
        *   RosterServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_PRISONER_TO_ROSTER_ERROR"
    DEFAULT_MESSAGE = "Roster addition failed: A captured token cannot be added to the roster of active pieces."