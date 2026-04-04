# src/logic/snapshot/timeline/exception/null/__init__.py

"""
Module: logic.snapshot.timeline.exception.null.__init__
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from system import NullException
from model.game import InvalidGameTimelineException

__all__ = [
    "NullGameTimelineException",
]


# ======================# NULL GAME_TIMELINE EXCEPTION #======================#
class NullGameTimelineException(InvalidGameTimelineException, NullException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate if an entity, method or operation required an GameTimeline but got null instead.

    Super Class:
        *   InvalidGameTimelineException
        *   NullException

    # PROVIDES:
    NullGameTimelineException

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "NULL_GAME_TIMELINE_EXCEPTION"
    MSG = "GameTimeline cannot be null."
