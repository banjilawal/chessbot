# src/chess/persona/key/validator/exception/flag/zero.py

"""
Module: chess.persona.key.validator.exception.flag.zero
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.persona import InvalidPersonaSuperKeyException

__all__ = [
    # ========================= ZERO_PERSONA_SUPER_KEYS EXCEPTION =========================#
    "ZeroPersonaSuperKeysException"
]


# ========================= ZERO_PERSONA_SUPER_KEYS EXCEPTION =========================#
class ZeroPersonaSuperKeysException(InvalidPersonaSuperKeyException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  no CatalogContext flag was enabled. One and only one Persona attribute-value tuple is required for
        a search.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidPersonaSuperKeyException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_CATALOG_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "Zero CatalogContext flags were set. One and only one map flag must be enabled,"
