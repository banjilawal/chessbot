# src/chess/exception/vector/insert.py

"""
Module: chess.exception.vector.insert
Author: Banji Lawal
Created: 2025-02-18
version: 1.0.0
"""

from chess.graph import GraphException
from chess.system import ComputationFailedException

__all__ = [
    # ======================# NODE_INSERTION_FAILURE EXCEPTION #======================#
    "NodeInsertionFailedException",
]


class NodeInsertionFailedException(GraphException, ComputationFailedException):
    pass