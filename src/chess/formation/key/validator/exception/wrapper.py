# src/chess/formation/validator/exception/base.py

"""
Module: chess.formation.validator.exception.base
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.formation import FormationKeyException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# FORMATION_KEY_VALIDATION_FAILURE EXCEPTION #======================#
    "FormationKeyValidationFailedException",
]


# ======================# FORMATION_KEY_VALIDATION_FAILURE EXCEPTION #======================#
class FormationKeyValidationFailedException(FormationKeyException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a FormationKey candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an FormationKeyValidationFailedException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The FormationKeyValidationFailedException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   FormationKeyException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FORMATION_KEY_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "FormationKey validation failed."