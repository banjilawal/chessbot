# src/chess/system/collection/operation/search/exception/wrapper.py

"""
Module: chess.system.collection.operation.search.exception.wrapper
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import OperationFailedException

__all__ = [
    # ======================# SEARCH_FAILURE EXCEPTION #======================#
    "SearchFailedException",
]


#======================# SEARCH_FAILURE EXCEPTION #======================#
class SearchFailedException(OperationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Indicate that an exception prevented a search operation from completing successfully.
    2.  Wrap an exception that hits the try-finally block of a Search method.
  
    # PARENT:
        *   SearchException
        *   OperationFailedException
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SEARCH_FAILED_ERROR"
    DEFAULT_MESSAGE = "search failed. An exception prevented the search from completing."
