# src/chess/graph/exception.py

"""
Module: chess.graph.exception
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

__all__ = [
    # ======================# GRAPH EXCEPTION #======================#
    "GraphException",
]

from chess.system import SuperClassException


# ======================# GRAPH EXCEPTION #======================#
class GraphException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of GraphDebugException

  # PARENT:
      *   SuperClassException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERROR_CODE = "GRAPH_ERROR"
    DEFAULT_MESSAGE = "Graph raised an exception."