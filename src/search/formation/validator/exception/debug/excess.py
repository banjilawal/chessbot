# src/logic/formation/key/validation/exception/debug/excess.py

"""
Module: logic.formation.key.validation.exception.debug.excess
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from catalog.formation import FormationKeyException
from system import ContextFlagCountException

__all__ = [
    # ========================= EXCESS_FORMATION_KEYS_VALIDATION EXCEPTION =========================#
    "ArenaFormationKeysException",
]


# ========================= EXCESS_FORMATION_KEYS_VALIDATION EXCEPTION =========================#
class ArenaFormationKeysException(FormationKeyException, ContextFlagCountException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a rank failed FormationKey validation because more than one attribute was enabled.

    Super Class:
        *   ContextFlagCountException
        *   InvalidFormationKeyException

    Provides:

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "EXCESS_FORMATION_KEYS_VALIDATION_EXCEPTION"
    MSG = (
        "FormationKey validation failed: More than one attribute is not-null.Only ond attribute should be enabled."
    )