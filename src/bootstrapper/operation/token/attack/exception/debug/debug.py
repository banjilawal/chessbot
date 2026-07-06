# src/logic/attack/exception/debug.py

"""
Module: logic.attack.exception.debug
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""


__all__ = [
    # ======================# ATTACK_DEBUG_EXCEPTION #======================#
    "AttackDebugException",
]

from operation.token.attack import AttackException
from system import DebugException


# ======================# ATTACK_DEBUG_EXCEPTION #======================#
class AttackDebugException(AttackException, DebugException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Describes the condition that caused a Attack operation failure.

    Super Class:
        *   AttackException
        *   DebugException

    Provides:


    # INHERITED ATTRIBUTES:
     None
    """
    ERR_CODE = "ATTACK_DEBUG_EXCEPTION"
    MSG = "A AttackDebugException was raised."