# src/chess/square/database/core/exception/insertion/name.py

"""
Module: chess.square.database.core.exception.insertion.name
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# NAME_ALREADY_USED_IN_SQUARE_DATASET EXCEPTION #======================#
    "SquareNameAlreadyInUseException",
]

from chess.square import SquareStackException


# ======================# NAME_ALREADY_USED_IN_SQUARE_DATASET EXCEPTION #======================#
class SquareNameAlreadyInUseException(SquareStackException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that inserting a item failed because the name was already in use by a collection member.

    # PARENT:
        *   SquareStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NAME_ALREADY_USED_IN_SQUARE_DATASET_ERROR"
    DEFAULT_MESSAGE = "Square insertion failed: Another item is already using the name."