# src/chess/edge/stack/exception/pop/wrapper.py

"""
Module: chess.edge.stack.exception.pop.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# EDGE_DELETION_FAILURE #======================#
    "PoppingEdgeException",
]

from chess.edge import EdgeStackException
from chess.system import DeletionException


# ======================# EDGE_DELETION_FAILURE #======================#
class PoppingEdgeException(EdgeStackException, DeletionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a EdgeStack deletion fails. The encapsulated exceptions create
        chain for tracing the source of the failure.

    # PARENT:
        *   EdgeStackException
        *   DeletionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EDGE_DELETION_FAILURE"
    DEFAULT_MESSAGE = "Edge deletion failed."