# src/chess/graph/square/validator/exception/debug/distance.py

"""
Module: chess.graph.square.validator.exception.debug/distance
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from chess.edge import EdgeDebugException

__all__ = [
    # ======================# EDGE_DISTANCE EXCEPTION #======================#
    "EdgeDistanceException",
]


# ======================# EDGE_DISTANCE EXCEPTION #======================#
class EdgeDistanceException(EdgeDebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate was not validated as an edge because its distance was a negative number.

    # PARENT:
        *   EdgeDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EDGE_DISTANCE_ERROR"
    DEFAULT_MESSAGE = "Edge validation failed: the distance cannot be a negative number."