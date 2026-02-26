# src/chess/system/service/request/exception/debug.py

"""
Module: chess.system.service.request.exception.debug
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

__all__ = [
    # ======================# SERVICE_REQUEST_DEBUG EXCEPTION #======================#
    "ServiceRequestDebugException",
]

from chess.system import DebugException, ServiceRequestException


# ======================# SERVICE_REQUEST_DEBUG EXCEPTION #======================#
class ServiceRequestDebugException(ServiceRequestException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a ServiceRequest request failure.

    # PARENT:
        *   DebugException
        *   ServiceRequestException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERR_CODE = "SERVICE_REQUEST_DEBUG_ERROR"
    MSG = "A ServiceRequestDebugException was raised."