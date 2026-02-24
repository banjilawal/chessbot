# src/chess/hostage/builder/exception/debug/victor/disabled.py

"""
Module: chess.hostage.builder.exception.debug.victor.disabled
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.hostage import HostageException
from chess.system import DebugException

__all__ = [
    # ======================# VICTOR_CANNOT_BE_DISABLED_TOKEN EXCEPTION #======================#
    "VictorCannotBeDisableTokenException",
]


# ======================# VICTOR_CANNOT_BE_DISABLED_TOKEN EXCEPTION #======================#

class VictorCannotBeDisableTokenException(HostageException, DebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that the Hostage build failed because the victor was not active for the build process.
        A occupant must be active when it creates a capture event.

    # PARENT:
        *   DebugException
        *   HostageException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "VICTOR_CANNOT_BE_DISABLED_TOKEN_ERROR"
    DEFAULT_MESSAGE = "Hostage build failed: Victor cannot be disabled. It must be active during the build."