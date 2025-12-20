# src/chess/snapshot/context/builder/exception.py

"""
Module: chess.snapshot.context.builder.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.system import BuildFailedException
from chess.game import GameSnapshotContextException

__all__ = [
    # ======================# SNAPSHOT_CONTEXT BUILD EXCEPTION #======================#
    "GameSnapshotContextBuildFailedException",
]


# ======================# SNAPSHOT_CONTEXT BUILD EXCEPTION #======================#
class GameSnapshotContextBuildFailedException(GameSnapshotContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised during GameSnapshotContext build process.
    2.  Wraps unhandled exception that hit the try-finally block of an GameSnapshotContextBuilder method.

    # PARENT:
        *   GameSnapshotContextException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SNAPSHOT_CONTEXT_BUILD_ERROR"
    DEFAULT_MESSAGE = "GameSnapshotContext build failed."