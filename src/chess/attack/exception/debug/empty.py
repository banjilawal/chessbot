# src/chess/attack/exception/debug/square.py

"""
Module: chess.attack.exception.debug.square
Author: Banji Lawal
Created: 2026-01-24
version: 1.0.0
"""

__all__ = [
    # ======================# ATTACKING_EMPTY_SQUARE EXCEPTION #======================#
    "AttackingVacantSquareException",
]

from chess.attack import AttackDebugException


# ======================# ATTACKING_EMPTY_SQUARE EXCEPTION #======================#
class AttackingVacantSquareException(AttackDebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attack failed because there was nothing in the square.

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
    DEFAULT_MESSAGE = "Attack failed: The square was empty. There was nothing to attack."