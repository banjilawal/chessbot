# src/chess/edge/context/validator/exception/debug/excess.py

"""
Module: chess.edge.context.validator.exception.debug.excess
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.edge import EdgeContextException

__all__ = [
    # ========================= ARENA_EDGE_CONTEXT_FLAG EXCEPTION =========================#
    "ArenaEdgeContextFlagsException"
]


# ========================= ARENA_EDGE_CONTEXT_FLAG EXCEPTION =========================#
class ArenaEdgeContextFlagsException(EdgeContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its validation as a EdgeContext because more than one of its attributes
        was enabled.

    # PARENT:
        *   ContextFlagCountException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ARENA_EDGE_CONTEXT_FLAG_ERROR"
    MSG = "EdgeContext validation failed: More than one flag was enable."