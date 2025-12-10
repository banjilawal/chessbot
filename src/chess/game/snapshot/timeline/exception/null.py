# src/chess/game/snapshot/timeline/exception/null/__init__.py

"""
Module: chess.game.snapshot.timeline.exception.null.__init__
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import NullException
from chess.game import InvalidGameTimelineException

__all__ = [
    "NullGameTimelineException",
]


# ======================# NULL GAME_TIMELINE EXCEPTION #======================#
class NullGameTimelineException(InvalidGameTimelineException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate if an entity, method or operation required an GameTimeline but got null instead.

    # PARENT
        *   InvalidGameTimelineException
        *   NullException

    # PROVIDES:
    NullGameTimelineException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_GAME_TIMELINE_ERROR"
    DEFAULT_MESSAGE = "GameTimeline cannot be null."
