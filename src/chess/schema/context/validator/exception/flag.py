# src/chess/schema/lookup/context/validator/exception/flag.py

"""
Module: chess.schema.lookup.context.validator.exception.flag
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.schema import InvalidSchemaContextException

__all__ = [
    # ========================= NO_SCHEMA_CONTEXT_FLAG EXCEPTION =========================#
    "ZeroSchemaContextFlagsException",
    # ========================= TOO_MANY_SCHEMA_CONTEXT_FLAGS EXCEPTION =========================#
    "ExcessiveSchemaContextFlagsException"
]


# ========================= NO_SCHEMA_CONTEXT_FLAG EXCEPTION =========================#
class ZeroSchemaContextFlagsException(InvalidSchemaContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate no SchemaContext flag is provided for a Schema lookup.

    # PARENT:
        *   InvalidSchemaContextException
        *   ContextFlagCountException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_SCHEMA_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = "No SchemaContext flag was selected. A context flag must be turned on with a target value."


# ========================= TOO_MANY_TEAMS_CHEMA_CONTEXT_FLAGS EXCEPTION =========================#
class ExcessiveSchemaContextFlagsException(InvalidSchemaContextException, ContextFlagCountException):
    """
    # ROLE: ContextFlagException, SchemaContextException

    # RESPONSIBILITIES:
    1.  Indicate if more than one Schema attribute is going to be used in a Schema lookup.

    # PARENT:
        *   InvalidSchemaContextException
        *   ContextFlagCountException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOO_MANY_SCHEMA_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "More than one SchemaContext flag was selected. Only one context flag is allowed."
