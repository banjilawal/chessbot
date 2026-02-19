# src/chess/node/stack/exception/push/duplicate.py

"""
Module: chess.node.stack.exception.push.duplicate
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from chess.node import NodeStackException

__all__ = [
    # ======================# ADDING_DUPLICATE_NODE EXCEPTION #======================#
    "AddingDuplicateNodeException",
]


# ======================# ADDING_DUPLICATE_NODE EXCEPTION #======================#
class AddingDuplicateNodeException(NodeStackException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to add a node to teh stack failed because it was already present.

    # PARENT:
        *   NodeStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_DUPLICATE_NODE_ERROR"
    DEFAULT_MESSAGE = "Pushing node onto stack failed: The node is already present."