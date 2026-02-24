# src/chess/hostage/databse/coreexception/search/wrapper.py

"""
Module: chess.hostage.database.core.exception.search.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# UNIQUE_SEARCH_FAILURE #======================#
    "UniqueHostageSearchException",
]

from chess.hostage import HostageException
from chess.system import SearchException


# ======================# UNIQUE_SEARCH_FAILURE #======================#
class UniqueHostageSearchException(HostageException, SearchException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why inserting a unique Hostage failed. The encapsulated
        exceptions create chain for tracing the source of the failure.

    # PARENT:
        *   HostageException
        *   SearchException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_SEARCH_FAILURE"
    DEFAULT_MESSAGE = "Unique Hostage search failed."