# src/chess/formation/validator/exception/base.py

"""
Module: chess.formation.validator.exception.base
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""


from chess.formation import FormationException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# FORMATION_VALIDATION EXCEPTION #======================#
    "InvalidFormationException",
]


# ======================# FORMATION_VALIDATION EXCEPTION #======================#
class InvalidFormationException(FormationException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during an Formation verification process.
    2.  Catchall Exception for BattleOrderValidator when a candidate fails a sanity check.
    3.  Wrap an exception that hits the try-finally block of an BattleOrderValidator method.

    # PARENT:
        *   FormationException
        *   ValidationFailedException

    # PROVIDES:
    InvalidFormationException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "FORMATION_VALIDATION"
    DEFAULT_MESSAGE = "Formation validation failed."