# src/chess/hostage/databse/coreexception/search/wrapper.py

"""
Module: chess.hostage.database.core.exception.search.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# UNIQUE_MANIFEST_SEARCH_FAILURE EXCEPTION #======================#
    "UniqueHostageManifestSearchException",
]

from chess.hostage import HostageManifestException
from chess.system import SearchException


# ======================# UNIQUE_MANIFEST_SEARCH_FAILURE EXCEPTION #======================#
class UniqueHostageManifestSearchException(HostageManifestException, SearchException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why inserting a unique HostageManifest failed. The encapsulated 
        exceptions create chain for tracing the source of the failure.

    # PARENT:
        *   HostageManifestException
        *   SearchException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_MANIFEST_SEARCH_FAILURE"
    DEFAULT_MESSAGE = "Unique HostageManifest search failed."