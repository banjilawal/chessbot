# src/chess/system/metadata/lookup/exception.py

"""
Module: chess.system.metadata.lookup.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException, OperationFailedException

__all__ = [
    # ======================# FAILED METADATA LOOKUP OPERATION EXCEPTION #======================#
    "LookupFailedException",
]


# ======================# FAILED METADATA LOOKUP OPERATION EXCEPTION #======================#
class LookupFailedException(ChessException, OperationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by MetadataLookup objects.
    2.  Wraps unhandled exceptions that hit the try-finally block of a Metadata method.

    # PARENT:
        *   LookuperException
        *   OperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FAILED_METADATA_LOOKUP_ERROR"
    DEFAULT_MESSAGE = "Metadata lookup failed."