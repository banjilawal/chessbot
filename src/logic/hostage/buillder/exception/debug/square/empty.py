# src/logic/hostage/builder/exception/debug/victor/empty.py

"""
Module: logic.hostage.builder.exception.debug.victor.empty
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from logic.hostage import HostageException
from logic.system import DebugException

__all__ = [
    # ======================# CAPTURED_SQUARE_CANNOT_BE_EMPTY EXCEPTION #======================#
    "CapturedSquareCannotBeEmptyException",
]


# ======================# CAPTURED_SQUARE_CANNOT_BE_EMPTY EXCEPTION #======================#

class CapturedSquareCannotBeEmptyException(HostageException, DebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that the Hostage build failed because the captured item was empty.

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
    ERR_CODE = "CAPTURED_SQUARE_CANNOT_BE_EMPTY_EXCEPTION"
    MSG = "Hostage build failed: The captured item cannot be empty during the build."