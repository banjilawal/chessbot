# src/chess/arena/validator/exception/wrapper.py

"""
Module: chess.arena.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.arena import ArenaContextException
from chess.system import ValidationException

__all__ = [
    # ======================# ARENA_CONTEXT_VALIDATION_FAILURE #======================#
    "ArenaContextValidationException",
]


# ======================# ARENA_CONTEXT_VALIDATION_FAILURE #======================#
class ArenaContextValidationException(ArenaContextException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as an ArenaContext. The
        encapsulated exceptions create a chain for tracing the source of the failure.

    # PARENT:
        *   ArenaContextException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ARENA_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "ArenaContext validation failed."