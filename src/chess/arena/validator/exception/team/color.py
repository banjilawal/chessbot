# src/chess/arena/validator/exception/team/color.py

"""
Module: chess.arena.validator.exception.team.color
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""


from chess.system import GameColorException
from chess.arena import ArenaValidationFailedException


__all__ = [
    # ======================# NULL ARENA EXCEPTION #======================#
    "TeamColorCollisionException",
]


# ======================# NULL ARENA EXCEPTION #======================#
class TeamColorCollisionException(ArenaValidationFailedException, GameColorException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if a both unique teams have the same color.

    # PARENT:
        *   ArenaValidationFailedException
        *   GameColorException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_COLOR_COLLISION_ERROR"
    DEFAULT_MESSAGE = (
        "Both unique teams in an Arena have the same color. Game can only be played wif both teams "
        "have different colors."
    )