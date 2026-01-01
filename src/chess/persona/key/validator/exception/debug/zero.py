# src/chess/persona/key/validator/exception/debug/zero.py

"""
Module: chess.persona.key.validator.exception.debug.zero
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.persona import PersonaSuperKeyException

__all__ = [
    # ========================= ZERO_PERSONA_SUPER_KEYS EXCEPTION =========================#
    "ZeroPersonaSuperKeysException"
]


# ========================= ZERO_PERSONA_SUPER_KEYS EXCEPTION =========================#
class ZeroPersonaSuperKeysException(PersonaSuperKeyException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed PersonaSuperKey validation because no attribute was enabled.

    # PARENT:
        *   ContextFlagCountException
        *   PersonaSuperKeyException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_PERSONA_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = (
        "PersonaSuperKey validation failed: All attributes were null. One attribute should be enabled."
    )
