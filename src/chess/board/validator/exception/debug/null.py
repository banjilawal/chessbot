# src/chess/board/validator/exception/null.py

"""
Module: chess.board.validator.exception.null
Author: Banji Lawal
Created: 2025-11-19
Version: 1.0.0
"""

__all__ = [
    # ======================# NULL_BOARD EXCEPTION #======================#
    "NullBoardException",
]

from chess.system import NullException
from chess.board import BoardDebugException


# ======================# NULL_BOARD EXCEPTION #======================#
class NullBoardException(BoardDebugException, NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failing ValidationResult was returned because the candidate was null.

    # PARENT:
        *   BoardDebugException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_BOARD_ERROR"
    DEFAULT_MESSAGE = "Board validation failed: The candidate cannot be null."