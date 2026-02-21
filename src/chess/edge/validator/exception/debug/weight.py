# src/chess/graph/square/validator/exception/debug/weight.py

"""
Module: chess.graph.square.validator.exception.debug/weight
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from chess.edge import EdgeDebugException

__all__ = [
    # ======================# EDGE_WEIGHT EXCEPTION #======================#
    "EdgeWeightException",
]


# ======================# EDGE_WEIGHT EXCEPTION #======================#
class EdgeWeightException(EdgeDebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate was not validated as an edge because its weight was not a number
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
    ERROR_CODE = "EDGE_WEIGHT_ERROR"
    DEFAULT_MESSAGE = "Edge validation failed: the weight was not a number in the valid range."