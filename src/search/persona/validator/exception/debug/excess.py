# src/logic/persona/key/validation/exception/debug/excess.py

"""
Module: logic.persona.key.validation.exception.debug.excess
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from logic.system import ContextFlagCountException
from logic.persona import PersonaKeyException

__all__ = [
    # ========================= ARENA_PERSONA_KEY EXCEPTION =========================#
    "ArenaPersonaKeysException"
]


# ========================= ARENA_PERSONA_KEY EXCEPTION =========================#
class ArenaPersonaKeysException(PersonaKeyException, ContextFlagCountException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a rank failed PersonaKey validation because more than one attribute was enabled.

    Super Class:
        *   ContextFlagCountException
        *   PersonaKeyException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ARENA_PERSONA_KEY_EXCEPTION"
    MSG = (
        "PersonaKey validation failed: More than one attribute is not-null. Only one attribute should be enabled."
    )
