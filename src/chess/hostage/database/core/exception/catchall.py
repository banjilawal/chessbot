# src/chess/hostage/databse/coreexception/catchall.py

"""
Module: chess.hostage.database.core.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.hostage import HostageManifestException
from chess.system import DataServiceException

__all__ = [
    # ======================# HOSTAGE_MANIFEST_LIST EXCEPTION #======================#
    "HostageManifestDataListException",
]


# ======================# HOSTAGE_MANIFEST_LIST EXCEPTION #======================#
class HostageManifestDataListException(HostageManifestException, DataServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap any exceptions raised by HostageManifestList methods that return Result objects.

    # PARENT:
        *   HostageManifestException
        *   StackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "HOSTAGE_MANIFEST_LIST_ERROR"
    DEFAULT_MESSAGE = "HostageManifestList raised an exception."