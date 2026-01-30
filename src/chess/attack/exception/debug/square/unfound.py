# src/chess/attack/exception/debug/item/unfound.py

"""
Module: chess.attack.exception.debug.item.unfound
Author: Banji Lawal
Created: 2026-01-24
version: 1.0.0
"""

__all__ = [
    # ======================# ROSTER_MEMBER_TO_REMOVE_DOES_NOT_EXIST EXCEPTION #======================#
    "AttackerSquareNotFoundException",
]

from chess.attack import AttackDebugException


# ======================# ROSTER_MEMBER_TO_REMOVE_DOES_NOT_EXIST EXCEPTION #======================#
class AttackerSquareNotFoundException(AttackDebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that the attack failed because no item was found at the attacker's coord.

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
    DEFAULT_MESSAGE = "Attack failed: No item was found at the attacker's position."