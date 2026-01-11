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
    "FormationValidationFailedException",
]


# ======================# FORMATION_VALIDATION_FAILURE EXCEPTION #======================#
class FormationValidationFailedException(FormationException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why a candidate failed its validation as a Formation. The encapsulated
        exceptions create a chain for tracing the source of the failure.
    
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