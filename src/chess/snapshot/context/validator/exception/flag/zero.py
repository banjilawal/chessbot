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
    "ZeroGameSnapshotContextFlagsException",
]


# ========================= NO_GAME_CONTEXT_FLAG EXCEPTION =========================#
class ZeroGameSnapshotContextFlagsException(InvalidGameSnapshotContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate no GameSnapshotContext flag is provided with a searcher value.

    # PARENT:
        *   InvalidGameSnapshotContextException
        *   ContextFlagCountException

    # PROVIDES:
    ZeroGameSnapshotContextFlagsException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_GAME_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = "No GameSnapshotContext flag was selected. A context flag must be turned on with a target value."