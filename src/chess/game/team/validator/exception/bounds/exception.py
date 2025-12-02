# src/chess/team/validator/exception/bounds/exception.py

"""
Module: chess.team.validator.exception.bounds.exception
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""


from chess.system import BoundsException
from chess.team import InvalidTeamException

__all__ = [
    # ======================# TEAM BOUNDS EXCEPTIONS #======================#
    "TeamAttributeOutOfBoundsException",
]


# ======================# TEAM BOUNDS EXCEPTIONS #======================#
class TeamAttributeOutOfBoundsException(InvalidTeamException, BoundsException):
    """
    Raised if a Team attribute is outside its schema settings. The use case for
    TeamAttributeOutOfBoundsException is for TeamContext validation.
    """
    ERROR_CODE = "TEAM_ATTRIBUTE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Team attribute is out of bounds."


class TeamNameBoundsException(TeamAttributeOutOfBoundsException):
    """Raised if a Team name is outside its schema settings."""
    ERROR_CODE = "TEAM_NAME_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Team name is out of bounds specified in TeamSchema."


class TeamColorBoundsException(TeamAttributeOutOfBoundsException):
    """Raised if a Team name is outside its schema settings."""
    ERROR_CODE = "TEAM_NAME_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Team name is out of bounds specified in TeamSchema."


class TeamColorBoundsException(TeamAttributeOutOfBoundsException):
    """Raised if a Team name is outside its schema settings."""
    ERROR_CODE = "TEAM_NAME_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Team name is out of bounds specified in TeamSchema."