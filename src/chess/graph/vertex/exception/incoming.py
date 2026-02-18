# src/chess/graph/node/exception/incoming.py

"""
Module: chess.graph.node.exception.incoming
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

from chess.graph import NodeException

__all__ = [
    # ======================# ADD_INCOMING_EDGE EXCEPTION #======================#
    "AddIncomingEdgeException",
]


class AddIncomingEdgeException(NodeException):
    pass