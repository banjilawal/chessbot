# src/chess/hostage/database/exception/catchall.py

"""
Module: chess.hostage.database.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

___all__ = [
    # ======================# HOSTAGE_MANIFEST_DIRECTORY_SERVICE EXCEPTION #======================#
    "HostageDatabase",
]

from chess.hostage import HostageManifestException
from chess.system import UniqueDataServiceException


# ======================# HOSTAGE_MANIFEST_DIRECTORY_SERVICE EXCEPTION #======================#
class HostageDatabaseException(HostageManifestException, UniqueDataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an HostageDatabase encountered an error which prevented the
        service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a HostageDatabase method.

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
    DEFAULT_MESSAGE = "HostageDatabase raised an exception."