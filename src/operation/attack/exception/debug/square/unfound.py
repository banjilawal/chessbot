# src/logic/attack/exception/debug/item/unfound.py

"""
Module: logic.attack.exception.debug.item.unfound
Author: Banji Lawal
Created: 2026-01-24
version: 1.0.0
"""

__all__ = [
    # ======================# ROSTER_MEMBER_TO_REMOVE_DOES_NOT_EXIST EXCEPTION #======================#
    "AttackerSquareNotFoundException",
]

from operation.attack import AttackDebugException


# ======================# ROSTER_MEMBER_TO_REMOVE_DOES_NOT_EXIST EXCEPTION #======================#
class AttackerSquareNotFoundException(AttackDebugException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that the attack failed because no item was found at the attacker's coord.

    Super Class:
        *   AttackDebugException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ATTACKING_EMPTY_SQUARE_EXCEPTION"
    MSG = "Attack failed: No item was found at the attacker's position."