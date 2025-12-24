# src/chess/snapshot/builder/exception.py

"""
Module: chess.snapshot.builder.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# SNAPSHOT_BUILD_FAILED EXCEPTION #======================#
    "SnapshotBuildFailedException",
]

from chess.snapshot import SnapshotException
from chess.system import BuildFailedException


# ======================# SNAPSHOT_BUILD_FAILED EXCEPTION #======================#
class SnapshotBuildFailedException(SnapshotException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the Snapshot build creates an exception. Failed check exceptions are encapsulated
        in an SnapshotBuildFailedException which is sent to the caller in a BuildResult.
    2.  The SnapshotBuildFailedException provides a trace for debugging and application recovery.tion recovery.

    # PARENT:
        *   SnapshotException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SNAPSHOT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Snapshot build failed."