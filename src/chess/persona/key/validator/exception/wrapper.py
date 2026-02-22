# src/chess/persona/key/validator/exception/wrapper.py

"""
Module: chess.persona.key.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# PERSONA_KEY_VALIDATION_FAILURE #======================#
    "PersonaKeyValidationException",
]

from chess.persona import PersonaKeyException
from chess.system import ValidationException


# ======================# PERSONA_KEY_VALIDATION_FAILURE #======================#
class PersonaKeyValidationException(PersonaKeyException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a PersonaKey candidate fails a validation test. Validation debug
        exceptions are encapsulated inside an PersonaKeyValidationException creating an exception chain.
        which is sent to the caller in a ValidationResult.
    2.  The PersonaKeyValidationException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   PersonaKeyException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PERSONA_KEY_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "PersonaKey validation failed."