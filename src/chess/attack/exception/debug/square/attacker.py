# src/chess/attack/exception/debug/item/item.py

"""
Module: chess.attack.exception.debug.item.item
Author: Banji Lawal
Created: 2026-01-24
version: 1.0.0
"""

__all__ = [
    # ======================# ATTACKER_INCONSISTENT_WITH_THEIR_SQUARE EXCEPTION #======================#
    "AttackerSquareInconsistencyException",
]

from chess.attack import AttackDebugException


# ======================# ATTACKER_INCONSISTENT_WITH_THEIR_SQUARE EXCEPTION #======================#
class AttackerSquareInconsistencyException(AttackDebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attack failed because the attacker's item does not have them as an occupant.

    # PARENT:
        *   AttackDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ATTACKING_EMPTY_SQUARE_ERROR"
    DEFAULT_MESSAGE = "Attack failed: The attacker was not the occupant of the item its shares a coord with."