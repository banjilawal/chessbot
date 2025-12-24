# src/chess/snapshot/builder/exception.py

"""
Module: chess.snapshot.builder.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.snapshot import SnapshotContextException

__all__ = [
    # ======================# SNAPSHOT_CONTEXT_BUILD_FAILED EXCEPTION #======================#
    "SnapshotContextBuildFailedException",
]


# ======================# SNAPSHOT_CONTEXT_BUILD_FAILED EXCEPTION #======================#
class SnapshotContextBuildFailedException(SnapshotContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the SnapshotContext build creates an exception. Failed check exceptions are encapsulated
        in an SnapshotContextBuildFailedException which is sent to the caller in a BuildResult.
    2.  The SnapshotContextBuildFailedException provides a trace for debugging and application recovery.tion recovery.

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
    ERROR_CODE = "SNAPSHOT_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "SnapshotContext build failed."