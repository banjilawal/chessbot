# src/logic/node/service/exception/edge/incoming/remove.py

"""
Module: logic.node.service.exception.edge.incoming.remove
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from logic.node import NodeException
from logic.system import InsertionException

__all__ = [
    # ======================# REMOVE_INCOMING_EDGE_FAILURE #======================#
    "RemoveIncomingEdgeFailedException",
]


# ======================# REMOVE_INCOMING_EDGE_FAILURE #======================#
class RemoveIncomingEdgeFailedException(NodeException, InsertionException):
    """
    Role:Exception Wrapper

    Responsibilities:
    1.  Wrap debug exceptions indicating why 

    Super Class:
        *   NodeException
        *   InsertionException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "REMOVE_INCOMING_EDGE_FAILURE"
    MSG = "Removing an incoming edge failed."