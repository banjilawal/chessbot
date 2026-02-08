# src/chess/board/database/core/exception/deletion/wrapper.py

"""
Module: chess.board.database.core.exception.deletion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_DELETION_FAILURE EXCEPTION #======================#
    "BoardDeletionFailedException",
]

from chess.board import BoardException
from chess.system import DeletionFailedException


# ======================# BOARD_DELETION_FAILURE EXCEPTION #======================#
class BoardDeletionFailedException(BoardException, DeletionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a BoardStack deletion fails. The encapsulated exceptions create
        chain for tracing the source of the failure.

    # PARENT:
        *   BoardException
        *   DeletionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_DELETION_FAILURE"
    DEFAULT_MESSAGE = "Board deletion failed."