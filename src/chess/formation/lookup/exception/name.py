# src/chess/team/schema/service/exception/name.py

"""
Module: chess.team.schema.service.exception.name
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.team import InvalidTeamSchemaException
from chess.system import BoundsException, NameException

__all__ = [
    # ======================# TEAM NAME BOUNDS EXCEPTIONS #======================#
    "TeamNameBoundsException",
]


# ======================# TEAM NAME BOUNDS EXCEPTIONS #======================#
class TeamNameBoundsException(InvalidTeamSchemaException, BoundsException, NameException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate an error occurred because a string is outside the range of acceptable Team names.

    # PARENT:
        *   InvalidTeamSchemaException
        *   BoundsException
        *   NameException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_NAME_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Name is not included in the set of permissible team names."