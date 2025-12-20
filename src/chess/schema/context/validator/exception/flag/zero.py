# src/chess/schema/context/validator/exception/flag/zero.py

"""
Module: chess.schema.context.validator.exception.flag.zero
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.schema import InvalidSchemaContextException

__all__ = [
    # ========================= ZERO_SCHEMA_CONTEXT_FLAGS EXCEPTION =========================#
    "ZeroSchemaContextFlagsException",
]


# ========================= ZERO_SCHEMA_CONTEXT_FLAGS EXCEPTION =========================#
class ZeroSchemaContextFlagsException(InvalidSchemaContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate no SchemaContext flag is provided for a Schema lookup.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidSchemaContextException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_SCHEMA_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = (
        "No SchemaContext flag was selected. A SchemaContext must be enabled with an attribute-value-tuple is "
        "required for a forward schema_entry lookup."
    )