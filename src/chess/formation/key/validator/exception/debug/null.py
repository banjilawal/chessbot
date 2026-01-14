# src/chess/formation/validator/exception/debug/null.py

"""
Module: chess.formation.validator.exception.debug.null
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import NullException
from chess.formation import FormationKeyException

__all__ = [
    # ======================# NULL_FORMATION_KEY EXCEPTION #======================#
    "NullFormationKeyException",
]


# ======================# NULL_FORMATION_KEY EXCEPTION #======================#
class NullFormationKeyException(FormationKeyException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that FormationKey validation failed because the candidate was null.

    # PARENT:
        *   NullException
        *   FormationKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_FORMATION_KEY_ERROR"
    DEFAULT_MESSAGE = "FormationKey validation failed: The candidate was null."