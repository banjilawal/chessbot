# src/chess/schema/lookup/exception/failure.py

"""
Module: chess.schema.lookup.exception.failure
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema import SchemaSuperKeyException
from chess.system import OperationFailedException



__all__ = [
    # ======================# CHEMA_LOOKUP_OPERATION_FAILED EXCEPTION #======================#
    "SchemaLookupFailedException",
]

# ======================# SCHEMA_LOOKUP_OPERATION_FAILED EXCEPTION #======================#
class SchemaLookupFailedException(SchemaLookupException, OperationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wrap an exception that hit the try-finally block of a SchemaLookup method.

    # PARENT:
        *   SchemaLookupException
        *   OperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "_SCHEMA_LOOKUP_OPERATION_ERROR"
    DEFAULT_MESSAGE = "SchemaLookup operation failed."

