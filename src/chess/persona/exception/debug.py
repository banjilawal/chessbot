# src/chess/persona/exception/debug.py

"""
Module: chess.persona.exception.debug
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""


__all__ = [
    # ======================# PERSONA_DEBUG EXCEPTION #======================#
    "PersonaDebugException",
]

from chess.persona import PersonaException
from chess.system import DebugException


# ======================# PERSONA_DEBUG EXCEPTION #======================#
class PersonaDebugException(PersonaException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Persona operation failure.

    # PARENT:
        *   PersonaException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERR_CODE = "PERSONA_DEBUG_ERROR"
    MSG = "A PersonaDebugException was raised."