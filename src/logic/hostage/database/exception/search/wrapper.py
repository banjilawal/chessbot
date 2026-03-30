# src/logic/hostage/databse/coreexception/search/validator.py

"""
Module: logic.hostage.database.kernel.exception.search.work
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# UNIQUE_SEARCH_FAILURE #======================#
    "UniqueHostageSearchException",
]

from logic.hostage import HostageException
from logic.system import SearchException


# ======================# UNIQUE_SEARCH_FAILURE #======================#
class UniqueHostageSearchException(HostageException, SearchException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Wrap debug exceptions indicating why inserting a unique Hostage failed. The encapsulated
        exceptions create chain for tracing the source of the failure.

    Super Class:
        *   HostageException
        *   SearchException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "UNIQUE_SEARCH_FAILURE"
    MSG = "Unique Hostage search failed."