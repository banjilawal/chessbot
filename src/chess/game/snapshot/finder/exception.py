# src/chess/game/snapshot/finder/exception.py

"""
Module: chess.game.snapshot.finder.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import FinderException

__all__ = [
    # ======================# GAME_SNAPSHOT_FINDER EXCEPTIONS #======================#
    "GameSnapshotFinderException",
]


# ======================# GAME_SNAPSHOT_FINDER EXCEPTIONS #======================#
class GameSnapshotFinderException(FinderException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by GameFinder objects.
    2.  Wraps unhandled exceptions that hit the try-finally block of an GameSnapshotFinder method.

    # PARENT
        *   FinderException

    # PROVIDES:
    GameSnapshotFinderException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_SNAPSHOT_FINDER_ERROR"
    DEFAULT_MESSAGE = "GameSnapshotFinder raised an exception."