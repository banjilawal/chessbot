# src/logic/persona/key/validation/exception/debug/null.py

"""
Module: logic.persona.key.validation.exception.debug.null
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from logic.system import NullException
from catalog.persona import PersonaKeyException

__all__ = [
    # ======================# NULL_PERSON_KEY EXCEPTION #======================#
    "NullPersonaKeyException",
]


# ======================# NULL_PERSON_KEY EXCEPTION #======================#
class NullPersonaKeyException(PersonaKeyException, NullException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that PersonKey validation failed because the rank was null.

    Super Class:
        *   NullException
        *   PersonaKeyException

    Provides:

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "NULL_PERSON_KEY_EXCEPTION"
    MSG = "PersonKey validation failed: The rank was null."