# src/chess/hostage/context/finder/exception/wrapper.py

"""
Module: chess.hostage.context.finder.exception.wrapper
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.hostage import HostageManifestException
from chess.system import SearchException

__all__ = [
    # ======================# HOSTAGE_MANIFEST_SEARCH_FAILURE EXCEPTION #======================#
    "HostageManifestSearchException",
]


# ======================# HOSTAGE_MANIFEST_SEARCH_FAILURE EXCEPTION #======================#
class HostageManifestSearchException(HostageManifestException, SearchException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any condition that prevents a search from completing creates a debug exception that explains why the query
        failed. That debug exception is wrapped in the HostageManifestSearchException which is the middle layer of the
        3-part exception chain.

    # PARENT:
        *   HostageManifestException
        *   SearchException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "HOSTAGE_MANIFEST_SEARCH_FAILURE"
    DEFAULT_MESSAGE = "HostageManifest search failed."