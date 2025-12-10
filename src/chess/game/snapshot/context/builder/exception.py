# src/chess/game/snapshot/context/builder/exception.py

"""
Module: chess.game.snapshot.context.builder.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.system import BuildFailedException
from chess.game import GameSnapshotContextException

__all__ = [
    # ======================# GAME_SNAPSHOT_CONTEXT BUILD EXCEPTIONS #======================#
    "GameSnapshotContextBuildFailedException",
]


# ======================# GAME_SNAPSHOT_CONTEXT BUILD EXCEPTIONS #======================#
class GameSnapshotContextBuildFailedException(GameSnapshotContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during GameSnapshotContext build process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an GameSnapshotContextBuilder method.

    # PARENT
        *   GameSnapshotContextException
        *   BuildFailedException

    # PROVIDES:
    GameSnapshotContextBuildFailedException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_SNAPSHOT_CONTEXT_BUILD_ERROR"
    DEFAULT_MESSAGE = "GameSnapshotContext build failed."