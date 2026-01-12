# src/chess/team/validator/exception/registration/owner.py

"""
Module: chess.team.validator.exception.registration.owner
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.team import TeamException
from chess.system import NotRegisteredException


__all__ = [
    # ======================# TEAM_NOT_REGISTERED_WITH_PLAYER EXCEPTION #======================#
    "TeamNotSubmitedOwnerRegistrationException",
]


#======================# TEAM_NOT_REGISTERED_WITH_PLAYER EXCEPTION #======================#
class TeamNotSubmitedOwnerRegistrationException(TeamException, NotRegisteredException):
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
    ERROR_CODE = "TEAM_NOT_REGISTERED_WITH_PLAYER_ERROR"
    DEFAULT_MESSAGE = "Team validation failed: The candidate was not found in its owner.teams."