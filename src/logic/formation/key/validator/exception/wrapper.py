# src/logic/formation/validator/exception/base.py

"""
Module: logic.formation.validator.exception.base
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from logic.formation import FormationKeyException
from logic.system import ValidationException

__all__ = [
    # ======================# FORMATION_KEY_VALIDATION_FAILURE #======================#
    "FormationKeyValidationException",
]


# ======================# FORMATION_KEY_VALIDATION_FAILURE #======================#
class FormationKeyValidationException(FormationKeyException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a FormationKey candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an FormationKeyValidationException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The FormationKeyValidationException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   FormationKeyException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "FORMATION_KEY_VALIDATION_FAILURE"
    MSG = "FormationKey validation failed."