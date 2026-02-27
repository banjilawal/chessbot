# src/chess/edge/exception/__init__.py

"""
Module: chess.edge.exception.__init__
Author: Banji Lawal
Created: 2025-02-18
version: 1.0.0
"""

___all__ = [
    # ======================# EDGE_STACK EXCEPTION #======================#
    "EdgeStackException",
]

from chess.edge import EdgeException
from chess.system import StackServiceException


# ======================# EDGE_STACK EXCEPTION #======================#
class EdgeStackException(EdgeException, StackServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap any exceptions raised by EdgeStack methods that return Result objects.

    # PARENT:
        *   EdgeException
        *   StackServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "EDGE_STACK_EXCEPTION"
    MSG = "EdgeStack raised an exception."