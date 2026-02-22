# src/chess/arena/builder/exception.py

"""
Module: chess.arena.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.arena import ArenaException
from chess.system import BuildException

__all__ = [
    # ======================# ARENA_BUILD_FAILURE #======================#
    "ArenaBuildException",
]


#======================# ARENA_BUILD_FAILURE #======================#
class ArenaBuildException(ArenaException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the Arena build creates an exception. Failed check exceptions are encapsulated
        in an ArenaBuildException which is sent to the caller in a BuildResult.
    2.  The ArenaBuildException provides a trace for debugging and application recovery.

    # PARENT:
        *   ArenaException
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "Arena_BUILD_FAILED"
    DEFAULT_MESSAGE = "Arena build failed."