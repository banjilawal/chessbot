# src/logic/edge/schema/exception/context/exist.py

"""
Module: logic.edge.schema.exception.context.exist
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""



__all__ = [
    # ======================# EDGE_NOT_FOUND EXCEPTION #======================#
    "EdgeNotFoundException",
]

from microservice.edge import EdgeDebugException


# ======================# EDGE_NOT_FOUND EXCEPTION #======================#
class EdgeNotFoundException(EdgeDebugException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attempt to remove instances of a item by a unique attribute failed because no bag
        matching the property were found in the collider_candidates.

    Super Class:
        *   NullException
        *   EdgeStackException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "EDGE_NOT_FOUND_EXCEPTION"
    MSG = "Edge deletion failed: The item was not found in the collider_candidates. Nothing to remove."