# src/logic/node/service/exception/edge/outgoing/remove.py

"""
Module: logic.node.service.exception.edge.outgoing.remove
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from graph.node import NodeException
from system import InsertionException

__all__ = [
    # ======================# REMOVE_OUTGOING_EDGE_FAILURE #======================#
    "RemoveOutgoingEdgeFailedException",
]


# ======================# REMOVE_OUTGOING_EDGE_FAILURE #======================#
class RemoveOutgoingEdgeFailedException(NodeException, InsertionException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Wrap debug exceptions indicating why 

    Super Class:
        *   NodeException
        *   InsertionException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "REMOVE_OUTGOING_EDGE_FAILURE"
    MSG = "Removing an outgoing edge failed."