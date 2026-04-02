# src/logic/node/schema/exception/push/duplicate.py

"""
Module: logic.node.schema.exception.push.duplicate
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from logic.node import NodeDebugException

__all__ = [
    # ======================# ADDING_DUPLICATE_NODE EXCEPTION #======================#
    "AddingDuplicateNodeException",
]


# ======================# ADDING_DUPLICATE_NODE EXCEPTION #======================#
class AddingDuplicateNodeException(NodeDebugException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attempt to add a node to teh schema failed because it was already present.

    Super Class:
        *   NodeStackException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ADDING_DUPLICATE_NODE_EXCEPTION"
    MSG = "Pushing node onto schema failed: The node is already present."