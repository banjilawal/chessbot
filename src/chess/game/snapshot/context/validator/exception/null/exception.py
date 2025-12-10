# src/chess/game/snapshot/context/validator/experience/null/exception.py

"""
Module: chess.game.snapshot.context.validator.experience.null.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import NullException
from chess.game import InvalidGameSnapshotContextException

__all__ = [
    # ======================# GAME_CONTEXT NULL EXCEPTIONS #======================#
    "NullGameSnapshotContextException",
]


# ======================# GAME_CONTEXT NULL EXCEPTIONS #======================#
class NullGameSnapshotContextException(InvalidGameSnapshotContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an GameSnapshotContext validation candidate is null.
    2.  Raised if an entity, method or operation requires an GameSnapshotContext but receives null instead.

    # PARENT:
        *   InvalidGameSnapshotContextException
        *   NullGameSnapshotContextException

    # PROVIDES:
    NullGameSnapshotContextException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_GAME_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "GameSnapshotContext cannot be null."


