# src/chess/team/validator/exception/registration/game

"""
Module: chess.team.validator.exception.registration.game
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.team import TeamException
from chess.system import NotRegisteredException

__all__ = [
    # ======================# TEAM_NOT_SUBMITTED_ARENA_REGISTRATION EXCEPTION #======================#
    "TeamNotSubmittedArenaRegistrationException",
]

#======================# TEAM_NOT_SUBMITTED_ARENA_REGISTRATION EXCEPTION #======================#
class TeamNotSubmittedArenaRegistrationException(TeamException, NotRegisteredException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate was not granted Team certification because it has not filled the open slot
        available in the arena.
    
    # PARENT:
        *   TeamException
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

