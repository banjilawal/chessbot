# src/chess/formation/key/validator/exception/debug/excess.py

"""
Module: chess.formation.key.validator.exception.debug.excess
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.formation import FormationSuperKeyException
from chess.system import ContextFlagCountException

__all__ = [
    # ========================= EXCESS_FORMATION_SUPER_KEYS_VALIDATION EXCEPTION =========================#
    "ExcessiveFormationSuperKeysException",
]


# ========================= EXCESS_FORMATION_SUPER_KEYS_VALIDATION EXCEPTION =========================#
class ExcessiveFormationSuperKeysException(FormationSuperKeyException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed FormationSuperKey validation because more than one attribute was enabled.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidFormationSuperKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESS_FORMATION_SUPER_KEYS_VALIDATION_ERROR"
    DEFAULT_MESSAGE = (
        "FormationSuperKey validation failed: More than one attribute is not-null.Only ond attribute should be enabled."
    )