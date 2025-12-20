# src/chess/schema/context/exception.py

"""
Module: chess.schema.context.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema import SchemaException
from chess.system import ContextException


__all__ = [
    # ======================# SCHEMA_CONTEXT EXCEPTION #======================#
    "SchemaContextException",
]


# ======================# SCHEMA_CONTEXT EXCEPTION #======================#
class SchemaContextException(SchemaException, ContextException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by SchemaContext objects.
    2.  Catchall for conditions which are not covered by lower level SchemaContext exception.

    # PARENT:
        *   SchemaException
        *   ContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_CONTEXT_ERROR"
    DEFAULT_ERROR_CODE = "SchemaContext raised an exception."