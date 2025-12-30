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
    1.  Indicate that a FormationSuperKey failed its safety certification because more than one attribute was enabled
        with a value.
    # a forward Formation lookup failed because more than one FormationSuperKey attribute was not null.

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
        "FormationSuperKey validation failed: More than one attribute is not-null. A FormationSuperKey can only have a "
        "single attribute enabled by a value."
    )