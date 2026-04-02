# src/logic/graph/square/validation/exception/debug/heuristic.py

"""
Module: logic.graph.square.validation.exception.debug/heuristic
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from logic.edge import EdgeDebugException

__all__ = [
    # ======================# EDGE_HEURISTIC EXCEPTION #======================#
    "EdgeHeuristicException",
]


# ======================# EDGE_HEURISTIC EXCEPTION #======================#
class EdgeHeuristicException(EdgeDebugException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a rank was not validated as an edge because its heuristic was not a number
        within the allowed range.

    Super Class:
        *   EdgeDebugException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "EDGE_HEURISTIC_EXCEPTION"
    MSG = "Edge validation failed: the heuristic was not a number in the valid range."