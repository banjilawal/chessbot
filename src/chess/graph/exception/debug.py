# src/chess/graph/exception/debug.py

"""
Module: chess.graph.exception.debug
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""


__all__ = [
    # ======================# GRAPH_DEBUG EXCEPTION #======================#
    "GraphDebugException",
]

from chess.graph import GraphException
from chess.system import DebugException


# ======================# GRAPH_DEBUG EXCEPTION #======================#
class GraphDebugException(GraphException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Graph operation failure.

    # PARENT:
        *   GraphException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "GRAPH_DEBUG_ERROR"
    DEFAULT_MESSAGE = "A GraphDebugException was raised."