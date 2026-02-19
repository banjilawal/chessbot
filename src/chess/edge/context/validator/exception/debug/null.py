# src/chess/edge/context/validator/exception/debug/null.py

"""
Module: chess.edge.context.validator.exception.debug.null
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from chess.system import NullException
from chess.edge import EdgeContextException

__all__ = [
    # ======================# NULL_EDGE_CONTEXT EXCEPTION #======================#
    "NullEdgeContextException",
]


# ======================# NULL_EDGE_CONTEXT EXCEPTION #======================#
class NullEdgeContextException(EdgeContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its validation as a EdgeContext because it was null.

    # PARENT:
        *   EdgeContextException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_EDGE_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "EdgeContext validation failed: The candidate was null."