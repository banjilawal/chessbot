# src/logic/node/schema/exception/pop/empty.py

"""
Module: logic.node.schema.exception.pop.empty
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""



__all__ = [
    # ======================# POPPING_EMPTY_NODE_STACK EXCEPTION #======================#
    "PoppingEmptyNodeStackException",
]

from model.state.node import NodeDebugException


# ======================# POPPING_EMPTY_NODE_STACK EXCEPTION #======================#
class PoppingEmptyNodeStackException(NodeDebugException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attempt to remove a item failed because the schema was empty

    Super Class:
        *   NodeException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "POPPING_EMPTY_NODE_STACK_EXCEPTION"
    MSG = "Node deletion failed: NodeStackService does not own any nodes."