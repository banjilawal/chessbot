# src/chess/arena/factory/exception.py

"""
Module: chess.arena.factory.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.arena import ArenaException
from chess.system import BuildFailedException

__all__ = [
    # ======================# ARENA_BUILD_FAILED EXCEPTION #======================#
    "ArenaBuildFailedException",
]


#======================# ARENA_BUILD_FAILED EXCEPTION #======================#
class ArenaBuildFailedException(ArenaException, BuildFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised during Arena build process.
    2.  Wraps unhandled exception that hit the try-finally block of an ArenaBuilder method.

    # PARENT:
        *   ArenaException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ARENA_BUILD_ERROR"
    DEFAULT_ERROR_CODE = "Arena build failed."