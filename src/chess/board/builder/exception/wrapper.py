# src/chess/board/builder/wrapper.py

"""
Module: chess.board.builder.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import BuildException

__all__ = [
    # ======================# BOARD_BUILD_FAILURE #======================#
    "BoardBuildException",
]


# ======================# BOARD_BUILD_FAILURE #======================#
class BoardBuildException(BuildException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in BoardBuilder.build that, prevented BuildResult.success() from
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
    ERROR_CODE = "BOARD_BUILD_FAILED"
    DEFAULT_MESSAGE = "Board build failed."