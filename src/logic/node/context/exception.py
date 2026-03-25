# src/logic/node/query/exception.py

"""
Module: logic.node.query.exception
Author: Banji Lawal
Created: 2026-02-19
version: 1.0.0
"""

from logic.node import NodeException
from logic.system import ContextException

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
    