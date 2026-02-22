# src/chess/node/service/exception/edge/incoming/remove.py

"""
Module: chess.node.service.exception.edge.incoming.remove
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from chess.node import NodeException
from chess.system import InsertionException

__all__ = [
    # ======================# REMOVE_INCOMING_EDGE_FAILURE #======================#
    "RemoveIncomingEdgeFailedException",
]


# ======================# REMOVE_INCOMING_EDGE_FAILURE #======================#
class RemoveIncomingEdgeFailedException(NodeException, InsertionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why 

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
    ERROR_CODE = "REMOVE_INCOMING_EDGE_FAILURE"
    DEFAULT_MESSAGE = "Removing an incoming edge failed."