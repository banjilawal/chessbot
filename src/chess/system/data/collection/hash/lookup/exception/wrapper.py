# src/chess/system/data/collection/hash/lookup/exception/wrapper.py

"""
Module: chess.system.data.collection.hash.lookup.exception.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import OperationFailedException

__all__ = [
    # ======================# LOOKUP_FAILURE EXCEPTION #======================#
    "LookupFailedException",
]


# ======================# LOOKUP_FAILURE EXCEPTION #======================#
class LookupFailedException(OperationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by Lookup operations.
    3.  Catchall for Metadata errors not covered by lower level LookupFailedExceptions.
  
    # PARENT:
        *   LookupException
        *   OperationFailedException
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
    None
  
    # INHERITED ATTRIBUTES:
    None
    """
    DEFAULT_CODE = "LOOKUP_FAILED_ERROR"
    DEFAULT_MESSAGE = "Lookup failed."