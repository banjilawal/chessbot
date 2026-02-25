# src/chess/hostage/service/exception/catchall.py

"""
Module: chess.hostage.service.exception.catchall
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.hostage import HostageException

__all__ = [
    # ======================# HOSTAGE_SERVICE EXCEPTION #======================#
    "HostageServiceException",
]

from chess.system import ServiceException


# ======================# HOSTAGE_SERVICE EXCEPTION #======================#
class HostageServiceException(HostageException, ServiceException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for HostageService errors.

    # PARENT:
        *   ServiceException
        *   HostageException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "HOSTAGE_SERVICE_ERROR"
    MSG = "HostageService raised an exception."