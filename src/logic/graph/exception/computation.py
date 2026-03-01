# src/logic/graph/exception/computation.py

"""
Module: logic.graph.exception.computation
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from logic.graph import GraphException
from logic.system import ComputationException

__all__ = [
    # ======================# GRAPH_COMPUTATION_FAILURE #======================#
    "GraphComputationException",
]

class GraphComputationException(GraphException, ComputationException):
    pass