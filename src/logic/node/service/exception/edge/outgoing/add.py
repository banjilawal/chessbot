# src/logic/node/service/exception/edge/outgoing/add.py

"""
Module: logic.node.service.exception.edge.outgoing.add
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from logic.node import NodeException
from logic.system import InsertionException

__all__ = [
    # ======================# ADD_OUTGOING_EDGE_FAILURE #======================#
    "AddOutgoingEdgeFailedException",
]

# ======================# ADD_OUTGOING_EDGE_FAILURE #======================#
class AddOutgoingEdgeFailedException(NodeException, InsertionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why adding a new outgoing edge to a node failed.

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
    ERR_CODE = "ADD_OUTGOING_EDGE_FAILURE"
    MSG = "Adding an outgoing edge failed."