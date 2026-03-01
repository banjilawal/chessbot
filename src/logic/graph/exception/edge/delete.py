# src/logic/graph/exception/edge/delete.py

"""
Module: logic.graph.exception.edge.delete
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from logic.graph import GraphException
from logic.system import ComputationException

__all__ = [
    # ======================# NODE_DELETION_FAILURE #======================#
    "NodeDeletionException",
]


class NodeDeletionException(GraphException, ComputationException):
    pass