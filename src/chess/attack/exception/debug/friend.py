# src/chess/attack/exception/debug/friend.py

"""
Module: chess.attack.exception.debug.friend
Author: Banji Lawal
Created: 2026-01-24
version: 1.0.0
"""

__all__ = [
    # ======================# ATTACKING_FRIENDLY_SQUARE EXCEPTION #======================#
    "AttackingFriendlySquareException",
]

from chess.attack import AttackDebugException


# ======================# ATTACKING_FRIENDLY_SQUARE EXCEPTION #======================#
class AttackingFriendlySquareException(AttackDebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attack failed because the square was occupied by a friend.
    
    # PARENT:
        *   AttackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ATTACKING_EMPTY_SQUARE_ERROR"
    DEFAULT_MESSAGE = "Attack failed: The square was occupied by a friend."