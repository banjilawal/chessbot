# src/chess/square/service/detection/exception/debug/wrapper.py

"""
Module: chess.square.service.detection.exception.debug.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_PUSH_FAILURE #======================#
    "PushingSquareException",
]

from chess.system import InsertionException


# ======================# SQUARE_PUSH_FAILURE #======================#
class PushingSquareException(InsertionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that pushing a Square on the Stack failed.

    # PARENT:
        *   SquareStackException
        *   PushFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_PUSH_FAILURE"
    DEFAULT_MESSAGE = "Square push failed."