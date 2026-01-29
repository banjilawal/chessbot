# src/chess/system/collectionoperation/search/context/service/exception/catchall.py

"""
Module: chess.system.collection.operation.search.context.service.exception.__init__
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import  ServiceException

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
    2.  Wrap an exception that hits the try-finally block of a ServiceContext method.

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