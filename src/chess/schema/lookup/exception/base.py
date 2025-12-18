# src/chess/schema/lookup/exception.base.py

"""
Module: chess.schema.lookup.exception.base
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""


from chess.schema import SchemaException

__all__ = [
    # ======================# SCHEMA_LOOKUP EXCEPTION #======================#
    "SchemaLookupException",
]


# ======================# SCHEMA_LOOKUP EXCEPTION #======================#
class SchemaLookupException(SchemaException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by SchemaLookup objects.
    2.  Wraps unhandled exceptions that hit the try-finally block of a SchemaLookup method.

    # PARENT:
        *   SchemaException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_LOOKUP_ERROR"
    DEFAULT_MESSAGE = "SchemaLookup raised an exception."