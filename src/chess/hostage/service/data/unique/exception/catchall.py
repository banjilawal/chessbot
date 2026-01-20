# src/chess/hostage/service/data/unique/exception/catchall.py

"""
Module: chess.hostage.service.data.unique.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

___all__ = [
    # ======================# UNIQUE_HOSTAGE_MANIFEST_DATA_SERVICE EXCEPTION #======================#
    "UniqueHostageManifestDataServiceException",
]

from chess.hostage import HostageManifestException
from chess.system import UniqueDataServiceException


# ======================# UNIQUE_HOSTAGE_MANIFEST_DATA_SERVICE EXCEPTION #======================#
class UniqueHostageManifestDataServiceException(HostageManifestException, UniqueDataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an UniqueHostageManifestDataService encountered an error which prevented the
        service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a UniqueHostageManifestDataService method.

    # PARENT:
        *   ServiceException
        *   HostageManifestException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_HOSTAGE_MANIFEST_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "UniqueHostageManifestDataService raised an exception."