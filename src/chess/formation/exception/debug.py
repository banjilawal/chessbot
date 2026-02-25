# src/chess/formation/exception/debug.py

"""
Module: chess.formation.exception.debug
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""


__all__ = [
    # ======================# FORMATION_DEBUG EXCEPTION #======================#
    "FormationDebugException",
]

from chess.formation import FormationException
from chess.system import DebugException


# ======================# FORMATION_DEBUG EXCEPTION #======================#
class FormationDebugException(FormationException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Formation operation failure.

    # PARENT:
        *   FormationException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERR_CODE = "FORMATION_DEBUG_ERROR"
    MSG = "A FormationDebugException was raised."