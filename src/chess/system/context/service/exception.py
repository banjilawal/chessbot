# src/chess/system/context/service/exception.py

"""
Module: chess.system.context.service.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ContextException, ServiceException

__all__ = [
    # ======================# CONTEXT_SERVICE EXCEPTION #======================#
    "ContextServiceException",
]




# ======================# CONTEXT_SERVICE EXCEPTION #======================#
class ContextServiceException(ContextException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by ServiceContext objects.
    2.  Wraps unhandled exceptions that hit the try-finally block of a ServiceContext method.

    # PARENT:
        *   ContextException
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "ContextService raised an exception."