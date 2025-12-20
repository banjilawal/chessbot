# src/chess/team/service/data/exception/registration/exception.py

"""
Module: chess.team.service.data.exception.registration.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.system import RegistrationException
from chess.team.validator import InvalidTeamException


__all__ = [
    #======================# TEAM_REGISTRATION EXCEPTION #======================#
    "TeamRegistrationException",
    "TeamNotRegisteredWithAgentException",
]


#======================# TEAM_REGISTRATION EXCEPTION #======================#
class TeamRegistrationException(InvalidTeamException, RegistrationException):
    """
    Catchall for when a Team does not have a relationship with another entity.
    """
    ERROR_CODE = "TEAM_REGISTRATION_ERROR"
    DEFAULT_MESSAGE = "Team is not registered with parent."


class TeamNotRegisteredWithAgentException(TeamRegistrationException):
    """Team was not found in the PlayerAgent's team_assignments list."""
    ERROR_CODE = "TEAM_NOT_REGISTERED_WITH_AGENT_ERROR"
    DEFAULT_MESSAGE = "Team not found in the PlayerAgent's team_assignments list."
