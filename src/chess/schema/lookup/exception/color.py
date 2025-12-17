# src/chess/team/schema/lookup/exception/color.py

"""
Module: chess.team.schema.lookup.exception.color
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.team import InvalidTeamSchemaException
from chess.system import BoundsException, GameColorException

__all__ = [
    # ======================# TEAM COLOR BOUNDS EXCEPTIONS #======================#
    "TeamColorBoundsException",
]


# ======================# TEAM COLOR BOUNDS EXCEPTIONS #======================#
class TeamColorBoundsException(InvalidTeamSchemaException, BoundsException, GameColorException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate an error occurred because a color is outside the range of acceptable Team colors.

    # PARENT:
        *   InvalidTeamSchemaException
        *   BoundsException
        *   GameColorException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_COLOR_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Color is not included in the set of permissible team colors."

