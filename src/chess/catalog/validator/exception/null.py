# src/chess/persona/validator/exception/null.py

"""
Module: chess.persona.validator.exception.null
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import NullException
from chess.persona import InvalidPersonaException


__all__ = [
    # ======================# NULL PERSONA EXCEPTION #======================#
    "NullPersonaException",
]


# ======================# NULL PERSONA EXCEPTION #======================#
class NullPersonaException(InvalidPersonaException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an Persona validation candidate is null.
    2.  Raised if an entity, method or operation requires an Persona but receives null instead.

    # PARENT:
        *   InvalidPersonaException
        *   NullException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_ORDER_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "Persona cannot be null."
