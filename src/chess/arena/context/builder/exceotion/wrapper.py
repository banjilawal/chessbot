# src/chess/arena/builder/exception.py

"""
Module: chess.arena.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import BuildException
from chess.arena import ArenaContextException

__all__ = [
    # ======================# ARENA_CONTEXT_BUILD_FAILURE EXCEPTION #======================#
    "ArenaContextBuildException",
]


# ======================# ARENA_CONTEXT_BUILD_FAILURE EXCEPTION #======================#
class ArenaContextBuildException(ArenaContextException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the ArenaContext build creates an exception. Failed check exceptions are encapsulated
        in an ArenaContextBuildException which is sent to the caller in a BuildResult.
    2.  The ArenaContextBuildException provides a trace for debugging and application recovery.

    # PARENT:
        *   ArenaContextException
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ARENA_CONTEXT_BUILD_FAILED"
    DEFAULT_MESSAGE = "ArenaContext build failed."