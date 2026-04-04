# src/logic/edge/schema/exception/pop/validator.py

"""
Module: logic.edge.schema.exception.pop.work
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# EDGE_DELETION_FAILURE #======================#
    "PoppingEdgeException",
]

from graph.edge import EdgeStackException
from logic.system import DeletionException


# ======================# EDGE_DELETION_FAILURE #======================#
class PoppingEdgeException(EdgeStackException, DeletionException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Wrap debug exceptions indicating why a EdgeStack deletion fails. The encapsulated exceptions create
        chain for tracing the source of the failure.

    Super Class:
        *   EdgeStackException
        *   DeletionException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "EDGE_DELETION_FAILURE"
    MSG = "Edge deletion failed."