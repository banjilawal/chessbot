# src/chess/team/validator/exception/debug/arena.py

"""
Module: chess.team.validator.exception.debug.arena
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""



__all__ = [
    # ======================# TEAM_NOT_SUBMITTED_ARENA_REGISTRATION EXCEPTION #======================#
    "TeamNotSubmittedArenaRegistrationException",
]

from chess.team import TeamDebugException


#======================# TEAM_NOT_SUBMITTED_ARENA_REGISTRATION EXCEPTION #======================#
class TeamNotSubmittedArenaRegistrationException(TeamDebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate was not granted Team certification because it has not filled the open slot
        available in the arena.
    
    # PARENT:
        *   TeamDebugException
        *   NotRegisteredException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_NOT_SUBMITTED_ARENA_REGISTRATION_ERROR"
    DEFAULT_MESSAGE = "Team validation failed: The candidate has not registered to fill the open in its arena."

