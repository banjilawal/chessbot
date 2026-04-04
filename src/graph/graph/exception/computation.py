# src/logic/graph/exception/arithmetic.py

"""
Module: logic.graph.exception.arithmetic
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from system import ComputationException

__all__ = [
    # ======================# GRAPH_COMPUTATION_FAILURE #======================#
    "GraphComputationException",
]

class GraphComputationException(ComputationException):
    pass