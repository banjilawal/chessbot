# src/chess/arena/builder/exception.py

"""
Module: chess.arena.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.arena import ArenaException
from chess.system import BuildFailedException

__all__ = [
    # ======================# ARENA_BUILD_FAILURE EXCEPTION #======================#
    "ArenaBuildFailedException",
]


#======================# ARENA_BUILD_FAILURE EXCEPTION #======================#
class ArenaBuildFailedException(ArenaException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the Arena build creates an exception. Failed check exceptions are encapsulated
        in an ArenaBuildFailedException which is sent to the caller in a BuildResult.
    2.  The ArenaBuildFailedException provides a trace for debugging and application recovery.

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
    ERROR_CODE = "Arena_BUILD_FAILED"
    DEFAULT_MESSAGE = "Arena build failed."