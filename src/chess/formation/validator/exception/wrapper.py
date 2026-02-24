# src/chess/formation/validator/exception/wrapper.py

"""
Module: chess.formation.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""

from chess.system import ValidationException

__all__ = [
    # ======================# FORMATION_VALIDATION_FAILURE #======================#
    "FormationValidationException",
]


# ======================# FORMATION_VALIDATION_FAILURE #======================#
class FormationValidationException(ValidationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in FormationValidator.validate that, prevented ValidationResult.success() 
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
    ERROR_CODE = "FORMATION_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Formation validation failed."