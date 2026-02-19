# src/chess/edge/context/exception.py

"""
Module: chess.edge.context.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.edge import EdgeException
from chess.system import ContextException

__all__ = [
    # ======================# EDGE_CONTEXT EXCEPTION #======================#
    "EdgeContextException",
]


# ======================# EDGE_CONTEXT EXCEPTION #======================#
class EdgeContextException(EdgeException, ContextException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for EdgeContext errors not covered by EdgeException subclasses.

    # PARENT:
        *   EdgeException
        *   ContextException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "EDGE_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "EdgeContext raised an exception."
    