# src/chess/player/builder/exception.py

"""
Module: chess.player.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from chess.system import BuildException

__all__ = [
    # ======================# PLAYER_BUILD_FAILURE #======================#
    "PlayerBuildException",
]


# ======================# PLAYER_BUILD_FAILURE #======================#
class PlayerBuildException(BuildException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in PlayerBuilder.build that, prevented BuildResult.success() from 
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
    ERROR_CODE = "PLAYER_BUILD_FAILED"
    DEFAULT_MESSAGE = "Player build failed."