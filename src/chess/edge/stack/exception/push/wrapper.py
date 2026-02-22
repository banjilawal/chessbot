# src/chess/edge/stack/exception/push/wrapper.py

"""
Module: chess.edge.stack.exception.push.wrapper
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

__all__ = [
    # ======================# EDGE_INSERTION_FAILURE #======================#
    "PushingEdgeException",
]

from chess.edge import EdgeStackException
from chess.system import InsertionException


# ======================# EDGE_INSERTION_FAILURE #======================#
class PushingEdgeException(EdgeStackException, InsertionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that pushing a Edge on the Stack failed.

    # PARENT:
        *   EdgeStackException
        *   InsertionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EDGE_INSERTION_FAILURE"
    DEFAULT_MESSAGE = "Edge insertion failed."