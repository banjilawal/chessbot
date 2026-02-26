# src/chess/square/service/command/exception/debug.py

"""
Module: chess.square.service.command.exception.debug
Author: Banji Lawal
Created: 2026-02-24
"""

__all__ = [
    # ======================# SERVICE_COMMAND_DEBUG EXCEPTION #======================#
    "ServiceCommandDebugException",
]

from chess.square import DebugException, ServiceCommandException


# ======================# SERVICE_COMMAND_DEBUG EXCEPTION #======================#
class ServiceCommandDebugException(ServiceCommandException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Command command failure.

    # PARENT:
        *   DebugException
        *   CommandException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERR_CODE = "SERVICE_COMMAND_DEBUG_ERROR"
    MSG = "A ServiceCommandDebugException was raised."