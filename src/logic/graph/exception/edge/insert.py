# src/logic/graph/exception/edge/insert.py

"""
Module: logic.graph.exception.edge.insert
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from logic.graph import GraphException
from logic.system import ComputationException

__all__ = [
    # ======================# NODE_INSERTION_FAILURE #======================#
    "NodeInsertionException",
]


class NodeInsertionException(GraphException, ComputationException):
    pass