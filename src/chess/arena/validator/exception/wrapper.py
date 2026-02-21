# src/chess/arena/validator/exception/base.py

"""
Module: chess.arena.validator.exception.base
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.arena import ArenaException
from chess.system import ValidationException

__all__ = [
    # ======================# ARENA_VALIDATION_FAILURE EXCEPTION #======================#
    "ArenaValidationException",
]


# ======================# ARENA_VALIDATION_FAILURE EXCEPTION #======================#
class ArenaValidationException(ArenaException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as an Arena. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   ArenaException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ARENA_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Arena validation failed."