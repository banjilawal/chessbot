# src/logic/schema/key/lookup/exception/validator.py

"""
Module: logic.schema.key.lookup.exception.work
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""





__all__ = [
    # ======================# SCHEMA_LOOKUP_FAILURE #======================#
    "SchemaLookupFailedException",
]

from catalog.schema import SchemaException
from system import ForwardLookupFailedException


# ======================# SCHEMA_LOOKUP_FAILURE #======================#
class SchemaLookupFailedException(SchemaException, ForwardLookupFailedException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Wrap an exception that hits the try-finally block of a SchemaLookupProcess method.

    Super Class:
        *   SchemaException
        *   ForwardLookupFailedException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SCHEMA_LOOKUP_FAILED"
    MSG = "SchemaLookupProcess failed."
