# src/logic/system/collection/operation/search/query/service/exception/super.py

"""
Module: logic.system.collection.operation.search.query.service.exception.__init__
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from logic.system import  ServiceException

__all__ = [
    # ======================# CONTEXT_SERVICE EXCEPTION #======================#
    "ContextServiceException",
]


# ======================# CONTEXT_SERVICE EXCEPTION #======================#
class ContextServiceException(ContextException, ServiceException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Parent of exceptions raised by ServiceContext objects.
    2.  Wrap an exception that hits the try-finally block of a ServiceContext method.

    Super Class:
        *   ContextException
        *   ServiceException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "CONTEXT_SERVICE_EXCEPTION"
    MSG = "ContextService raised an exception."