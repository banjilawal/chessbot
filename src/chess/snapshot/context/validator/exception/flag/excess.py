# src/chess/snapshot/map/validator/experience/flag/exception.py

"""
Module: chess.snapshot.map.validator.experience.flag.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.snapshot import InvalidSnapshotContextException


__all__ = [
    # ========================= EXCESSIVE_SNAPSHOT_CONTEXT_FLAGS EXCEPTION =========================#
    "ExcessiveSnapshotContextFlagsException",
]


# ========================= EXCESSIVE_SNAPSHOT_CONTEXT_FLAGS EXCEPTION =========================#
class ExcessiveSnapshotContextFlagsException(InvalidSnapshotContextException, ContextFlagCountException):
    """
    # ROLE: ContextFlagException, SnapshotContextException

    # RESPONSIBILITIES:
    1.  Indicate if more than one Game attribute is going to be used in an SnapshotFinder.

    # PARENT:
        *   InvalidSnapshotContextException
        *   ContextFlagCountException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOO_MANY_GAME_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "More than one SnapshotContext flag was selected. Only one map flag is allowed."