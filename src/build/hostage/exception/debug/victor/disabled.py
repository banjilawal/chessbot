# src/logic/hostage/build/exception/debug/victor/disabled.py

"""
Module: logic.hostage.build.exception.debug.victor.disabled
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from model.hostage import HostageException
from system import DebugException

__all__ = [
    # ======================# VICTOR_CANNOT_BE_DISABLED_HOSTAGE EXCEPTION #======================#
    "VictorCannotBeDisableHostageException",
]


# ======================# VICTOR_CANNOT_BE_DISABLED_HOSTAGE EXCEPTION #======================#

class VictorCannotBeDisableHostageException(HostageException, DebugException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that the Hostage build failed because the victor was not active for the build exception.
        A occupant must be active when it creates a capture event.

    Super Class:
        *   DebugException
        *   HostageException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "VICTOR_CANNOT_BE_DISABLED_HOSTAGE_EXCEPTION"
    MSG = "Hostage build failed: Victor cannot be disabled. It must be active during the build."