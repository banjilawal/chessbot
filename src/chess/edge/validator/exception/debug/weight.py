# src/chess/graph/square/validator/exception/debug/weight.py

"""
Module: chess.graph.square.validator.exception.debug/weight
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from chess.graph import EdgeException
from chess.system import DebugException

__all__ = [
    # ======================# EDGE_WEIGHT EXCEPTION #======================#
    "EdgeWeightException",
]

class EdgeWeightException(EdgeException, DebugException):
    pass