# src/chess/formation/validator/exception/base.py

"""
Module: chess.formation.validator.exception.base
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""


from chess.formation import FormationException
from chess.system import ValidationException

_
__all__ = [
    # ======================# FORMATION_VALIDATION_FAILURE #======================#
    "FormationValidationException",
]


# ======================# FORMATION_VALIDATION_FAILURE #======================#
class FormationValidationException(FormationException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a Formation. The exception chain traces the ultimate source of failure.
    
    # PARENT:
        *   FormationException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FORMATION_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Formation validation failed."