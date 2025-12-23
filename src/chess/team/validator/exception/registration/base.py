# src/chess/team/validator/exception/registration/base.py

"""
Module: chess.team.validator.exception.registration.base
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.team import InvalidTeamException
from chess.system import RegistrationException

__all__ = [
    #======================# TEAM_REGISTRATION EXCEPTION #======================#
    "TeamRegistrationException"
]


#======================# TEAM_REGISTRATION EXCEPTION #======================#
class TeamRegistrationException(InvalidTeamException, RegistrationException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall Exception for when a Team has set its owner correctly but the owner does not
        have the team in its collection.

    # PARENT:
        *   InvalidTeamException
        *   NoRegistrationException

    # PROVIDES:
    TeamRegistrationException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_REGISTRATION_ERROR"
    DEFAULT_MESSAGE = "Team not registered with parent."