# src/logic/node/service/exception/edge/incoming/tail.py

"""
Module: logic.node.service.exception.edge.incoming.tail
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from graph.node import NodeException
from system import InsertionException

__all__ = [
    # ======================# INCOMING_EDGE_WRONG_TAIL EXCEPTION #======================#
    "IncomingEdgeWrongTailException",
]


# ======================# INCOMING_EDGE_WRONG_TAIL EXCEPTION #======================#
class IncomingEdgeWrongTailException(NodeException, InsertionException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Indicate that adding an incoming edge failed because the edge was pointing to a different
        node.

    Super Class:
        *   NodeException
        *   InsertionException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "INCOMING_EDGE_WRONG_TAIL_EXCEPTION"
    MSG = "Adding an incoming edge failed: The edge was pointing to a different node."