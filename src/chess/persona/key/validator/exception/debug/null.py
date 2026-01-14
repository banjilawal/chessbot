# src/chess/persona/key/validator/exception/debug/null.py

"""
Module: chess.persona.key.validator.exception.debug.null
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import NullException
from chess.persona import PersonaKeyException

__all__ = [
    # ======================# NULL_PERSON_KEY EXCEPTION #======================#
    "NullPersonaKeyException",
]


# ======================# NULL_PERSON_KEY EXCEPTION #======================#
class NullPersonaKeyException(PersonaKeyException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that PersonKey validation failed because the candidate was null.

    # PARENT:
        *   NullException
        *   PersonaKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_PERSON_KEY_ERROR"
    DEFAULT_MESSAGE = "PersonKey validation failed: The candidate was null."