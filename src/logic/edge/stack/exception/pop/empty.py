# src/logic/edge/schema/exception/pop/empty.py

"""
Module: logic.edge.schema.exception.pop.empty
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""



__all__ = [
    # ======================# POPPING_EMPTY_EDGE_STACK EXCEPTION #======================#
    "PoppingEmptyEdgeStackException",
]

from logic.edge import EdgeDebugException
from logic.system import PoppingEmptyStackException


# ======================# POPPING_EMPTY_EDGE_STACK EXCEPTION #======================#
class PoppingEmptyEdgeStackException(EdgeDebugException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attempt to remove a item failed because the schema was empty

    Super Class:
        *   EdgeException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "POPPING_EMPTY_EDGE_STACK_EXCEPTION"
    MSG = "Edge deletion failed: EdgeStack does not own any edges."