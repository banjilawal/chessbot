# src/chess/persona/key/validator/exception/wrapper.py

"""
Module: chess.persona.key.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# PERSONA_KEY_VALIDATION_FAILURE EXCEPTION #======================#
    "PersonaKeyValidationFailedException",
]

from chess.persona import PersonaKeyException
from chess.system import ValidationFailedException


# ======================# PERSONA_KEY_VALIDATION_FAILURE EXCEPTION #======================#
class PersonaKeyValidationFailedException(PersonaKeyException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a PersonaKey candidate fails a validation test. Validation debug
        exceptions are encapsulated inside an PersonaKeyValidationFailedException creating an exception chain.
        which is sent to the caller in a ValidationResult.
    2.  The PersonaKeyValidationFailedException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   PersonaKeyException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PERSONA_KEY_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "PersonaKey validation failed."