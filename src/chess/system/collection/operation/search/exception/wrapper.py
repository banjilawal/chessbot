# src/chess/system/collection/operation/search/exception/wrapper.py

"""
Module: chess.system.collection.operation.search.exception.wrapper
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import CollectionOperationException

__all__ = [
    # ======================# SEARCH_FAILURE #======================#
    "SearchException",
]


# ======================# SEARCH_FAILURE #======================#
class SearchException(CollectionOperationException):
    """
    # ROLE: Debug Wrapper, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Encapsulate the Layer-1 DebugException which describes the cause the search failed.

    # PARENT:
        *   CollectionOperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SEARCH_FAILURE"
    DEFAULT_MESSAGE = "Search failed."
