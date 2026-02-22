# src/chess/graph/exception/computation.py

"""
Module: chess.graph.exception.computation
Author: Banji Lawal
Created: 2025-02-18
version: 1.0.0
"""

from chess.graph import GraphException
from chess.system import ComputationException

__all__ = [
    # ======================# GRAPH_COMPUTATION_FAILURE #======================#
    "GraphComputationException",
]

class GraphComputationException(GraphException, ComputationException):
    pass