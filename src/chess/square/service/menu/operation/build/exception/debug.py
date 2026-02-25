# src/chess/square/service/menu/operation/exception/debug.py

"""
Module: chess.square.service.menu.operation.exception.debug
Author: Banji Lawal
Created: 2026-02-24
"""

__all__ = [
    # ======================# SERVICE_OPERATION_DEBUG EXCEPTION #======================#
    "ServiceOperationDebugException",
]

from chess.square import DebugException, ServiceOperationException


# ======================# SERVICE_OPERATION_DEBUG EXCEPTION #======================#
class ServiceOperationDebugException(ServiceOperationException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a ServiceOperation operation failure.

    # PARENT:
        *   DebugException
        *   ServiceOperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "SERVICE_OPERATION_DEBUG_ERROR"
    DEFAULT_MESSAGE = "A ServiceOperationDebugException was raised."