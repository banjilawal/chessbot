# src/chess/snapshot/map/builder/exception.py

"""
Module: chess.snapshot.map.builder.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.system import BuildFailedException
from chess.game import SnapshotContextException

__all__ = [
    # ======================# SNAPSHOT_CONTEXT BUILD EXCEPTION #======================#
    "SnapshotContextBuildFailedException",
]


# ======================# SNAPSHOT_CONTEXT BUILD EXCEPTION #======================#
class SnapshotContextBuildFailedException(SnapshotContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised during SnapshotContext build process.
    2.  Wraps an exception that hits the try-finally block of an SnapshotContextBuilder method.

    # PARENT:
        *   SnapshotContextException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SNAPSHOT_CONTEXT_BUILD_ERROR"
    DEFAULT_MESSAGE = "SnapshotContext build failed."