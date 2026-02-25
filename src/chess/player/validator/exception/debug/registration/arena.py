# src/chess/player/validator/exception/registration/arena.py

"""
Module: chess.player.validator.exception.registration.arena
Author: Banji Lawal
Created: 2026-01-08
version: 1.0.0
"""

from chess.player import PlayerDebugException
from chess.system import NotRegisteredException

__all__ = [
    # ======================# PLAYER_NOT_REGISTERED_WITH_ARENA EXCEPTION #======================#
    "PlayerNotRegisteredArenaException",
]


# ======================# PLAYER_NOT_REGISTERED_WITH_ARENA EXCEPTION #======================#
class PlayerNotRegisteredArenaException(PlayerDebugException, NotRegisteredException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing ValidationResult was returned because the candidate player had not registered with its arena.

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
    ERR_CODE = "PLAYER_NOT_REGISTERED_WITH_ARENA_ERROR"
    MSG = "Player validation failed: The candidate player had not registered with its arena."