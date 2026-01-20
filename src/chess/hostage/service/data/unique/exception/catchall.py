# src/chess/hostage/service/data/unique/exception/catchall.py

"""
Module: chess.hostage.service.data.unique.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

___all__ = [
    # ======================# HOSTAGE_MANIFEST_DIRECTORY_SERVICE EXCEPTION #======================#
    "HostageManifestDirectoryServiceException",
]

from chess.hostage import HostageManifestException
from chess.system import UniqueDataServiceException


# ======================# HOSTAGE_MANIFEST_DIRECTORY_SERVICE EXCEPTION #======================#
class HostageManifestDirectoryServiceException(HostageManifestException, UniqueDataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an HostageManifestDirectoryService encountered an error which prevented the
        service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a HostageManifestDirectoryService method.

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
    ERROR_CODE = "HOSTAGE_MANIFEST_DIRECTORY_SERVICE_ERROR"
    DEFAULT_MESSAGE = "HostageManifestDirectoryService raised an exception."