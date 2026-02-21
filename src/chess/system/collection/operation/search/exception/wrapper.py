# src/chess/system/collection/operation/search/exception/wrapper.py

"""
Module: chess.system.collection.operation.search.exception.wrapper
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import CollectionOperationFailedException

__all__ = [
    # ======================# SEARCH_FAILURE #======================#
    "SearchException",
]


# ======================# SEARCH_FAILURE #======================#
class SearchException(CollectionOperationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a search operation failed. The exception chain 
        traces the ultimate source of failure.

    # PARENT:
        *   OperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SEARCH_FAILURE"
    DEFAULT_MESSAGE = "Search failed."
