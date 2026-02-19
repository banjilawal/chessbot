# src/chess/edge/stack/exception/pop/exist.py

"""
Module: chess.edge.stack.exception.pop.exist
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""



__all__ = [
    # ======================# EDGE_NOT_FOUND EXCEPTION #======================#
    "EdgeNotFoundException",
]

from chess.edge import EdgeStackException
from chess.system import NullException


# ======================# EDGE_NOT_FOUND EXCEPTION #======================#
class EdgeNotFoundException(EdgeStackException, NullException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove instances of a item by a unique attribute failed because no bag
        matching the property were found in the dataset.

    # PARENT:
        *   NullException
        *   EdgeStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EDGE_NOT_FOUND_ERROR"
    DEFAULT_MESSAGE = "Edge deletion failed: The item was not found in the dataset. Nothing to remove."