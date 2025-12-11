# src/chess/game/snapshot/context/validator/experience/flag/exception.py

"""
Module: chess.game.snapshot.context.validator.experience.flag.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.game import InvalidGameSnapshotContextException

__all__ = [
    # ========================= NO_GAME_CONTEXT_FLAG EXCEPTION =========================#
    "NoGameSnapshotContextFlagException",
    # ========================= TOO_MANY_GAME_CONTEXT_FLAGS EXCEPTION =========================#
    "TooManyGameSnapshotContextFlagsException"
]


# ========================= NO_GAME_CONTEXT_FLAG EXCEPTION =========================#
class NoGameSnapshotContextFlagException(InvalidGameSnapshotContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate no GameSnapshotContext flag is provided with a searcher value.

    # PARENT:
        *   InvalidGameSnapshotContextException
        *   ContextFlagCountException

    # PROVIDES:
    NoGameSnapshotContextFlagException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_GAME_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = "No GameSnapshotContext flag was selected. A context flag must be turned on with a target value."


# ========================= TOO_MANY_GAME_CONTEXT_FLAGS EXCEPTION =========================#
class TooManyGameSnapshotContextFlagsException(InvalidGameSnapshotContextException, ContextFlagCountException):
    """
    # ROLE: ContextFlagException, GameSnapshotContextException

    # RESPONSIBILITIES:
    1.  Indicate if more than one Game attribute is going to be used in an GameSnapshotFinder.

    # PARENT:
        *   InvalidGameSnapshotContextException
        *   ContextFlagCountException

    # PROVIDES:
    TooManyGameSnapshotContextFlagsException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOO_MANY_GAME_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "More than one GameSnapshotContext flag was selected. Only one context flag is allowed."