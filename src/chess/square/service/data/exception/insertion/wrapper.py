# src/chess/square/service/data/exception/insertion/wrapper.py

"""
Module: chess.square.service.data.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_INSERTION_FAILURE #======================#
    "SquareInsertionFailedException",
]

from chess.square import SquareDataServiceException


# ======================# SQUARE_INSERTION_FAILURE #======================#
class SquareInsertionFailedException(SquareDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that add a token to the roster failed.

    # PARENT:
        *   SquareDataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_INSERTION_FAILURE_ERROR"
    DEFAULT_MESSAGE = "Square insertion failed."