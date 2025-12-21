# src/chess/snapshot/finder/exception.py

"""
Module: chess.snapshot.finder.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import FinderException

__all__ = [
    # ======================# SNAPSHOT_FINDER EXCEPTION #======================#
    "SnapshotFinderException",
]


# ======================# SNAPSHOT_FINDER EXCEPTION #======================#
class SnapshotFinderException(FinderException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by GameFinder objects.
    2.  Wraps unhandled exception that hit the try-finally block of an SnapshotFinder method.

    # PARENT:
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