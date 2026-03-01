# src/logic/node/service/exception/edge/incoming/add.py

"""
Module: logic.node.service.exception.edge.incoming.add
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from logic.node import NodeException
from logic.system import InsertionException

__all__ = [
    # ======================# ADD_INCOMING_EDGE_FAILURE #======================#
    "AddIncomingEdgeFailedException",
]

# ======================# ADD_INCOMING_EDGE_FAILURE #======================#
class AddIncomingEdgeFailedException(NodeException, InsertionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why adding a new edge to a node failed.

    # PARENT:
        *   NodeException
        *   InsertionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ADD_INCOMING_EDGE_FAILURE"
    MSG = "Adding an incoming edge failed."