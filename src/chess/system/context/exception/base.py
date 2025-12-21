# src/chess/system/context/exception/base.py

"""
Module: chess.system.context.exception.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# CONTEXT EXCEPTION #======================#
    "ContextException",
]


# ======================# CONTEXT EXCEPTION #======================#
class ContextException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by CONTEXT objects
    3.  Catchall for CONTEXT errors not covered by lower level CONTEXT exception.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CONTEXT_ERROR"
    DEFAULT_MESSAGE = "CONTEXT raised an exception."
