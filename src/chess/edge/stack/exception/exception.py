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
from chess.system import StackException


# ======================# EDGE_STACK EXCEPTION #======================#
class EdgeStackException(EdgeException, StackException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wrap any exceptions raised by EdgeStack methods that return Result objects.

    # PARENT:
        *   EdgeException
        *   StackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EDGE_STACK_ERROR"
    DEFAULT_MESSAGE = "EdgeStack raised an exception."