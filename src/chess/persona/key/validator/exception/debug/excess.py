# src/chess/persona/key/validator/exception/debug/excess.py

"""
Module: chess.persona.key.validator.exception.debug.excess
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.persona import PersonaKeyException

__all__ = [
    # ========================= EXCESSIVE_PERSONA_KEY EXCEPTION =========================#
    "ExcessivePersonaKeysException"
]


# ========================= EXCESSIVE_PERSONA_KEY EXCEPTION =========================#
class ExcessivePersonaKeysException(PersonaKeyException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed PersonaKey validation because more than one attribute was enabled.

    # PARENT:
        *   ContextFlagCountException
        *   PersonaKeyException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESSIVE_PERSONA_KEY_ERROR"
    DEFAULT_MESSAGE = (
        "PersonaKey validation failed: More than one attribute is not-null. Only one attribute should be enabled."
    )
