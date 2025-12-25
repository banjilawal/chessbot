# src/chess/formation/validator/exception/null.py

"""
Module: chess.formation.validator.exception.null
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import NullException
from chess.formation import InvalidFormationSuperKeyException

__all__ = [
    # ======================# NULL_FORMATION_SUPER_KEY EXCEPTION #======================#
    "NullFormationSuperKeyException",
]


# ======================# NULL_FORMATION_SUPER_KEY EXCEPTION #======================#
class NullFormationSuperKeyException(InvalidFormationSuperKeyException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an OrderContext validation candidate is null.

    # PARENT:
        *   NullException
        *   InvalidFormationSuperKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_FORMATION_SUPER_KEY_ERROR"
    DEFAULT_MESSAGE = "FormationSuperKey cannot be null."