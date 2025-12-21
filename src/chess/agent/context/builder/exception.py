# src/chess/agent/map/builder/exception.py

"""
Module: chess.agent.map.builder.exception
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
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised during AgentContext build process.
    2.  Wraps unhandled exception that hit the try-finally block of an AgentContextBuilder method.
    
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
    ERROR_CODE = "AGENT_CONTEXT_BUILD_ERROR"
    DEFAULT_MESSAGE = "PlayerAgent build failed."