# src/logic/owner/validation/exception/registration/arena.py

"""
Module: logic.owner.validation.exception.registration.arena
Author: Banji Lawal
Created: 2026-01-08
version: 1.0.0
"""

from logic.board import BoardDebugException
from logic.system import NotRegisteredException

__all__ = [
    # ======================# BOARD_NOT_REGISTERED_WITH_ARENA EXCEPTION #======================#
    "BoardNotRegisteredArenaException",
]


# ======================# BOARD_NOT_REGISTERED_WITH_ARENA EXCEPTION #======================#
class BoardNotRegisteredArenaException(BoardDebugException, NotRegisteredException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  A failing ValidationResult was returned because the rank board had not registered with its arena.

    Super Class:
        *   BoardDebugException
        *   NotRegisteredException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "BOARD_NOT_REGISTERED_WITH_ARENA_EXCEPTION"
    MSG = "Board validation failed: The rank board had not registered with its arena."