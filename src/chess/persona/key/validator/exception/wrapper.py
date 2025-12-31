# src/chess/persona/key/validator/exception/wrapper.py

"""
Module: chess.persona.key.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# PERSONA_SUPER_KEY_VALIDATION_FAILURE EXCEPTION #======================#
    "PersonaSuperKeyValidationFailedException",
]

from chess.persona import PersonaSuperKeyException
from chess.system import ValidationFailedException


# ======================# PERSONA_SUPER_KEY_VALIDATION_FAILURE EXCEPTION #======================#
class PersonaSuperKeyValidationFailedException(PersonaSuperKeyException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a PersonaSuperKey candidate fails a validation test. Validation debug 
        exceptions are encapsulated inside an PersonaSuperKeyValidationFailedException creating an exception chain. 
        which is sent to the caller in a ValidationResult.
    2.  The PersonaSuperKeyValidationFailedException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   PersonaSuperKeyException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PERSONA_SUPER_KEY_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "PersonaSuperKey validation failed."