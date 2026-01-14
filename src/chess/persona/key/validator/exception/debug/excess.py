# src/chess/persona/key/validator/exception/debug/excess.py

"""
Module: chess.persona.key.validator.exception.debug.excess
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.persona import PersonaSuperKeyException

__all__ = [
    # ========================= EXCESSIVE_PERSONA_KEY EXCEPTION =========================#
    "ExcessivePersonaSuperKeysException"
]


# ========================= EXCESSIVE_PERSONA_KEY EXCEPTION =========================#
class ExcessivePersonaSuperKeysException(PersonaSuperKeyException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed PersonaSuperKey validation because more than one attribute was enabled.

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
    ERROR_CODE = "EXCESSIVE_PERSONA_KEY_ERROR"
    DEFAULT_MESSAGE = (
        "PersonaSuperKey validation failed: More than one attribute is not-null. Only one attribute should be enabled."
    )
