# src/chess/system/service/menu/execution/exception/debug.py

"""
Module: chess.system.service.menu.execution.exception.debug
Author: Banji Lawal
Created: 2026-02-24
"""

__all__ = [
    # ======================# SERVICE_EXECUTION_DEBUG EXCEPTION #======================#
    "ServiceExecutionDebugException",
]

from chess.system import DebugException, ServiceExecutionException


# ======================# SERVICE_EXECUTION_DEBUG EXCEPTION #======================#
class ServiceExecutionDebugException(ServiceExecutionException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a ServiceExecution execution failure.

    # PARENT:
        *   DebugException
        *   ServiceExecutionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "SERVICE_EXECUTION_DEBUG_ERROR"
    DEFAULT_MESSAGE = "A ServiceExecutionDebugException was raised."