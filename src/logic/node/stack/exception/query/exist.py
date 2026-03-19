# src/logic/node/stack/exception/query/exist.py

"""
Module: logic.node.stack.exception.query.exist
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""



__all__ = [
    # ======================# NODE_NOT_FOUND EXCEPTION #======================#
    "NodeNotFoundException",
]

from logic.node import NodeDebugException


# ======================# NODE_NOT_FOUND EXCEPTION #======================#
class NodeNotFoundException(NodeDebugException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attempt to remove instances of a item by a unique attribute failed because no bag
        matching the property were found in the collider_candidates.

    Super Class:
        *   NullException
        *   NodeStackException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NODE_NOT_FOUND_EXCEPTION"
    MSG = "Node deletion failed: The item was not found in the collider_candidates. Nothing to remove."