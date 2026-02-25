# src/chess/player/validator/exception/registration/game.py

"""
Module: chess.player.validator.exception.registration.game
Author: Banji Lawal
Created: 2026-01-08
version: 1.0.0
"""

from chess.player import PlayerDebugException
from chess.system import NotRegisteredException

__all__ = [
    # ======================# PLAYER_NOT_REGISTERED_WITH_GAME EXCEPTION #======================#
    "PlayerNotRegisteredGameException",
]


# ======================# PLAYER_NOT_REGISTERED_WITH_GAME EXCEPTION #======================#
class PlayerNotRegisteredGameException(PlayerDebugException, NotRegisteredException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing ValidationResult was returned because the candidate player had not registered with its game.

    # PARENT:
        *   PlayerDebugException
        *   NotRegisteredException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PLAYER_NOT_REGISTERED_WITH_GAME_ERROR"
    MSG = "Player validation failed: The candidate player had not registered with its game."