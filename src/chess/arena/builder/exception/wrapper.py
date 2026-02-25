# src/chess/arena/builder/wrapper.py

"""
Module: chess.arena.builder.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import BuildException

__all__ = [
    # ======================# ARENA_BUILD_FAILURE #======================#
    "ArenaBuildException",
]


# ======================# ARENA_BUILD_FAILURE #======================#
class ArenaBuildException(BuildException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in ArenaBuilder.build that, prevented BuildResult.success() from
        being returned.

    # PARENT:
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ARENA_BUILD_FAILED"
    MSG = "Arena build failed."