# src/chess/hostage/builder/exception/debug/victor/empty.py

"""
Module: chess.hostage.builder.exception.debug.victor.empty
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.hostage import HostageManifestException
from chess.system import DebugException

__all__ = [
    # ======================# CAPTURED_SQUARE_CANNOT_BE_EMPTY EXCEPTION #======================#
    "CapturedSquareCannotBeEmptyException",
]


# ======================# CAPTURED_SQUARE_CANNOT_BE_EMPTY EXCEPTION #======================#

class CapturedSquareCannotBeEmptyException(HostageManifestException, DebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that the HostageManifest build failed because the captured square was empty.

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
    ERROR_CODE = "CAPTURED_SQUARE_CANNOT_BE_EMPTY_ERROR"
    DEFAULT_MESSAGE = "HostageManifest build failed: The captured square cannot be empty during the build."