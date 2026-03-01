# src/logic/node/service/exception/edge/outgoing/head.py

"""
Module: logic.node.service.exception.edge.outgoing.head
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from logic.node import NodeException
from logic.system import InsertionException

__all__ = [
    # ======================# OUTGOING_EDGE_WRONG_HEAD EXCEPTION #======================#
    "OutgoingEdgeWrongHeadException",
]


# ======================# OUTGOING_EDGE_WRONG_HEAD EXCEPTION #======================#
class OutgoingEdgeWrongHeadException(NodeException, InsertionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that adding outgoing edge failed because the edge was originated from a different
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
    ERR_CODE = "OUTGOING_EDGE_WRONG_HEAD_EXCEPTION"
    MSG = "Inserting an outgoing edge failed: The edge was originated from a different node."