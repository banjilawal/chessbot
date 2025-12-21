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
    # ROLE: ContextFlagException, SchemaSuperKeyException

    # RESPONSIBILITIES:
    1.  Indicate more than one SchemaSuperKey was provided to process a forward Schema lookup.

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
        "More than one SchemaSuperKey was set. A forward schema_entry lookup can only be performed with "
        "one and only one SuperKey."
    )