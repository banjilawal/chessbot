# src/chess/snapshot/finder/exception/base.py

"""
Module: chess.snapshot.finder.exception.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import FinderException, OperationFailedException

__all__ = [
    # ======================# SNAPSHOT_FINDER EXCEPTION #======================#
    "SnapshotFinderException",
]


# ======================# SNAPSHOT_FINDER EXCEPTION #======================#
class SnapshotFinderException(FinderException, OperationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Parent of exception raised by GameFinder objects.
    2.  Wraps an exception that hits the try-finally block of an SnapshotFinder method.

    # PARENT:
        *   SnapshotException
        *   FinderException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SNAPSHOT_FINDER_ERROR"
    DEFAULT_MESSAGE = "SnapshotFinder raised an exception."