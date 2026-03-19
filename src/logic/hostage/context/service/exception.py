# src/logic/hostage/context/service/exception.py

"""
Module: logic.hostage.context.service.exception
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from logic.system import ServiceException
from logic.hostage import CaptivityContextException

__all__ = [
    # ======================# CAPTIVITY_CONTEXT_SERVICE EXCEPTION #======================#
    "CaptivityContextServiceException",
]


# ======================# CAPTIVITY_CONTEXT_SERVICE EXCEPTION #======================#
class CaptivityContextServiceException(CaptivityContextException, ServiceException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Indicate that an HostageContextService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of an HostageContextService method.

    Super Class:
        *   ServiceException
        *   CaptivityContextException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "CAPTIVITY_CONTEXT_SERVICE_EXCEPTION"
    MSG = "HostageContextService raised an exception."