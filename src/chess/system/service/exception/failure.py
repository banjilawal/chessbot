# src/chess/system/service/exception/failure.py

"""
Module: chess.system.service.exception.failure
Author: Banji Lawal
Created: 2025-11-18
"""

from chess.system import OperationFailedException, ServiceException

__all__ = [
    # ======================# SERVICE_OPERATION_FAILED EXCEPTION #======================#
    "ServiceOperationFailedException",
]


# ======================# SERVICE_OPERATION_FAILED EXCEPTION #======================#
class ServiceOperationFailedException(ServiceException, OperationFailedException):
    """
    # ROLE: Error Tracing, Debugging, Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate That  a Service's method caught an unhandled exception in its try-catch-finally block.

    # PARENT:
        *   ServiceException
        *   OperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SERVICE_OPERATION_FAILED_ERROR"
    DEFAULT_MESSAGE = "Service operation failed."