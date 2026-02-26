# src/chess/formation/key/validator/exception/debug/excess.py

"""
Module: chess.formation.key.validator.exception.debug.excess
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.formation import FormationKeyException
from chess.system import ContextFlagCountException

__all__ = [
    # ========================= EXCESS_FORMATION_KEYS_VALIDATION EXCEPTION =========================#
    "ArenaFormationKeysException",
]


# ========================= EXCESS_FORMATION_KEYS_VALIDATION EXCEPTION =========================#
class ArenaFormationKeysException(FormationKeyException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed FormationKey validation because more than one attribute was enabled.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidFormationKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "EXCESS_FORMATION_KEYS_VALIDATION_ERROR"
    MSG = (
        "FormationKey validation failed: More than one attribute is not-null.Only ond attribute should be enabled."
    )