# src/chess/hostage/builder/exception/debug/victor/disabled.py

"""
Module: chess.hostage.builder.exception.debug.victor.disabled
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.hostage import HostageManifestException
from chess.system import DebugException

__all__ = [
    # ======================# VICTOR_CANNOT_BE_DISABLED_TOKEN EXCEPTION #======================#
    "VictorCannotBeDisableTokenException",
]


# ======================# VICTOR_CANNOT_BE_DISABLED_TOKEN EXCEPTION #======================#

class VictorCannotBeDisableTokenException(HostageManifestException, DebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that the HostageManifest build failed because the victor was not active for the build process.
        A token must be active when it creates a capture event.

    # PARENT:
        *   DebugException
        *   HostageManifestException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "VICTOR_CANNOT_BE_DISABLED_TOKEN_ERROR"
    DEFAULT_MESSAGE = "HostageManifest build failed: Victor cannot be disabled. It must be active during the build."