# src/logic/formation/validator/exception/debug/zero.py

"""
Module: logic.formation.validator.exception.debug.zero
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

__all__ = [
    # ========================= ZERO_FORMATION_KEYS_VALIDATION EXCEPTION =========================#
    "ZeroFormationKeysException",
]

from logic.formation.key.validator.exception.wrapper import InvalidFormationKeyException
from logic.system import ContextFlagCountException


# ========================= ZERO_FORMATION_KEYS_VALIDATION EXCEPTION =========================#
class ZeroFormationKeysException(InvalidFormationKeyException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a FormationKey failed its safety certification because no attribute was enabled with a value.
    # 1.  Indicate that forward Formation lookup failed because all the FormationKey attributes were null.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidFormationKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "ZERO_FORMATION_KEYS_VALIDATION_EXCEPTION"
    MSG = (
        "FormationKey validation failed: All attributes are null. A FormationKey must have a "
        "single attribute enabled by a value."
    )