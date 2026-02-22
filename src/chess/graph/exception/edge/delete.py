# src/chess/graph/exception/edge/delete.py

"""
Module: chess.graph.exception.edge.delete
Author: Banji Lawal
Created: 2025-02-18
version: 1.0.0
"""

from chess.graph import GraphException
from chess.system import ComputationException

__all__ = [
    # ======================# NODE_DELETION_FAILURE #======================#
    "NodeDeletionException",
]


class NodeDeletionException(GraphException, ComputationException):
    pass