# src/logic/attack/exception/debug/item/empty.py

"""
Module: logic.attack.exception.debug.item.empty
Author: Banji Lawal
Created: 2026-01-24
version: 1.0.0
"""

__all__ = [
    # ======================# ATTACKING_EMPTY_SQUARE EXCEPTION #======================#
    "AttackingVacantSquareException",
]

from logic.attack import AttackDebugException


# ======================# ATTACKING_EMPTY_SQUARE EXCEPTION #======================#
class AttackingVacantSquareException(AttackDebugException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attack failed because there was nothing in the item.

    Super Class:
        *   AttackDebugException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ATTACKING_EMPTY_SQUARE_EXCEPTION"
    MSG = "Attack failed: The item was empty. There was nothing to attack."