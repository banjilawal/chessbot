# src/chess/formation/validator/exception/debug/null.py

"""
Module: chess.formation.validator.exception.debug.null
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import NullException
from chess.formation import FormationSuperKeyException

__all__ = [
    # ======================# NULL_FORMATION_SUPER_KEY EXCEPTION #======================#
    "NullFormationSuperKeyException",
]


# ======================# NULL_FORMATION_SUPER_KEY EXCEPTION #======================#
class NullFormationSuperKeyException(FormationSuperKeyException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that FormationSuperKey validation failed because the candidate was null.

    # PARENT:
        *   NullException
        *   FormationSuperKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_FORMATION_SUPER_KEY_ERROR"
    DEFAULT_MESSAGE = "FormationSuperKey validation failed: The candidate was null."