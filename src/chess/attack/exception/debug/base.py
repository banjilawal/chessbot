# src/chess/attack/exception/debug/base.py

"""
Module: chess.attack.exception.debug.base
Author: Banji Lawal
Created: 2025-01-24
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
    1.  Describes the condition that caused an Attack operation failure.

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
    ERROR_CODE = "DEBUG_ERROR"
    DEFAULT_MESSAGE = "An attack debug error occurred."