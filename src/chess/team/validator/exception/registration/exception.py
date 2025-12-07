# src/chess/team/validator/exception/registration/exception.py

"""
Module: chess.team.validator.exception.registration.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.team import InvalidTeamException
from chess.system import RegistrationException

__all__ = [
    # ======================# TEAM_REGISTRATION EXCEPTIONS #======================#
    "TeamRegistrationException",
    "TeamNotRegisteredWithAgentException",
    "TeamNotRegisteredWithBoardException",
]


# ======================# TEAM_REGISTRATION EXCEPTIONS #======================#
class TeamRegistrationException(InvalidTeamException, RegistrationException):
    """
    Catchall for when a Team does not have a relationship with another entity.
    """
    ERROR_CODE = "TEAM_REGISTRATION_ERROR"
    DEFAULT_MESSAGE = "Team is not registered with parent."


class TeamNotRegisteredWithAgentException(TeamRegistrationException):
    ERROR_CODE = "TEAM_NOT_REGISTERED_WITH_AGENT_ERROR"
    DEFAULT_MESSAGE = "Team is not registered in Agent.team_assignments. There is no relationship between them."


class TeamNotRegisteredWithBoardException(TeamRegistrationException):
    ERROR_CODE = "TEAM_NOT_REGISTERED_WITH_BOARD_ERROR"
    DEFAULT_MESSAGE = "Team is not registered with Board. There is no relationship between them."