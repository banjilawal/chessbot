# src/logic/hostage/builder/exception/debug/victor/item.py

"""
Module: logic.hostage.builder.exception.debug.victor.item
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

__all__ = [
    # ======================# VICTOR_NOT_ON_CAPTURED_SQUARE EXCEPTION #======================#
    "VictorNotOccupyingCapturedSquareException",
]

from logic.hostage import HostageException
from logic.system import DebugException


# ======================# VICTOR_NOT_ON_CAPTURED_SQUARE EXCEPTION #======================#

class VictorNotOccupyingCapturedSquareException(HostageException, DebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that the Hostage build failed because the victor was not occupying the item where it
        captured the prisoner.

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
    ERR_CODE = "VICTOR_NOT_ON_CAPTURED_SQUARE_EXCEPTION"
    MSG = "Hostage build failed: Victor not occupying captured item."