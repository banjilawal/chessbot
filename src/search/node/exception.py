# src/logic/node/context/exception.py

"""
Module: logic.node.context.exception
Author: Banji Lawal
Created: 2026-02-19
version: 1.0.0
"""

from model.graph.node import NodeException
from system import ContextException

__all__ = [
    # ======================# NODE_CONTEXT EXCEPTION #======================#
    "NodeContextException",
]


# ======================# NODE_CONTEXT EXCEPTION #======================#
class NodeContextException(NodeException, ContextException):
    """
    Role:Super Exception

    Responsibilities:
    1.  Super for NodeContext errors not covered by NodeException subclasses.

    Super Class:
        *   NodeException
        *   ContextException

    Provides:

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "NODE_CONTEXT_EXCEPTION"
    MSG = "NodeContext raised an exception."
    