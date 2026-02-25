# src/chess/player/builder/exception.py

"""
Module: chess.player.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import BuildException
from chess.agent import AgentContextException


__all__ = [
    # ======================# PLAYER_CONTEXT_BUILD_FAILURE #======================#
    "AgentContextBuildException",
]


#======================# PLAYER_CONTEXT_BUILD_FAILURE #======================#
class AgentContextBuildException(AgentContextException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the AgentContext build creates an exception. Failed check exceptions are encapsulated
        in an AgentContextBuildException which is sent to the caller in a BuildResult.
    2.  The AgentContextBuildException provides a trace for debugging and application recovery.
    
    # PARENT:
        *   AgentContextException
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "AGENT_CONTEXT_BUILD_FAILED"
    MSG = "AgentContext build failed."