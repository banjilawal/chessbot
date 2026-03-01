# src/logic/node/stack/exception/push/wrapper.py

"""
Module: logic.node.stack.exception.push.wrapper
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

__all__ = [
    # ======================# NODE_INSERTION_FAILURE #======================#
    "NodePushException",
]

from logic.node import NodeStackException
from logic.system import InsertionException


# ======================# NODE_INSERTION_FAILURE #======================#
class NodePushException(NodeStackException, InsertionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that pushing a Node on the Stack failed.

    # PARENT:
        *   NodeStackException
        *   InsertionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NODE_INSERTION_FAILURE"
    MSG = "Node insertion failed."