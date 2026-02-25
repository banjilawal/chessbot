# src/chess/square/context/exception/debug.py

"""
Module: chess.square.context.exception.debug
Author: Banji Lawal
Created: 2026-02-23
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_CONTEXT EXCEPTION #======================#
    "SquareContextException",
]

from chess.system import SuperClassException


# ======================# SQUARE_CONTEXT EXCEPTION #======================#
class SquareContextException(SuperClassException):
    """
    # ROLE: DebugException Parent, Exception Chain Layer 0

    # RESPONSIBILITIES:
    Layer-0 of Exception chain which is the Parent of SquareContextDebugException

    # PARENT:
        *   SuperClassException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_CONTEXT_ERROR"
    MSG = "SquareContext raised an exception."
    