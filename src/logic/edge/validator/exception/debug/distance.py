# src/logic/graph/square/validation/exception/debug/distance.py

"""
Module: logic.graph.square.validation.exception.debug/distance
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from logic.edge import EdgeDebugException

__all__ = [
    # ======================# EDGE_DISTANCE EXCEPTION #======================#
    "EdgeDistanceException",
]


# ======================# EDGE_DISTANCE EXCEPTION #======================#
class EdgeDistanceException(EdgeDebugException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a candidate was not validated as an edge because its distance was a negative number.

    Super Class:
        *   EdgeDebugException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "EDGE_DISTANCE_EXCEPTION"
    MSG = "Edge validation failed: the distance cannot be a negative number."