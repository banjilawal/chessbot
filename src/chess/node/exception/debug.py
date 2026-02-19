# src/chess/node/exception/debug.py

"""
Module: chess.node.exception.debug
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

__all__ = [
    # ======================# NODE_DEBUG EXCEPTION #======================#
    "NodeDebugException",
]

from chess.node import NodeException
from chess.system import DebugException


# ======================# NODE_DEBUG EXCEPTION #======================#
class NodeDebugException(NodeException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Node operation failure.

    # PARENT:
        *   NodeException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "NODE_DEBUG_ERROR"
    DEFAULT_MESSAGE = "A item debug error occurred."