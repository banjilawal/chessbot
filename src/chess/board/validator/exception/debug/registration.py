# src/chess/owner/validator/exception/registration/arena.py

"""
Module: chess.owner.validator.exception.registration.arena
Author: Banji Lawal
Created: 2026-01-08
version: 1.0.0
"""

from chess.board import BoardDebugException
from chess.system import NotRegisteredException

__all__ = [
    # ======================# BOARD_NOT_REGISTERED_WITH_ARENA EXCEPTION #======================#
    "BoardNotRegisteredArenaException",
]


# ======================# BOARD_NOT_REGISTERED_WITH_ARENA EXCEPTION #======================#
class BoardNotRegisteredArenaException(BoardDebugException, NotRegisteredException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing ValidationResult was returned because the candidate board had not registered with its arena.

    # PARENT:
        *   BoardDebugException
        *   NotRegisteredException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "BOARD_NOT_REGISTERED_WITH_ARENA_EXCEPTION"
    MSG = "Board validation failed: The candidate board had not registered with its arena."