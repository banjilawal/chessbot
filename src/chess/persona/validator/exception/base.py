# src/chess/persona/validator/exception/base.py

"""
Module: chess.persona.validator.exception.base
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.persona import PersonaException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# PERSONA_CONTEXT VALIDATION EXCEPTION #======================#
    "InvalidPersonaException",
]


# ======================# PERSONA VALIDATION EXCEPTION #======================#
class InvalidPersonaException(PersonaException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by PersonaValidation objects.
    2.  Wrap an exception that hits the try-finally-block in PersonaValidator methods.

    # PARENT:
        *   PersonaException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "_PERSONA_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Persona validation failed."