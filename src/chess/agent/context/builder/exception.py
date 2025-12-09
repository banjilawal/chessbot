# src/chess/agent/context/builder/exception.py

"""
Module: chess.agent.context.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.agent import AgentContextException


__all__ = [
    #======================# AGENT_CONTEXT BUILD EXCEPTIONS #======================#
    "AgentContextBuildFailedException",
]


#======================# AGENT_CONTEXT BUILD EXCEPTIONS #======================#
class AgentContextBuildFailedException(AgentContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during AgentContext build process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an AgentContextBuilder method.
    
    # PARENT
        *   AgentContextException
        *   BuildFailedException

    # PROVIDES:
    AgentContextBuildFailedException

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_CONTEXT_BUILD_ERROR"
    DEFAULT_MESSAGE = "Agent build failed."