# src/chess/snapshot/exception.py

"""
Module: chess.snapshot.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ContextException
from chess.snapshot import SnapshotException


__all__ = [
    # ======================# SNAPSHOT_CONTEXT EXCEPTION #======================#
    "SnapshotContextException",
]


# ======================# SNAPSHOT_CONTEXT EXCEPTION #======================#
class SnapshotContextException(SnapshotException, ContextException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Parent of exception raised by SnapshotContext objects.
    2.  Catchall for conditions which are not covered by lower level SnapshotContext exception.

    # PARENT:
        *   ContextException
        *   SnapshotException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SNAPSHOT_CONTEXT_ERROR"
    DEFAULT_ERR_CODE = "SnapshotContext raised an exception."