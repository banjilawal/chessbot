# src/chess/node/exception.py

"""
Module: chess.node.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# NODE EXCEPTION #======================#
    "NodeException",
]

from chess.system import SuperClassException


# ======================# NODE EXCEPTION #======================#
class NodeException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of NodeDebugException

  # PARENT:
      *   SuperClassException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERROR_CODE = "NODE_ERROR"
    DEFAULT_MESSAGE = "Node raised an exception."