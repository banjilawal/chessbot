# src/chess/square/service/data/exception/insertion/wrapper.py

"""
Module: chess.square.service.data.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# UNIQUE_SQUARE_INSERTION_FAILURE EXCEPTION #======================#
    "UniqueSquareInsertionFailedException",
]

from chess.square import SquareException
from chess.system import InsertionFailedException


# ======================# UNIQUE_SQUARE_INSERTION_FAILURE EXCEPTION #======================#
class UniqueSquareInsertionFailedException(SquareException, InsertionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why inserting a unique square failed. The encapsulated exceptions create 
        chain for tracing the source of the failure.

    # PARENT:
        *   SquareException
        *   InsertionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_SQUARE_INSERTION_FAILURE"
    DEFAULT_MESSAGE = "Unique square insertion failed."