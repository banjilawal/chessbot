# src/chess/schema/map/validator/exception/flag/excess.py

"""
Module: chess.schema.map.validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.schema import InvalidSchemaSuperKeyException

__all__ = [
    # ========================= EXCESS_SCHEMA_SUPER_KEYS EXCEPTION =========================#
    "ExcessiveSchemaSuperKeysException",
]

# ========================= EXCESS_SCHEMA_SUPER_KEYS EXCEPTION =========================#
class ExcessiveSchemaSuperKeysException(InvalidSchemaSuperKeyException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates a forward Schema lookup failed because more than one SchemaSuperKey attribute was not null.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidSchemaSuperKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESS_SCHEMA_SUPER_KEYS_ERROR"
    DEFAULT_MESSAGE = (
        "More than one SchemaSuperKey field is not null. A forward Schema lookup can only be performed with "
        "one and only one SuperKey attribute set."
    )