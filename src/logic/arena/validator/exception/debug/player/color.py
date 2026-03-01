# src/logic/arena/validator/exception/debug/player/color.py

"""
Module: logic.arena.validator.exception.debug.player.color
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""


from logic.arena import ArenaDebugException


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
    ERR_CODE = "PLAYER_COLOR_COLLISION_EXCEPTION"
    MSG = (
        "Both unique players in an Arena have the same color. Game can only be played wif both players "
        "have different colors."
    )