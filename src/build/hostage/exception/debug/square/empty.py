# src/logic/hostage/build/exception/debug/victor/empty.py

"""
Module: logic.hostage.build.exception.debug.victor.empty
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from model.hostage import HostageException
from system import DebugException

__all__ = [
    # ======================# CAPTURED_SQUARE_CANNOT_BE_EMPTY EXCEPTION #======================#
    "CapturedSquareCannotBeEmptyException",
]


# ======================# CAPTURED_SQUARE_CANNOT_BE_EMPTY EXCEPTION #======================#

class CapturedSquareCannotBeEmptyException(HostageException, DebugException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that the Hostage build failed because the captured item was empty.

    Super Class:
        *   DebugException
        *   HostageException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "CAPTURED_SQUARE_CANNOT_BE_EMPTY_EXCEPTION"
    MSG = "Hostage build failed: The captured item cannot be empty during the build."