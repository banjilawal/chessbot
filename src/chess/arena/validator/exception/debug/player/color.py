# src/chess/arena/validator/exception/player/color.py

"""
Module: chess.arena.validator.exception.player.color
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""


from chess.system import GameColorException
from chess.arena import ArenaDebugException


__all__ = [
    # ======================# BOTH_PLAYERS_HAVE_THE_SAME_COLOR EXCEPTION #======================#
    "PlayerColorCollisionException",
]


# ======================# BOTH_PLAYERS_HAVE_THE_SAME_COLOR EXCEPTION #======================#
class PlayerColorCollisionException(ArenaDebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if a both unique players have the same color.

    # PARENT:
        *   ArenaDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PLAYER_COLOR_COLLISION_ERROR"
    DEFAULT_MESSAGE = (
        "Both unique players in an Arena have the same color. Game can only be played wif both players "
        "have different colors."
    )