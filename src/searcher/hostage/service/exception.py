# src/logic/hostage/context/service/exception.py

"""
Module: logic.hostage.context.service.exception
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from system import ServiceException
from model.hostage import CaptivityContextException

__all__ = [
    # ======================# CAPTIVITY_CONTEXT_SERVICE EXCEPTION #======================#
    "CaptivityContextServiceException",
]


# ======================# CAPTIVITY_CONTEXT_SERVICE EXCEPTION #======================#
class CaptivityContextServiceException(CaptivityContextException, ServiceException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Indicate that an HostageQueryService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of an HostageQueryService method.

    Super Class:
        *   ServiceException
        *   CaptivityContextException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "CAPTIVITY_CONTEXT_SERVICE_EXCEPTION"
    MSG = "HostageQueryService raised an exception."