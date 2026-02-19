# src/chess/node/stack/exception/pop/exist.py

"""
Module: chess.node.stack.exception.pop.exist
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""



__all__ = [
    # ======================# NODE_NOT_FOUND EXCEPTION #======================#
    "NodeNotFoundException",
]

from chess.node import NodeStackException
from chess.system import NullException


# ======================# NODE_NOT_FOUND EXCEPTION #======================#
class NodeNotFoundException(NodeStackException, NullException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove instances of a item by a unique attribute failed because no bag
        matching the property were found in the dataset.

    # PARENT:
        *   NullException
        *   NodeStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NODE_NOT_FOUND_ERROR"
    DEFAULT_MESSAGE = "Node deletion failed: The item was not found in the dataset. Nothing to remove."