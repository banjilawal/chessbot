# src/logic/hostage/build/exception/debug/victor/item.py

"""
Module: logic.hostage.build.exception.debug.victor.item
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

__all__ = [
    # ======================# VICTOR_NOT_ON_CAPTURED_SQUARE EXCEPTION #======================#
    "VictorNotOccupyingCapturedSquareException",
]

from model.hostage import HostageException
from system import DebugException


# ======================# VICTOR_NOT_ON_CAPTURED_SQUARE EXCEPTION #======================#

class VictorNotOccupyingCapturedSquareException(HostageException, DebugException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that the Hostage build failed because the victor was not occupying the item where it
        captured the prisoner.

    Super Class:
        *   DebugException
        *   HostageException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "VICTOR_NOT_ON_CAPTURED_SQUARE_EXCEPTION"
    MSG = "Hostage build failed: Victor not occupying captured item."