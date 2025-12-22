# src/chess/arena/map/builder/exception.py

"""
Module: chess.arena.map.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.arena import ArenaContextException

__all__ = [
    # ======================# ARENA_CONTEXT BUILD EXCEPTION #======================#
    "ArenaContextBuildFailedException",
]


# ======================# ARENA_CONTEXT BUILD EXCEPTION #======================#
class ArenaContextBuildFailedException(ArenaContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised during ArenaContext build process.
    2.  Wraps an exception that hits the try-finally block of an ArenaContextBuilder method.

    # PARENT:
        *   ArenaContextException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ARENA_CONTEXT_BUILD_ERROR"
    DEFAULT_MESSAGE = "PlayerArena build failed."