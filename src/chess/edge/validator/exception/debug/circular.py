# src/chess/edge/validator/exception/debug/circular.py

"""
Module: chess.edge.validator.exception.debug.circular
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from chess.edge import EdgeDebugException

__all__ = [
    # ======================# CIRCULAR_EDGE EXCEPTION #======================#
    "CircularEdgeException",
]


# ======================# CIRCULAR_EDGE EXCEPTION #======================#
class CircularEdgeException(EdgeDebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate was not validated as an edge because its head and tail were the same node.
        Edges are not allowed to be circular.

    # PARENT:
        *   EdgeDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CIRCULAR_EDGE_ERROR"
    DEFAULT_MESSAGE = "Edge validation failed: An edge cannot have the same node as its head and tail."