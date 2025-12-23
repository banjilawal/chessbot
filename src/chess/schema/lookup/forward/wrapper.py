# src/chess/schema/lookup/exception/failure.py

"""
Module: chess.schema.lookup.exception.failure
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""





__all__ = [
    # ======================# FORWARD_SCHEMA_LOOKUP_FAILED EXCEPTION #======================#
    "ForwardSchemaFailedException",
]

from chess.schema import SchemaException
from chess.system import ForwardLookupFailedException


# ======================# FORWARD_SCHEMA_LOOKUP_FAILED EXCEPTION #======================#
class ForwardSchemaFailedException(SchemaException, ForwardLookupFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wrap an exception that hits the try-finally block of a ForwardSchemaLookuo method.

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
    ERROR_CODE = "FORWARD_SCHEMA_LOOKUP_FAILED"
    DEFAULT_MESSAGE = "ForwardSchemaLookup operation failed."

