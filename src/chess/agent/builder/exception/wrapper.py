# src/chess/agent/builder/exception.py

"""
Module: chess.agent.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from chess.agent import AgentException
from chess.system import BuildFailedException

__all__ = [
    # ======================# AGENT_BUILD_FAILED EXCEPTION #======================#
    "AgentBuildFailedException",
]


#======================# AGENT_BUILD_FAILED EXCEPTION #======================#
class AgentBuildFailedException(AgentException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the AgentContext build creates an exception. Failed check exceptions are encapsulated
        in an AgentContextBuildFailedException which is sent to the caller in a BuildResult.
    2.  The AgentContextBuildFailedException provides a trace for debugging and application recovery.

    # PARENT:
        *   AgentException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_BUILD_FAILED"
    DEFAULT_ERROR_CODE = "PlayerAgent build failed."