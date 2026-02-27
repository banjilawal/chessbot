# src/chess/player/context/validator/exception/debug/route.py

"""
Module: chess.player.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NO_PERSONA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "PlayerContextValidationRouteException",
]

from chess.player import PlayerContextException
from chess.system import NoExecutionRouteException


# ======================# NO_PLAYER_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class PlayerContextValidationRouteException(PlayerContextException, NoExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the PlayerContext validation failed because there was no build route for the PlayerContext key.

    # PARENT:
        *   PlayerContextException
        *   NoExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_PLAYER_CONTEXT_VALIDATION_ROUTE_EXCEPTION"
    MSG = "PlayerContext validation failed: No validation route was provided for the Player attribute."