# src/chess/edge/stack/exception/pop/empty.py

"""
Module: chess.edge.stack.exception.pop.empty
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""



__all__ = [
    # ======================# POPPING_EMPTY_EDGE_STACK EXCEPTION #======================#
    "PoppingEmptyEdgeStackException",
]

from chess.edge import EdgeDebugException
from chess.system import PoppingEmptyStackException


# ======================# POPPING_EMPTY_EDGE_STACK EXCEPTION #======================#
class PoppingEmptyEdgeStackException(EdgeDebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove a item failed because the stack was empty

    # PARENT:
        *   EdgeException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "POPPING_EMPTY_EDGE_STACK_ERROR"
    DEFAULT_MESSAGE = "Edge deletion failed: EdgeStack does not own any edges."