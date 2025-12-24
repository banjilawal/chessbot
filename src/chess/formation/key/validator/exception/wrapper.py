# src/chess/formation/validator/exception/base.py

"""
Module: chess.formation.validator.exception.base
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.formation import FormationSuperKeyException, OrderContextException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# FORMATION_SUPER_KEY_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidFormationSuperKeyException",
]


# ======================# FORMATION_SUPER_KEY_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidFormationSuperKeyException(FormationSuperKeyException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a FormationSuperKey candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an InvalidFormationSuperKeyException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The InvalidFormationSuperKeyException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   FormationSuperKeyException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FORMATION_SUPER_KEY_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "FormationSuperKey validation failed."