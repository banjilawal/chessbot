# src/chess/hostage/builder/exception/debug/victor/square.py

"""
Module: chess.hostage.builder.exception.debug.victor.square
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

__all__ = [
    # ======================# VICTOR_NOT_ON_CAPTURED_SQUARE EXCEPTION #======================#
    "VictorNotOccupyingCapturedSquareException",
]

from chess.hostage import HostageManifestException
from chess.system import DebugException


# ======================# VICTOR_NOT_ON_CAPTURED_SQUARE EXCEPTION #======================#

class VictorNotOccupyingCapturedSquareException(HostageManifestException, DebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that the HostageManifest build failed because the victor was not occupying the square where it
        captured the prisoner.

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
    ERROR_CODE = "VICTOR_NOT_ON_CAPTURED_SQUARE_ERROR"
    DEFAULT_MESSAGE = "HostageManifest build failed: Victor not occupying captured square."