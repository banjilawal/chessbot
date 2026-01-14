# src/chess/formation/validator/exception/debug/zero.py

"""
Module: chess.formation.validator.exception.debug.zero
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

__all__ = [
    # ========================= ZERO_FORMATION_KEYS_VALIDATION EXCEPTION =========================#
    "ZeroFormationSuperKeysException",
]

from chess.formation.key.validator.exception.wrapper import InvalidFormationSuperKeyException
from chess.system import ContextFlagCountException


# ========================= ZERO_FORMATION_KEYS_VALIDATION EXCEPTION =========================#
class ZeroFormationSuperKeysException(InvalidFormationSuperKeyException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a FormationKey failed its safety certification because no attribute was enabled with a value.
    # 1.  Indicate that forward Formation lookup failed because all the FormationKey attributes were null.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidFormationSuperKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_FORMATION_KEYS_VALIDATION_ERROR"
    DEFAULT_MESSAGE = (
        "FormationKey validation failed: All attributes are null. A FormationKey must have a "
        "single attribute enabled by a value."
    )