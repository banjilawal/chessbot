# src/chess/system/collection/hash/lookup/exception/wrapper.py

"""
Module: chess.system.collection.hash.lookup.exception.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import OperationException

__all__ = [
    # ======================# LOOKUP_FAILURE #======================#
    "LookupException",
]


# ======================# LOOKUP_FAILURE #======================#
class LookupException(OperationException):
    """
    # ROLE: Exception Wrapper
  
    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by Lookup operations.
    3.  Catchall for Metadata errors not covered by lower level LookupFailedExceptions.
  
    # PARENT:
        *   LookupException
        *   OperationException
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
    None
  
    # INHERITED ATTRIBUTES:
    None
    """
    DEFAULT_CODE = "LOOKUP_FAILED_ERROR"
    DEFAULT_MESSAGE = "Lookup failed."