# src/chess/persona/validator/exception/base.py

"""
Module: chess.persona.validator.exception.base
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.persona import PersonaException
from chess.system import ValidationException

_
__all__ = [
    # ======================# PERSONA_VALIDATION_FAILURE #======================#
    "PersonaValidationException",
]


# ======================# PERSONA_VALIDATION_FAILURE #======================#
class PersonaValidationException(PersonaException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a Persona. The exception chain traces the ultimate source of failure.
    
    # PARENT:
        *   PersonaException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PERSONA_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Persona validation failed."