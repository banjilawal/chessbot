# src/chess/node/stack/exception/pop/empty.py

"""
Module: chess.node.stack.exception.pop.empty
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""



__all__ = [
    # ======================# POPPING_EMPTY_NODE_STACK EXCEPTION #======================#
    "PoppingEmptyNodeStackException",
]

from chess.node import NodeDebugException
from chess.system import PoppingEmptyStackException


# ======================# POPPING_EMPTY_NODE_STACK EXCEPTION #======================#
class PoppingEmptyNodeStackException(NodeDebugException, PoppingEmptyStackException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove a item failed because the stack was empty

    # PARENT:
        *   NodeException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "POPPING_EMPTY_NODE_STACK_ERROR"
    DEFAULT_MESSAGE = "Node deletion failed: NodeStack does not own any nodes."