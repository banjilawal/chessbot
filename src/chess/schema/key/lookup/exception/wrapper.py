# src/chess/schema/key/lookup/exception/wrapper.py

"""
Module: chess.schema.key.lookup.exception.wrapper
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""





__all__ = [
    # ======================# SCHEMA_LOOKUP_FAILED EXCEPTION #======================#
    "SchemaLookupFailedException",
]

from chess.schema import SchemaException
from chess.system import ForwardLookupFailedException


# ======================# SCHEMA_LOOKUP_FAILED EXCEPTION #======================#
class SchemaLookupFailedException(SchemaException, ForwardLookupFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wrap an exception that hits the try-finally block of a SchemaLookup method.

    # PARENT:
        *   SchemaException
        *   ForwardLookupFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_LOOKUP_FAILED"
    DEFAULT_MESSAGE = "SchemaLookup failed."
