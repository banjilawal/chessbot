# src/chess/square/service/menu/route/exception/debug.py

"""
Module: chess.square.service.menu.route.exception.debug
Author: Banji Lawal
Created: 2026-02-24
"""

__all__ = [
    # ======================# SERVICE_ROUTE_DEBUG EXCEPTION #======================#
    "ServiceRouteDebugException",
]

from chess.square import DebugException, ServiceRouteException


# ======================# SERVICE_ROUTE_DEBUG EXCEPTION #======================#
class ServiceRouteDebugException(ServiceRouteException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a ServiceRoute route failure.

    # PARENT:
        *   DebugException
        *   ServiceRouteException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "SERVICE_ROUTE_DEBUG_ERROR"
    DEFAULT_MESSAGE = "A ServiceRouteDebugException was raised."