# src/logic/player/validation/exception/registration/arena.py

"""
Module: logic.player.validation.exception.registration.arena
Author: Banji Lawal
Created: 2026-01-08
version: 1.0.0
"""

from logic.player import PlayerDebugException
from system import NotRegisteredException

__all__ = [
    # ======================# PLAYER_NOT_REGISTERED_WITH_ARENA EXCEPTION #======================#
    "PlayerNotRegisteredArenaException",
]


# ======================# PLAYER_NOT_REGISTERED_WITH_ARENA EXCEPTION #======================#
class PlayerNotRegisteredArenaException(PlayerDebugException, NotRegisteredException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  A failing ValidationResult was returned because the rank player had not registered with its arena.

    Super Class:
        *   PlayerDebugException
        *   NotRegisteredException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PLAYER_NOT_REGISTERED_WITH_ARENA_EXCEPTION"
    MSG = "Player validation failed: The rank player had not registered with its arena."