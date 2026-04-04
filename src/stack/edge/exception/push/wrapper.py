# src/logic/edge/schema/exception/push/validator.py

"""
Module: logic.edge.schema.exception.push.work
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

__all__ = [
    # ======================# EDGE_INSERTION_FAILURE #======================#
    "PushingEdgeException",
]

from graph.edge import EdgeStackException
from system import InsertionException


# ======================# EDGE_INSERTION_FAILURE #======================#
class PushingEdgeException(EdgeStackException, InsertionException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Indicate that pushing a Edge on the Stack failed.

    Super Class:
        *   EdgeStackException
        *   InsertionException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "EDGE_INSERTION_FAILURE"
    MSG = "Edge insertion failed."