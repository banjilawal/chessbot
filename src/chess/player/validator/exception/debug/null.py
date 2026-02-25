# src/chess/player/validator/exception/null.py

"""
Module: chess.player.validator.exception.null
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_PLAYER EXCEPTION #======================#
    "NullPlayerException",
]

from chess.system import NullException
from chess.player import PlayerDebugException


# ======================# NULL_PLAYER EXCEPTION #======================#
class NullPlayerException(PlayerDebugException, NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failing ValidationResult was returned because the candidate was null.

    # PARENT:
        *   PlayerDebugException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_PLAYER_ERROR"
    DEFAULT_MESSAGE = "Player validation failed: The candidate cannot be null."
