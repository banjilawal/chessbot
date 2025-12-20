# src/chessS/game/snapshot.base.py

"""
Module: chess.game/snapshot.exception
Author: Banji Lawal
Created: 2025-09-27
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# SNAPSHOT EXCEPTION #======================#
    "GameSnapshotException",
]


# ======================# SNAPSHOT EXCEPTION #======================#
class GameSnapshotException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by Snapshot objects.
    2.  Catchall for conditions which are not covered by lower level Snapshot exception.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SNAPSHOT_ERROR"
    DEFAULT_MESSAGE = "Snapshot raised an exception."