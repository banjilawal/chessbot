# src/chess/catalog/validator/exception/flag/zero.py

"""
Module: chess.catalog.validator.exception.flag.zero
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.catalog import InvalidPersonaSuperKeyException

__all__ = [
    # ========================= ZERO_PERSONA_SUPER_KEYS_VALIDATION EXCEPTION =========================#
    "ZeroPersonaSuperKeysException",
]


# ========================= ZERO_PERSONA_SUPER_KEYS_VALIDATION EXCEPTION =========================#
class ZeroPersonaSuperKeysException(InvalidPersonaSuperKeyException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a PersonaSuperKey failed its safety certification because no attribute was enabled with a value.
    # 1.  Indicate that forward Persona lookup failed because all the PersonaSuperKey attributes were null.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidPersonaSuperKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_PERSONA_SUPER_KEYS_VALIDATION_ERROR"
    DEFAULT_MESSAGE = (
        "PersonaSuperKey validation failed: All attributes are null. A PersonaSuperKey must have a "
        "single attribute enabled by a value."
    )