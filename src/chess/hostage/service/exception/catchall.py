# src/chess/hostage/service/exception/catchall.py

"""
Module: chess.hostage.service.exception.catchall
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.hostage import HostageManifestException

__all__ = [
    # ======================# HOSTAGE_MANIFEST_SERVICE EXCEPTION #======================#
    "HostageManifestServiceException",
]

from chess.system import ServiceException


# ======================# HOSTAGE_MANIFEST_SERVICE EXCEPTION #======================#
class HostageManifestServiceException(HostageManifestException, ServiceException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for HostageManifestService errors.

    # PARENT:
        *   ServiceException
        *   HostageManifestException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "HOSTAGE_MANIFEST_SERVICE_ERROR"
    DEFAULT_MESSAGE = "HostageManifestService raised an exception."