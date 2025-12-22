# src/chess/system/find/exception/failure.py

"""
Module: chess.system.find.exception.failure
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import OperationFailedException, SearchException

__all__ = [
    # ======================# SEARCH_FAILED #======================#
    "SearchFailedException",
]


#======================# SEARCH_FAILED #======================#
class SearchFailedException(SearchException, OperationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Indicates an exception prevented a search operation from completing successfully.
    2.  Wraps exceptions that hit the try-finally block of a Search method.
  
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
