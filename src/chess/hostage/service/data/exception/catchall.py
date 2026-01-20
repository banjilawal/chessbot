# src/chess/hostage/service/data/exception/catchall.py

"""
Module: chess.hostage.service.data.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.hostage import HostageManifestException
from chess.system import DataServiceException

__all__ = [
    # ======================# HOSTAGE_MANIFEST_DATA_SERVICE EXCEPTION #======================#
    "HostageManifestDataServiceException",
]


# ======================# HOSTAGE_MANIFEST_DATA_SERVICE EXCEPTION #======================#
class HostageManifestDataServiceException(HostageManifestException, DataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wrap any exceptions raised by HostageManifestDataService methods that return Result objects.

    # PARENT:
        *   HostageManifestException
        *   DataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "HOSTAGE_MANIFEST_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "HostageManifestDataService raised an exception."