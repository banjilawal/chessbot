# src/chess/hostage/context/finder/exception/wrapper.py

"""
Module: chess.hostage.context.finder.exception.wrapper
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.hostage import HostageException
from chess.system import SearchException

__all__ = [
    # ======================# HOSTAGE_SEARCH_FAILURE #======================#
    "HostageSearchException",
]


# ======================# HOSTAGE_SEARCH_FAILURE #======================#
class HostageSearchException(HostageException, SearchException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any condition that prevents a search from completing creates a debug exception that explains why the query
        failed. That debug exception is wrapped in the HostageSearchException which is the middle layer of the
        3-part exception chain.

    # PARENT:
        *   HostageException
        *   SearchException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "HOSTAGE_SEARCH_FAILURE"
    MSG = "Hostage search failed."