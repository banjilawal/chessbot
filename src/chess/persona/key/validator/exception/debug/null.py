# src/chess/persona/key/validator/exception/null.py

"""
Module: chess.persona.key.validator.exception.null
Author: Banji Lawal
Created: 2025-09-08
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
    1.  Indicate that FormationSuperKey validation failed because the candidate was null.

    # PARENT:
        *   NullException
        *   InvalidFormationSuperKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_FORMATION_SUPER_KEY_ERROR"
    DEFAULT_MESSAGE = "FormationSuperKey validation failed: The candidate was null."