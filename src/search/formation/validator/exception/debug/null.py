# src/logic/formation/validation/exception/debug/null.py

"""
Module: logic.formation.validation.exception.debug.null
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from logic.system import NullException
from catalog.formation import FormationKeyException

__all__ = [
    # ======================# NULL_FORMATION_KEY EXCEPTION #======================#
    "NullFormationKeyException",
]


# ======================# NULL_FORMATION_KEY EXCEPTION #======================#
class NullFormationKeyException(FormationKeyException, NullException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that FormationKey validation failed because the rank was null.

    Super Class:
        *   NullException
        *   FormationKeyException

    Provides:

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "NULL_FORMATION_KEY_EXCEPTION"
    MSG = "FormationKey validation failed: The rank was null."