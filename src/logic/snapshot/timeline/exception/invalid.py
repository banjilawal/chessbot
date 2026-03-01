# src/logic/snapshot/timeline/exception/invalid/__init__.py

"""
Module: logic.snapshot.timeline.exception.invalid.__init__
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from logic.game import GameTimelineException
from logic.system import ValidationException

__all__ = [
    # ======================# GAME_TIMELINE VALIDATION EXCEPTION #======================#
    "InvalidGameTimelineException",
]




# ======================# GAME_TIMELINE VALIDATION EXCEPTION #======================#
class InvalidGameTimelineException(GameTimelineException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Parent of exception raised during GameTimeline verification process.
    2.  Wraps an exception that hits the try-finally block of an GameTimelineValidator method.

    # PARENT:
        *   GameTimelineException
        *   ValidationException

    # PROVIDES:
    InvalidGameTimelineException

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "GAME_TIMELINE_VALIDATION_EXCEPTION"
    MSG = "GameTimeline validation failed."