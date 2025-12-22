# src/chess/arena/map/validator/exception/base.py

"""
Module: chess.arena.arena.map.validator.exception.base
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.arena import ArenaContextException
from chess.system import ValidationFailedException


__all__ = [
    # ======================# ARENA_CONTEXT VALIDATION EXCEPTION #======================#
    "InvalidArenaContextException",
]


# ======================# ARENA_CONTEXT VALIDATION EXCEPTION #======================#
class InvalidArenaContextException(ArenaContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised ArenaContext validation.
    2.  Wrap an exception that hit the try-finally-block in ArenaContextValidator methods.

    # PARENT:
        *   ArenaContextException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ARENA_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "ArenaContext validation failed."