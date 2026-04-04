# src/logic/node/schema/exception/push/validator.py

"""
Module: logic.node.schema.exception.push.work
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

__all__ = [
    # ======================# NODE_INSERTION_FAILURE #======================#
    "NodePushException",
]

from graph.node import NodeStackException
from logic.system import InsertionException


# ======================# NODE_INSERTION_FAILURE #======================#
class NodePushException(NodeStackException, InsertionException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Indicate that pushing a Node on the Stack failed.

    Super Class:
        *   NodeStackException
        *   InsertionException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NODE_INSERTION_FAILURE"
    MSG = "Node insertion failed."