# src/chess/persona/validator/exception/null.py

"""
Module: chess.persona.validator.exception.null
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_PERSONA EXCEPTION #======================#
    "NullPersonaException",
]

from chess.system import NullException
from chess.persona import PersonaDebugException


# ======================# NULL_PERSONA EXCEPTION #======================#
class NullPersonaException(PersonaDebugException, NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failing ValidationResult was returned because the validation candidate was null.

    # PARENT:
        *   PersonaDebugException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_PERSONA_ERROR"
    DEFAULT_MESSAGE = "Persona validation failed: The validation candidate cannot be null."
