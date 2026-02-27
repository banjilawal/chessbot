# src/chess/vector/exception/debug.py

"""
Module: chess.vector.exception.debug
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""


__all__ = [
    # ======================# VECTOR_DEBUG EXCEPTION #======================#
    "VectorDebugException",
]

from chess.vector import VectorException
from chess.system import DebugException


# ======================# VECTOR_DEBUG EXCEPTION #======================#
class VectorDebugException(VectorException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Vector operation failure.

    # PARENT:
        *   VectorException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERR_CODE = "VECTOR_DEBUG_EXCEPTION"
    MSG = "A VectorDebugException was raised."