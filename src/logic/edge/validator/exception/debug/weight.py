# src/logic/graph/square/validator/exception/debug/weight.py

"""
Module: logic.graph.square.validator.exception.debug/weight
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from logic.edge import EdgeDebugException

__all__ = [
    # ======================# EDGE_WEIGHT EXCEPTION #======================#
    "EdgeWeightException",
]


# ======================# EDGE_WEIGHT EXCEPTION #======================#
class EdgeWeightException(EdgeDebugException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a candidate was not validated as an edge because its weight was not a number
        within the allowed range.

    Super Class:
        *   EdgeDebugException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "EDGE_WEIGHT_EXCEPTION"
    MSG = "Edge validation failed: the weight was not a number in the valid range."