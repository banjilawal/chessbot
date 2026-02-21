# src/chess/owner/builder/exception.py

"""
Module: chess.owner.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from chess.player import PlayerException
from chess.system import BuildException

__all__ = [
    # ======================# PLAYER_BUILD_FAILURE EXCEPTION #======================#
    "PlayerBuildException",
]


#======================# PLAYER_BUILD_FAILURE EXCEPTION #======================#
class PlayerBuildException(PlayerException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the PlayerContext build creates an exception. Failed check exceptions are encapsulated
        in an PlayerContextBuildFailedException which is sent to the caller in a BuildResult.
    2.  The PlayerContextBuildFailedException provides a trace for debugging and application recovery.

    # PARENT:
        *   PlayerException
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PLAYER_BUILD_FAILED"
    DEFAULT_ERROR_CODE = "Player build failed."