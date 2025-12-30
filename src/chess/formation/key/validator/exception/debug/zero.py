# src/chess/formation/validator/exception/debug/zero.py

"""
Module: chess.formation.validator.exception.debug.zero
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

__all__ = [
    # ========================= ZERO_FORMATION_SUPER_KEYS_VALIDATION EXCEPTION =========================#
    "ZeroFormationSuperKeysException",
]

from chess.formation.key.validator.exception.wrapper import InvalidFormationSuperKeyException
from chess.system import ContextFlagCountException


# ========================= ZERO_FORMATION_SUPER_KEYS_VALIDATION EXCEPTION =========================#
class ZeroFormationSuperKeysException(InvalidFormationSuperKeyException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a FormationSuperKey failed its safety certification because no attribute was enabled with a value.
    # 1.  Indicate that forward Formation lookup failed because all the FormationSuperKey attributes were null.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidFormationSuperKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_FORMATION_SUPER_KEYS_VALIDATION_ERROR"
    DEFAULT_MESSAGE = (
        "FormationSuperKey validation failed: All attributes are null. A FormationSuperKey must have a "
        "single attribute enabled by a value."
    )