# src/chess/persona/key/validator/exception/debug/null.py

"""
Module: chess.persona.key.validator.exception.debug.null
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import NullException
from chess.persona import PersonaSuperKeyException

__all__ = [
    # ======================# NULL_PERSON_SUPER_KEY EXCEPTION #======================#
    "NullPersonaSuperKeyException",
]


# ======================# NULL_PERSON_SUPER_KEY EXCEPTION #======================#
class NullPersonaSuperKeyException(PersonaSuperKeyException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that PersonSuperKey validation failed because the candidate was null.

    # PARENT:
        *   NullException
        *   PersonaSuperKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_PERSON_SUPER_KEY_ERROR"
    DEFAULT_MESSAGE = "PersonSuperKey validation failed: The candidate was null."