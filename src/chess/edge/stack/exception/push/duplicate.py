# src/chess/edge/stack/exception/push/duplicate.py

"""
Module: chess.edge.stack.exception.push.duplicate
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from chess.edge import EdgeDebugException

__all__ = [
    # ======================# ADDING_DUPLICATE_EDGE EXCEPTION #======================#
    "AddingDuplicateEdgeException",
]


# ======================# ADDING_DUPLICATE_EDGE EXCEPTION #======================#
class AddingDuplicateEdgeException(EdgeDebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to add a edge to teh stack failed because it was already present.

    # PARENT:
        *   EdgeStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_DUPLICATE_EDGE_ERROR"
    DEFAULT_MESSAGE = "Pushing edge onto stack failed: The edge is already present."