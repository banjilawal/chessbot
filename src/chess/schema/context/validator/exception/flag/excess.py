# src/chess/schema/context/validator/exception/flag/excess.py

"""
Module: chess.schema.context.validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.schema import InvalidSchemaMapException

__all__ = [
    # ========================= EXCESS_SCHEMA_MAP_KEYS EXCEPTION =========================#
    "ExcessiveSchemaMapKeysException",
]

# ========================= EXCESS_SCHEMA_MAP_KEYS EXCEPTION =========================#
class ExcessiveSchemaMapKeysException(InvalidSchemaMapException, ContextFlagCountException):
    """
    # ROLE: ContextFlagException, SchemaContextException

    # RESPONSIBILITIES:
    1.  Indicate more than one SchemaMap key-value was provided for a Schema entry lookup.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidSchemaMapException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESS_SCHEMA_MAP_KEYS_ERROR"
    DEFAULT_MESSAGE = (
        "More than one SchemaMap flag was enabled. A forward schema_entry lookup can only be performed with "
        "one and only one attribute-value-tuple."
    )