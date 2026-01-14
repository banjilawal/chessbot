# src/chess/persona/key/validator/exception/debug/zero.py

"""
Module: chess.persona.key.validator.exception.debug.zero
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.persona import PersonaKeyException

__all__ = [
    # ========================= ZERO_PERSONA_KEYS EXCEPTION =========================#
    "ZeroPersonaKeysException"
]


# ========================= ZERO_PERSONA_KEYS EXCEPTION =========================#
class ZeroPersonaKeysException(PersonaKeyException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed PersonaKey validation because no attribute was enabled.

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
    ERROR_CODE = "ZERO_PERSONA_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = (
        "PersonaKey validation failed: All attributes were null. One attribute should be enabled."
    )
