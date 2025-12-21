# src/chess/schema/map/validator/exception/flag/zero.py

"""
Module: chess.schema.map.validator.exception.flag.zero
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.schema import InvalidSchemaSuperKeyException



__all__ = [
    # ========================= ZERO_SCHEMA_SUPER_KEY_KEYS EXCEPTION =========================#
    "ZeroSchemaMapKeysException",
]



# ========================= ZERO_SCHEMA_SUPER_KEY_KEYS EXCEPTION =========================#
class ZeroSchemaMapKeysException(InvalidSchemaSuperKeyException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate no SchemaSuperKey key-value was provided to run a forward Schema lookup.
    1.  Indicate more than one SchemaSuperKey key-value was provided for a Schema entry lookup.
    # PARENT:
        *   ContextFlagCountException
        *   InvalidSchemaSuperKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_SCHEMA_SUPER_KEY_KEYS_ERROR"
    DEFAULT_MESSAGE = (
        "No SchemaSuperKey key-value was provided. A single key-value pair must be provided to run a forward Schema "
        "entry lookup."
    )