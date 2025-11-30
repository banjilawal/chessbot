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
    # ======================# AGENT_CONTEXT BUILD EXCEPTIONS #======================#
    "AgentContextBuildFailedException",
]


# ======================# AGENT_CONTEXT BUILD EXCEPTIONS #======================#
class AgentContextBuildFailedException(AgentContextException, BuildFailedException):
    """Catchall exception for when AgentContextBuilder encounters an error during an AgentContext build."""
    ERROR_CODE = "AGENT_CONTEXT_BUILD_ERROR"
    DEFAULT_MESSAGE = "Agent build failed."