# src/logic/edge/schema/exception/push/duplicate.py

"""
Module: logic.edge.schema.exception.push.duplicate
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from logic.edge import EdgeDebugException

__all__ = [
    # ======================# ADDING_DUPLICATE_EDGE EXCEPTION #======================#
    "AddingDuplicateEdgeException",
]


# ======================# ADDING_DUPLICATE_EDGE EXCEPTION #======================#
class AddingDuplicateEdgeException(EdgeDebugException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attempt to add a edge to teh schema failed because it was already present.

    Super Class:
        *   EdgeStackException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ADDING_DUPLICATE_EDGE_EXCEPTION"
    MSG = "Pushing edge onto schema failed: The edge is already present."