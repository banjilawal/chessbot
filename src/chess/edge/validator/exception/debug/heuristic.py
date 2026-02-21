# src/chess/graph/square/validator/exception/debug/heuristic.py

"""
Module: chess.graph.square.validator.exception.debug/heuristic
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from chess.edge import EdgeDebugException

__all__ = [
    # ======================# EDGE_HEURISTIC EXCEPTION #======================#
    "EdgeHeuristicException",
]


# ======================# EDGE_HEURISTIC EXCEPTION #======================#
class EdgeHeuristicException(EdgeDebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate was not validated as an edge because its heuristic was not a number 
        within the allowed range.

    # PARENT:
        *   EdgeDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EDGE_HEURISTIC_ERROR"
    DEFAULT_MESSAGE = "Edge validation failed: the heuristic was not a number in the valid range."