# src/chess/snapshot/exception.py

"""
Module: chess.snapshot.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# SNAPSHOT EXCEPTION #======================#
    "SnapshotException",
]

from chess.system import SuperClassException


# ======================# SNAPSHOT EXCEPTION #======================#
class SnapshotException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of SnapshotDebugException

  # PARENT:
      *   SuperClassException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERR_CODE = "SNAPSHOT_ERROR"
    MSG = "Snapshot raised an exception."