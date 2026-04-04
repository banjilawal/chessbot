# src/logic/persona/key/validation/exception/validator.py

"""
Module: logic.persona.key.validation.exception.work
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# PERSONA_KEY_VALIDATION_FAILURE #======================#
    "PersonaKeyValidationException",
]

from catalog.persona import PersonaKeyException
from logic.system import ValidationException


# ======================# PERSONA_KEY_VALIDATION_FAILURE #======================#
class PersonaKeyValidationException(PersonaKeyException, ValidationException):
    """
    Role:Exception Work

    Responsibilities:
    1.  A debug exception is created when a PersonaKey rank fails a validation test. Validation debug
        exceptions are encapsulated inside an PersonaKeyValidationException creating an exception chain.
        which is sent to the caller in a ValidationResult.
    2.  The PersonaKeyValidationException chain is useful for tracing a  failure to its source.

    Super Class:
        *   PersonaKeyException
        *   ValidationException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PERSONA_KEY_VALIDATION_FAILURE"
    MSG = "PersonaKey validation failed."