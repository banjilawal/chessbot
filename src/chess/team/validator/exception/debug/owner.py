# src/chess/team/validator/exception/registration/player_player.py

"""
Module: chess.team.validator.exception.registration.player_player
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""




__all__ = [
    # ======================# TEAM_NOT_REGISTERED_WITH_OWNER EXCEPTION #======================#
    "TeamNotRegisteredWithOwnerException",
]

from chess.team import TeamException
from chess.system import NotRegisteredException



#======================# TEAM_NOT_REGISTERED_WITH_OWNER EXCEPTION #======================#
class TeamNotRegisteredWithOwnerException(TeamException, NotRegisteredException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate was not granted Team certification because it was not found
        in its owner's teams.

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
    ERROR_CODE = "TEAM_NOT_REGISTERED_WITH_OWNER_ERROR"
    DEFAULT_MESSAGE = "Team validation failed: The candidate was not found in its owner.team_assignments."