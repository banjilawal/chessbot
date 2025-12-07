# src/chess/agent/factory/exception.py

"""
Module: chess.agent.factory.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentException
from chess.system import BuildFailedException

__all__ = [
    # ======================# AGENT BUILD EXCEPTIONS #======================#
    "AgentBuildFailedException",
]


# ======================# AGENT BUILD EXCEPTIONS #======================#
class AgentBuildFailedException(AgentException, BuildFailedException):
    """
    # ROLE: BuildFailedException, AgentContextException

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during AgentContext build process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an AgentContextBuilder method.

    # Parent
        *   AgentContextException
        *   BuildFailedException

    # PROVIDES:
    BuildResult[AgentContext] containing either:
            - On success: AgentContext in the payload.
            - On failure: Exception.

    # ATTRIBUTES:
    None
    """
    """Catchall exception for when AgentFactory encounters an error during an Agent build."""
    ERROR_CODE = "AGENT_BUILD_ERROR"
    DEFAULT_ERROR_CODE = "Agent build failed."