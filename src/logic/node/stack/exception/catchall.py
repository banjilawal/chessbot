# src/logic/node/exception/__init__.py

"""
Module: logic.node.exception.__init__
Author: Banji Lawal
Created: 2025-02-18
version: 1.0.0
"""

___all__ = [
    # ======================# NODE_STACK EXCEPTION #======================#
    "NodeStackException",
]

from logic.node import NodeException
from logic.system import StackServiceException


# ======================# NODE_STACK EXCEPTION #======================#
class NodeStackException(NodeException, StackServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap any exceptions raised by NodeStackService methods that return Result objects.

    # PARENT:
        *   NodeException
        *   StackServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NODE_STACK_EXCEPTION"
    MSG = "NodeStackService raised an exception."