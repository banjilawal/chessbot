# src/chess/persona/validator/exception/base.py

"""
Module: chess.persona.validator.exception.base
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.persona import PersonaException
from chess.system import ValidationFailedException

_
__all__ = [
    # ======================# PERSONA_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidPersonaException",
]


# ======================# PERSONA_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidPersonaException(PersonaException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a Persona candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an InvalidPersonaException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The InvalidPersonaException chain is useful for tracing a  failure to its source.
    
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
    ERROR_CODE = "PERSONA_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Persona validation failed."