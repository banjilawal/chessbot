# src/chess/system/find/exception/operation.py

"""
Module: chess.system.find.exception.operation
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import FinderException, OperationFailedException

__all__ = [
    # ======================# SEARCH_OPERATION_FAILED EXCEPTION #======================#
    "SearchOperationFailedException",
]

# ======================# SEARCH_OPERATION_FAILED EXCEPTION #======================#
class SearchOperationFailedException(FinderException, OperationFailedException):
    """
    # ROLE: Error Tracing, Debugging, Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Catch all for when a search encounters an error.
    2.  Indicates a search failed to produce either an empty or success result.

    # PARENT:
        *   FinderException
        *   OperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SEARCH_OPERATION_ERROR"
    DEFAULT_MESSAGE = "Search operation raised an exception."