# src/chess/snapshot/validator/exception/null.py

"""
Module: chess.snapshot.validator.exception.null
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_SNAPSHOT_CONTEXT EXCEPTION #======================#
    "NullSnapshotContextException",
]

from chess.system import NullException
from chess.snapshot import InvalidSnapshotContextException


# ======================# NULL_SNAPSHOT_CONTEXT EXCEPTION #======================#
class NullSnapshotContextException(InvalidSnapshotContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that SnapshotContext validation failed because the candidate was null.

    # PARENT:
        *   NullSnapshotContextException
        *   InvalidSnapshotContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_SNAPSHOT_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "SnapshotContext validation failed: The candidate was null."