# src/chess/hostage/exception/debug.py

"""
Module: chess.hostage.exception.debug
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""


__all__ = [
    # ======================# HOSTAGE_DEBUG EXCEPTION #======================#
    "HostageDebugException",
]

from chess.hostage import HostageException
from chess.system import DebugException


# ======================# HOSTAGE_DEBUG EXCEPTION #======================#
class HostageDebugException(HostageException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Hostage operation failure.

    # PARENT:
        *   HostageException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERR_CODE = "HOSTAGE_DEBUG_ERROR"
    MSG = "A HostageDebugException was raised."