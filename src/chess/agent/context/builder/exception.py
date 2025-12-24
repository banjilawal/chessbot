# src/chess/agent/builder/exception.py

"""
Module: chess.agent.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.agent import AgentContextException


__all__ = [
    #======================# AGENT_CONTEXT BUILD EXCEPTION #======================#
    "AgentContextBuildFailedException",
]


#======================# AGENT_CONTEXT BUILD EXCEPTION #======================#
class AgentContextBuildFailedException(AgentContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the AgentContext build creates an exception. Failed check exceptions are encapsulated
        in an AgentContextBuildFailedException which is sent to the caller in a BuildResult.
    2.  The AgentContextBuildFailedException provides a trace for debugging and application recovery.tion recovery.
    
    # PARENT:
        *   AgentContextException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "AgentContext build failed."