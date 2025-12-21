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
    # ========================= EXCESS_SCHEMA_SUPER_KEY_KEYS EXCEPTION =========================#
    "ExcessiveSchemaMapKeysException",
]

# ========================= EXCESS_SCHEMA_SUPER_KEY_KEYS EXCEPTION =========================#
class ExcessiveSchemaMapKeysException(InvalidSchemaSuperKeyException, ContextFlagCountException):
    """
    # ROLE: ContextFlagException, SchemaSuperKeyException

    # RESPONSIBILITIES:
    1.  Indicate more than one SchemaSuperKey key-value was provided for a Schema entry lookup.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidSchemaSuperKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESS_SCHEMA_SUPER_KEY_KEYS_ERROR"
    DEFAULT_MESSAGE = (
        "More than one SchemaSuperKey flag was enabled. A forward schema_entry lookup can only be performed with "
        "one and only one attribute-value-tuple."
    )