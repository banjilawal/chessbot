# src/chess/attack/exception/debug.py

"""
Module: chess.attack.exception.debug
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""


__all__ = [
    # ======================# ATTACK_DEBUG EXCEPTION #======================#
    "AttackDebugException",
]

from chess.attack import AttackException
from chess.system import DebugException


# ======================# ATTACK_DEBUG EXCEPTION #======================#
class AttackDebugException(AttackException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Attack operation failure.

    # PARENT:
        *   AttackException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERR_CODE = "ATTACK_DEBUG_EXCEPTION"
    MSG = "A AttackDebugException was raised."