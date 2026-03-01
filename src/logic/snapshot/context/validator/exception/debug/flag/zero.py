# src/logic/snapshot/validator/experience/flag/exception.py

"""
Module: logic.snapshot.validator.experience.flag.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from logic.system import ContextFlagCountException
from logic.game import InvalidSnapshotContextException

__all__ = [
    # ========================= NO_GAME_CONTEXT_FLAG EXCEPTION =========================#
    "ZeroSnapshotContextFlagsException",
]


# ========================= NO_GAME_CONTEXT_FLAG EXCEPTION =========================#
class ZeroSnapshotContextFlagsException(InvalidSnapshotContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate no SnapshotContext flag is provided with a searcher value.

    # PARENT:
        *   SnapshotContextValidationException
        *   ContextFlagCountException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_GAME_CONTEXT_FLAG_EXCEPTION"
    MSG = "No SnapshotContext flag was selected. A map flag must be turned on with a target value."