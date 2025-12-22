# src/chess/arena/validator/exception/base.py

"""
Module: chess.arena.validator.exception.base
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.arena import ArenaException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# INVALID_ARENA EXCEPTION #======================#
    "InvalidArenaException",
]


# ======================# ARENA VALIDATION EXCEPTION #======================#
class InvalidArenaException(ArenaException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised Arena validation.
    2.  Wrap an exception that hits the try-finally-block in ArenaValidator methods.

    # PARENT:
        *   ArenaException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ARENA__VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Arena validation failed."