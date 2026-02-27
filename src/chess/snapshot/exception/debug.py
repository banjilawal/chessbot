# src/chess/snapshot/exception/debug.py

"""
Module: chess.snapshot.exception.debug
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""


__all__ = [
    # ======================# SNAPSHOT_DEBUG EXCEPTION #======================#
    "SnapshotDebugException",
]

from chess.snapshot import SnapshotException
from chess.system import DebugException


# ======================# SNAPSHOT_DEBUG EXCEPTION #======================#
class SnapshotDebugException(SnapshotException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Snapshot operation failure.

    # PARENT:
        *   SnapshotException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERR_CODE = "SNAPSHOT_DEBUG_EXCEPTION"
    MSG = "A SnapshotDebugException was raised."