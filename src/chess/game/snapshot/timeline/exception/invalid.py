# src/chess/game/snapshot/timeline/exception/invalid/__init__.py

"""
Module: chess.game.snapshot.timeline.exception.invalid.__init__
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.game import GameTimelineException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# GAME_TIMELINE VALIDATION EXCEPTIONS #======================#
    "InvalidGameTimelineException",
]




# ======================# GAME_TIMELINE VALIDATION EXCEPTIONS #======================#
class InvalidGameTimelineException(GameTimelineException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during GameTimeline verification process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an GameTimelineValidator method.

    # PARENT:
        *   GameTimelineException
        *   ValidationFailedException

    # PROVIDES:
    InvalidGameTimelineException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_TIMELINE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "GameTimeline validation failed."