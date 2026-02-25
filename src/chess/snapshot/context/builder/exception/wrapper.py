# src/chess/snapshot/builder/exception.py

"""
Module: chess.snapshot.builder.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import BuildException
from chess.snapshot import SnapshotContextException

__all__ = [
    # ======================# SNAPSHOT_CONTEXT_BUILD_FAILURE #======================#
    "SnapshotContextBuildException",
]


# ======================# SNAPSHOT_CONTEXT_BUILD_FAILURE #======================#
class SnapshotContextBuildException(SnapshotContextException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the SnapshotContext build creates an exception. Failed check exceptions are encapsulated
        in an SnapshotContextBuildException which is sent to the caller in a BuildResult.
    2.  The SnapshotContextBuildException provides a trace for debugging and application recovery.

    # PARENT:
        *   SnapshotContextException
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SNAPSHOT_CONTEXT_BUILD_FAILED"
    MSG = "SnapshotContext build failed."