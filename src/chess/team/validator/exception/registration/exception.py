# src/chess/team/validator/exception/registration/exception.py

"""
Module: chess.team.validator.exception.registration.exception
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.team import InvalidTeamException
from chess.system import RegistrationException

__all__ = [
    # ======================# TEAM_REGISTRATION EXCEPTIONS #======================#  
    "TeamRegistrationException",
    "TeamNotRegisteredWithActorException",
]


# ======================# TEAM_REGISTRATION EXCEPTIONS #======================#  
class TeamRegistrationException(InvalidTeamException, RegistrationException):
    """
    Catchall for when a Team does not have a relationship with another entity.
    """
    ERROR_CODE = "TEAM_REGISTRATION_ERROR"
    DEFAULT_MESSAGE = "Team is not registered in the collection."


class TeamNotRegisteredWithActorException(TeamRegistrationException):
    ERROR_CODE = "TEAM_NOT_REGISTERED_WITH_ACTOR_ERROR"
    DEFAULT_MESSAGE = (
        "Team is not registered in Actor.team_stack. There is no relationship between them."
    )
