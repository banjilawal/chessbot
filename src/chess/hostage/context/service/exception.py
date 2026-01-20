# src/chess/hostage/context/service/exception.py

"""
Module: chess.hostage.context.service.exception
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import ServiceException
from chess.hostage import CaptivityContextException

__all__ = [
    # ======================# CAPTIVITY_CONTEXT_SERVICE EXCEPTION #======================#
    "CaptivityContextServiceException",
]


# ======================# CAPTIVITY_CONTEXT_SERVICE EXCEPTION #======================#
class CaptivityContextServiceException(CaptivityContextException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an CaptivityContextService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of an CaptivityContextService method.

    # PARENT:
        *   ServiceException
        *   CaptivityContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CAPTIVITY_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CaptivityContextService raised an exception."