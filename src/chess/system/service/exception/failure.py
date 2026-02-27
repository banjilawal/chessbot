# src/chess/system/service/exception/failure.py

"""
Module: chess.system.service.exception.failure
Author: Banji Lawal
Created: 2025-11-18
"""

from chess.system import OperationException, ServiceException

__all__ = [
    # ======================# SERVICE_OPERATION_FAILURE #======================#
    "ServiceOperationException",
]


# ======================# SERVICE_OPERATION_FAILURE #======================#
class ServiceOperationException(ServiceException, OperationException):
    """
    # ROLE: Error Tracing, Debugging, Exception Wrapper, Super Exception

    # RESPONSIBILITIES:
    1.  Indicate That  a AbstractService's method caught an unhandled exception in its try-catch-finally block.

    # PARENT:
        *   ServiceException
        *   OperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SERVICE_OPERATION_FAILED_ERROR"
    MSG = "AbstractService operation failed."