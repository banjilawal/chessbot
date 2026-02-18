# src/chess/node/exception/outgoing.py

"""
Module: chess.node.exception.outgoing
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

from chess.graph import NodeException

__all__ = [
    # ======================# ADD_OUTGOING_EDGE EXCEPTION #======================#
    "AddOutgoingEdgeException",
]

class AddOutgoingEdgeException(NodeException):
    pass