# src/chess/snapshot/validator/exception/null.py

"""
Module: chess.snapshot.validator.exception.null
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import NullException
from chess.game import InvalidSnapshotContextException

__all__ = [
    # ======================# GAME_CONTEXT NULL EXCEPTION #======================#
    "NullSnapshotContextException",
]


# ======================# GAME_CONTEXT NULL EXCEPTION #======================#
class NullSnapshotContextException(InvalidSnapshotContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an SnapshotContext validation candidate is null.
    2.  Raised if an entity, method or operation requires an SnapshotContext but receives null instead.

    # PARENT:
        *   InvalidSnapshotContextException
        *   NullSnapshotContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_GAME_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "SnapshotContext cannot be null."


