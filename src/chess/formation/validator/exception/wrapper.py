# src/chess/formation/validator/exception/base.py

"""
Module: chess.formation.validator.exception.base
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""


from chess.formation import FormationException
from chess.system import ValidationFailedException

_
__all__ = [
    # ======================# FORMATION_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidFormationException",
]


# ======================# FORMATION_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidFormationException(FormationException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a Formation candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an InvalidFormationException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The InvalidFormationException chain is useful for tracing a  failure to its source.
    
    # PARENT:
        *   FormationException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FORMATION_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Formation validation failed."