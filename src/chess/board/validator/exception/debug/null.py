# src/chess/board/validator/exception/null.py

"""
Module: chess.board.validator.exception.null
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.system import NullException
from chess.board import BoardValidationException

__all__ = [
    # ======================# NULL_BOARD EXCEPTION #======================#
    "NullBoardException",
]


# ======================# NULL_BOARD EXCEPTION #======================#
class NullBoardException(BoardValidationException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if a Board validation candidate is null.
    2.  Raised if an entity, method or operation requires a Board but receives null instead.

    # PARENT:
        *   NullBoardException
        *   BoardValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_BOARD___ERROR"
    DEFAULT_MESSAGE = "Board cannot be null."