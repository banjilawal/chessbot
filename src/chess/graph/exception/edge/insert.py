# src/chess/graph/exception/edge/insert.py

"""
Module: chess.graph.exception.edge.insert
Author: Banji Lawal
Created: 2025-02-18
version: 1.0.0
"""

from chess.graph import GraphException
from chess.system import ComputationException

__all__ = [
    # ======================# NODE_INSERTION_FAILURE #======================#
    "NodeInsertionException",
]


class NodeInsertionException(GraphException, ComputationException):
    pass