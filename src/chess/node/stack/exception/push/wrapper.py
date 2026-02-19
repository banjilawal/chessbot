# src/chess/node/stack/exception/push/wrapper.py

"""
Module: chess.node.stack.exception.push.wrapper
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

__all__ = [
    # ======================# NODE_INSERTION_FAILURE #======================#
    "NodePushException",
]

from chess.node import NodeStackException
from chess.system import InsertionFailedException


# ======================# NODE_INSERTION_FAILURE #======================#
class NodePushException(NodeStackException, InsertionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that pushing a Node on the Stack failed.

    # PARENT:
        *   NodeStackException
        *   InsertionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NODE_INSERTION_FAILURE_ERROR"
    DEFAULT_MESSAGE = "Node insertion failed."