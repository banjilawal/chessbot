# src/logic/node/stack/exception/pop/wrapper.py

"""
Module: logic.node.stack.exception.pop.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# NODE_DELETION_FAILURE #======================#
    "NodePopException",
]

from logic.node import NodeStackException
from logic.system import DeletionException


# ======================# NODE_DELETION_FAILURE #======================#
class NodePopException(NodeStackException, DeletionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a NodeStack deletion fails. The encapsulated exceptions create
        chain for tracing the source of the failure.

    # PARENT:
        *   NodeStackException
        *   DeletionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NODE_DELETION_FAILURE"
    MSG = "Node deletion failed."