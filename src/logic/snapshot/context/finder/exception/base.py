# src/logic/snapshot/finder/exception/base.py

"""
Module: logic.snapshot.finder.exception.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from logic.system import FinderException, OperationException

__all__ = [
    # ======================# SNAPSHOT_FINDER EXCEPTION #======================#
    "SnapshotFinderException",
]


# ======================# SNAPSHOT_FINDER EXCEPTION #======================#
class SnapshotFinderException(FinderException, OperationException):
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
    ERR_CODE = "SNAPSHOT_FINDER_EXCEPTION"
    MSG = "SnapshotFinder raised an exception."