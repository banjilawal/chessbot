# src/chess/arena/validator/exception/wrapper.py

"""
Module: chess.arena.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.arena import ArenaContextException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# ARENA_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
    "ArenaContextValidationFailedException",
]


# ======================# ARENA_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
class ArenaContextValidationFailedException(ArenaContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a ArenaContext candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an ArenaContextValidationFailedException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The ArenaContextValidationFailedException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   ArenaContextException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ARENA_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "ArenaContext validation failed."