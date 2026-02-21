# src/chess/edge/validator/exception/debug/null.py

"""
Module: chess.edge.validator.exception.debug.null
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_EDGE EXCEPTION #======================#
    "NullEdgeException",
]

from chess.system import NullException
from chess.edge import EdgeDebugException


# ======================# NULL_EDGE EXCEPTION #======================#
class NullEdgeException(EdgeDebugException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that an entity, method, or operation that required a Edge but got null instead.

    # PARENT:
        *   NullException
        *   EdgeDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_EDGE_ERROR"
    DEFAULT_MESSAGE = "Edge cannot be null."