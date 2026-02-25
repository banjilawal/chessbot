# src/chess/persona/validator/exception/wrapper.py

"""
Module: chess.persona.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""

from chess.system import ValidationException

__all__ = [
    # ======================# PERSONA_VALIDATION_FAILURE #======================#
    "PersonaValidationException",
]


# ======================# PERSONA_VALIDATION_FAILURE #======================#
class PersonaValidationException(ValidationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in PersonaValidator.validate that, prevented A successful validation result 
        from being returned.

    # PARENT:
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PERSONA_VALIDATION_FAILURE"
    MSG = "Persona validation failed."