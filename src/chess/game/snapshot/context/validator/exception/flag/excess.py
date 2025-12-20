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
    # ========================= TOO_MANY_GAME_CONTEXT_FLAGS EXCEPTION =========================#
    "ExcessiveGameSnapshotContextFlagsException",
]


# ========================= TOO_MANY_GAME_CONTEXT_FLAGS EXCEPTION =========================#
class ExcessiveGameSnapshotContextFlagsException(InvalidGameSnapshotContextException, ContextFlagCountException):
    """
    # ROLE: ContextFlagException, GameSnapshotContextException

    # RESPONSIBILITIES:
    1.  Indicate if more than one Game attribute is going to be used in an GameSnapshotFinder.

    # PARENT:
        *   InvalidGameSnapshotContextException
        *   ContextFlagCountException

    # PROVIDES:
    ExcessiveGameSnapshotContextFlagsException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOO_MANY_GAME_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "More than one GameSnapshotContext flag was selected. Only one context flag is allowed."