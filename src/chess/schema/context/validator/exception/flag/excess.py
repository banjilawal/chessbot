# src/chess/schema/context/validator/exception/flag/excess.py

"""
Module: chess.schema.context.validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.schema import InvalidSchemaContextException

__all__ = [
    # ========================= TOO_MANY_SCHEMA_CONTEXT_FLAGS EXCEPTION =========================#
    "ExcessiveSchemaContextFlagsException",
]

# ========================= EXCESS_SCHEMA_CONTEXT_FLAGS EXCEPTION =========================#
class ExcessiveSchemaContextFlagsException(InvalidSchemaContextException, ContextFlagCountException):
    """
    # ROLE: ContextFlagException, SchemaContextException

    # RESPONSIBILITIES:
    1.  Indicate more than one SchemaContext flag was provided for a Schema lookup.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidSchemaContextException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESS_SCHEMA_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = (
        "More than one SchemaContext flag was enabled. A forward schema_entry lookup can only be performed with "
        "one and only one attribute-value-tuple."
    )