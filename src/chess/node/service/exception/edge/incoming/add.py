# src/chess/node/service/exception/edge/incoming/add.py

"""
Module: chess.node.service.exception.edge.incoming.add
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from chess.node import NodeException
from chess.system import InsertionException

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
    ERROR_CODE = "ADD_INCOMING_EDGE_FAILURE"
    DEFAULT_MESSAGE = "Adding an incoming edge failed."