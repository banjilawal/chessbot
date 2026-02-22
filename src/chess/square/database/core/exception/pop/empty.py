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

from chess.square import SquareStackException


# ======================# POPPING_EMPTY_SQUARE_STACK EXCEPTION #======================#
class PoppingEmptySquareStackException(SquareStackException):
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
    DEFAULT_MESSAGE = "Popping SquareStackService failed: Cannot pop squares from an empty stack."