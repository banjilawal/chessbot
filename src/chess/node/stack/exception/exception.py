# src/chess/node/exception/__init__.py

"""
Module: chess.node.exception.__init__
Author: Banji Lawal
Created: 2025-02-18
version: 1.0.0
"""

___all__ = [
    # ======================# NODE_STACK EXCEPTION #======================#
    "NodeStackException",
]

from chess.node import NodeException
from chess.system import StackException


# ======================# NODE_STACK EXCEPTION #======================#
class NodeStackException(NodeException, StackException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wrap any exceptions raised by NodeStack methods that return Result objects.

    # PARENT:
        *   NodeException
        *   StackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NODE_STACK_ERROR"
    DEFAULT_MESSAGE = "NodeStack raised an exception."