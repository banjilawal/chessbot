# src/chess/scalar/exception/debug.py

"""
Module: chess.scalar.exception.debug
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""


__all__ = [
    # ======================# SCALAR_DEBUG EXCEPTION #======================#
    "ScalarDebugException",
]

from chess.scalar import ScalarException
from chess.system import DebugException


# ======================# SCALAR_DEBUG EXCEPTION #======================#
class ScalarDebugException(ScalarException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Scalar operation failure.

    # PARENT:
        *   ScalarException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERR_CODE = "SCALAR_DEBUG_EXCEPTION"
    MSG = "A ScalarDebugException was raised."