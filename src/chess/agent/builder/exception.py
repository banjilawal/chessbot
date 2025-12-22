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
    #======================# AGENT BUILD EXCEPTION #======================#
    "AgentBuildFailedException",
]


#======================# AGENT BUILD EXCEPTION #======================#
class AgentBuildFailedException(AgentException, BuildFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised during PlayerAgent build process.
    2.  Wraps an exception that hits the try-finally block of an AgentBuilder method.

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
    ERROR_CODE = "AGENT_BUILD_ERROR"
    DEFAULT_ERROR_CODE = "PlayerAgent build failed."