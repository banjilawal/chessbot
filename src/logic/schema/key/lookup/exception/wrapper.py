# src/logic/schema/key/lookup/exception/worker.py

"""
Module: logic.schema.key.lookup.exception.wrapper
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""





__all__ = [
    # ======================# SCHEMA_LOOKUP_FAILURE #======================#
    "SchemaLookupFailedException",
]

from logic.schema import SchemaException
from logic.system import ForwardLookupFailedException


# ======================# SCHEMA_LOOKUP_FAILURE #======================#
class SchemaLookupFailedException(SchemaException, ForwardLookupFailedException):
    """
    Role:Exception Wrapper

    Responsibilities:
    1.  Wrap an exception that hits the try-finally block of a SchemaLookup method.

    Super Class:
        *   SchemaException
        *   ForwardLookupFailedException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SCHEMA_LOOKUP_FAILED"
    MSG = "SchemaLookup failed."
