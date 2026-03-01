# src/logic/snapshot/validator/experience/flag/exception.py

"""
Module: logic.snapshot.validator.experience.flag.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from logic.system import ContextFlagCountException
from logic.snapshot import InvalidSnapshotContextException


__all__ = [
    # ========================= ARENA_SNAPSHOT_CONTEXT_FLAGS EXCEPTION =========================#
    "ArenaSnapshotContextFlagsException",
]


# ========================= ARENA_SNAPSHOT_CONTEXT_FLAGS EXCEPTION =========================#
class ArenaSnapshotContextFlagsException(InvalidSnapshotContextException, ContextFlagCountException):
    """
    # ROLE: ContextFlagException, SnapshotContextException

    # RESPONSIBILITIES:
    1.  Indicate if more than one Game attribute is going to be used in an SnapshotFinder.

    # PARENT:
        *   SnapshotContextValidationException
        *   ContextFlagCountException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "TOO_MANY_GAME_CONTEXT_FLAGS_EXCEPTION"
    MSG = "More than one SnapshotContext flag was selected. Only one map flag is allowed."