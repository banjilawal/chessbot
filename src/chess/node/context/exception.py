# src/chess/node/context/exception.py

"""
Module: chess.node.context.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.node import NodeException
from chess.system import ContextException

__all__ = [
    # ======================# NODE_CONTEXT EXCEPTION #======================#
    "NodeContextException",
]


# ======================# NODE_CONTEXT EXCEPTION #======================#
class NodeContextException(NodeException, ContextException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for NodeContext errors not covered by NodeException subclasses.

    # PARENT:
        *   NodeException
        *   ContextException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NODE_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "NodeContext raised an exception."
    