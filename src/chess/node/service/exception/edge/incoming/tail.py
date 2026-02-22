# src/chess/node/service/exception/edge/incoming/tail.py

"""
Module: chess.node.service.exception.edge.incoming.tail
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from chess.node import NodeException
from chess.system import InsertionException

__all__ = [
    # ======================# INCOMING_EDGE_WRONG_TAIL EXCEPTION #======================#
    "IncomingEdgeWrongTailException",
]


# ======================# INCOMING_EDGE_WRONG_TAIL EXCEPTION #======================#
class IncomingEdgeWrongTailException(NodeException, InsertionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that adding an incoming edge failed because the edge was pointing to a different
        node.

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
    ERROR_CODE = "INCOMING_EDGE_WRONG_TAIL_ERROR"
    DEFAULT_MESSAGE = "Adding an incoming edge failed: The edge was pointing to a different node."