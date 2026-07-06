# src/logic/attack/exception/debug/item/item.py

"""
Module: logic.attack.exception.debug.item.item
Author: Banji Lawal
Created: 2026-01-24
version: 1.0.0
"""

__all__ = [
    # ======================# ATTACKER_INCONSISTENT_WITH_THEIR_SQUARE EXCEPTION #======================#
    "AttackerSquareInconsistencyException",
]

from operation.token.attack import AttackDebugException


# ======================# ATTACKER_INCONSISTENT_WITH_THEIR_SQUARE EXCEPTION #======================#
class AttackerSquareInconsistencyException(AttackDebugException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attack failed because the attacker's item does not have them as an occupant.

    Super Class:
        *   AttackDebugException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ATTACKING_EMPTY_SQUARE_EXCEPTION"
    MSG = "Attack failed: The attacker was not the occupant of the item its shares a coord with."