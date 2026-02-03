# src/chess/square/database/core/exception/deletion/empty.py

"""
Module: chess.square.database.core.exception.deletion.empty
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""



__all__ = [
    # ======================# POPPING_EMPTY_SQUARE_STACK EXCEPTION #======================#
    "PoppingEmptySquareStackException",
]

from chess.square import SquareDebugException
from chess.system import PoppingEmptyStackException


# ======================# POPPING_EMPTY_SQUARE_STACK EXCEPTION #======================#
class PoppingEmptySquareStackException(SquareDebugException, PoppingEmptyStackException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove a item failed because the stack was empty

    # PARENT:
        *   SquareException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "POPPING_EMPTY_SQUARE_STACK_ERROR"
    DEFAULT_MESSAGE = "Square deletion failed: SquareStack does not own any squares."