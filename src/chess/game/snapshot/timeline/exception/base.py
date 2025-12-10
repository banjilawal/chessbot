# src/chess/game/snapshot/timeline/exception/base/__init__.py

"""
Module: chess.game.snapshot.timeline.exception.base.__init__
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# GAME_TIMELINE EXCEPTIONS #======================#
    "GameTimelineException",
]


# ======================# GAME_TIMELINE EXCEPTIONS #======================#
class GameTimelineException(ResultStackException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by GameTimeline objects.
    2.  Parent of exceptions raised by classes that highly cohere with GameTimeline objects.
    3.  Catchall for GameTimeline failure states that are not covered by a lower level GameTimeline exception.

    # PARENT
        *   ResultStackException

    # PROVIDES:
    GameTimelineException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_TIMELINE_ERROR"
    DEFAULT_ERROR_CODE = "GameTimeline raised an exception."