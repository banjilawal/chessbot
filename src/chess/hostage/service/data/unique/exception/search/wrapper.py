# src/chess/hostage/service/data/exception/search/wrapper.py

"""
Module: chess.hostage.service.data.exception.search.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# UNIQUE_MANIFEST_SEARCH_FAILURE EXCEPTION #======================#
    "UniqueHostageManifestSearchFailedException",
]

from chess.hostage import HostageManifestException
from chess.system import SearchFailedException


# ======================# UNIQUE_MANIFEST_SEARCH_FAILURE EXCEPTION #======================#
class UniqueHostageManifestSearchFailedException(HostageManifestException, SearchFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why inserting a unique HostageManifest failed. The encapsulated 
        exceptions create chain for tracing the source of the failure.

    # PARENT:
        *   HostageManifestException
        *   SearchFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_MANIFEST_SEARCH_FAILURE"
    DEFAULT_MESSAGE = "Unique HostageManifest search failed."