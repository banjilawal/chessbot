# src/chess/snapshot/timeline/exception/base/__init__.py

"""
Module: chess.snapshot.timeline.exception.base.__init__
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# GAME_TIMELINE EXCEPTION #======================#
    "GameTimelineException",
]


# ======================# GAME_TIMELINE EXCEPTION #======================#
class GameTimelineException(ResultStackException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Parent of exception raised by GameTimeline objects.
    2.  Parent of exception raised by classes that highly cohere with GameTimeline objects.
    3.  Super for GameTimeline errors not covered by lower level  GameTimeline exception.

    # PARENT:
        *   ResultStackException

    # PROVIDES:
    GameTimelineException

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "GAME_TIMELINE_EXCEPTION"
    DEFAULT_ERR_CODE = "GameTimeline raised an exception."